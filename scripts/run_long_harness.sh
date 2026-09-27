#!/usr/bin/env bash
# Long-run learner QA (run from project root, inside venv or uses .venv/bin/python).
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"
PY="${ROOT}/.venv/bin/python"
LOOPS="${1:-60}"
SLEEP="${2:-15}"
echo "Starting harness: loops=$LOOPS sleep=${SLEEP}s — log UX_HARNESS_LOG.md"
exec "$PY" scripts/learner_harness.py --wait-lock --loops "$LOOPS" --sleep "$SLEEP"
