#!/usr/bin/env python3
"""Exercise verbpractice CLI like a learner: flags, pauses, status, random misses."""

from __future__ import annotations

import random
import re
import subprocess
import sys
import time
from dataclasses import dataclass, field
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_COURSE = ROOT / "data/courses/default.json"
LOG = ROOT / "UX_HARNESS_LOG.md"
HARNESS_LOCK = ROOT / "data/courses/.harness.lock"
VP = [sys.executable, "-m", "verbpractice"]


@dataclass
class Scenario:
    name: str
    args: list[str]
    stdin: str = ""
    expect_in_stdout: list[str] = field(default_factory=list)
    expect_exit: int = 0


def run_vp(extra: list[str], stdin: str = "", cwd: Path = ROOT) -> subprocess.CompletedProcess:
    return subprocess.run(
        VP + extra,
        input=stdin,
        capture_output=True,
        text=True,
        cwd=cwd,
        timeout=120,
    )


def append_log(lines: list[str]) -> None:
    LOG.parent.mkdir(parents=True, exist_ok=True)
    with LOG.open("a", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")


def check_scenario(s: Scenario) -> tuple[bool, str]:
    proc = run_vp(s.args, s.stdin)
    ok = proc.returncode == s.expect_exit
    out = proc.stdout + proc.stderr
    for needle in s.expect_in_stdout:
        if needle not in out:
            ok = False
            return ok, f"{s.name}: missing {needle!r} in output\n{out[:800]}"
    if not ok:
        return False, f"{s.name}: exit {proc.returncode}\n{out[:800]}"
    return True, f"{s.name}: ok"


def learner_pipe(
    count: int,
    extra_args: list[str],
    *,
    course: Path,
    seed: int,
    verb: str | None,
    wrong_first: bool = True,
    quit_after: int | None = None,
    garbage: bool = False,
) -> str:
    """Build stdin: optional quit early, else wrong then correct per prompt."""
    from verbpractice.load import load_course
    from verbpractice.select import next_prompt
    from verbpractice.verb_flags import ensure_flags_for_lesson

    sys.path.insert(0, str(ROOT))
    ctx = load_course(str(course))
    filters = {}
    for a in extra_args:
        if a.startswith("--dimension") or "=" in a:
            continue
    # parse dimensions from extra_args
    dims: list[str] = []
    i = 0
    while i < len(extra_args):
        if extra_args[i] == "--dimension" and i + 1 < len(extra_args):
            dims.append(extra_args[i + 1])
            i += 2
            continue
        i += 1
    for d in dims:
        k, v = d.split("=", 1)
        filters[k] = v

    skip_2p = "--skip-second-person" in extra_args
    verb_ids = {verb} if verb else None
    ensure_flags_for_lesson(
        ctx, filters or None, skip_second_person=skip_2p, verb_ids=verb_ids
    )
    rng = random.Random(seed)
    lv, lt = None, None
    lines: list[str] = []
    sticky = "--no-sticky-verb" not in extra_args
    n = quit_after if quit_after is not None else count
    for _ in range(n):
        item = next_prompt(
            ctx,
            filters or None,
            skip_second_person=skip_2p,
            verb_ids=verb_ids,
            sticky_verb=lv if sticky else None,
            sticky_tense=lt if sticky else None,
            rng=rng,
        )
        if not item:
            break
        r = item["unit_ref"]
        lv, lt = r.verb_id, r.tense_id
        if garbage:
            lines.append(rng.choice(["!!!", "###", "???", "xxx", "WRONG"]))
        elif wrong_first and rng.random() < 0.85:
            lines.append("WRONG")
        else:
            lines.append(item["answers"][0])
        if "--no-retry-on-wrong" not in extra_args and (wrong_first or garbage):
            lines.append(item["answers"][0])
    if quit_after is not None:
        lines.append("")
    return "\n".join(lines) + "\n"


def run_batch(course: Path) -> tuple[int, int]:
    scenarios: list[Scenario] = [
        Scenario("validate-lib", ["validate", str(ROOT / "data/libraries/core-50.json")]),
        Scenario(
            "status-default",
            ["status", "--course", str(course)],
            expect_in_stdout=["Eligible units:", "practiced"],
        ),
        Scenario(
            "status-present",
            [
                "status",
                "--course",
                str(course),
                "--dimension",
                "time=present",
                "--dimension",
                "mood=indicative",
                "--skip-second-person",
            ],
            expect_in_stdout=["Person filter"],
        ),
        Scenario(
            "library-info",
            ["library-info", str(ROOT / "data/libraries/core-50.json")],
            expect_in_stdout=["Tense catalog"],
        ),
    ]

    flag_matrix: list[tuple[str, list[str]]] = [
        ("bare-min", []),
        ("no-accents", ["--no-accents"]),
        ("strict-acc", ["--strict-accents"]),
        ("skip-2p", ["--no-accents", "--skip-second-person"]),
        ("dim-present-ind", [
            "--no-accents",
            "--skip-second-person",
            "--dimension",
            "time=present",
            "--dimension",
            "mood=indicative",
        ]),
        ("verb-falar", ["--no-accents", "--skip-second-person", "--verb", "falar"]),
        ("verb-ser", ["--no-accents", "--skip-second-person", "--verb", "ser"]),
        ("no-sticky", ["--no-accents", "--verb", "falar", "--no-sticky-verb"]),
        ("no-retry", ["--no-accents", "--verb", "falar", "--no-retry-on-wrong"]),
        ("seed-42", ["--no-accents", "--verb", "comer", "--seed", "42"]),
        ("future-subj", [
            "--no-accents",
            "--dimension",
            "time=future",
            "--dimension",
            "mood=subjunctive",
            "--count",
            "3",
        ]),
        ("imperative", [
            "--no-accents",
            "--dimension",
            "mood=imperative",
            "--count",
            "3",
        ]),
        ("preterite-ind", [
            "--no-accents",
            "--skip-second-person",
            "--dimension",
            "time=past",
            "--dimension",
            "mood=indicative",
            "--dimension",
            "aspect=perfective",
            "--verb",
            "falar",
        ]),
        ("imperfect-ind", [
            "--no-accents",
            "--skip-second-person",
            "--dimension",
            "time=past",
            "--dimension",
            "mood=indicative",
            "--dimension",
            "aspect=imperfective",
            "--verb",
            "comer",
        ]),
        ("multi-verb", [
            "--no-accents",
            "--skip-second-person",
            "--verb",
            "ser",
            "--verb",
            "partir",
            "--count",
            "4",
        ]),
        ("count-1", ["--no-accents", "--verb", "falar", "--count", "1"]),
        ("present-subj", [
            "--no-accents",
            "--skip-second-person",
            "--dimension",
            "time=present",
            "--dimension",
            "mood=subjunctive",
            "--verb",
            "ser",
            "--count",
            "3",
        ]),
    ]

    passed = 0
    failed = 0
    batch = [f"\n## Batch {time.strftime('%H:%M:%S')}"]

    for s in scenarios:
        ok, msg = check_scenario(s)
        batch.append(f"- {msg}")
        passed += ok
        failed += not ok

    for name, flags in flag_matrix:
        count = "5"
        if any(x.startswith("--count") for x in flags):
            count = next(flags[i + 1] for i, x in enumerate(flags) if x == "--count")
        args = [
            "practice",
            "--course",
            str(course),
            "--count",
            count if count else "5",
        ] + flags
        if "--count" not in flags:
            args[4] = "6"
        seed = hash(name) % 10000
        if "--seed" not in flags:
            args.extend(["--seed", str(seed)])
        verb = None
        if "--verb" in flags:
            verb = flags[flags.index("--verb") + 1]
        try:
            stdin = learner_pipe(
                int(args[args.index("--count") + 1]),
                args,
                course=course,
                seed=seed,
                verb=verb,
            )
        except Exception as e:
            batch.append(f"- FAIL {name}: precompute {e}")
            failed += 1
            continue
        proc = run_vp(args, stdin)
        out = proc.stdout
        ok = proc.returncode == 0 and "Session:" in out
        if ok and "Traceback" in proc.stderr:
            ok = False
        batch.append(
            f"- practice/{name}: {'ok' if ok else 'FAIL rc='+str(proc.returncode)} "
            f"({re.search(r'Session:.*', out).group(0) if ok else out[:120]!r})"
        )
        passed += ok
        failed += not ok
        # pause + status between some runs
        if name in ("verb-falar", "dim-present-ind", "imperative"):
            st = run_vp(["status", "--course", str(course), "--skip-second-person"])
            batch.append(
                f"- status after {name}: {'ok' if st.returncode == 0 else 'FAIL'}"
            )
        time.sleep(0.05)

    # pause: quit on empty line
    quit_stdin = learner_pipe(
        10,
        ["--no-accents", "--verb", "partir"],
        course=course,
        seed=1,
        verb="partir",
        quit_after=2,
    )
    proc = run_vp(
        ["practice", "--course", str(course), "--count", "10", "--no-accents", "--verb", "partir"],
        quit_stdin,
    )
    ok = proc.returncode == 0 and "Stopped." in proc.stdout
    batch.append(f"- pause/empty-quit: {'ok' if ok else 'FAIL'}")
    passed += ok
    failed += not ok

    # retry skip: wrong then empty on retry
    proc = run_vp(
        [
            "practice",
            "--course",
            str(course),
            "--count",
            "1",
            "--no-accents",
            "--verb",
            "falar",
        ],
        "bad\n\n",
    )
    ok = "Stopped." in proc.stdout
    batch.append(f"- pause/empty-on-retry-quits: {'ok' if ok else 'FAIL'}")
    passed += ok
    failed += not ok

    # random garbage failures (stdin matched to seed via learner_pipe)
    mix_args = [
        "practice",
        "--course",
        str(course),
        "--count",
        "4",
        "--no-accents",
        "--verb",
        "ser",
        "--seed",
        "777",
    ]
    mix_stdin = learner_pipe(
        4, mix_args, course=course, seed=777, verb="ser", garbage=True
    )
    proc = run_vp(mix_args, mix_stdin)
    ok = proc.returncode == 0 and "Wrong" in proc.stdout and "Session:" in proc.stdout
    batch.append(f"- random-fail-mix: {'ok' if ok else 'FAIL'}")
    passed += ok
    failed += not ok

    proc = run_vp(
        ["set-pool", "--course", str(course), "--cap", "2"]
    )
    batch.append(f"- set-pool/cap-2: {'ok' if proc.returncode == 0 else 'FAIL'}")
    passed += proc.returncode == 0
    failed += proc.returncode != 0
    st = run_vp(["status", "--course", str(course)])
    ok = st.returncode == 0 and "Eligible units:" in st.stdout
    batch.append(f"- status-after-set-pool: {'ok' if ok else 'FAIL'}")
    passed += ok
    failed += not ok

    proc = run_vp(
        [
            "practice",
            "--course",
            str(course),
            "--count",
            "5",
            "--no-accents",
            "--verb",
            "falar",
        ],
        "",
    )
    ok = proc.returncode == 0 and "Stopped." in proc.stdout
    batch.append(f"- pause/immediate-eof: {'ok' if ok else 'FAIL'}")
    passed += ok
    failed += not ok

    proc = run_vp(["set-pool", "--course", str(course), "--cap", "5"])
    batch.append(
        f"- set-pool/restore-cap-5: {'ok' if proc.returncode == 0 else 'FAIL'}"
    )
    passed += proc.returncode == 0
    failed += proc.returncode != 0

    batch.append(f"\n**Totals:** {passed} passed, {failed} failed")
    append_log(batch)
    print("\n".join(batch))
    return passed, failed


def acquire_harness_lock(wait: bool) -> int | None:
    """Return open lock file handle, or None if another harness holds the lock."""
    try:
        import fcntl
    except ImportError:
        return -1  # sentinel: no lock

    HARNESS_LOCK.parent.mkdir(parents=True, exist_ok=True)
    lf = HARNESS_LOCK.open("w", encoding="utf-8")
    flags = fcntl.LOCK_EX | (0 if wait else fcntl.LOCK_NB)
    try:
        fcntl.flock(lf, flags)
    except BlockingIOError:
        lf.close()
        return None
    lf.write(str(time.time()) + "\n")
    lf.flush()
    return lf  # type: ignore[return-value]


def main() -> int:
    import argparse

    ap = argparse.ArgumentParser(description="Long-run learner harness")
    ap.add_argument("--loops", type=int, default=1, help="Repeat full batch N times")
    ap.add_argument("--sleep", type=float, default=0.0, help="Seconds between loops")
    ap.add_argument(
        "--course",
        type=Path,
        default=DEFAULT_COURSE,
        help="Course JSON to exercise (default: data/courses/default.json)",
    )
    ap.add_argument(
        "--wait-lock",
        action="store_true",
        help="Wait for harness lock instead of exiting if another run is active",
    )
    args = ap.parse_args()
    course = args.course.resolve()

    lock = acquire_harness_lock(args.wait_lock)
    if lock is None:
        print("Another harness is running (see data/courses/.harness.lock)", file=sys.stderr)
        return 2

    if not LOG.exists():
        append_log(["# Harness log", f"Started {time.strftime('%Y-%m-%d %H:%M:%S')}"])

    total_fail = 0
    try:
        for loop in range(args.loops):
            if args.loops > 1:
                append_log([f"\n### Loop {loop + 1}/{args.loops}"])
            passed, failed = run_batch(course)
            total_fail += failed
            if args.sleep and loop + 1 < args.loops:
                time.sleep(args.sleep)
    finally:
        if lock not in (None, -1):
            import fcntl

            fcntl.flock(lock, fcntl.LOCK_UN)
            lock.close()
    return 1 if total_fail else 0


if __name__ == "__main__":
    raise SystemExit(main())
