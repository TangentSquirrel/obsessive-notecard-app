#!/usr/bin/env python3
"""One random learner spot-check (for manual long-run QA)."""

from __future__ import annotations

import random
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
COURSE = ROOT / "data/courses/default.json"
VP = [sys.executable, "-m", "verbpractice"]


def main() -> int:
    seeds = list(range(1, 500))
    verbs = ["ser", "falar", "comer", "partir"]
    packs = [
        ["--no-accents", "--skip-second-person"],
        ["--strict-accents", "--skip-second-person", "--verb", random.choice(verbs)],
        [
            "--no-accents",
            "--dimension",
            "time=present",
            "--dimension",
            "mood=indicative",
            "--skip-second-person",
        ],
        ["--no-accents", "--no-sticky-verb", "--verb", random.choice(verbs)],
        ["--no-accents", "--no-retry-on-wrong", "--verb", random.choice(verbs)],
        [
            "--no-accents",
            "--dimension",
            "mood=imperative",
            "--count",
            "4",
        ],
    ]
    flags = random.choice(packs)
    seed = random.choice(seeds)
    count = next((flags[i + 1] for i, x in enumerate(flags) if x == "--count"), "7")
    if "--count" not in flags:
        flags = ["--count", count] + flags

    sys.path.insert(0, str(ROOT / "scripts"))
    from learner_harness import learner_pipe  # noqa: PLC0415

    args = ["practice", "--course", str(COURSE), "--seed", str(seed)] + flags
    verb = None
    if "--verb" in flags:
        verb = flags[flags.index("--verb") + 1]
    stdin = learner_pipe(int(count), args, course=COURSE, seed=seed, verb=verb)
    proc = subprocess.run(
        VP + args,
        input=stdin,
        capture_output=True,
        text=True,
        cwd=ROOT,
        timeout=120,
    )
    ok = proc.returncode == 0 and (
        "Session:" in proc.stdout or "Stopped." in proc.stdout
    )
    tag = "ok" if ok else "FAIL"
    print(f"spot {tag} seed={seed} flags={' '.join(flags)}")
    if not ok:
        print(proc.stdout[:400], proc.stderr[:200])
    subprocess.run(
        VP + ["status", "--course", str(COURSE), "--skip-second-person"],
        cwd=ROOT,
        timeout=60,
    )
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
