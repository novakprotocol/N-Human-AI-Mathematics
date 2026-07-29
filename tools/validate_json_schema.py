#!/usr/bin/env python3
"""Validate public JSON instances with committed JSON Schemas."""

from __future__ import annotations

import argparse
import importlib.metadata
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

import jsonschema
from jsonschema.validators import validator_for


SCHEMA = "n.human_ai_mathematics.json_schema_validation.v1"
VALIDATION_PAIRS = (
    ("schemas/research-index.schema.json", "research-index.json"),
    ("schemas/full-lean-portfolio.schema.json", "formal-verification-status.json"),
    ("schemas/paper-1-3-full-lean-status.schema.json", "PAPER_1_3_FULL_LEAN_STATUS.json"),
    ("schemas/paper-status.schema.json", "papers/HINC-001/STATUS.json"),
    ("schemas/paper-status.schema.json", "papers/ABF-001/STATUS.json"),
    ("schemas/publication-gate.schema.json", "reports/publication-gates/HINC-001.json"),
    ("schemas/publication-gate.schema.json", "reports/publication-gates/ABF-001.json"),
)


@dataclass(frozen=True)
class Record:
    schema_file: str
    instance_file: str
    validator: str
    validator_version: str
    result: str
    errors: list[str]


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def validate_pair(root: Path, schema_rel: str, instance_rel: str) -> Record:
    schema = load_json(root / schema_rel)
    instance = load_json(root / instance_rel)
    klass = validator_for(schema)
    klass.check_schema(schema)
    validator = klass(schema)
    errors = sorted(validator.iter_errors(instance), key=lambda item: list(item.path))
    return Record(
        schema_file=schema_rel,
        instance_file=instance_rel,
        validator=f"jsonschema.{klass.__name__}",
        validator_version=importlib.metadata.version("jsonschema"),
        result="PASS" if not errors else "FAIL",
        errors=[f"/{'/'.join(map(str, error.path))}: {error.message}" for error in errors],
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path.cwd())
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    root = args.root.resolve()

    records = [validate_pair(root, schema, instance) for schema, instance in VALIDATION_PAIRS]
    failures = [record for record in records if record.result != "PASS"]
    payload = {
        "schema": SCHEMA,
        "result": "PASS" if not failures else "FAIL",
        "validator_package": "jsonschema",
        "validator_version": importlib.metadata.version("jsonschema"),
        "record_count": len(records),
        "failure_count": len(failures),
        "records": [asdict(record) for record in records],
    }
    text = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8", newline="\n")
    print(text, end="")
    return 0 if payload["result"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
