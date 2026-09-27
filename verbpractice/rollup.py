from __future__ import annotations

from collections import defaultdict
from typing import Any

from verbpractice.display import TENSE_SLICE_DIMENSIONS
from verbpractice.models import CourseContext, UnitRef

SliceStatus = str  # mastered | in_progress | untrained


def slice_status(units: list[UnitRef], progress: dict[str, Any]) -> SliceStatus:
    if not units:
        return "untrained"
    has_attempt = False
    all_solid = True
    for u in units:
        p = progress.get(u.unit_id) or {}
        if p.get("attempts", 0) > 0:
            has_attempt = True
        if p.get("state") != "solid":
            all_solid = False
    if all_solid and has_attempt:
        return "mastered"
    if has_attempt:
        return "in_progress"
    return "untrained"


def group_verb_tense(refs: list[UnitRef]) -> dict[tuple[str, str], list[UnitRef]]:
    groups: dict[tuple[str, str], list[UnitRef]] = defaultdict(list)
    for ref in refs:
        groups[(ref.verb_id, ref.tense_id)].append(ref)
    return dict(groups)


def group_tense_slice(refs: list[UnitRef]) -> dict[tuple[str, ...], list[UnitRef]]:
    groups: dict[tuple[str, ...], list[UnitRef]] = defaultdict(list)
    for ref in refs:
        key = tuple(ref.dimensions.get(k, "?") for k in TENSE_SLICE_DIMENSIONS)
        groups[key].append(ref)
    return dict(groups)


def group_verb_tense_slice(
    refs: list[UnitRef],
) -> dict[tuple[str, tuple[str, ...]], list[UnitRef]]:
    groups: dict[tuple[str, tuple[str, ...]], list[UnitRef]] = defaultdict(list)
    for ref in refs:
        key = (
            ref.verb_id,
            tuple(ref.dimensions.get(k, "?") for k in TENSE_SLICE_DIMENSIONS),
        )
        groups[key].append(ref)
    return dict(groups)


def verb_mastered_in_course(
    verb_id: str,
    refs: list[UnitRef],
    progress: dict[str, Any],
) -> bool:
    verb_refs = [r for r in refs if r.verb_id == verb_id]
    if not verb_refs:
        return False
    groups = group_verb_tense(verb_refs)
    for units in groups.values():
        if slice_status(units, progress) != "mastered":
            return False
    return True


def verb_is_unmastered(
    verb_id: str,
    refs: list[UnitRef],
    progress: dict[str, Any],
) -> bool:
    verb_refs = [r for r in refs if r.verb_id == verb_id]
    if not verb_refs:
        return False
    groups = group_verb_tense(verb_refs)
    for units in groups.values():
        st = slice_status(units, progress)
        if st != "mastered":
            return True
    return False


def count_mastered_slices(
    verb_id: str,
    refs: list[UnitRef],
    progress: dict[str, Any],
) -> tuple[int, int]:
    verb_refs = [r for r in refs if r.verb_id == verb_id]
    groups = group_verb_tense(verb_refs)
    total = len(groups)
    mastered = sum(
        1 for units in groups.values() if slice_status(units, progress) == "mastered"
    )
    return mastered, total
