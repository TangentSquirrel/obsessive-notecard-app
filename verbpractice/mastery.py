from __future__ import annotations

from datetime import datetime, timezone
from typing import Any

from verbpractice.models import default_unit_progress


def _rolling_accuracy(history: list[bool], window: int) -> float | None:
    if not history:
        return None
    slice_ = history[-window:]
    return sum(slice_) / len(slice_)


def record_attempt(
    progress: dict[str, Any], correct: bool, config: dict[str, Any]
) -> None:
    if not progress.get("attempts"):
        if progress.get("state") == "unknown":
            progress["state"] = "learning"

    progress["attempts"] = progress.get("attempts", 0) + 1
    if correct:
        progress["correct"] = progress.get("correct", 0) + 1
        progress["consecutiveCorrect"] = progress.get("consecutiveCorrect", 0) + 1
        progress["consecutiveWrong"] = 0
    else:
        progress["consecutiveWrong"] = progress.get("consecutiveWrong", 0) + 1
        progress["consecutiveCorrect"] = 0

    history: list[bool] = progress.setdefault("history", [])
    history.append(correct)
    max_hist = max(config.get("rollingWindowAttempts", 10) * 2, 20)
    if len(history) > max_hist:
        progress["history"] = history[-max_hist:]

    progress["lastSeenAt"] = datetime.now(timezone.utc).isoformat()

    _apply_state_transitions(progress, config)


def _apply_state_transitions(progress: dict[str, Any], config: dict[str, Any]) -> None:
    state = progress.get("state", "unknown")
    window = config.get("rollingWindowAttempts", 10)
    threshold = config.get("resetIfRollingAccuracyBelow", 0.5)
    history = progress.get("history") or []
    acc = _rolling_accuracy(history, window)
    # Do not zero a fresh correct streak on the same turn the learner got it right.
    if (
        acc is not None
        and len(history) >= window
        and acc < threshold
        and not history[-1]
    ):
        progress["state"] = "unknown"
        progress["consecutiveCorrect"] = 0
        progress["consecutiveWrong"] = 0
        return

    solid_after = config.get("solidAfterConsecutiveCorrect", 5)
    review_after = config.get("reviewAfterConsecutiveWrong", 3)
    recover = config.get("reviewRecoverAfterConsecutiveCorrect", 2)

    if progress.get("consecutiveWrong", 0) >= review_after:
        progress["state"] = "review"
        return

    if state == "review" and progress.get("consecutiveCorrect", 0) >= recover:
        progress["state"] = "learning"

    if progress.get("consecutiveCorrect", 0) >= solid_after:
        progress["state"] = "solid"


def ensure_progress_keys(progress: dict[str, Any]) -> dict[str, Any]:
    base = default_unit_progress()
    for k, v in base.items():
        progress.setdefault(k, v if not isinstance(v, list) else list(v))
    return progress
