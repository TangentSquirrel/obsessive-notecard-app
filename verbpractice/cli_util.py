"""Small helpers shared by CLI commands."""

from __future__ import annotations

import sys

USE_COLOR = sys.stdout.isatty()
_COLORS = {
    "unknown": "\033[90m",
    "learning": "\033[33m",
    "solid": "\033[32m",
    "review": "\033[31m",
}


def color_state(state: str) -> str:
    if not USE_COLOR:
        return state
    return f"{_COLORS.get(state, '')}{state}\033[0m"


def format_filters(filters: dict[str, str]) -> str:
    if not filters:
        return "(none — all eligible tenses/persons)"
    return ", ".join(f"{k}={v}" for k, v in sorted(filters.items()))
