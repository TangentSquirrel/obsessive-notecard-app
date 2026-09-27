# Harness log
Started 2026-09-26 18:43:01

## Batch 18:43:01
- validate-lib: exit 0
OK: core-50 (4 verbs)

- status-default: exit 0
Course: Default course (course-1)
Eligible units: 188
Flagged verbs (5 cap): comer, falar, partir, ser

Verb × tense slice (time · mood · aspect):
  verb     time     mood        aspect      persons status
  comer    Future   Indicative  —           [----] 0/6 untrained
  comer    Future   Subjunctive —           [----] 0/6 untrained
  comer    Past     Indicative  Imperfect   [----] 0/6 untrained
  comer    Past     Indicative  Perfect (preterite) [----] 0/6 untrained
  comer    Past     Subjunctive Imperfect   [----] 0/6 untrained
  comer    Present  Imperative  —           [----] 0/5 untrained
  comer    Present  Indicative  —           [----] 0/6 in_progress
  comer    Present  Subjunctive —           [----] 0/6 untrained
  falar    Future   Indicative  —           [----] 0/6 untrained
- status-present: exit 0
Course: Default course (course-1)
Eligible units: 16
Person filter: skipping 2sg (tu) and 2pl (vós)
Flagged verbs (5 cap): comer, falar, partir, ser

Verb × tense slice (time · mood · aspect):
  verb     time     mood        aspect      persons status
  comer    Present  Indicative  —           [----] 0/4 in_progress
  falar    Present  Indicative  —           [----] 0/4 in_progress
  partir   Present  Indicative  —           [----] 0/4 in_progress
  ser      Present  Indicative  —           [----] 0/4 in_progress

Course-wide tense slices (all verbs):
  Present · Indicative · —             [----] 0/16 in_progress

Dimension: Time (time)
  Present          [----] 0/16 (0.0%)

Dimension: Mood (mood)
  Indicative       [----] 0/16 (0.0%)

Dimension: Aspect (aspect)
  —                [----] 
- library-info: exit 0
Library: Core verb library (seed) (core-50)
Verbs: 4
Regularity: irregular=1, regular=3

Tense catalog (time · mood · aspect):
  present_indicative       Present · Indicative · —
  preterite_indicative     Past · Indicative · Perfect (preterite)
  imperfect_indicative     Past · Indicative · Imperfect
  present_subjunctive      Present · Subjunctive · —
  imperfect_subjunctive    Past · Subjunctive · Imperfect
  future_indicative        Future · Indicative · —
  future_subjunctive       Future · Subjunctive · —
  imperative_affirmative   Present · Imperative · —

Units per tense: future_indicative=24, future_subjunctive=24, imperative_affirmative=20, imperfect_indicative=24, imperfect_subjunctive=24, present_indicative=24, present_subjunctive=24, preterite_indicative=24

