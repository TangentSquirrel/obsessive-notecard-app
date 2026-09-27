#!/usr/bin/env python3
"""Golden contract tests — same scenarios for CLI engine and (later) Android."""

from __future__ import annotations

import json
import shutil
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONTRACT_DIR = ROOT / "data/contract"
LIBRARY = ROOT / "data/libraries/core-50.json"


def run_scenario(spec: dict) -> dict:
    from verbpractice.course_init import init_course
    from verbpractice.load import load_course
    from verbpractice.practice_session import PracticeOptions, PracticeSession

    tmp = Path(tempfile.mkdtemp(prefix="vp-contract-"))
    course_path = tmp / "course.json"
    try:
        init_course(
            LIBRARY,
            course_path,
            course_id="contract",
            name="Contract",
            unmastered_cap=5,
        )
        ctx = load_course(course_path)
        opts = PracticeOptions(
            count=spec["count"],
            filters=spec.get("filters"),
            skip_second_person=spec.get("skip_second_person", False),
            verb_ids=set(spec["verbs"]) if spec.get("verbs") else None,
            seed=spec.get("seed"),
            require_accents=spec.get("require_accents", False),
            retry_on_wrong=spec.get("retry_on_wrong", True),
            sticky_verb=spec.get("sticky_verb", True),
        )
        session = PracticeSession(ctx, opts)
        session.start()
        prompts: list[dict] = []
        for _ in range(spec["count"]):
            view = session.current_prompt()
            if view is None:
                break
            prompts.append(
                {
                    "unit_id": view.unit_id,
                    "verb_id": view.verb_id,
                    "tense_id": view.tense_id,
                    "expected_answer": view.answers[0],
                }
            )
            session.submit(view.answers[0])
        return {"prompts": prompts, "summary": session.session_summary()}
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def main() -> int:
    path = CONTRACT_DIR / "practice-baseline.json"
    if not path.is_file():
        print(f"Missing {path}", file=sys.stderr)
        return 1
    spec = json.loads(path.read_text(encoding="utf-8"))
    expected = spec.get("expected")
    if not expected:
        print("Recording expected output (-- record mode)")
        out = run_scenario(spec)
        spec["expected"] = out
        path.write_text(json.dumps(spec, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        print(f"Wrote expected prompts to {path}")
        return 0
    actual = run_scenario(spec)
    if actual != expected:
        print("Contract FAIL", file=sys.stderr)
        print("expected:", json.dumps(expected, indent=2)[:1200], file=sys.stderr)
        print("actual:  ", json.dumps(actual, indent=2)[:1200], file=sys.stderr)
        return 1
    print(f"Contract ok ({len(expected['prompts'])} prompts)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
