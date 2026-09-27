# Verbpractice Android (pilot)

Open this folder in **Android Studio** after installing JDK 17 and the Android SDK.

Full architecture and the recursive test loop: **[../docs/ANDROID_PILOT.md](../docs/ANDROID_PILOT.md)**.

## Pilot scope

- Jetpack Compose single activity: practice flow only (no status grid v0).
- Ship `core-50.json` + a starter course under `app/src/main/assets/`.
- Embed Python via **Chaquopy** and call `verbpractice.practice_session.PracticeSession` (same as CLI contract tests).

## Not scaffolded yet

Gradle project files are added in the next step once Chaquopy + package name are confirmed. Run contract tests from repo root today:

```bash
.venv/bin/python scripts/contract_harness.py
```

## Asset sync (manual until Gradle task exists)

```bash
mkdir -p app/src/main/assets/courses app/src/main/assets/libraries
cp ../data/libraries/core-50.json app/src/main/assets/libraries/
cp ../data/courses/default.json app/src/main/assets/courses/default.json
```

Adjust `librarySpec.path` in the bundled course to point at `libraries/core-50.json` relative to assets.
