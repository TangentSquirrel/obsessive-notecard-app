#!/usr/bin/env bash
# Run ON marmot (or via: ssh marmot 'bash -lc "$HOME/Dev/.../deploy.sh"').
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="${REPO_ROOT:-$(cd "$SCRIPT_DIR/../../../.." && pwd)}"
ANDROID_DIR="$REPO_ROOT/android"

DO_PULL=1
DO_BUILD=1
for arg in "$@"; do
  case "$arg" in
    --pull) DO_BUILD=0 ;;
    --build) DO_PULL=0 ;;
    -h | --help)
      echo "Usage: deploy.sh [--pull|--build]  (default: pull + assembleDebug)"
      exit 0
      ;;
    *)
      echo "Unknown arg: $arg" >&2
      exit 2
      ;;
  esac
done

log() { printf '[deploy] %s\n' "$*"; }

require_cmd() {
  if ! command -v "$1" >/dev/null 2>&1; then
    log "missing command: $1"
    exit 1
  fi
}

if [[ ! -d "$REPO_ROOT/.git" ]]; then
  log "REPO_ROOT is not a git checkout: $REPO_ROOT"
  exit 1
fi

if [[ "$DO_PULL" -eq 1 ]]; then
  require_cmd git
  log "git pull (ff-only) in $REPO_ROOT"
  git -C "$REPO_ROOT" pull --ff-only
fi

if [[ "$DO_BUILD" -eq 1 ]]; then
  if [[ ! -f "$ANDROID_DIR/gradlew" ]]; then
    log "Android project not ready (no $ANDROID_DIR/gradlew). Scaffold android/ first."
    exit 1
  fi
  require_cmd java
  if [[ -z "${ANDROID_HOME:-}" ]]; then
    log "ANDROID_HOME is not set (see scripts/deploy/marmot/README.md)"
    exit 1
  fi
  log "assembleDebug in $ANDROID_DIR"
  cd "$ANDROID_DIR"
  chmod +x gradlew
  ./gradlew --no-daemon assembleDebug
  APK="$ANDROID_DIR/app/build/outputs/apk/debug/app-debug.apk"
  if [[ ! -f "$APK" ]]; then
    log "expected APK missing: $APK"
    exit 1
  fi
  log "build ok"
  echo "ARTIFACT=$APK"
fi
