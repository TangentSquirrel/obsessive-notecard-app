from __future__ import annotations

import random
from typing import Any, Literal

from verbpractice.display import format_practice_prompt
from verbpractice.load import filter_units
from verbpractice.models import CourseContext, UnitRef
from verbpractice.verb_flags import open_flagged_verbs

PromptKind = Literal["focus", "review"]


def _unit_weight(ref: UnitRef, progress: dict[str, Any], config: dict[str, Any]) -> float:
    p = progress.get(ref.unit_id) or {}
    state = p.get("state", "unknown")
    weight = 1.0
    if state == "solid":
        weight *= config.get("solidSamplingWeight", 0.05)
    elif state == "review":
        weight *= config.get("reviewBoostWeight", 3.0)
    elif state == "unknown":
        weight *= 1.2
    attempts = p.get("attempts", 0)
    if attempts == 0:
        weight *= 1.5
    return max(weight, 0.001)


def _pick_weighted(
    candidates: list[UnitRef], ctx: CourseContext, rng: random.Random
) -> UnitRef | None:
    if not candidates:
        return None
    weights = [_unit_weight(r, ctx.progress, ctx.config) for r in candidates]
    return rng.choices(candidates, weights=weights, k=1)[0]


def _maintenance_bucket(state: str) -> str:
    if state == "review":
        return "review"
    if state == "solid":
        return "solid"
    return "unknown"


def select_next_unit(
    ctx: CourseContext,
    filters: dict[str, str] | None = None,
    *,
    skip_second_person: bool = False,
    verb_ids: set[str] | None = None,
    sticky_verb: str | None = None,
    sticky_tense: str | None = None,
    rng: random.Random | None = None,
) -> tuple[UnitRef | None, PromptKind]:
    if rng is None:
        rng = random.Random()

    refs = filter_units(
        ctx.eligible,
        filters,
        skip_second_person=skip_second_person,
        verb_ids=verb_ids,
    )
    if not refs:
        return None, "focus"

    scheduling = ctx.config.get("scheduling") or {}
    primary_share = scheduling.get("primaryShare", 0.85)
    maint_weights = scheduling.get("maintenanceWeights") or {
        "review": 0.5,
        "unknown": 0.2,
        "solid": 0.3,
    }

    cap = int(ctx.active_pool.get("targetUnmasteredVerbs", 5))
    active = set(
        open_flagged_verbs(ctx, filters, skip_second_person=skip_second_person)[:cap]
    )
    primary_refs = [r for r in refs if r.verb_id in active]
    maintenance_refs = [r for r in refs if r.verb_id not in active]

    use_primary = rng.random() < primary_share or not maintenance_refs
    pool = primary_refs if use_primary else maintenance_refs
    kind: PromptKind = "focus" if use_primary and primary_refs else "review"

    if not use_primary and maintenance_refs:
        by_bucket: dict[str, list[UnitRef]] = {"review": [], "unknown": [], "solid": []}
        for r in maintenance_refs:
            st = (ctx.progress.get(r.unit_id) or {}).get("state", "unknown")
            by_bucket[_maintenance_bucket(st)].append(r)
        buckets = [b for b in ("review", "unknown", "solid") if by_bucket[b]]
        if buckets:
            bw = [maint_weights.get(b, 0.1) for b in buckets]
            chosen_bucket = rng.choices(buckets, weights=bw, k=1)[0]
            pool = by_bucket[chosen_bucket]

    if not pool:
        pool = refs
        kind = "focus"

    if sticky_verb:
        same_verb = [r for r in pool if r.verb_id == sticky_verb]
        if same_verb and rng.random() < 0.8:
            pool = same_verb
    if sticky_tense and sticky_verb:
        same_tense = [r for r in pool if r.tense_id == sticky_tense]
        if same_tense and rng.random() < 0.7:
            pool = same_tense

    ref = _pick_weighted(pool, ctx, rng)
    return ref, kind


def next_prompt(
    ctx: CourseContext,
    filters: dict[str, str] | None = None,
    *,
    skip_second_person: bool = False,
    verb_ids: set[str] | None = None,
    sticky_verb: str | None = None,
    sticky_tense: str | None = None,
    rng: random.Random | None = None,
) -> dict[str, Any] | None:
    ref, kind = select_next_unit(
        ctx,
        filters,
        skip_second_person=skip_second_person,
        verb_ids=verb_ids,
        sticky_verb=sticky_verb,
        sticky_tense=sticky_tense,
        rng=rng,
    )
    if ref is None:
        return None
    prompt = ref.unit.get("prompt") or {}
    return {
        "unit_ref": ref,
        "kind": kind,
        "display": format_practice_prompt(ref, ctx.library),
        "hint_en": prompt.get("en", ""),
        "answers": ref.unit.get("answers") or [],
    }
