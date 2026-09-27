#!/usr/bin/env bash
# Run verbpractice using only this project's .venv (never global pip/python tools).
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
VENV="$ROOT/.venv"

if [[ ! -x "$VENV/bin/python" ]]; then
  echo "Creating local venv at $VENV ..."
  python3 -m venv "$VENV"
  "$VENV/bin/pip" install -e "$ROOT"
fi

exec "$VENV/bin/python" -m verbpractice "$@"
