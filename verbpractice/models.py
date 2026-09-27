from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

STATES = frozenset({"unknown", "learning", "solid", "review"})


def default_unit_progress() -> dict[str, Any]:
    return {
        "state": "unknown",
        "consecutiveCorrect": 0,
        "consecutiveWrong": 0,
        "attempts": 0,
        "correct": 0,
        "history": [],
    }


def default_course_config() -> dict[str, Any]:
    return {
        "requireAccents": True,
        "solidAfterConsecutiveCorrect": 5,
        "reviewAfterConsecutiveWrong": 3,
        "reviewRecoverAfterConsecutiveCorrect": 2,
        "resetIfRollingAccuracyBelow": 0.5,
        "rollingWindowAttempts": 10,
        "solidSamplingWeight": 0.05,
        "reviewBoostWeight": 3.0,
        "scheduling": {
            "primaryShare": 0.85,
            "maintenanceShare": 0.15,
            "maintenanceWeights": {
                "review": 0.5,
                "unknown": 0.2,
                "solid": 0.3,
            },
        },
    }


def default_active_pool(unmastered_cap: int = 5) -> dict[str, Any]:
    return {
        "targetUnmasteredVerbs": unmastered_cap,
        "selection": "auto",
        "pinnedVerbIds": [],
    }


@dataclass
class UnitRef:
    unit_id: str
    verb_id: str
    lemma: str
    tense_id: str
    unit: dict[str, Any]

    @property
    def dimensions(self) -> dict[str, str]:
        return self.unit.get("dimensions") or {}


@dataclass
class CourseContext:
    course_path: str
    course: dict[str, Any]
    library: dict[str, Any]
    eligible: list[UnitRef] = field(default_factory=list)

    @property
    def config(self) -> dict[str, Any]:
        return self.course.setdefault("config", default_course_config())

    @property
    def active_pool(self) -> dict[str, Any]:
        return self.course.setdefault("activePool", default_active_pool())

    @property
    def progress(self) -> dict[str, Any]:
        return self.course.setdefault("progress", {})

    def progress_for(self, unit_id: str) -> dict[str, Any]:
        if unit_id not in self.progress:
            self.progress[unit_id] = default_unit_progress()
        return self.progress[unit_id]
