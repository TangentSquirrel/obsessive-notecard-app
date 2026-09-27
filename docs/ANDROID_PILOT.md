# Android pilot + recursive test loop

## Harness stopped

Long CLI harness was stopped manually (~loop **109/160**). Logs remain in `UX_HARNESS_LOG.md`.

## Goal

Ship a **pilot Android app** that reuses the same **course/library JSON** and **practice rules** as the CLI, with a **recursive QA loop** analogous to `scripts/learner_harness.py`.

## What you need on a dev machine

| Piece | Purpose |
|--------|---------|
| **Android Studio** (Ladybug+) | SDK, emulator, Gradle |
| **JDK 17** | Android Gradle Plugin |
| **API 34** emulator (or device) | Run pilot |
| This repo | Python core + assets |

This CI/sandbox host has **no JDK/Android SDK** — build and instrumented tests run on your laptop or Android CI.

## Architecture (recommended for pilot)

```
data/libraries/*.json  data/courses/*.json
         │                      │
         └──────────┬───────────┘
                    ▼
         verbpractice/ (Python core)
    load · grade · mastery · select · practice_session
                    │
      ┌─────────────┴─────────────┐
      ▼                           ▼
  CLI (__main__)          Android (Chaquopy)
  learner_harness         Compose UI → PracticeSession
      │                           │
      └─────────────┬─────────────┘
                    ▼
         data/contract/*.json
         scripts/contract_harness.py
```

**Chaquopy** embeds the same `verbpractice` package in the APK so you do **not** reimplement grading/mastery in Kotlin for v0. Alternative: Kotlin port + contract tests only (more work).

## Recursive testing loop (layers)

1. **Contract (headless, fast)** — `scripts/contract_harness.py`  
   Fresh course → `PracticeSession` with fixed seed → compare prompt `unit_id`s and answers to `data/contract/practice-baseline.json`.  
   Run on every commit; Android CI runs the same check via Chaquopy JUnit or a `python -m` step before assemble.

2. **CLI learner matrix (existing)** — `scripts/learner_harness.py`  
   Flag matrix, pauses, garbage input, status.

3. **Android UI loop (to add)** — `scripts/android_learner_harness.sh`  
   - Copy `data/` into app assets (or sync task)  
   - `./gradlew connectedDebugAndroidTest`  
   - Espresso: open app → practice N cards with scripted wrong/right → assert session summary TextView  
   - Optional: Macrobenchmark / screenshot diff later  

4. **Spot checks** — `scripts/spot_learner.py` (CLI) + manual emulator smoke.

**Gate for “pilot done”:** contract green + one instrumented test file green + course progress persists on device under app private storage.

## Android project layout

```
android/
  README.md           ← build/run
  app/
    src/main/assets/courses/…   ← packaged course (sync from ../data)
    src/main/java/…/MainActivity.kt
    src/androidTest/…/PracticeFlowTest.kt
```

Pilot UI (Compose): header (filters), prompt lines, text field, submit, wrong/retry, empty quit, session summary — mirror CLI semantics from `PracticePromptView` / `SubmitResult`.

## Setup steps (developer)

1. Open `android/` in Android Studio; let Gradle sync.  
2. Add **Chaquopy** plugin to `app/build.gradle.kts` (see [chaquo.com](https://chaquo.com/chaquopy/)) and `pip { install "verbpractice" }` from parent path or vendored copy.  
3. Gradle task **syncAssets**: copy `data/libraries/core-50.json` + default course into `app/src/main/assets/`.  
4. Implement `PracticeRepository` calling `PracticeSession` from Python.  
5. Record contract:  
   `python scripts/contract_harness.py` (first run writes `expected` into JSON).  
6. Wire GitHub Action / local: `contract_harness.py && ./gradlew test connectedAndroidTest`.

## Next implementation tasks

- [ ] Chaquopy + asset sync Gradle task  
- [ ] Compose practice screen wired to `PracticeSession`  
- [ ] Persist course via `save_course` to `filesDir/courses/active.json`  
- [ ] Espresso test: seed 42, comer, 3 prompts, assert labels  
- [ ] `android_learner_harness.sh` calling Gradle + append `ANDROID_HARNESS_LOG.md`
