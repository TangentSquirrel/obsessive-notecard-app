#!/usr/bin/env bash
# Run on your LAPTOP: remote build → scp APK → adb install -r
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/../../.." && pwd)"
REMOTE="${MARMOT_HOST:-marmot}"
REMOTE_USER="${MARMOT_USER:-thelemur}"
REMOTE_REPO="${MARMOT_REPO:-\$HOME/Dev/verb-notecard-app}"
SSH_ID="${MARMOT_SSH_ID:-$HOME/.ssh/thelemur-marmot-id_rsa}"

SSH=(ssh -i "$SSH_ID" -o BatchMode=yes "${REMOTE_USER}@${REMOTE}")
SCP=(scp -i "$SSH_ID" -o BatchMode=yes)

REMOTE_DEPLOY="bash -lc \"\${REPO_ROOT:-$REMOTE_REPO}/scripts/deploy/marmot/remote/deploy.sh\""

log() { printf '[pull-and-install] %s\n' "$*"; }

require_cmd() {
  command -v "$1" >/dev/null || {
    log "missing: $1"
    exit 1
  }
}

require_cmd adb

log "remote build on $REMOTE"
OUTPUT="$("${SSH[@]}" "REPO_ROOT=$REMOTE_REPO $REMOTE_DEPLOY")"
printf '%s\n' "$OUTPUT"
APK="$(printf '%s\n' "$OUTPUT" | sed -n 's/^ARTIFACT=//p' | tail -1)"
if [[ -z "$APK" ]]; then
  log "no ARTIFACT= line from remote deploy"
  exit 1
fi

LOCAL="/tmp/verbpractice-app-debug.apk"
log "scp $REMOTE:$APK -> $LOCAL"
"${SCP[@]}" "${REMOTE_USER}@${REMOTE}:$APK" "$LOCAL"

log "adb install -r"
adb install -r "$LOCAL"
log "done — open the app on your phone"
