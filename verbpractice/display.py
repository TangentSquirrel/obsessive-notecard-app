from __future__ import annotations

from typing import Any

from verbpractice.models import UnitRef

# Axes that define a tense form (excluding person and register).
TENSE_SLICE_DIMENSIONS = ("time", "mood", "aspect")

# Match pedagogical order: when → mood → aspect → who → regularity
STATUS_DIMENSION_ORDER = ("time", "mood", "aspect", "person", "register")

PERSON_ORDINAL: dict[str, str] = {
    "1sg": "1st singular",
    "2sg": "2nd singular",
    "3sg": "3rd singular",
    "1pl": "1st plural",
    "2pl": "2nd plural",
    "3pl": "3rd plural",
}


def dimension_labels(library: dict[str, Any]) -> dict[str, dict[str, str]]:
    out: dict[str, dict[str, str]] = {}
    for dim in library.get("dimensionDefinitions") or []:
        dim_id = dim.get("id")
        if not dim_id:
            continue
        out[dim_id] = {
            v["id"]: v.get("label", v["id"])
            for v in dim.get("values") or []
            if v.get("id")
        }
    return out


def label_for(
    labels: dict[str, dict[str, str]], dim_id: str, val_id: str, *, empty_na: str = "—"
) -> str:
    if dim_id == "aspect" and val_id == "na":
        return empty_na
    return labels.get(dim_id, {}).get(val_id, val_id)


def tense_slice_tuple(ref: UnitRef) -> tuple[str, ...]:
    d = ref.dimensions
    return tuple(d.get(k, "?") for k in TENSE_SLICE_DIMENSIONS)


def format_tense_slice(
    ref: UnitRef, labels: dict[str, dict[str, str]], sep: str = " · "
) -> str:
    parts = [
        label_for(labels, dim_id, ref.dimensions.get(dim_id, "?"))
        for dim_id in TENSE_SLICE_DIMENSIONS
    ]
    return sep.join(parts)


def tense_catalog_by_id(library: dict[str, Any]) -> dict[str, dict[str, Any]]:
    return {t["id"]: t for t in library.get("tenseCatalog") or [] if t.get("id")}


def format_person_for_prompt(
    person_id: str, labels: dict[str, dict[str, str]] | None = None
) -> str:
    """e.g. '2nd singular (tu/você)'"""
    ordinal = PERSON_ORDINAL.get(person_id, person_id)
    pronoun = person_id
    if labels:
        pronoun = label_for(labels, "person", person_id)
    return f"{ordinal} ({pronoun})"


def format_practice_prompt(ref: UnitRef, library: dict[str, Any]) -> str:
    labels = dimension_labels(library)
    tense = format_tense_slice(ref, labels)
    person = format_person_for_prompt(ref.dimensions.get("person", "?"), labels)
    return f"{ref.lemma} · {tense} · {person}"
