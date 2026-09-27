# UX iteration log (agent learner loop)

## Change 1 (after trials 1–5)
- Disable ANSI state colors when stdout is not a TTY (piped/agent runs).
- Print filters as `time=present, mood=indicative` instead of Python dict.
- Wrong-answer line shows what you typed vs expected; session shows `n/m (pct%)`.

## Change 2 (after trials 6–10)
- Compact practice header (one line + focus verbs); dropped repeated filter/person lines.

## Change 3 (code trim + UX, ~trial 15)
- Removed dead `build_active_pool`; merged `course_tenses.py` into `course_init.py`.
- Added `--retry-on-wrong`: one immediate re-try on the same prompt after a miss.
- Empty/EOF on retry skips retry instead of ending the whole session.

## Change 4 (trials 24–28)
- Practice prompt split: tense/person line + `Verb: …` on second line.
- Session summary notes prompt count when retries inflate attempt count.

## Change 5
- `--seed N` on practice for repeatable prompt sequences (testing / study drills).

## Change 6 (code trim + behavior)
- Flag new verbs only at session start (and after one masters mid-session), not on every prompt pick.
- Fixed practice-loop indentation regression from that edit.

---

## Learner loop summary (agent run)

- **Trials:** ~50+ prompt attempts via CLI (piped input + one 25-prompt `--seed 42` session with `--retry-on-wrong`).
- **UX themes:** raw ANSI in pipes, verbose headers, dict filters, no retry on same card, verb/person easy to misread on one line.
- **Stopped coding** after change 6; further runs were sanity checks (retry + two-line prompt + seed help study drills).

### Suggested command for you (present, no tu/vós, retry, seed)

```bash
verbpractice practice --course data/courses/default.json \
  --count 10 --no-accents --skip-second-person \
  --dimension time=present --dimension mood=indicative --seed 1
```

## Change 7 (WM / learner pass — continued)
- **Sticky verb** (default): ~80% of prompts stay on the same verb as the previous one.
- **`--verb falar`**: limit drill to one or more verbs; flags respect verb filter.
- **`(focus)` / `(review)`** on each prompt; **reset note** when rolling accuracy clears a form.
- **“(same form again this session)”** when a unit repeats within one sitting.

## Change 8
- **Retry on wrong is now default**; use `--no-retry-on-wrong` to disable.
- **“(second try)”** on correct after a retry; **`cli_util.py`** for colors/filter text.

## Change 9
- **Sticky tense** (with sticky verb): ~70% stay on same `tenseId` so persons cluster (easier WM).

---

## What we had been missing (reflection)

- **Working memory**: random verb *and* person jumps; fix = sticky verb + sticky tense + optional `--verb`.
- **Feedback loop**: one miss then move on; fix = default retry + show `(second try)`.
- **Why this card?** `(focus)` vs `(review)` labels.
- **Silent progress resets** → note when rolling accuracy clears a form.
- **Repeats in one sitting** → “same form again this session” (intentional, not bug).

## Trial batch (continuing loop)

- 12× falar @ seed 11, 15× falar @ seed 20, 10× ser @ seed 21 — learner pattern `?` then correct on retry (~50% attempts correct).
- **25+ trials since change 9** with no further code changes planned this round; tell me when to stop or next focus (e.g. `-ar` ending hints).

## Change 10
- After **Correct**, show **streak n/5** toward solid on that form (configurable threshold).

## Change 13
- **`set-pool --cap N`** trims excess `flaggedVerbs` entries; **status** lists only up to cap.

## Change 12 (long-run harness)
- **`scripts/learner_harness.py`**: flag matrix, status between runs, pauses, random garbage answers.
- **Empty line always quits** the session (no “skip retry and continue”).

## Change 11
- **Mastery**: rolling-accuracy reset no longer fires on the same turn as a **correct** answer (fixes `streak 0/5` after a good retry).

## Change 15
- **Status bars** fill by **practiced** units (≥1 attempt); counts show `n/m practiced (k solid)` so progress isn’t all `0/4` after drilling.

## Change 14 (long-run stability + harness)
- **Course file lock** (`*.lock` + `fcntl`) on load/save to stop parallel harness/CLI JSON races (`rc=1` flakes).
- Harness: **single-instance lock**, `--wait-lock`, seeded **garbage stdin** via `learner_pipe`, extra flag matrix (preterite/imperfect, multi-verb, present subj, EOF quit), **set-pool** + status checks.
- `learner_pipe` uses session **`rng`** (not global `random`) so stdin matches `--seed`.
