from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from verbpractice.display import format_person_for_prompt

PERSONS = ["1sg", "2sg", "3sg", "1pl", "2pl", "3pl"]
# Affirmative imperative: no 1sg (eu); 3sg = você, 3pl = vocês
IMPERATIVE_PERSONS = ["2sg", "3sg", "1pl", "2pl", "3pl"]

# Slice axes: each tenseId is exactly one (time, mood, aspect). Person + register sit on units.
TENSE_SLICE_AXES = ("time", "mood", "aspect")

DIMENSION_DEFINITIONS = [
    {
        "id": "time",
        "label": "Time",
        "values": [
            {"id": "past", "label": "Past"},
            {"id": "present", "label": "Present"},
            {"id": "future", "label": "Future"},
        ],
    },
    {
        "id": "mood",
        "label": "Mood",
        "values": [
            {"id": "indicative", "label": "Indicative"},
            {"id": "subjunctive", "label": "Subjunctive"},
            {"id": "imperative", "label": "Imperative"},
        ],
    },
    {
        "id": "aspect",
        "label": "Aspect",
        "values": [
            {"id": "perfective", "label": "Perfect (preterite)"},
            {"id": "imperfective", "label": "Imperfect"},
            {"id": "na", "label": "—"},
        ],
    },
    {
        "id": "person",
        "label": "Person",
        "values": [
            {"id": "1sg", "label": "eu"},
            {"id": "2sg", "label": "tu/você"},
            {"id": "3sg", "label": "ele/ela"},
            {"id": "1pl", "label": "nós"},
            {"id": "2pl", "label": "vós"},
            {"id": "3pl", "label": "eles/elas"},
        ],
    },
    {
        "id": "register",
        "label": "Regularity",
        "values": [
            {"id": "normal", "label": "Regular pattern"},
            {"id": "special", "label": "Irregular / special"},
        ],
    },
]

# id, label, time, mood, aspect — single source of truth for tense ↔ dimension mapping
TENSE_SPECS: list[tuple[str, str, str, str, str]] = [
    ("present_indicative", "Present indicative", "present", "indicative", "na"),
    ("preterite_indicative", "Preterite indicative", "past", "indicative", "perfective"),
    ("imperfect_indicative", "Imperfect indicative", "past", "indicative", "imperfective"),
    ("present_subjunctive", "Present subjunctive", "present", "subjunctive", "na"),
    ("imperfect_subjunctive", "Imperfect subjunctive", "past", "subjunctive", "imperfective"),
    ("future_indicative", "Future indicative", "future", "indicative", "na"),
    ("future_subjunctive", "Future subjunctive", "future", "subjunctive", "na"),
    ("imperative_affirmative", "Affirmative imperative", "present", "imperative", "na"),
]

TENSE_PERSONS: dict[str, list[str]] = {
    "imperative_affirmative": IMPERATIVE_PERSONS,
}

TENSE_DIMS: dict[str, dict[str, str]] = {
    tid: {"time": t, "mood": m, "aspect": a}
    for tid, _label, t, m, a in TENSE_SPECS
}

TENSE_CATALOG: list[dict[str, Any]] = []
for tid, label, *_rest in TENSE_SPECS:
    entry: dict[str, Any] = {
        "id": tid,
        "label": label,
        "dimensions": dict(TENSE_DIMS[tid]),
    }
    if tid in TENSE_PERSONS:
        entry["persons"] = list(TENSE_PERSONS[tid])
    TENSE_CATALOG.append(entry)

DIMENSION_INTERACTION = {
    "tenseSliceAxes": list(TENSE_SLICE_AXES),
    "unitAxes": ["person", "register"],
    "rules": [
        "Each tenseId maps to exactly one (time, mood, aspect) triple.",
        "Units add person (6 forms) and register (regular vs irregular verb).",
        "Past indicative splits by aspect: perfective = preterite, imperfective = imperfect.",
        "Past subjunctive uses imperfect aspect only (imperfect subjunctive).",
        "Present, future, and imperative use aspect 'na' (not applicable).",
        "Imperative uses five persons (2sg, 3sg/você, 1pl, 2pl, 3pl/vocês); no 1sg.",
        "Practice filters combine dimensions; progress is stored per unit (verb × tenseId × person).",
    ],
}


