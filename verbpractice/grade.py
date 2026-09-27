from __future__ import annotations

import unicodedata
from typing import Iterable


def normalize_answer(text: str, require_accents: bool) -> str:
    text = text.strip().lower()
    text = unicodedata.normalize("NFC", text)
    if not require_accents:
        text = "".join(
            c for c in unicodedata.normalize("NFD", text) if unicodedata.category(c) != "Mn"
        )
    return text


def grade_answer(
    user_input: str, accepted: Iterable[str], require_accents: bool
) -> bool:
    normalized_user = normalize_answer(user_input, require_accents)
    for ans in accepted:
        if normalize_answer(ans, require_accents) == normalized_user:
            return True
    return False
