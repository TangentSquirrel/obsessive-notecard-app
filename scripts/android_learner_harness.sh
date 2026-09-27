#!/usr/bin/env bash
# Recursive Android QA entrypoint (run on a machine with Android SDK + emulator/device).
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

PY="${ROOT}/.venv/bin/python"
LOG="${ROOT}/ANDROID_HARNESS_LOG.md"

echo "## $(date -Iseconds)" | tee -a "$LOG"
echo "- contract_harness" | tee -a "$LOG"
"$PY" scripts/contract_harness.py | tee -a "$LOG"

if [[ ! -d "${ROOT}/android/app" ]]; then
  echo "- gradle: SKIP (android/app not scaffolded yet)" | tee -a "$LOG"
  exit 0
fi

echo "- connectedDebugAndroidTest" | tee -a "$LOG"
(cd android && ./gradlew connectedDebugAndroidTest) 2>&1 | tee -a "$LOG"
