from __future__ import annotations

import argparse
import random
import sys
from pathlib import Path

from verbpractice.cli_util import color_state, format_filters
from verbpractice.completion import (
    format_practice_bar,
    format_slice_progress_label,
    format_status_bar,
    mastery_summary,
    slice_progress_counts,
)
from verbpractice.display import STATUS_DIMENSION_ORDER, dimension_labels, label_for
from verbpractice.course_init import add_tenses_to_course, init_course
from verbpractice.grade import grade_answer
from verbpractice.library_seed import write_core_library
from verbpractice.load import filter_units, load_course, load_library
from verbpractice.mastery import ensure_progress_keys, record_attempt
from verbpractice.persist import save_course
from verbpractice.rollup import group_tense_slice, group_verb_tense_slice, slice_status
from verbpractice.select import next_prompt
from verbpractice.verb_flags import clear_mastered_flags, ensure_flags_for_lesson, open_flagged_verbs
from verbpractice.validate import ValidationError, validate_library

def _parse_dimension_args(raw: list[str] | None) -> dict[str, str]:
    out: dict[str, str] = {}
    for item in raw or []:
        if "=" not in item:
            raise SystemExit(f"Invalid dimension filter {item!r}; use dim=value")
        k, v = item.split("=", 1)
        out[k.strip()] = v.strip()
    return out


def cmd_seed_library(args: argparse.Namespace) -> int:
    path = Path(args.out)
    write_core_library(path)
    print(f"Wrote library to {path}")
    return 0


def cmd_validate_library(args: argparse.Namespace) -> int:
    library = load_library(Path(args.library))
    print(f"OK: {library['id']} ({len(library.get('verbs') or [])} verbs)")
    return 0


def cmd_library_info(args: argparse.Namespace) -> int:
    library = load_library(Path(args.library))
    labels = dimension_labels(library)
    verbs = library.get("verbs") or []
    by_reg: dict[str, int] = {}
    by_tense: dict[str, int] = {}
    for verb in verbs:
        by_reg[verb.get("regularity", "?")] = by_reg.get(verb.get("regularity", "?"), 0) + 1
        for unit in verb.get("units") or []:
            tid = unit.get("tenseId", "?")
            by_tense[tid] = by_tense.get(tid, 0) + 1
    print(f"Library: {library.get('label')} ({library.get('id')})")
    print(f"Verbs: {len(verbs)}")
    print("Regularity:", ", ".join(f"{k}={v}" for k, v in sorted(by_reg.items())))
    print("\nTense catalog (time · mood · aspect):")
    for entry in library.get("tenseCatalog") or []:
        d = entry.get("dimensions") or {}
        slice_label = " · ".join(
            label_for(labels, axis, d.get(axis, "?")) for axis in ("time", "mood", "aspect")
        )
        print(f"  {entry.get('id'):24} {slice_label}")
    print("\nUnits per tense:", ", ".join(f"{k}={v}" for k, v in sorted(by_tense.items())))
    return 0


def cmd_init_course(args: argparse.Namespace) -> int:
    out = Path(args.out)
    init_course(
        Path(args.library),
        out,
        course_id=args.course_id,
        name=args.name,
        unmastered_cap=args.unmastered_cap,
    )
    print(f"Created course at {out}")
    return 0


def cmd_add_tenses(args: argparse.Namespace) -> int:
    added = add_tenses_to_course(args.course, args.tense or None)
    if added:
        print(f"Added tenses: {', '.join(added)}")
    else:
        print("No new tenses (already in course).")
    return 0


def cmd_set_pool(args: argparse.Namespace) -> int:
    ctx = load_course(args.course)
    ctx.active_pool["targetUnmasteredVerbs"] = args.cap
    flags = ctx.course.get("flaggedVerbs") or {}
    if len(flags) > args.cap:
        # Keep stable order: sorted keys, drop extras over cap
        for vid in sorted(flags.keys())[args.cap :]:
            del flags[vid]
    save_course(ctx.course_path, ctx.course)
    print(f"Set targetUnmasteredVerbs to {args.cap}")
    return 0


