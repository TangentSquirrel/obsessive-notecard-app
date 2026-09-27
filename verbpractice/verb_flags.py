from __future__ import annotations

from datetime import datetime, timezone
from typing import Any

from verbpractice.load import filter_units
from verbpractice.models import CourseContext
from verbpractice.rollup import count_mastered_slices, verb_is_unmastered, verb_mastered_in_course


def _now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def default_verb_flag() -> dict[str, Any]:
    return {"status": "active", "since": _now_iso()}


def flagged_verbs_map(course: dict[str, Any]) -> dict[str, Any]:
    return course.setdefault("flaggedVerbs", {})


def clear_mastered_flags(ctx: CourseContext) -> list[str]:
    """Remove flags for verbs fully mastered in this course. Returns removed verb ids."""
    flags = flagged_verbs_map(ctx.course)
    removed: list[str] = []
    for verb_id in list(flags.keys()):
        if verb_mastered_in_course(verb_id, ctx.eligible, ctx.progress):
            del flags[verb_id]
            removed.append(verb_id)
    return removed


def _eligible_verb_ids(
    ctx: CourseContext,
    filters: dict[str, str] | None,
    *,
    skip_second_person: bool = False,
    verb_ids: set[str] | None = None,
) -> list[str]:
    refs = filter_units(
        ctx.eligible,
        filters,
        skip_second_person=skip_second_person,
        verb_ids=verb_ids,
    )
    return sorted({r.verb_id for r in refs})


def open_flagged_verbs(
    ctx: CourseContext,
    filters: dict[str, str] | None = None,
    *,
    skip_second_person: bool = False,
    verb_ids: set[str] | None = None,
) -> list[str]:
    """Verbs with an active flag that are still unmastered (course-wide mastery)."""
    flags = flagged_verbs_map(ctx.course)
    in_scope = set(
        _eligible_verb_ids(
            ctx, filters, skip_second_person=skip_second_person, verb_ids=verb_ids
        )
    )
    open_ids: list[str] = []
    for verb_id, entry in flags.items():
        if entry.get("status") != "active":
            continue
        if verb_id not in in_scope:
            continue
        if verb_mastered_in_course(verb_id, ctx.eligible, ctx.progress):
            continue
        open_ids.append(verb_id)
    return sorted(open_ids)


def ensure_flags_for_lesson(
    ctx: CourseContext,
    filters: dict[str, str] | None = None,
    *,
    skip_second_person: bool = False,
    verb_ids: set[str] | None = None,
) -> list[str]:
    """
    Prepare primary verbs for a session:
    1. Drop flags for mastered verbs.
    2. Keep existing open flags (still unmastered).
    3. If under cap, flag new unmastered verbs until cap is reached.
    Returns verb ids to treat as the active (primary) pool for this lesson.
    """
    clear_mastered_flags(ctx)
    cap = int(ctx.active_pool.get("targetUnmasteredVerbs", 5))
    flags = flagged_verbs_map(ctx.course)
    refs = filter_units(
        ctx.eligible,
        filters,
        skip_second_person=skip_second_person,
        verb_ids=verb_ids,
    )
    scope_verbs = {r.verb_id for r in refs}

    open_ids = open_flagged_verbs(
        ctx,
        filters,
        skip_second_person=skip_second_person,
        verb_ids=verb_ids,
    )

    candidates = [
        v
        for v in _eligible_verb_ids(
            ctx,
            filters,
            skip_second_person=skip_second_person,
            verb_ids=verb_ids,
        )
        if verb_is_unmastered(v, ctx.eligible, ctx.progress) and v not in flags
    ]
    candidates.sort(key=lambda vid: (count_mastered_slices(vid, ctx.eligible, ctx.progress)[0], vid))

    idx = 0
    while len(open_ids) < cap and idx < len(candidates):
        verb_id = candidates[idx]
        idx += 1
        if verb_id not in scope_verbs:
            continue
        flags[verb_id] = default_verb_flag()
        open_ids.append(verb_id)

    return sorted(set(open_ids))[:cap]
