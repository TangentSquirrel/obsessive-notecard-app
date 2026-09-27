from __future__ import annotations

import json
import os
from contextlib import contextmanager
from pathlib import Path
from typing import Any, Iterator

try:
    import fcntl
except ImportError:  # pragma: no cover
    fcntl = None  # type: ignore[assignment]


def _lock_path(course_path: Path) -> Path:
    return course_path.with_suffix(course_path.suffix + ".lock")


@contextmanager
def course_file_lock(course_path: str | Path, *, exclusive: bool) -> Iterator[None]:
    """Serialize course JSON reads/writes (multiple CLI / harness processes)."""
    path = Path(course_path)
    if fcntl is None:
        yield
        return
    lock = _lock_path(path)
    lock.parent.mkdir(parents=True, exist_ok=True)
    with lock.open("w", encoding="utf-8") as lf:
        fcntl.flock(lf, fcntl.LOCK_EX if exclusive else fcntl.LOCK_SH)
        try:
            yield
        finally:
            fcntl.flock(lf, fcntl.LOCK_UN)


def load_course_json(course_path: str | Path) -> dict[str, Any]:
    path = Path(course_path)
    with course_file_lock(path, exclusive=False):
        with path.open(encoding="utf-8") as f:
            return json.load(f)


def save_course(course_path: str | Path, course: dict[str, Any]) -> None:
    path = Path(course_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    with course_file_lock(path, exclusive=True):
        with tmp.open("w", encoding="utf-8") as f:
            json.dump(course, f, indent=2, ensure_ascii=False)
            f.write("\n")
        os.replace(tmp, path)