def cmd_status(args: argparse.Namespace) -> int:
    ctx = load_course(args.course)
    filters = _parse_dimension_args(args.dimension)
    skip_2p = args.skip_second_person
    refs = filter_units(ctx.eligible, filters, skip_second_person=skip_2p)
    cap = int(ctx.active_pool.get("targetUnmasteredVerbs", 5))
    pool = open_flagged_verbs(ctx, filters, skip_second_person=skip_2p)[:cap]
    print(f"Course: {ctx.course.get('name')} ({ctx.course.get('id')})")
    print(f"Eligible units: {len(refs)}")
    if skip_2p:
        print("Person filter: skipping 2sg (tu) and 2pl (vós)")
    flagged = pool or []
    print(
        f"Flagged verbs ({cap} cap): {', '.join(flagged) or '(none — start practice to assign flags)'}"
    )

    summary = mastery_summary(
        ctx,
        group_by=args.group_by,
        filters=filters,
        skip_second_person=skip_2p,
    )
    if summary["verbs_fully_mastered"]:
        print("Fully mastered verbs:", ", ".join(summary["verbs_fully_mastered"]))

    labels = dimension_labels(ctx.library)

    print("\nVerb × tense slice (time · mood · aspect):")
    print(f"  {'verb':8} {'time':8} {'mood':11} {'aspect':11} {'persons':7} status")
    vts_groups = group_verb_tense_slice(refs)
    for (verb_id, slice_key), units in sorted(vts_groups.items()):
        st = slice_status(units, ctx.progress)
        solid, practiced, n_units = slice_progress_counts(units, ctx.progress)
        bar = format_practice_bar(practiced, n_units)
        counts = format_slice_progress_label(solid, practiced, n_units)
        mark = " *" if st == "mastered" else ""
        time_v, mood_v, aspect_v = slice_key
        print(
            f"  {verb_id:8} "
            f"{label_for(labels, 'time', time_v):8} "
            f"{label_for(labels, 'mood', mood_v):11} "
            f"{label_for(labels, 'aspect', aspect_v):11} "
            f"{bar} {counts} {st}{mark}"
        )

    print("\nCourse-wide tense slices (all verbs):")
    for slice_key, units in sorted(group_tense_slice(refs).items()):
        st = slice_status(units, ctx.progress)
        solid, practiced, n_units = slice_progress_counts(units, ctx.progress)
        bar = format_practice_bar(practiced, n_units)
        counts = format_slice_progress_label(solid, practiced, n_units)
        slice_label = " · ".join(
            label_for(labels, d, v)
            for d, v in zip(("time", "mood", "aspect"), slice_key)
        )
        mark = " COMPLETE" if st == "mastered" else ""
        print(f"  {slice_label:36} {bar} {counts} {st}{mark}")

    if args.group_by:
        print(f"\nGrouped by {args.group_by}:")
        for key, info in sorted(summary["grouped"].items()):
            bar = format_status_bar(info["solid"], info["total"])
            complete = " COMPLETE" if info["complete"] else ""
            print(f"  {key:24} {bar} {info['solid']}/{info['total']}{complete}")

    if not args.group_by:
        dim_order = [
            d["id"]
            for d in ctx.library.get("dimensionDefinitions") or []
            if d.get("id")
        ]
        for dim_id in STATUS_DIMENSION_ORDER:
            if dim_id not in dim_order:
                continue
            cells = summary["dimension_cells"].get(dim_id, {})
            if not cells:
                continue
            dim_label = next(
                (
                    d.get("label", dim_id)
                    for d in ctx.library.get("dimensionDefinitions") or []
                    if d.get("id") == dim_id
                ),
                dim_id,
            )
            print(f"\nDimension: {dim_label} ({dim_id})")
            value_order = [
                v["id"]
                for v in next(
                    (
                        d.get("values") or []
                        for d in ctx.library.get("dimensionDefinitions") or []
                        if d.get("id") == dim_id
                    ),
                    [],
                )
                if v.get("id")
            ]
            ordered_keys = [k for k in value_order if k in cells]
            ordered_keys.extend(k for k in sorted(cells) if k not in ordered_keys)
            for val_id in ordered_keys:
                info = cells[val_id]
                bar = format_status_bar(info["solid"], info["total"])
                val_label = label_for(labels, dim_id, val_id)
                complete = " COMPLETE" if info["complete"] else ""
                print(
                    f"  {val_label:16} {bar} {info['solid']}/{info['total']} "
                    f"({info['pct']}%){complete}"
                )

    return 0