- practice/bare-min: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/no-accents: ok ('Session: 3/11 correct (27%) · 6 prompts')
- practice/strict-acc: ok ('Session: 2/10 correct (20%) · 6 prompts')
- practice/skip-2p: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 4/10 correct (40%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 6/12 correct (50%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 6/10 correct (60%) · 6 prompts')
- practice/no-sticky: ok ('Session: 3/11 correct (27%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 0/12 correct (0%) · 6 prompts')
- practice/future-subj: ok ('Session: 2/5 correct (40%) · 3 prompts')
- practice/imperative: ok ('Session: 2/6 correct (33%) · 3 prompts')
- status after imperative: ok
- pause/empty-quit: FAIL
- pause/retry-skip: ok
- random-fail-mix: FAIL

**Totals:** 13 passed, 6 failed

## Batch 18:43:15
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 6/12 correct (50%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/11 correct (9%) · 6 prompts')
- practice/strict-acc: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/skip-2p: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 6/12 correct (50%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 4/11 correct (36%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 2/10 correct (20%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/11 correct (18%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 0/12 correct (0%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/6 correct (17%) · 3 prompts')
- status after imperative: ok
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: FAIL

**Totals:** 18 passed, 1 failed

### Loop 1/30

## Batch 18:43:26
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 2/10 correct (20%) · 6 prompts')
- practice/no-accents: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/strict-acc: FAIL rc=1 ('Practice · Default course · 6 prompts · (none — all eligible tenses/persons) · accents on · sticky verb\nFocus verbs: com')
- practice/skip-2p: ok ('Session: 5/12 correct (42%) · 6 prompts')
- practice/dim-present-ind: FAIL rc=1 ('Practice · Default course · 6 prompts · mood=indicative, time=present · no tu/vós · accents off · sticky verb\nFocus verb')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 2/11 correct (18%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 2/10 correct (20%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/10 correct (20%) · 6 prompts')
- practice/no-retry: ok ('Session: 2/6 correct (33%)')
- practice/seed-42: ok ('Session: 0/12 correct (0%) · 6 prompts')
- practice/future-subj: ok ('Session: 2/6 correct (33%) · 3 prompts')
- practice/imperative: ok ('Session: 3/6 correct (50%) · 3 prompts')
- status after imperative: ok
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok

**Totals:** 17 passed, 2 failed

## Batch 18:43:26
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 4/11 correct (36%) · 6 prompts')
- practice/no-accents: ok ('Session: 5/12 correct (42%) · 6 prompts')
- practice/strict-acc: FAIL rc=1 ('Practice · Default course · 6 prompts · (none — all eligible tenses/persons) · accents on · sticky verb\nFocus verbs: com')
- practice/skip-2p: ok ('Session: 5/12 correct (42%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 5/11 correct (45%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 4/11 correct (36%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 3/11 correct (27%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/10 correct (20%) · 6 prompts')
- practice/no-retry: ok ('Session: 1/6 correct (17%)')
- practice/seed-42: FAIL rc=1 ('Practice · Default course · 6 prompts · (none — all eligible tenses/persons) · verbs comer · accents off · sticky verb\nF')
- practice/future-subj: ok ('Session: 3/3 correct (100%)')
- practice/imperative: ok ('Session: 2/5 correct (40%) · 3 prompts')
- status after imperative: ok
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: FAIL

**Totals:** 16 passed, 3 failed

### Loop 2/30

## Batch 18:43:37
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 4/11 correct (36%) · 6 prompts')
- practice/no-accents: ok ('Session: 2/11 correct (18%) · 6 prompts')
- practice/strict-acc: ok ('Session: 4/10 correct (40%) · 6 prompts')
- practice/skip-2p: ok ('Session: 5/12 correct (42%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 6/12 correct (50%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/11 correct (9%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 5/10 correct (50%) · 6 prompts')
- practice/no-sticky: ok ('Session: 4/11 correct (36%) · 6 prompts')
- practice/no-retry: ok ('Session: 1/6 correct (17%)')
- practice/seed-42: ok ('Session: 0/12 correct (0%) · 6 prompts')
- practice/future-subj: ok ('Session: 3/6 correct (50%) · 3 prompts')
- practice/imperative: ok ('Session: 3/6 correct (50%) · 3 prompts')
- status after imperative: ok
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok

**Totals:** 19 passed, 0 failed

### Loop 3/30

## Batch 18:43:48
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 5/11 correct (45%) · 6 prompts')
- practice/no-accents: ok ('Session: 3/12 correct (25%) · 6 prompts')
- practice/strict-acc: ok ('Session: 6/12 correct (50%) · 6 prompts')
- practice/skip-2p: ok ('Session: 1/11 correct (9%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 6/11 correct (55%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 5/12 correct (42%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 6/12 correct (50%) · 6 prompts')
- practice/no-sticky: ok ('Session: 5/12 correct (42%) · 6 prompts')
- practice/no-retry: ok ('Session: 1/6 correct (17%)')
- practice/seed-42: ok ('Session: 0/12 correct (0%) · 6 prompts')
- practice/future-subj: ok ('Session: 2/5 correct (40%) · 3 prompts')
- practice/imperative: ok ('Session: 3/6 correct (50%) · 3 prompts')
- status after imperative: ok
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok

**Totals:** 19 passed, 0 failed

## Batch 18:44:00
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 6/12 correct (50%) · 6 prompts')
- practice/no-accents: ok ('Session: 4/11 correct (36%) · 6 prompts')
- practice/strict-acc: ok ('Session: 5/12 correct (42%) · 6 prompts')
- practice/skip-2p: ok ('Session: 5/12 correct (42%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 4/11 correct (36%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 4/10 correct (40%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 3/11 correct (27%) · 6 prompts')
- practice/no-sticky: ok ('Session: 3/11 correct (27%) · 6 prompts')
- practice/no-retry: ok ('Session: 3/6 correct (50%)')
- practice/seed-42: ok ('Session: 0/12 correct (0%) · 6 prompts')
- practice/future-subj: ok ('Session: 3/6 correct (50%) · 3 prompts')
- practice/imperative: ok ('Session: 1/6 correct (17%) · 3 prompts')
- status after imperative: ok
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok

**Totals:** 19 passed, 0 failed

## Batch 18:44:45
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 2/12 correct (17%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 2/12 correct (17%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-retry: ok ('Session: 1/6 correct (17%)')
- practice/seed-42: ok ('Session: 0/12 correct (0%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/6 correct (17%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 3/12 correct (25%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/2 correct (50%) · 1 prompts')
- practice/present-subj: ok ('Session: 3/6 correct (50%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: FAIL
- status-after-set-pool: ok
- pause/immediate-eof: ok

**Totals:** 26 passed, 1 failed

## Batch 18:44:57
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/11 correct (9%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/11 correct (9%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/11 correct (9%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/no-retry: ok ('Session: 1/6 correct (17%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 2/11 correct (18%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 5/12 correct (42%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/2 correct (50%) · 1 prompts')
- practice/present-subj: ok ('Session: 2/4 correct (50%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok

**Totals:** 27 passed, 0 failed
nohup: failed to run command './scripts/run_long_harness.sh': Permission denied
Starting harness: loops=200 sleep=20s — log UX_HARNESS_LOG.md

### Loop 1/200

## Batch 18:45:14
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 4/10 correct (40%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/no-sticky: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 0/12 correct (0%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 2/11 correct (18%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 2/10 correct (20%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/2 correct (50%) · 1 prompts')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok

**Totals:** 27 passed, 0 failed

### Loop 2/200

## Batch 18:45:39
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 4/10 correct (40%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 3/12 correct (25%) · 6 prompts')
- practice/no-sticky: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 0/12 correct (0%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 2/11 correct (18%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 2/10 correct (20%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/2 correct (50%) · 1 prompts')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok

**Totals:** 27 passed, 0 failed

### Loop 3/200
Starting harness: loops=200 sleep=20s — log UX_HARNESS_LOG.md

### Loop 1/200

## Batch 18:46:08
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 3/10 correct (30%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 3/10 correct (30%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/10 correct (20%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 0/12 correct (0%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 2/6 correct (33%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/10 correct (40%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/2 correct (50%) · 1 prompts')
- practice/present-subj: ok ('Session: 2/5 correct (40%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

### Loop 2/200

## Batch 18:46:33
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 3/10 correct (30%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 3/10 correct (30%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/10 correct (20%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 0/12 correct (0%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 2/6 correct (33%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/10 correct (40%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/2 correct (50%) · 1 prompts')
- practice/present-subj: ok ('Session: 2/5 correct (40%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

### Loop 3/200

## Batch 18:46:57
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 2/10 correct (20%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 3/10 correct (30%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 2/12 correct (17%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/10 correct (20%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 0/12 correct (0%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 2/6 correct (33%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/10 correct (40%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/2 correct (50%) · 1 prompts')
- practice/present-subj: ok ('Session: 2/5 correct (40%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

### Loop 4/200

## Batch 18:47:21
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/11 correct (9%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 3/10 correct (30%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 2/12 correct (17%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/10 correct (20%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 0/12 correct (0%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 2/6 correct (33%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/10 correct (40%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/2 correct (50%) · 1 prompts')
- practice/present-subj: ok ('Session: 2/5 correct (40%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

### Loop 5/200

## Batch 18:47:46
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 2/10 correct (20%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 4/9 correct (44%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 2/12 correct (17%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 1/11 correct (9%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 0/12 correct (0%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 2/6 correct (33%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 3/10 correct (30%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/2 correct (50%) · 1 prompts')
- practice/present-subj: ok ('Session: 3/5 correct (60%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

### Loop 6/200

## Batch 18:48:10
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 2/10 correct (20%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 4/9 correct (44%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/10 correct (20%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 0/12 correct (0%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 2/6 correct (33%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 5/10 correct (50%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/2 correct (50%) · 1 prompts')
- practice/present-subj: ok ('Session: 2/5 correct (40%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

## Batch 18:46:08
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 3/10 correct (30%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 3/10 correct (30%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/10 correct (20%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 0/12 correct (0%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 2/6 correct (33%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/10 correct (40%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/2 correct (50%) · 1 prompts')
- practice/present-subj: ok ('Session: 2/5 correct (40%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

## Batch 18:46:33
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 3/10 correct (30%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 3/10 correct (30%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/10 correct (20%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 0/12 correct (0%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 2/6 correct (33%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/10 correct (40%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/2 correct (50%) · 1 prompts')
- practice/present-subj: ok ('Session: 2/5 correct (40%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

## Batch 18:46:57
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 2/10 correct (20%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 3/10 correct (30%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 2/12 correct (17%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/10 correct (20%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 0/12 correct (0%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 2/6 correct (33%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/10 correct (40%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/2 correct (50%) · 1 prompts')
- practice/present-subj: ok ('Session: 2/5 correct (40%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

## Batch 18:47:21
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/11 correct (9%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 3/10 correct (30%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 2/12 correct (17%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/10 correct (20%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 0/12 correct (0%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 2/6 correct (33%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/10 correct (40%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/2 correct (50%) · 1 prompts')
- practice/present-subj: ok ('Session: 2/5 correct (40%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

## Batch 18:47:46
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 2/10 correct (20%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 4/9 correct (44%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 2/12 correct (17%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 1/11 correct (9%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 0/12 correct (0%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 2/6 correct (33%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 3/10 correct (30%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/2 correct (50%) · 1 prompts')
- practice/present-subj: ok ('Session: 3/5 correct (60%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

## Batch 18:48:10
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 2/10 correct (20%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 4/9 correct (44%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/10 correct (20%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 0/12 correct (0%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 2/6 correct (33%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 5/10 correct (50%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/2 correct (50%) · 1 prompts')
- practice/present-subj: ok ('Session: 2/5 correct (40%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed
### Loop 7/200

## Batch 18:48:34
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 2/10 correct (20%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 4/9 correct (44%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/10 correct (20%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 0/12 correct (0%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 2/6 correct (33%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 5/10 correct (50%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/2 correct (50%) · 1 prompts')
- practice/present-subj: ok ('Session: 2/5 correct (40%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

### Loop 8/200

## Batch 18:48:58
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 2/10 correct (20%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 4/9 correct (44%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/10 correct (20%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 0/12 correct (0%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 2/6 correct (33%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/10 correct (40%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/2 correct (50%) · 1 prompts')
- practice/present-subj: ok ('Session: 2/5 correct (40%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

### Loop 9/200

## Batch 18:49:23
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 2/10 correct (20%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 4/9 correct (44%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/10 correct (20%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 0/12 correct (0%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 2/6 correct (33%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 5/10 correct (50%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/2 correct (50%) · 1 prompts')
- practice/present-subj: ok ('Session: 2/5 correct (40%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

### Loop 10/200

## Batch 18:49:47
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 3/10 correct (30%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 3/10 correct (30%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/10 correct (20%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 0/12 correct (0%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 2/6 correct (33%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 5/10 correct (50%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/2 correct (50%) · 1 prompts')
- practice/present-subj: ok ('Session: 2/5 correct (40%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

### Loop 11/200

## Batch 18:50:12
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 3/10 correct (30%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 3/10 correct (30%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/10 correct (20%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 0/12 correct (0%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 2/6 correct (33%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 5/10 correct (50%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/2 correct (50%) · 1 prompts')
- practice/present-subj: ok ('Session: 2/5 correct (40%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

### Loop 12/200

## Batch 18:50:37
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 2/10 correct (20%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 3/10 correct (30%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/10 correct (20%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 0/12 correct (0%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/6 correct (17%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 5/10 correct (50%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/2 correct (50%) · 1 prompts')
- practice/present-subj: ok ('Session: 3/5 correct (60%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed


## Batch 18:48:34
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 2/10 correct (20%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 4/9 correct (44%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/10 correct (20%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 0/12 correct (0%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 2/6 correct (33%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 5/10 correct (50%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/2 correct (50%) · 1 prompts')
- practice/present-subj: ok ('Session: 2/5 correct (40%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

## Batch 18:48:58
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 2/10 correct (20%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 4/9 correct (44%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/10 correct (20%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 0/12 correct (0%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 2/6 correct (33%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/10 correct (40%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/2 correct (50%) · 1 prompts')
- practice/present-subj: ok ('Session: 2/5 correct (40%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

## Batch 18:49:23
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 2/10 correct (20%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 4/9 correct (44%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/10 correct (20%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 0/12 correct (0%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 2/6 correct (33%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 5/10 correct (50%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/2 correct (50%) · 1 prompts')
- practice/present-subj: ok ('Session: 2/5 correct (40%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

## Batch 18:49:47
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 3/10 correct (30%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 3/10 correct (30%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/10 correct (20%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 0/12 correct (0%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 2/6 correct (33%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 5/10 correct (50%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/2 correct (50%) · 1 prompts')
- practice/present-subj: ok ('Session: 2/5 correct (40%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

## Batch 18:50:12
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 3/10 correct (30%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 3/10 correct (30%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/10 correct (20%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 0/12 correct (0%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 2/6 correct (33%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 5/10 correct (50%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/2 correct (50%) · 1 prompts')
- practice/present-subj: ok ('Session: 2/5 correct (40%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

## Batch 18:50:37
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 2/10 correct (20%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 3/10 correct (30%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/10 correct (20%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 0/12 correct (0%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/6 correct (17%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 5/10 correct (50%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/2 correct (50%) · 1 prompts')
- practice/present-subj: ok ('Session: 3/5 correct (60%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed
### Loop 13/200

## Batch 18:51:02
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 3/12 correct (25%) · 6 prompts')
- practice/no-accents: ok ('Session: 2/10 correct (20%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 3/10 correct (30%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/10 correct (20%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 0/12 correct (0%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/6 correct (17%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 5/10 correct (50%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/2 correct (50%) · 1 prompts')
- practice/present-subj: ok ('Session: 2/5 correct (40%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

### Loop 14/200

## Batch 18:51:26
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/no-accents: ok ('Session: 3/10 correct (30%) · 6 prompts')
- practice/strict-acc: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/skip-2p: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 3/10 correct (30%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/10 correct (20%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 0/12 correct (0%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 2/6 correct (33%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 5/10 correct (50%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/2 correct (50%) · 1 prompts')
- practice/present-subj: ok ('Session: 2/5 correct (40%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

### Loop 15/200

## Batch 18:51:51
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/11 correct (9%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 3/10 correct (30%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/10 correct (20%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 0/12 correct (0%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 2/6 correct (33%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 5/10 correct (50%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/2 correct (50%) · 1 prompts')
- practice/present-subj: ok ('Session: 2/5 correct (40%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

### Loop 16/200

## Batch 18:52:15
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/no-accents: ok ('Session: 3/10 correct (30%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 3/10 correct (30%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/10 correct (20%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 0/12 correct (0%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 2/6 correct (33%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 5/10 correct (50%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/2 correct (50%) · 1 prompts')
- practice/present-subj: ok ('Session: 2/5 correct (40%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

### Loop 17/200

## Batch 18:52:39
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 2/10 correct (20%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 3/10 correct (30%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/10 correct (20%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 0/12 correct (0%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 2/6 correct (33%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 5/10 correct (50%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/2 correct (50%) · 1 prompts')
- practice/present-subj: ok ('Session: 2/5 correct (40%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

### Loop 18/200

## Batch 18:53:03
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 2/10 correct (20%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 3/10 correct (30%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/10 correct (20%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 0/12 correct (0%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 2/6 correct (33%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 5/10 correct (50%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/2 correct (50%) · 1 prompts')
- practice/present-subj: ok ('Session: 2/5 correct (40%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed


## Batch 18:51:02
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 3/12 correct (25%) · 6 prompts')
- practice/no-accents: ok ('Session: 2/10 correct (20%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 3/10 correct (30%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/10 correct (20%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 0/12 correct (0%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/6 correct (17%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 5/10 correct (50%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/2 correct (50%) · 1 prompts')
- practice/present-subj: ok ('Session: 2/5 correct (40%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

## Batch 18:51:26
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/no-accents: ok ('Session: 3/10 correct (30%) · 6 prompts')
- practice/strict-acc: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/skip-2p: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 3/10 correct (30%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/10 correct (20%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 0/12 correct (0%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 2/6 correct (33%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 5/10 correct (50%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/2 correct (50%) · 1 prompts')
- practice/present-subj: ok ('Session: 2/5 correct (40%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

## Batch 18:51:51
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/11 correct (9%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 3/10 correct (30%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/10 correct (20%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 0/12 correct (0%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 2/6 correct (33%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 5/10 correct (50%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/2 correct (50%) · 1 prompts')
- practice/present-subj: ok ('Session: 2/5 correct (40%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

## Batch 18:52:15
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/no-accents: ok ('Session: 3/10 correct (30%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 3/10 correct (30%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/10 correct (20%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 0/12 correct (0%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 2/6 correct (33%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 5/10 correct (50%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/2 correct (50%) · 1 prompts')
- practice/present-subj: ok ('Session: 2/5 correct (40%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

## Batch 18:52:39
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 2/10 correct (20%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 3/10 correct (30%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/10 correct (20%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 0/12 correct (0%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 2/6 correct (33%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 5/10 correct (50%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/2 correct (50%) · 1 prompts')
- practice/present-subj: ok ('Session: 2/5 correct (40%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

## Batch 18:53:03
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 2/10 correct (20%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 3/10 correct (30%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/10 correct (20%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 0/12 correct (0%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 2/6 correct (33%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 5/10 correct (50%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/2 correct (50%) · 1 prompts')
- practice/present-subj: ok ('Session: 2/5 correct (40%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed
### Loop 19/200

## Batch 18:53:28
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 2/10 correct (20%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 3/10 correct (30%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/10 correct (20%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 0/12 correct (0%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 2/6 correct (33%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 5/10 correct (50%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/2 correct (50%) · 1 prompts')
- practice/present-subj: ok ('Session: 3/5 correct (60%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

### Loop 20/200

## Batch 18:53:52
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 3/10 correct (30%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 3/10 correct (30%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/10 correct (20%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 0/12 correct (0%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 2/6 correct (33%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 5/10 correct (50%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/2 correct (50%) · 1 prompts')
- practice/present-subj: ok ('Session: 2/5 correct (40%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

### Loop 21/200

## Batch 18:54:16
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 2/10 correct (20%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 3/10 correct (30%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/10 correct (20%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 0/12 correct (0%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 2/6 correct (33%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 5/10 correct (50%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/2 correct (50%) · 1 prompts')
- practice/present-subj: ok ('Session: 2/5 correct (40%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

### Loop 22/200

## Batch 18:54:40
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 3/10 correct (30%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 3/10 correct (30%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/10 correct (20%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 0/12 correct (0%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 2/6 correct (33%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 5/10 correct (50%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/2 correct (50%) · 1 prompts')
- practice/present-subj: ok ('Session: 2/5 correct (40%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

### Loop 23/200

## Batch 18:55:05
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 3/10 correct (30%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 3/10 correct (30%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/10 correct (20%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 0/12 correct (0%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 2/6 correct (33%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 5/10 correct (50%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/2 correct (50%) · 1 prompts')
- practice/present-subj: ok ('Session: 2/5 correct (40%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

### Loop 24/200

## Batch 18:55:29
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 2/10 correct (20%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 3/10 correct (30%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/10 correct (20%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 0/12 correct (0%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 2/6 correct (33%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 5/10 correct (50%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/2 correct (50%) · 1 prompts')
- practice/present-subj: ok ('Session: 2/5 correct (40%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed


## Batch 18:53:28
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 2/10 correct (20%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 3/10 correct (30%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/10 correct (20%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 0/12 correct (0%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 2/6 correct (33%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 5/10 correct (50%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/2 correct (50%) · 1 prompts')
- practice/present-subj: ok ('Session: 3/5 correct (60%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

## Batch 18:53:52
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 3/10 correct (30%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 3/10 correct (30%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/10 correct (20%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 0/12 correct (0%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 2/6 correct (33%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 5/10 correct (50%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/2 correct (50%) · 1 prompts')
- practice/present-subj: ok ('Session: 2/5 correct (40%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

## Batch 18:54:16
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 2/10 correct (20%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 3/10 correct (30%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/10 correct (20%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 0/12 correct (0%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 2/6 correct (33%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 5/10 correct (50%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/2 correct (50%) · 1 prompts')
- practice/present-subj: ok ('Session: 2/5 correct (40%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

## Batch 18:54:40
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 3/10 correct (30%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 3/10 correct (30%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/10 correct (20%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 0/12 correct (0%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 2/6 correct (33%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 5/10 correct (50%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/2 correct (50%) · 1 prompts')
- practice/present-subj: ok ('Session: 2/5 correct (40%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

## Batch 18:55:05
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 3/10 correct (30%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 3/10 correct (30%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/10 correct (20%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 0/12 correct (0%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 2/6 correct (33%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 5/10 correct (50%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/2 correct (50%) · 1 prompts')
- practice/present-subj: ok ('Session: 2/5 correct (40%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

## Batch 18:55:29
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 2/10 correct (20%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 3/10 correct (30%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/10 correct (20%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 0/12 correct (0%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 2/6 correct (33%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 5/10 correct (50%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/2 correct (50%) · 1 prompts')
- practice/present-subj: ok ('Session: 2/5 correct (40%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed
### Loop 25/200

## Batch 18:55:53
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 2/10 correct (20%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 3/10 correct (30%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/10 correct (20%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 0/12 correct (0%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 2/6 correct (33%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 5/10 correct (50%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/2 correct (50%) · 1 prompts')
- practice/present-subj: ok ('Session: 2/5 correct (40%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

### Loop 26/200

## Batch 18:56:17
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 2/10 correct (20%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 3/10 correct (30%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/10 correct (20%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 0/12 correct (0%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 2/6 correct (33%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 5/10 correct (50%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/2 correct (50%) · 1 prompts')
- practice/present-subj: ok ('Session: 2/5 correct (40%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

### Loop 27/200

## Batch 18:56:41
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 2/10 correct (20%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 3/10 correct (30%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/10 correct (20%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 0/12 correct (0%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 2/6 correct (33%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 5/10 correct (50%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/2 correct (50%) · 1 prompts')
- practice/present-subj: ok ('Session: 2/5 correct (40%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

### Loop 28/200

## Batch 18:57:05
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 2/10 correct (20%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 3/10 correct (30%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/10 correct (20%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 0/12 correct (0%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 2/6 correct (33%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 5/10 correct (50%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/2 correct (50%) · 1 prompts')
- practice/present-subj: ok ('Session: 2/5 correct (40%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

### Loop 29/200

## Batch 18:57:30
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 2/10 correct (20%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 3/10 correct (30%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/10 correct (20%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 0/12 correct (0%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 2/6 correct (33%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 5/10 correct (50%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/2 correct (50%) · 1 prompts')
- practice/present-subj: ok ('Session: 2/5 correct (40%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

### Loop 30/200

## Batch 18:57:54
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 2/10 correct (20%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 3/10 correct (30%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/10 correct (20%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 0/12 correct (0%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 2/6 correct (33%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 5/10 correct (50%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/2 correct (50%) · 1 prompts')
- practice/present-subj: ok ('Session: 2/5 correct (40%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed


## Batch 18:55:53
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 2/10 correct (20%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 3/10 correct (30%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/10 correct (20%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 0/12 correct (0%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 2/6 correct (33%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 5/10 correct (50%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/2 correct (50%) · 1 prompts')
- practice/present-subj: ok ('Session: 2/5 correct (40%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

## Batch 18:56:17
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 2/10 correct (20%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 3/10 correct (30%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/10 correct (20%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 0/12 correct (0%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 2/6 correct (33%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 5/10 correct (50%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/2 correct (50%) · 1 prompts')
- practice/present-subj: ok ('Session: 2/5 correct (40%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

## Batch 18:56:41
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 2/10 correct (20%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 3/10 correct (30%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/10 correct (20%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 0/12 correct (0%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 2/6 correct (33%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 5/10 correct (50%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/2 correct (50%) · 1 prompts')
- practice/present-subj: ok ('Session: 2/5 correct (40%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

## Batch 18:57:05
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 2/10 correct (20%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 3/10 correct (30%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/10 correct (20%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 0/12 correct (0%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 2/6 correct (33%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 5/10 correct (50%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/2 correct (50%) · 1 prompts')
- practice/present-subj: ok ('Session: 2/5 correct (40%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

## Batch 18:57:30
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 2/10 correct (20%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 3/10 correct (30%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/10 correct (20%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 0/12 correct (0%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 2/6 correct (33%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 5/10 correct (50%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/2 correct (50%) · 1 prompts')
- practice/present-subj: ok ('Session: 2/5 correct (40%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

## Batch 18:57:54
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 2/10 correct (20%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 3/10 correct (30%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/10 correct (20%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 0/12 correct (0%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 2/6 correct (33%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 5/10 correct (50%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/2 correct (50%) · 1 prompts')
- practice/present-subj: ok ('Session: 2/5 correct (40%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed
### Loop 31/200

## Batch 18:58:18
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 2/10 correct (20%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 3/10 correct (30%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/10 correct (20%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 0/12 correct (0%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 2/6 correct (33%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 5/10 correct (50%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/2 correct (50%) · 1 prompts')
- practice/present-subj: ok ('Session: 2/5 correct (40%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

### Loop 32/200

## Batch 18:58:42
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 2/10 correct (20%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 3/10 correct (30%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/10 correct (20%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 0/12 correct (0%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 2/6 correct (33%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 5/10 correct (50%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/2 correct (50%) · 1 prompts')
- practice/present-subj: ok ('Session: 2/5 correct (40%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

### Loop 33/200

## Batch 18:59:06
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 2/10 correct (20%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 3/10 correct (30%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/10 correct (20%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 0/12 correct (0%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 2/6 correct (33%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 5/10 correct (50%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/2 correct (50%) · 1 prompts')
- practice/present-subj: ok ('Session: 2/5 correct (40%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

### Loop 34/200

## Batch 18:59:30
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 2/10 correct (20%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 3/10 correct (30%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/10 correct (20%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 0/12 correct (0%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 2/6 correct (33%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 5/10 correct (50%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/2 correct (50%) · 1 prompts')
- practice/present-subj: ok ('Session: 2/5 correct (40%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

### Loop 35/200

## Batch 18:59:54
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 2/10 correct (20%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 3/10 correct (30%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/10 correct (20%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 0/12 correct (0%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 2/6 correct (33%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 5/10 correct (50%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/2 correct (50%) · 1 prompts')
- practice/present-subj: ok ('Session: 2/5 correct (40%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

### Loop 36/200

## Batch 19:00:18
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 2/10 correct (20%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 3/10 correct (30%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/10 correct (20%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 0/12 correct (0%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 2/6 correct (33%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 5/10 correct (50%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/2 correct (50%) · 1 prompts')
- practice/present-subj: ok ('Session: 2/5 correct (40%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed


## Batch 18:58:18
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 2/10 correct (20%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 3/10 correct (30%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/10 correct (20%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 0/12 correct (0%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 2/6 correct (33%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 5/10 correct (50%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/2 correct (50%) · 1 prompts')
- practice/present-subj: ok ('Session: 2/5 correct (40%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

## Batch 18:58:42
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 2/10 correct (20%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 3/10 correct (30%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/10 correct (20%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 0/12 correct (0%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 2/6 correct (33%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 5/10 correct (50%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/2 correct (50%) · 1 prompts')
- practice/present-subj: ok ('Session: 2/5 correct (40%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

## Batch 18:59:06
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 2/10 correct (20%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 3/10 correct (30%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/10 correct (20%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 0/12 correct (0%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 2/6 correct (33%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 5/10 correct (50%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/2 correct (50%) · 1 prompts')
- practice/present-subj: ok ('Session: 2/5 correct (40%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

## Batch 18:59:30
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 2/10 correct (20%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 3/10 correct (30%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/10 correct (20%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 0/12 correct (0%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 2/6 correct (33%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 5/10 correct (50%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/2 correct (50%) · 1 prompts')
- practice/present-subj: ok ('Session: 2/5 correct (40%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

## Batch 18:59:54
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 2/10 correct (20%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 3/10 correct (30%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/10 correct (20%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 0/12 correct (0%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 2/6 correct (33%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 5/10 correct (50%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/2 correct (50%) · 1 prompts')
- practice/present-subj: ok ('Session: 2/5 correct (40%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

## Batch 19:00:18
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 2/10 correct (20%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 3/10 correct (30%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/10 correct (20%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 0/12 correct (0%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 2/6 correct (33%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 5/10 correct (50%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/2 correct (50%) · 1 prompts')
- practice/present-subj: ok ('Session: 2/5 correct (40%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed
### Loop 37/200

## Batch 19:00:43
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 2/10 correct (20%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 3/10 correct (30%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/10 correct (20%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 0/12 correct (0%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 2/6 correct (33%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 5/10 correct (50%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/2 correct (50%) · 1 prompts')
- practice/present-subj: ok ('Session: 2/5 correct (40%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

### Loop 38/200

## Batch 19:01:07
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 2/10 correct (20%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 3/10 correct (30%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/10 correct (20%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 0/12 correct (0%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 2/6 correct (33%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 5/10 correct (50%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/2 correct (50%) · 1 prompts')
- practice/present-subj: ok ('Session: 2/5 correct (40%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

### Loop 39/200

## Batch 19:01:31
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 2/10 correct (20%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 3/10 correct (30%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/10 correct (20%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 0/12 correct (0%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 2/6 correct (33%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 5/10 correct (50%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/2 correct (50%) · 1 prompts')
- practice/present-subj: ok ('Session: 2/5 correct (40%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

### Loop 40/200

## Batch 19:01:55
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 2/10 correct (20%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 3/10 correct (30%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/10 correct (20%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 0/12 correct (0%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 2/6 correct (33%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 5/10 correct (50%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/2 correct (50%) · 1 prompts')
- practice/present-subj: ok ('Session: 2/5 correct (40%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

### Loop 41/200

## Batch 19:02:19
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 2/10 correct (20%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 3/10 correct (30%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/10 correct (20%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 0/12 correct (0%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 2/6 correct (33%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 5/10 correct (50%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/2 correct (50%) · 1 prompts')
- practice/present-subj: ok ('Session: 2/5 correct (40%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

--- harness restarted 2026-09-26T19:02:44-05:00 after Change 15 ---
Starting harness: loops=160 sleep=20s — log UX_HARNESS_LOG.md

### Loop 1/160

## Batch 19:02:44
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

### Loop 2/160

## Batch 19:03:08
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

### Loop 3/160

## Batch 19:03:33
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

### Loop 4/160

## Batch 19:03:57
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

### Loop 5/160

## Batch 19:04:21
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

### Loop 6/160

## Batch 19:04:45
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

## Batch 19:02:44
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

## Batch 19:03:08
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

## Batch 19:03:33
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

## Batch 19:03:57
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

## Batch 19:04:21
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

## Batch 19:04:45
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed
### Loop 7/160

## Batch 19:05:10
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

### Loop 8/160

## Batch 19:05:34
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

### Loop 9/160

## Batch 19:05:59
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

### Loop 10/160

## Batch 19:06:23
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

### Loop 11/160

## Batch 19:06:47
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 0/12 correct (0%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

### Loop 12/160

## Batch 19:07:12
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 0/12 correct (0%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed


## Batch 19:05:10
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

## Batch 19:05:34
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

## Batch 19:05:59
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

## Batch 19:06:23
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

## Batch 19:06:47
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 0/12 correct (0%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

## Batch 19:07:12
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 0/12 correct (0%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed
### Loop 13/160

## Batch 19:07:36
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

### Loop 14/160

## Batch 19:08:00
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

### Loop 15/160

## Batch 19:08:25
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

### Loop 16/160

## Batch 19:08:49
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

### Loop 17/160

## Batch 19:09:15
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

### Loop 18/160

## Batch 19:09:40
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed


## Batch 19:07:36
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

## Batch 19:08:00
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

## Batch 19:08:25
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

## Batch 19:08:49
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

## Batch 19:09:15
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

## Batch 19:09:40
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed
### Loop 19/160

## Batch 19:10:05
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

### Loop 20/160

## Batch 19:10:29
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

### Loop 21/160

## Batch 19:10:54
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

### Loop 22/160

## Batch 19:11:19
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

### Loop 23/160

## Batch 19:11:43
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

### Loop 24/160

## Batch 19:12:07
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed


## Batch 19:10:05
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

## Batch 19:10:29
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

## Batch 19:10:54
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

## Batch 19:11:19
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

## Batch 19:11:43
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

## Batch 19:12:07
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed
### Loop 25/160

## Batch 19:12:32
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

### Loop 26/160

## Batch 19:12:56
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

### Loop 27/160

## Batch 19:13:21
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

### Loop 28/160

## Batch 19:13:45
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

### Loop 29/160

## Batch 19:14:09
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

### Loop 30/160

## Batch 19:14:33
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed


## Batch 19:12:32
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

## Batch 19:12:56
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

## Batch 19:13:21
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

## Batch 19:13:45
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

## Batch 19:14:09
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

## Batch 19:14:33
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed
### Loop 31/160

## Batch 19:14:57
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

### Loop 32/160

## Batch 19:15:21
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

### Loop 33/160

## Batch 19:15:46
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

### Loop 34/160

## Batch 19:16:10
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

### Loop 35/160

## Batch 19:16:34
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

### Loop 36/160

## Batch 19:16:58
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed


## Batch 19:14:57
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

## Batch 19:15:21
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

## Batch 19:15:46
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

## Batch 19:16:10
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

## Batch 19:16:34
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

## Batch 19:16:58
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed
### Loop 37/160

## Batch 19:17:23
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

### Loop 38/160

## Batch 19:17:47
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

### Loop 39/160

## Batch 19:18:12
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

### Loop 40/160

## Batch 19:18:36
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

### Loop 41/160

## Batch 19:19:00
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

### Loop 42/160

## Batch 19:19:24
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed


## Batch 19:17:23
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

## Batch 19:17:47
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

## Batch 19:18:12
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

## Batch 19:18:36
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

## Batch 19:19:00
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

## Batch 19:19:24
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed
### Loop 43/160

## Batch 19:19:48
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

### Loop 44/160

## Batch 19:20:12
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

### Loop 45/160

## Batch 19:20:37
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

### Loop 46/160

## Batch 19:21:02
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

### Loop 47/160

## Batch 19:21:27
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

### Loop 48/160

## Batch 19:21:51
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed


## Batch 19:19:48
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

## Batch 19:20:12
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

## Batch 19:20:37
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

## Batch 19:21:02
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

## Batch 19:21:27
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

## Batch 19:21:51
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed
### Loop 49/160

## Batch 19:22:15
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

### Loop 50/160

## Batch 19:22:40
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

### Loop 51/160

## Batch 19:23:04
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

### Loop 52/160

## Batch 19:23:28
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

### Loop 53/160

## Batch 19:23:53
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

### Loop 54/160

## Batch 19:24:17
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed


## Batch 19:22:15
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

## Batch 19:22:40
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

## Batch 19:23:04
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

## Batch 19:23:28
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

## Batch 19:23:53
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

## Batch 19:24:17
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed
### Loop 55/160

## Batch 19:24:43
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

### Loop 56/160

## Batch 19:25:09
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

### Loop 57/160

## Batch 19:25:33
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

### Loop 58/160

## Batch 19:25:58
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

### Loop 59/160

## Batch 19:26:23
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

### Loop 60/160

## Batch 19:26:47
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed


## Batch 19:24:43
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

## Batch 19:25:09
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

## Batch 19:25:33
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

## Batch 19:25:58
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

## Batch 19:26:23
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

## Batch 19:26:47
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed
### Loop 61/160

## Batch 19:27:11
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

### Loop 62/160

## Batch 19:27:35
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

### Loop 63/160

## Batch 19:28:00
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

### Loop 64/160

## Batch 19:28:26
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

### Loop 65/160

## Batch 19:28:52
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

### Loop 66/160

## Batch 19:29:16
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed


## Batch 19:27:11
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

## Batch 19:27:35
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

## Batch 19:28:00
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

## Batch 19:28:26
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

## Batch 19:28:52
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

## Batch 19:29:16
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed
### Loop 67/160

## Batch 19:29:40
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

### Loop 68/160

## Batch 19:30:05
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

### Loop 69/160

## Batch 19:30:29
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

### Loop 70/160

## Batch 19:30:53
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

### Loop 71/160

## Batch 19:31:17
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

### Loop 72/160

## Batch 19:31:42
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed


## Batch 19:29:40
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

## Batch 19:30:05
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

## Batch 19:30:29
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

## Batch 19:30:53
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

## Batch 19:31:17
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

## Batch 19:31:42
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed
### Loop 73/160

## Batch 19:32:06
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

### Loop 74/160

## Batch 19:32:30
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

### Loop 75/160

## Batch 19:32:56
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

### Loop 76/160

## Batch 19:33:20
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

### Loop 77/160

## Batch 19:33:44
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

### Loop 78/160

## Batch 19:34:08
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed


## Batch 19:32:06
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

## Batch 19:32:30
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

## Batch 19:32:56
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

## Batch 19:33:20
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

## Batch 19:33:44
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

## Batch 19:34:08
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed
### Loop 79/160

## Batch 19:34:33
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

### Loop 80/160

## Batch 19:34:57
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

### Loop 81/160

## Batch 19:35:22
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

### Loop 82/160

## Batch 19:35:46
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

### Loop 83/160

## Batch 19:36:10
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

### Loop 84/160

## Batch 19:36:35
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed


## Batch 19:34:33
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

## Batch 19:34:57
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

## Batch 19:35:22
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

## Batch 19:35:46
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

## Batch 19:36:10
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

## Batch 19:36:35
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed
### Loop 85/160

## Batch 19:36:59
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

### Loop 86/160

## Batch 19:37:23
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

### Loop 87/160

## Batch 19:37:48
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

### Loop 88/160

## Batch 19:38:12
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

### Loop 89/160

## Batch 19:38:36
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

### Loop 90/160

## Batch 19:39:00
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed


## Batch 19:36:59
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

## Batch 19:37:23
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

## Batch 19:37:48
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

## Batch 19:38:12
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

## Batch 19:38:36
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

## Batch 19:39:00
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed
### Loop 91/160

## Batch 19:39:24
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

### Loop 92/160

## Batch 19:39:48
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

### Loop 93/160

## Batch 19:40:12
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

### Loop 94/160

## Batch 19:40:36
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

### Loop 95/160

## Batch 19:41:00
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

### Loop 96/160

## Batch 19:41:25
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed


## Batch 19:39:24
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

## Batch 19:39:48
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

## Batch 19:40:12
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

## Batch 19:40:36
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

## Batch 19:41:00
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

## Batch 19:41:25
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed
### Loop 97/160

## Batch 19:41:49
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

### Loop 98/160

## Batch 19:42:13
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

### Loop 99/160

## Batch 19:42:38
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

### Loop 100/160

## Batch 19:43:03
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

### Loop 101/160

## Batch 19:43:27
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

### Loop 102/160

## Batch 19:43:51
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed


## Batch 19:41:49
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

## Batch 19:42:13
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

## Batch 19:42:38
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

## Batch 19:43:03
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

## Batch 19:43:27
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

## Batch 19:43:51
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed
### Loop 103/160

## Batch 19:44:16
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

### Loop 104/160

## Batch 19:44:42
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

### Loop 105/160

## Batch 19:45:07
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

### Loop 106/160

## Batch 19:45:32
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

### Loop 107/160

## Batch 19:45:58
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

### Loop 108/160

## Batch 19:46:23
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed


## Batch 19:44:16
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

## Batch 19:44:42
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

## Batch 19:45:07
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

## Batch 19:45:32
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

## Batch 19:45:58
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed

## Batch 19:46:23
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed
### Loop 109/160

## Batch 19:46:49
- validate-lib: ok
- status-default: ok
- status-present: ok
- library-info: ok
- practice/bare-min: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-accents: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/strict-acc: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/skip-2p: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/dim-present-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after dim-present-ind: ok
- practice/verb-falar: ok ('Session: 1/12 correct (8%) · 6 prompts')
- status after verb-falar: ok
- practice/verb-ser: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/no-sticky: ok ('Session: 2/12 correct (17%) · 6 prompts')
- practice/no-retry: ok ('Session: 0/6 correct (0%)')
- practice/seed-42: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/future-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- practice/imperative: ok ('Session: 1/5 correct (20%) · 3 prompts')
- status after imperative: ok
- practice/preterite-ind: ok ('Session: 1/12 correct (8%) · 6 prompts')
- practice/imperfect-ind: ok ('Session: 4/12 correct (33%) · 6 prompts')
- practice/multi-verb: ok ('Session: 0/8 correct (0%) · 4 prompts')
- practice/count-1: ok ('Session: 1/1 correct (100%)')
- practice/present-subj: ok ('Session: 1/6 correct (17%) · 3 prompts')
- pause/empty-quit: ok
- pause/empty-on-retry-quits: ok
- random-fail-mix: ok
- set-pool/cap-2: ok
- status-after-set-pool: ok
- pause/immediate-eof: ok
- set-pool/restore-cap-5: ok

**Totals:** 28 passed, 0 failed
