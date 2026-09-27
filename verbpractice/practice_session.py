"""UI-agnostic practice session (CLI, Android via Chaquopy, contract tests)."""

from __future__ import annotations

import random
from dataclasses import dataclass, field
from typing import Any

from verbpractice.grade import grade_answer
from verbpractice.mastery import ensure_progress_keys, record_attempt
from verbpractice.models import CourseContext
from verbpractice.select import next_prompt
from verbpractice.verb_flags import clear_mastered_flags, ensure_flags_for_lesson


@dataclass
class PracticeOptions:
    count: int = 20
    filters: dict[str, str] | None = None
    skip_second_person: bool = False
    verb_ids: set[str] | None = None
    seed: int | None = None
    require_accents: bool | None = None
    retry_on_wrong: bool = True
    sticky_verb: bool = True


@dataclass
class PracticePromptView:
    index: int
    total: int
    kind: str
    display: str
    lemma: str
    detail: str
    unit_id: str
    verb_id: str
    tense_id: str
    answers: list[str]
    hint_en: str | None = None
    repeat_in_session: bool = False


@dataclass
class SubmitResult:
    correct: bool
    expected: str
    state: str
    consecutive_correct: int
    used_retry: bool
    retry_available: bool
    rolling_reset: bool
    cleared_flags: list[str]
    session_complete: bool
    prompts_finished: int
    correct_total: int
    attempts_total: int


@dataclass
class PracticeSession:
    ctx: CourseContext
    options: PracticeOptions
    focus_verbs: list[str] = field(default_factory=list)
    _rng: random.Random | None = None
    _last_verb: str | None = None
    _last_tense: str | None = None
    _seen_units: set[str] = field(default_factory=set)
    _done: int = 0
    _correct: int = 0
    _attempts: int = 0
    _current: dict[str, Any] | None = None
    _allow_retry: bool = True
    _used_retry: bool = False
    _require_accents: bool = True

    def start(self) -> list[str]:
        if self.options.require_accents is None:
            self._require_accents = bool(self.ctx.config.get("requireAccents", True))
        else:
            self._require_accents = self.options.require_accents
        self._rng = random.Random(self.options.seed) if self.options.seed is not None else None
        self.focus_verbs = ensure_flags_for_lesson(
            self.ctx,
            self.options.filters,
            skip_second_person=self.options.skip_second_person,
            verb_ids=self.options.verb_ids,
        )
        return list(self.focus_verbs)

    def _pick_next(self) -> bool:
        if self._done >= self.options.count:
            self._current = None
            return False
        sticky = self.options.sticky_verb
        item = next_prompt(
            self.ctx,
            self.options.filters,
            skip_second_person=self.options.skip_second_person,
            verb_ids=self.options.verb_ids,
            sticky_verb=self._last_verb if sticky else None,
            sticky_tense=self._last_tense if sticky else None,
            rng=self._rng,
        )
        if item is None:
            self._current = None
            return False
        ref = item["unit_ref"]
        self._last_verb = ref.verb_id
        self._last_tense = ref.tense_id
        self._allow_retry = self.options.retry_on_wrong
        self._used_retry = False
        item = {**item, "_repeat": ref.unit_id in self._seen_units}
        self._seen_units.add(ref.unit_id)
        self._current = item
        return True

    def current_prompt(self) -> PracticePromptView | None:
        if self._current is None:
            if self._done >= self.options.count:
                return None
            if not self._pick_next():
                return None
        item = self._current
        ref = item["unit_ref"]
        disp = item["display"]
        lemma, _, rest = disp.partition(" · ")
        repeat = bool(item.get("_repeat"))
        prog = ensure_progress_keys(self.ctx.progress_for(ref.unit_id))
        return PracticePromptView(
            index=self._done + 1,
            total=self.options.count,
            kind=item.get("kind") or "focus",
            display=disp,
            lemma=lemma or ref.lemma,
            detail=rest or disp,
            unit_id=ref.unit_id,
            verb_id=ref.verb_id,
            tense_id=ref.tense_id,
            answers=list(item["answers"]),
            hint_en=item.get("hint_en"),
            repeat_in_session=repeat,
        )

    def submit(self, answer: str) -> SubmitResult:
        if self._current is None:
            raise RuntimeError("No active prompt")
        item = self._current
        ref = item["unit_ref"]
        prog = ensure_progress_keys(self.ctx.progress_for(ref.unit_id))
        state_before = prog.get("state", "unknown")
        self._attempts += 1
        ok = grade_answer(answer, item["answers"], self._require_accents)
        record_attempt(prog, ok, self.ctx.config)
        rolling_reset = state_before != "unknown" and prog.get("state") == "unknown"
        cleared = clear_mastered_flags(self.ctx)
        if cleared:
            ensure_flags_for_lesson(
                self.ctx,
                self.options.filters,
                skip_second_person=self.options.skip_second_person,
                verb_ids=self.options.verb_ids,
            )
        expected = ", ".join(item["answers"])
        need = int(self.ctx.config.get("solidAfterConsecutiveCorrect", 5))
        cc = int(prog.get("consecutiveCorrect", 0))
        if ok:
            self._correct += 1
            self._done += 1
            self._current = None
            self._pick_next()
            return SubmitResult(
                correct=True,
                expected=expected,
                state=str(prog.get("state", "unknown")),
                consecutive_correct=cc,
                used_retry=self._used_retry,
                retry_available=False,
                rolling_reset=rolling_reset,
                cleared_flags=cleared,
                session_complete=self._done >= self.options.count or self._current is None,
                prompts_finished=self._done,
                correct_total=self._correct,
                attempts_total=self._attempts,
            )
        retry_avail = self._allow_retry
        if self._allow_retry:
            self._allow_retry = False
            self._used_retry = True
        else:
            self._done += 1
            self._current = None
            self._pick_next()
        return SubmitResult(
            correct=False,
            expected=expected,
            state=str(prog.get("state", "unknown")),
            consecutive_correct=cc,
            used_retry=self._used_retry and not ok,
            retry_available=retry_avail,
            rolling_reset=rolling_reset,
            cleared_flags=cleared,
            session_complete=self._done >= self.options.count
            or (self._current is None and not retry_avail),
            prompts_finished=self._done,
            correct_total=self._correct,
            attempts_total=self._attempts,
        )

    def session_summary(self) -> dict[str, Any]:
        return {
            "correct": self._correct,
            "attempts": self._attempts,
            "prompts": self._done,
        }