def cmd_practice(args: argparse.Namespace) -> int:
    ctx = load_course(args.course)
    filters = _parse_dimension_args(args.dimension)
    count = args.count
    correct_n = 0
    attempted = 0
    prompts_done = 0

    if args.no_accents:
        require_accents = False
    elif args.strict_accents:
        require_accents = True
    else:
        require_accents = ctx.config.get("requireAccents", True)

    skip_2p = args.skip_second_person
    verb_ids = set(args.verb) if args.verb else None
    primary = ensure_flags_for_lesson(
        ctx, filters, skip_second_person=skip_2p, verb_ids=verb_ids
    )
    save_course(ctx.course_path, ctx.course)
    bits = [f"{count} prompts", format_filters(filters)]
    if skip_2p:
        bits.append("no tu/vós")
    if verb_ids:
        bits.append("verbs " + ",".join(sorted(verb_ids)))
    bits.append("accents " + ("on" if require_accents else "off"))
    if not args.no_sticky_verb:
        bits.append("sticky verb")
    print(f"Practice · {ctx.course.get('name')} · " + " · ".join(bits))
    print(f"Focus verbs: {', '.join(primary) or '(none)'}  (empty line to quit)\n")
    rng = random.Random(args.seed) if args.seed is not None else None
    sticky = not args.no_sticky_verb
    last_verb: str | None = None
    last_tense: str | None = None
    seen_units: set[str] = set()
    done = 0
    while done < count:
        item = next_prompt(
            ctx,
            filters,
            skip_second_person=skip_2p,
            verb_ids=verb_ids,
            sticky_verb=last_verb if sticky else None,
            sticky_tense=last_tense if sticky else None,
            rng=rng,
        )
        if item is None:
            print("No eligible prompts.")
            break
        ref = item["unit_ref"]
        last_verb = ref.verb_id
        last_tense = ref.tense_id
        prog = ensure_progress_keys(ctx.progress_for(ref.unit_id))
        hint = item.get("hint_en")
        disp = item["display"]
        lemma, _, rest = disp.partition(" · ")
        tag = "focus" if item.get("kind") == "focus" else "review"
        line = f"[{done + 1}/{count}] ({tag}) {rest or disp}"
        if hint:
            line += f" — {hint}"
        print(line)
        if rest:
            print(f"  Verb: {lemma}")
        if ref.unit_id in seen_units:
            print("  (same form again this session — good for memory)")
        seen_units.add(ref.unit_id)
        allow_retry = not args.no_retry_on_wrong
        used_retry = False
        while True:
            try:
                answer = input("> ").strip()
            except EOFError:
                print()
                print("Stopped.")
                return 0
            if not answer:
                print("Stopped.")
                return 0
            attempted += 1
            state_before = prog.get("state", "unknown")
            ok = grade_answer(answer, item["answers"], require_accents)
            record_attempt(prog, ok, ctx.config)
            if state_before != "unknown" and prog.get("state") == "unknown":
                print("  Note: this form was reset (rolling accuracy fell below threshold).")
            cleared = clear_mastered_flags(ctx)
            if cleared:
                print(f"  Mastered — unflagged: {', '.join(cleared)}")
                ensure_flags_for_lesson(
                    ctx, filters, skip_second_person=skip_2p, verb_ids=verb_ids
                )
            save_course(ctx.course_path, ctx.course)
            st = color_state(prog["state"])
            if ok:
                correct_n += 1
                extra = " (second try)" if used_retry else ""
                need = ctx.config.get("solidAfterConsecutiveCorrect", 5)
                cc = prog.get("consecutiveCorrect", 0)
                streak = f" · streak {cc}/{need}" if cc < need else " · solid next"
                print(f"  Correct.{extra} [{st}]{streak}\n")
                break
            expected = ", ".join(item["answers"])
            print(f"  Wrong — you: {answer!r} → expected: {expected} [{st}]")
            if allow_retry:
                allow_retry = False
                used_retry = True
                print("  Try again (same prompt):\n")
                continue
            print()
            break
        prompts_done += 1
        done += 1

    if attempted:
        pct = round(100 * correct_n / attempted)
        tail = f"{correct_n}/{attempted} correct ({pct}%)"
        if not args.no_retry_on_wrong and attempted > prompts_done:
            tail += f" · {prompts_done} prompts"
        print(f"Session: {tail}")
    else:
        print("Session: no answers recorded")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="verbpractice", description="Portuguese verb practice CLI")
    sub = parser.add_subparsers(dest="command", required=True)

    p_seed = sub.add_parser("seed-library", help="Write the seed core-50 JSON library")
    p_seed.add_argument(
        "--out",
        default="data/libraries/core-50.json",
        help="Output path for library JSON",
    )
    p_seed.set_defaults(func=cmd_seed_library)

    p_val = sub.add_parser("validate", help="Validate a verb library JSON file")
    p_val.add_argument("library", help="Path to library JSON")
    p_val.set_defaults(func=cmd_validate_library)

    p_info = sub.add_parser("library-info", help="Summarize a verb library")
    p_info.add_argument("library", help="Path to library JSON")
    p_info.set_defaults(func=cmd_library_info)

    p_init = sub.add_parser("init-course", help="Create a new course of study")
    p_init.add_argument("--library", required=True, help="Path to library JSON")
    p_init.add_argument("--out", required=True, help="Output course JSON path")
    p_init.add_argument("--course-id", default="course-1")
    p_init.add_argument("--name", default="My course")
    p_init.add_argument("--unmastered-cap", type=int, default=5)
    p_init.set_defaults(func=cmd_init_course)

    p_tenses = sub.add_parser(
        "add-tenses",
        help="Add tenseIds to course (keeps existing progress on other tenses)",
    )
    p_tenses.add_argument("--course", required=True)
    p_tenses.add_argument(
        "--tense",
        action="append",
        help="tenseId to add (repeatable). Omit to add every catalog tense not yet in the course.",
    )
    p_tenses.set_defaults(func=cmd_add_tenses)

    p_pool = sub.add_parser("set-pool", help="Set active unmastered verb cap")
    p_pool.add_argument("--course", required=True)
    p_pool.add_argument("--cap", type=int, required=True)
    p_pool.set_defaults(func=cmd_set_pool)

    p_status = sub.add_parser("status", help="Show progress and mastery grids")
    p_status.add_argument("--course", required=True)
    p_status.add_argument(
        "--dimension",
        action="append",
        help="Filter/practice slice, e.g. time=present (repeatable)",
    )
    p_status.add_argument(
        "--group-by",
        help="Dimension id for grouped completion (time, person, mood, ...)",
    )
    p_status.add_argument(
        "--skip-second-person",
        action="store_true",
        help="Exclude tu (2sg) and vós (2pl); keep eu, você/ele, nós, vocês/eles",
    )
    p_status.set_defaults(func=cmd_status)

    p_practice = sub.add_parser("practice", help="Run a practice session")
    p_practice.add_argument("--course", required=True)
    p_practice.add_argument("--count", type=int, default=20, help="Number of prompts")
    p_practice.add_argument(
        "--seed",
        type=int,
        default=None,
        help="Random seed for prompt order (repeatable sessions)",
    )
    p_practice.add_argument("--dimension", action="append")
    accent = p_practice.add_mutually_exclusive_group()
    accent.add_argument(
        "--no-accents",
        action="store_true",
        help="Ignore accents for this session (e.g. e = é)",
    )
    accent.add_argument(
        "--strict-accents",
        action="store_true",
        help="Require accents for this session (overrides course if set)",
    )
    p_practice.add_argument(
        "--skip-second-person",
        action="store_true",
        help="Exclude tu (2sg) and vós (2pl); keep eu, você/ele, nós, vocês/eles",
    )
    p_practice.add_argument(
        "--no-retry-on-wrong",
        action="store_true",
        help="Do not re-prompt after a wrong answer (default: one retry)",
    )
    p_practice.add_argument(
        "--verb",
        action="append",
        help="Limit to verb id(s), e.g. --verb falar (repeatable)",
    )
    p_practice.add_argument(
        "--no-sticky-verb",
        action="store_true",
        help="Jump between verbs freely; default keeps ~80%% of prompts on same verb",
    )
    p_practice.set_defaults(func=cmd_practice)

    args = parser.parse_args(argv)
    try:
        return args.func(args)
    except ValidationError as e:
        print(f"Validation error:\n{e}", file=sys.stderr)
        return 1
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
