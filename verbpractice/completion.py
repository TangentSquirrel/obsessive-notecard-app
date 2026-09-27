from __future__ import annotations

from collections import defaultdict
from typing import Any

from verbpractice.load import filter_units
from verbpractice.models import CourseContext, UnitRef
from verbpractice.rollup import group_verb_tense, slice_status, verb_mastered_in_course


def mastery_summary(
    ctx: CourseContext,
    group_by: str | None = None,
    filters: dict[str, str] | None = None,
    *,
    skip_second_person: bool = False,
) -> dict[str, Any]:
    refs = filter_units(
        ctx.eligible, filters, skip_second_person=skip_second_person
    )
    progress = ctx.progress

    verb_tense_groups = group_verb_tense(refs)
    vt_cells: dict[str, str] = {}
    for (verb_id, tense_id), units in sorted(verb_tense_groups.items()):
        key = f"{verb_id} × {tense_id}"
        vt_cells[key] = slice_status(units, progress)

    verbs_mastered = [
        v for v in sorted({r.verb_id for r in refs}) if verb_mastered_in_course(v, refs, progress)
    ]

    dim_counts: dict[str, dict[str, dict[str, int]]] = defaultdict(
        lambda: defaultdict(lambda: {"total": 0, "solid": 0})
    )
    for ref in refs:
        p = progress.get(ref.unit_id) or {}
        for dim_id, val_id in ref.dimensions.items():
            cell = dim_counts[dim_id][val_id]
            cell["total"] += 1
            if p.get("state") == "solid":
                cell["solid"] += 1

    dim_completion: dict[str, dict[str, Any]] = {}
    for dim_id, values in dim_counts.items():
        dim_completion[dim_id] = {}
        for val_id, counts in values.items():
            total = counts["total"]
            solid = counts["solid"]
            dim_completion[dim_id][val_id] = {
                "total": total,
                "solid": solid,
                "complete": total > 0 and solid == total,
                "pct": round(100 * solid / total, 1) if total else 0.0,
            }

    grouped: dict[str, Any] = {}
    if group_by:
        buckets: dict[str, list[UnitRef]] = defaultdict(list)
        for ref in refs:
            val = ref.dimensions.get(group_by, "?")
            buckets[val].append(ref)
        for val, units in sorted(buckets.items()):
            solid_n = sum(
                1
                for u in units
                if (progress.get(u.unit_id) or {}).get("state") == "solid"
            )
            grouped[f"{group_by}={val}"] = {
                "total": len(units),
                "solid": solid_n,
                "complete": len(units) > 0 and solid_n == len(units),
            }

    return {
        "verb_tense": vt_cells,
        "verbs_fully_mastered": verbs_mastered,
        "dimension_cells": dim_completion,
        "grouped": grouped,
        "eligible_units": len(refs),
    }


def format_status_bar(solid: int, total: int, width: int = 4) -> str:
    if total <= 0:
        return "[----]"
    filled = round(width * solid / total)
    filled = max(0, min(width, filled))
    if solid == total and total > 0:
        return "[" + "=" * width + "]"
    return "[" + "=" * filled + "-" * (width - filled) + "]"


def slice_progress_counts(
    units: list[UnitRef], progress: dict[str, Any]
) -> tuple[int, int, int]:
    """Return (solid_count, practiced_count, total_units)."""
    total = len(units)
    solid = 0
    practiced = 0
    for u in units:
        p = progress.get(u.unit_id) or {}
        if p.get("state") == "solid":
            solid += 1
        if p.get("attempts", 0) > 0:
            practiced += 1
    return solid, practiced, total


def format_practice_bar(practiced: int, total: int, width: int = 4) -> str:
    """Bar fill = share of units with at least one attempt (learner-visible progress)."""
    if total <= 0:
        return "[----]"
    filled = round(width * practiced / total)
    filled = max(0, min(width, filled))
    if practiced == total and total > 0:
        return "[" + "=" * width + "]"
    return "[" + "=" * filled + "-" * (width - filled) + "]"


def format_slice_progress_label(solid: int, practiced: int, total: int) -> str:
    if practiced == 0:
        return f"{solid}/{total}"
    if solid == practiced:
        return f"{practiced}/{total} ({solid} solid)"
    return f"{practiced}/{total} practiced ({solid} solid)"