def _conj_paradigm(tense_id: str, conj: list[str] | dict[str, Any]) -> tuple[list[str], list[str]]:
    if isinstance(conj, dict):
        persons = list(conj["persons"])
        forms = list(conj["forms"])
    else:
        persons = TENSE_PERSONS.get(tense_id, PERSONS)
        forms = list(conj)
    if len(persons) != len(forms):
        raise ValueError(f"{tense_id}: persons and forms length mismatch")
    return persons, forms


def _units_for_verb(
    verb_id: str,
    lemma: str,
    forms: dict[str, list[str] | dict[str, Any]],
    *,
    register: str,
) -> list[dict[str, Any]]:
    person_dim = next(d for d in DIMENSION_DEFINITIONS if d["id"] == "person")
    person_label_map = {
        v["id"]: v.get("label", v["id"])
        for v in person_dim.get("values") or []
        if v.get("id")
    }
    labels = {"person": person_label_map}

    units: list[dict[str, Any]] = []
    for tense_id, conj in forms.items():
        if tense_id not in TENSE_DIMS:
            raise ValueError(f"{verb_id}: unknown tenseId {tense_id!r}")
        persons, answers = _conj_paradigm(tense_id, conj)
        base_dims = dict(TENSE_DIMS[tense_id])
        td = base_dims
        aspect_disp = td["aspect"] if td["aspect"] != "na" else "—"
        for person, answer in zip(persons, answers):
            dims = {**base_dims, "person": person, "register": register}
            uid = f"{verb_id}.{tense_id}.{person}"
            who = format_person_for_prompt(person, labels)
            hint = f"{lemma} · {td['time']}/{td['mood']}/{aspect_disp} · {who}"
            units.append(
                {
                    "id": uid,
                    "tenseId": tense_id,
                    "prompt": {"ptHint": hint, "en": ""},
                    "answers": [answer],
                    "dimensions": dims,
                }
            )
    return units


