from __future__ import annotations

from pathlib import Path
from typing import Any

from verbpractice.display import tense_catalog_by_id
from verbpractice.load import load_course, load_library
from verbpractice.models import default_active_pool, default_course_config
from verbpractice.persist import save_course


def init_course(
    library_path: Path,
    out_path: Path,
    *,
    course_id: str = "course-1",
    name: str = "My course",
    tense_ids: list[str] | None = None,
    unmastered_cap: int = 5,
    library_spec_path: str | None = None,
) -> dict[str, Any]:
    library_path = library_path.resolve()
    library = load_library(library_path)

    if tense_ids is None:
        tense_ids = [
            t["id"]
            for t in library.get("tenseCatalog") or []
            if t.get("id")
        ]

    if library_spec_path is None:
        try:
            library_spec_path = str(
                library_path.relative_to(out_path.parent.resolve())
            )
        except ValueError:
            library_spec_path = str(library_path)

    course: dict[str, Any] = {
        "id": course_id,
        "name": name,
        "librarySpec": {
            "path": library_spec_path,
            "libraryId": library["id"],
            "schemaVersion": library["schemaVersion"],
            "verbSelection": {"mode": "all", "verbIds": [], "tagsInclude": [], "tagsExclude": []},
            "tenseSelection": {"mode": "listed", "tenseIds": tense_ids},
        },
        "activeDimensions": [d["id"] for d in library.get("dimensionDefinitions") or []],
        "activePool": default_active_pool(unmastered_cap),
        "config": default_course_config(),
        "progress": {},
        "flaggedVerbs": {},
    }
    save_course(out_path, course)
    return course


def add_tenses_to_course(
    course_path: str, tense_ids: list[str] | None = None
) -> list[str]:
    ctx = load_course(course_path)
    catalog = tense_catalog_by_id(ctx.library)
    sel = ctx.course["librarySpec"]["tenseSelection"]
    if sel.get("mode") != "listed":
        raise ValueError("Only courses with tenseSelection.mode=listed are supported")

    current = list(sel.get("tenseIds") or [])
    if not tense_ids:
        tense_ids = [tid for tid in sorted(catalog.keys()) if tid not in current]

    added: list[str] = []
    for tid in tense_ids:
        if tid not in catalog:
            raise ValueError(f"Unknown tenseId {tid!r} (not in library tenseCatalog)")
        if tid not in current:
            current.append(tid)
            added.append(tid)

    sel["tenseIds"] = current
    save_course(ctx.course_path, ctx.course)
    return added
