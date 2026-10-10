#!/usr/bin/env python3
"""Validate the repo's JSON data against its schemas.

Run from anywhere: python3 tools/validate.py
Needs: pip install jsonschema
"""
import json
import re
import sys
from pathlib import Path

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parent.parent

# instance -> schema
PAIRS = {
    "playtest/personas/persona_bank_v1.json": "playtest/personas/persona_bank_v1.schema.json",
    "skills/personas/jaded_systems_designer_v1.json": "skills/personas/jaded_systems_designer_v1.schema.json",
    "playtest/examples/example_event_log.json": "playtest/schemas/playtest_event_log_v1.schema.json",
    "playtest/examples/example_session_summary.json": "playtest/schemas/playtest_session_summary_v1.schema.json",
    "playtest/examples/example_misread_catalog.json": "playtest/schemas/misread_catalog_v1.schema.json",
}

errors = []


def fail(msg):
    errors.append(msg)


_cache = {}


def load(rel):
    """Parse once; report a parse error once."""
    if rel not in _cache:
        try:
            _cache[rel] = json.loads((ROOT / rel).read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as e:
            fail(f"{rel}: {e}")
            _cache[rel] = None
    return _cache[rel]


# 1. Every JSON file parses.
for path in sorted(ROOT.rglob("*.json")):
    if ".git" not in path.parts:
        load(path.relative_to(ROOT).as_posix())

# 2. Instances match their schemas.
for inst, schema in PAIRS.items():
    data, sch = load(inst), load(schema)
    if data is None or sch is None:
        continue
    Draft202012Validator.check_schema(sch)
    for err in Draft202012Validator(sch).iter_errors(data):
        loc = "/".join(str(p) for p in err.absolute_path) or "(root)"
        fail(f"{inst} at {loc}: {err.message}")

# 3. Persona bank consistency.
bank = load("playtest/personas/persona_bank_v1.json")
ids = set()
if bank:
    personas = bank.get("personas", [])
    ids = [p.get("persona_id") for p in personas]
    if bank.get("count") != len(personas):
        fail(f"persona bank: count is {bank.get('count')} but there are {len(personas)} personas")
    dupes = {i for i in ids if ids.count(i) > 1}
    if dupes:
        fail(f"persona bank: duplicate persona_id {sorted(dupes)}")
    for p in personas:
        if p.get("persona_id") and p.get("persona_id") in p.get("label", ""):
            fail(f"persona bank: {p['persona_id']} label repeats its ID")
    ids = set(ids)

    # README quick list matches the bank.
    readme = (ROOT / "playtest/personas/README.md").read_text(encoding="utf-8")
    listed = dict(re.findall(r"^- \*\*(P\d{3})\*\*: (.+?) \(", readme, re.M))
    for p in personas:
        if listed.get(p["persona_id"]) != p["label"]:
            fail(f"personas README: {p['persona_id']} is listed as {listed.get(p['persona_id'])!r}, bank says {p['label']!r}")

# 4. Example logs only reference personas that exist.
log = load("playtest/examples/example_event_log.json")
if log and ids:
    for pl in log.get("players", []):
        if "persona_id" in pl and pl["persona_id"] not in ids:
            fail(f"example_event_log: unknown persona_id {pl['persona_id']}")

# 5. Persona IDs mentioned in SKILL.md exist.
skill = (ROOT / "claude_skill/SKILL.md").read_text(encoding="utf-8")
if not skill.startswith("---\n"):
    fail("SKILL.md: missing YAML frontmatter")
if ids:  # skip if the bank itself failed to load
    for pid in sorted(set(re.findall(r"\bP\d{3}\b", skill)) - ids):
        fail(f"SKILL.md: references unknown persona {pid}")

# 6. Manifest asset paths resolve.
manifest = load("claude_skill/manifest.json")
if manifest:
    base = ROOT / "claude_skill"
    for key, rel in manifest.get("assets", {}).items():
        if not (base / rel).exists():
            fail(f"manifest.json: asset {key!r} -> {rel} does not exist")
    if not (base / manifest.get("entrypoint", "")).is_file():
        fail("manifest.json: entrypoint does not exist")

if errors:
    print(f"{len(errors)} problem(s):")
    for e in errors:
        print(f"  - {e}")
    sys.exit(1)
print("All checks passed.")