# Most tenses: six forms (PERSONS). Imperative: see IMPERATIVE_PERSONS.
VERB_CONJUGATIONS: dict[str, dict[str, list[str] | dict[str, Any]]] = {
    "ser": {
        "present_indicative": ["sou", "és", "é", "somos", "sois", "são"],
        "preterite_indicative": ["fui", "foste", "foi", "fomos", "fostes", "foram"],
        "imperfect_indicative": ["era", "eras", "era", "éramos", "íeis", "eram"],
        "present_subjunctive": ["seja", "sejas", "seja", "sejamos", "sejais", "sejam"],
        "imperfect_subjunctive": ["fosse", "fosses", "fosse", "fôssemos", "fôsseis", "fossem"],
        "future_indicative": ["serei", "serás", "será", "seremos", "sereis", "serão"],
        "future_subjunctive": ["for", "fores", "for", "formos", "fordes", "forem"],
        "imperative_affirmative": {
            "persons": IMPERATIVE_PERSONS,
            "forms": ["sê", "seja", "sejamos", "sede", "sejam"],
        },
    },
    "falar": {
        "present_indicative": ["falo", "falas", "fala", "falamos", "falais", "falam"],
        "preterite_indicative": ["falei", "falaste", "falou", "falamos", "falastes", "falaram"],
        "imperfect_indicative": ["falava", "falavas", "falava", "falávamos", "faláveis", "falavam"],
        "present_subjunctive": ["fale", "fales", "fale", "falemos", "faleis", "falem"],
        "imperfect_subjunctive": ["falasse", "falasses", "falasse", "falássemos", "falásseis", "falassem"],
        "future_indicative": ["falarei", "falarás", "falará", "falaremos", "falareis", "falarão"],
        "future_subjunctive": ["falar", "falares", "falar", "falarmos", "falardes", "falarem"],
        "imperative_affirmative": {
            "persons": IMPERATIVE_PERSONS,
            "forms": ["fala", "fale", "falemos", "falai", "falem"],
        },
    },
    "comer": {
        "present_indicative": ["como", "comes", "come", "comemos", "comeis", "comem"],
        "preterite_indicative": ["comi", "comeste", "comeu", "comemos", "comestes", "comeram"],
        "imperfect_indicative": ["comia", "comias", "comia", "comíamos", "comíeis", "comiam"],
        "present_subjunctive": ["coma", "comas", "coma", "comamos", "comais", "comam"],
        "imperfect_subjunctive": ["comesse", "comesses", "comesse", "comêssemos", "comêsseis", "comessem"],
        "future_indicative": ["comerei", "comerás", "comerá", "comeremos", "comereis", "comerão"],
        "future_subjunctive": ["comer", "comeres", "comer", "comermos", "comerdes", "comerem"],
        "imperative_affirmative": {
            "persons": IMPERATIVE_PERSONS,
            "forms": ["come", "coma", "comamos", "comei", "comam"],
        },
    },
    "partir": {
        "present_indicative": ["parto", "partes", "parte", "partimos", "partis", "partem"],
        "preterite_indicative": ["parti", "partiste", "partiu", "partimos", "partistes", "partiram"],
        "imperfect_indicative": ["partia", "partias", "partia", "partíamos", "partíeis", "partiam"],
        "present_subjunctive": ["parta", "partas", "parta", "partamos", "partais", "partam"],
        "imperfect_subjunctive": ["partisse", "partisses", "partisse", "partíssemos", "partísseis", "partissem"],
        "future_indicative": ["partirei", "partirás", "partirá", "partiremos", "partireis", "partirão"],
        "future_subjunctive": ["partir", "partires", "partir", "partirmos", "partirdes", "partirem"],
        "imperative_affirmative": {
            "persons": IMPERATIVE_PERSONS,
            "forms": ["parte", "parta", "partamos", "parti", "partam"],
        },
    },
}

VERB_META: list[dict[str, Any]] = [
    {
        "id": "ser",
        "lemma": "ser",
        "translation": "to be",
        "regularity": "irregular",
        "tags": ["essential", "irregular"],
        "register": "special",
    },
    {
        "id": "falar",
        "lemma": "falar",
        "translation": "to speak",
        "regularity": "regular",
        "tags": ["essential", "regular", "ar"],
        "register": "normal",
    },
    {
        "id": "comer",
        "lemma": "comer",
        "translation": "to eat",
        "regularity": "regular",
        "tags": ["essential", "regular", "er"],
        "register": "normal",
    },
    {
        "id": "partir",
        "lemma": "partir",
        "translation": "to leave",
        "regularity": "regular",
        "tags": ["essential", "regular", "ir"],
        "register": "normal",
    },
]


def build_core_library() -> dict[str, Any]:
    verbs = []
    for meta in VERB_META:
        vid = meta["id"]
        verbs.append(
            {
                **{k: meta[k] for k in ("id", "lemma", "translation", "regularity", "tags")},
                "units": _units_for_verb(
                    vid,
                    meta["lemma"],
                    VERB_CONJUGATIONS[vid],
                    register=meta["register"],
                ),
            }
        )

    return {
        "schemaVersion": 1,
        "id": "core-50",
        "label": "Core verb library (seed)",
        "dimensionDefinitions": DIMENSION_DEFINITIONS,
        "dimensionInteraction": DIMENSION_INTERACTION,
        "tenseCatalog": TENSE_CATALOG,
        "verbs": verbs,
        "meta": {
            "targetIrregular": 25,
            "targetRegular": 25,
            "note": "Seed ships 4 exemplar verbs; extend VERB_CONJUGATIONS to reach 50+50.",
        },
    }


def write_core_library(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    lib = build_core_library()
    with path.open("w", encoding="utf-8") as f:
        json.dump(lib, f, indent=2, ensure_ascii=False)
        f.write("\n")
