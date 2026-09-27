from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from verbpractice.models import CourseContext, UnitRef
from verbpractice.persist import load_course_json
from verbpractice.validate import validate_library


class LoadError(Exception):
    pass


def load_json(path: Path) -> dict[str, Any]:
    with path.open(encoding="utf-8") as f:
        return json.load(f)


def load_library(path: Path) -> dict[str, Any]:
    library = load_json(path)
    validate_library(library)
    return library


def resolve_library_path(course_path: Path, library_spec: dict[str, Any]) -> Path:
    raw = library_spec.get("path")
    if not raw:
        raise LoadError("librarySpec.path is required")
    lib_path = Path(raw)
    if not lib_path.is_absolute():
        lib_path = (course_path.parent / lib_path).resolve()
    return lib_path


def verb_matches_selection(verb: dict[str, Any], sel: dict[str, Any]) -> bool:
    mode = sel.get("mode", "all")
    if mode == "all":
        pass
    elif mode == "listed":
        if verb["id"] not in sel.get("verbIds", []):
            return False
    else:
        raise LoadError(f"Unknown verbSelection.mode: {mode}")

    tags = set(verb.get("tags") or [])
    include = set(sel.get("tagsInclude") or [])
    exclude = set(sel.get("tagsExclude") or [])
    if include and not (tags & include):
        return False
    if tags & exclude:
        return False
    return True


def tense_allowed(tense_id: str, sel: dict[str, Any]) -> bool:
    mode = sel.get("mode", "listed")
    if mode == "all":
        return True
    if mode == "listed":
        return tense_id in sel.get("tenseIds", [])
    raise LoadError(f"Unknown tenseSelection.mode: {mode}")


def build_eligible_units(
    library: dict[str, Any], course: dict[str, Any]
) -> list[UnitRef]:
    lib_spec = course["librarySpec"]
    verb_sel = lib_spec.get("verbSelection") or {"mode": "all"}
    tense_sel = lib_spec.get("tenseSelection") or {"mode": "listed", "tenseIds": []}

    refs: list[UnitRef] = []
    for verb in library.get("verbs") or []:
        if not verb_matches_selection(verb, verb_sel):
            continue
        for unit in verb.get("units") or []:
            tense_id = unit.get("tenseId")
            if not tense_id or not tense_allowed(tense_id, tense_sel):
                continue
            uid = unit["id"]
            refs.append(
                UnitRef(
                    unit_id=uid,
                    verb_id=verb["id"],
                    lemma=verb.get("lemma", verb["id"]),
                    tense_id=tense_id,
                    unit=unit,
                )
            )
    return refs


def load_course(course_path: str | Path) -> CourseContext:
    path = Path(course_path).resolve()
    course = load_course_json(path)
    if "librarySpec" not in course:
        raise LoadError("Course missing librarySpec")

    lib_path = resolve_library_path(path, course["librarySpec"])
    if not lib_path.is_file():
        raise LoadError(f"Library not found: {lib_path}")

    library = load_library(lib_path)
    spec = course["librarySpec"]
    if library.get("id") != spec.get("libraryId"):
        raise LoadError(
            f"libraryId mismatch: course expects {spec.get('libraryId')!r}, "
            f"file has {library.get('id')!r}"
        )
    if library.get("schemaVersion") != spec.get("schemaVersion"):
        raise LoadError(
            f"schemaVersion mismatch: course expects {spec.get('schemaVersion')!r}, "
            f"file has {library.get('schemaVersion')!r}"
        )

    ctx = CourseContext(course_path=str(path), course=course, library=library)
    ctx.eligible = build_eligible_units(library, course)
    return ctx


def dimension_filter(
    refs: list[UnitRef], filters: dict[str, str] | None
) -> list[UnitRef]:
    if not filters:
        return refs
    out: list[UnitRef] = []
    for ref in refs:
        dims = ref.dimensions
        if all(dims.get(k) == v for k, v in filters.items()):
            out.append(ref)
    return out


SECOND_PERSON_IDS = frozenset({"2sg", "2pl"})


def filter_units(
    refs: list[UnitRef],
    filters: dict[str, str] | None = None,
    *,
    skip_second_person: bool = False,
    verb_ids: set[str] | None = None,
) -> list[UnitRef]:
    out = dimension_filter(refs, filters)
    if skip_second_person:
        out = [r for r in out if r.dimensions.get("person") not in SECOND_PERSON_IDS]
    if verb_ids:
        out = [r for r in out if r.verb_id in verb_ids]
    return out
