#!/usr/bin/env python3
"""Run adversarial JSON Schema negative controls for public status schemas."""

from __future__ import annotations

import argparse
import importlib.metadata
import json
from copy import deepcopy
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any, Callable

from jsonschema.validators import validator_for


SCHEMA = "n.human_ai_mathematics.json_schema_negative_controls.v1"


@dataclass(frozen=True)
class NegativeControl:
    control_id: str
    schema_file: str
    synthetic_instance: str
    expected_schema_path: str
    expected_validation_error: str
    mutate: Callable[[dict[str, Any]], dict[str, Any]]


@dataclass(frozen=True)
class Record:
    control_id: str
    schema_file: str
    synthetic_instance: str
    expected_schema_path: str
    expected_validation_error: str
    actual_result: str
    actual_error_count: int
    actual_errors: list[str]
    expected_schema_path_present: bool
    expected_validation_error_present: bool


def load_json(root: Path, rel: str) -> Any:
    return json.loads((root / rel).read_text(encoding="utf-8"))


def hinc_status(root: Path) -> dict[str, Any]:
    return deepcopy(load_json(root, "papers/HINC-001/STATUS.json"))


def research_index(root: Path) -> dict[str, Any]:
    return deepcopy(load_json(root, "research-index.json"))


def replace_paper(index: dict[str, Any], paper_id: str, mutator: Callable[[dict[str, Any]], None]) -> dict[str, Any]:
    for paper in index["papers"]:
        if paper["id"] == paper_id:
            mutator(paper)
            return index
    raise AssertionError(f"missing paper {paper_id}")


def controls(root: Path) -> list[NegativeControl]:
    return [
        NegativeControl(
            control_id="JSC_NEG_01",
            schema_file="schemas/research-index.schema.json",
            synthetic_instance="invalid paper state enum",
            expected_schema_path="/properties/papers/items/properties/state/enum",
            expected_validation_error="'active_public_theorem' is not one of",
            mutate=lambda data: replace_paper(data, "HINC-001", lambda paper: paper.__setitem__("state", "active_public_theorem")),
        ),
        NegativeControl(
            control_id="JSC_NEG_02",
            schema_file="schemas/paper-status.schema.json",
            synthetic_instance="missing required formal field",
            expected_schema_path="/properties/formal_verification/required",
            expected_validation_error="'claim_map_complete' is a required property",
            mutate=lambda data: (data["formal_verification"].pop("claim_map_complete", None), data)[1],
        ),
        NegativeControl(
            control_id="JSC_NEG_03",
            schema_file="schemas/paper-status.schema.json",
            synthetic_instance="wrong full-manuscript Lean type",
            expected_schema_path="/properties/formal_verification/properties/full_manuscript_lean_verified/type",
            expected_validation_error="is not of type 'boolean'",
            mutate=lambda data: data | {
                "formal_verification": data["formal_verification"] | {"full_manuscript_lean_verified": "false"}
            },
        ),
        NegativeControl(
            control_id="JSC_NEG_04",
            schema_file="schemas/paper-status.schema.json",
            synthetic_instance="unsupported external-review value",
            expected_schema_path="/properties/status_controls/properties/external_specialist_review/enum",
            expected_validation_error="'complete' is not one of",
            mutate=lambda data: data | {
                "status_controls": data["status_controls"] | {"external_specialist_review": "complete"}
            },
        ),
        NegativeControl(
            control_id="JSC_NEG_05",
            schema_file="schemas/paper-status.schema.json",
            synthetic_instance="unsupported historical-priority value",
            expected_schema_path="/properties/status_controls/properties/historical_priority/enum",
            expected_validation_error="'world_first' is not one of",
            mutate=lambda data: data | {
                "status_controls": data["status_controls"] | {"historical_priority": "world_first"}
            },
        ),
        NegativeControl(
            control_id="JSC_NEG_06",
            schema_file="schemas/paper-status.schema.json",
            synthetic_instance="HINC active state paired with public authorization false",
            expected_schema_path="/allOf/0/then/properties/status_controls/properties/public_release_authorized/const",
            expected_validation_error="True was expected",
            mutate=lambda data: data | {
                "status_controls": data["status_controls"] | {"public_release_authorized": False}
            },
        ),
        NegativeControl(
            control_id="JSC_NEG_07",
            schema_file="schemas/research-index.schema.json",
            synthetic_instance="FSG active state paired with mathematical blocker true",
            expected_schema_path="/properties/papers/items/allOf/2/then/properties/state/const",
            expected_validation_error="'hold' was expected",
            mutate=lambda data: replace_paper(data, "FSG-001", lambda paper: paper.__setitem__("state", "active_review")),
        ),
    ]


def base_instance(root: Path, schema_file: str) -> dict[str, Any]:
    if schema_file.endswith("paper-status.schema.json"):
        return hinc_status(root)
    if schema_file.endswith("research-index.schema.json"):
        return research_index(root)
    raise AssertionError(f"unsupported schema for negative control: {schema_file}")


def validate_control(root: Path, control: NegativeControl) -> Record:
    schema = load_json(root, control.schema_file)
    instance = control.mutate(base_instance(root, control.schema_file))
    klass = validator_for(schema)
    klass.check_schema(schema)
    validator = klass(schema)
    errors = sorted(validator.iter_errors(instance), key=lambda item: (list(item.path), list(item.schema_path)))
    error_texts = [
        f"instance=/{'/'.join(map(str, error.path))}; schema=/{'/'.join(map(str, error.schema_path))}; message={error.message}"
        for error in errors
    ]
    joined = "\n".join(error_texts)
    return Record(
        control_id=control.control_id,
        schema_file=control.schema_file,
        synthetic_instance=control.synthetic_instance,
        expected_schema_path=control.expected_schema_path,
        expected_validation_error=control.expected_validation_error,
        actual_result="REJECTED" if errors else "ACCEPTED",
        actual_error_count=len(errors),
        actual_errors=error_texts,
        expected_schema_path_present=control.expected_schema_path in joined,
        expected_validation_error_present=control.expected_validation_error in joined,
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path.cwd())
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    root = args.root.resolve()
    records = [validate_control(root, control) for control in controls(root)]
    failures = [
        record
        for record in records
        if record.actual_result != "REJECTED"
        or not record.expected_schema_path_present
        or not record.expected_validation_error_present
    ]
    payload = {
        "schema": SCHEMA,
        "result": "PASS" if not failures else "FAIL",
        "validator_package": "jsonschema",
        "validator_version": importlib.metadata.version("jsonschema"),
        "negative_control_count": len(records),
        "negative_controls_passed": len(records) - len(failures),
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
