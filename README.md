# verbpractice

CLI Portuguese verb tense practice. Core logic is UI-agnostic JSON + Python.

**Everything runs in `./.venv` only.** Do not `pip install` globally; the project has zero PyPI dependencies beyond the editable install of this package.

## Setup (local venv only)

From the project root:

```bash
cd /opt/cursor-draft-verb-notecard-app
python3 -m venv .venv
.venv/bin/pip install -e .
```

Or skip manual setup and use the launcher (creates `.venv` on first run):

```bash
chmod +x run.sh
./run.sh --help
```

## How to run the CLI

Pick **one** of these — all use the local venv:

| Method | Example |
|--------|---------|
| **Launcher (recommended)** | `./run.sh practice --course data/courses/default.json --count 10` |
| **Module, no activate** | `.venv/bin/python -m verbpractice status --course data/courses/default.json` |
| **Entrypoint, no activate** | `.venv/bin/verbpractice validate data/libraries/core-50.json` |
| **After activate** | `source .venv/bin/activate` then `verbpractice ...` |

If you see `verbpractice: not found`, your shell PATH does not include `.venv/bin`. Use `./run.sh` or a path from the table above — do not install into system Python.

## Quick start

```bash
./run.sh seed-library --out data/libraries/core-50.json
./run.sh validate data/libraries/core-50.json
./run.sh library-info data/libraries/core-50.json

./run.sh init-course \
  --library data/libraries/core-50.json \
  --out data/courses/my.json \
  --unmastered-cap 5

./run.sh status --course data/courses/default.json
./run.sh practice --course data/courses/default.json --count 10
./run.sh practice --course data/courses/default.json --verb falar \
  --dimension time=present --dimension mood=indicative --skip-second-person --no-accents

./run.sh set-pool --course data/courses/my.json --cap 7

# Add subjunctive (or other) tenses without resetting indicative progress
./run.sh add-tenses --course data/courses/default.json \
  --tense present_subjunctive --tense imperfect_subjunctive

./run.sh practice --course data/courses/default.json --dimension mood=subjunctive
```

## Data model

- **Library** (`data/libraries/*.json`): `tenseCatalog` defines each **tenseId** as one `(time, mood, aspect)` slice; units add **person** + **register** and the conjugated **answers**.
- **Course** (`data/courses/*.json`): `librarySpec`, `activePool`, `config`, per-unit `progress`.

Seven tenses in the seed catalog: present / preterite / imperfect indicative, present / imperfect subjunctive, future indicative, future subjunctive. See `dimensionInteraction` in the library JSON for how axes combine.

```bash
verbpractice library-info data/libraries/core-50.json
```

Extend `VERB_CONJUGATIONS` in `verbpractice/library_seed.py` to grow toward 25+25 verbs.

## Android pilot

See **[docs/ANDROID_PILOT.md](docs/ANDROID_PILOT.md)** and **`android/README.md`**. Headless parity check:

```bash
.venv/bin/python scripts/contract_harness.py
```
