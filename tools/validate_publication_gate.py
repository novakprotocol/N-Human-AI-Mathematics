#!/usr/bin/env python3
"""Fail-closed validation of mandatory publication-gate receipts."""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

SCHEMA_VERSION = "n.human_llm_mathematics.publication_gate.v1"
PUBLIC_STATES = {"active_review", "published"}
PASS_STATUSES = {
    "PASS_PUBLIC_TECHNICAL_REVIEW",
    "PASS_ARCHIVAL_RELEASE",
    "PASS_JOURNAL_SUBMISSION",
}
ALL_STATUSES = PASS_STATUSES | {"HOLD"}
REQUIRED_REPOSITORY_FILES = {
    "PUBLICATION_GATES.md",
    "schemas/publication-gate.schema.json",
    "tools/validate_publication_gate.py",
}
REQUIRED_GATES = {
    "claim_boundary",
    "proof",
    "hostile_review",
    "prior_art_search",
    "independent_challenge",
    "clean_execution",
    "provenance",
    "owner_authorization",
}
PAPER_ID_RE = re.compile(r"^[A-Z]{2,8}-[0-9]{3}$")
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
SHA40_RE = re.compile(r"^[0-9a-f]{40}$")
SHA64_RE = re.compile(r"^[0-9a-f]{64}$")


@dataclass(frozen=True)
class Finding:
    level: str
    path: str
    message: str


def load_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        raise ValueError(f"missing JSON file: {path}") from None
    except json.JSONDecodeError as exc:
        raise ValueError(
            f"invalid JSON at {path}:{exc.lineno}:{exc.colno}: {exc.msg}"
        ) from exc


def require(condition: bool, path: str, message: str) -> list[Finding]:
    return [] if condition else [Finding("ERROR", path, message)]


def validate_evidence_paths(root: Path, label: str, evidence: Any) -> list[Finding]:
    findings: list[Finding] = []
    if not isinstance(evidence, list) or not evidence:
        return [Finding("ERROR", label, "evidence must be a nonempty array")]
    for index, item in enumerate(evidence):
        item_label = f"{label}.evidence[{index}]"
        if not isinstance(item, str) or not item.strip():
            findings.append(
                Finding("ERROR", item_label, "evidence entry must be nonempty text")
            )
            continue
        # External identifiers, PR/issue references, descriptive hashes, and
        # explicit HOLD/NOTE entries are allowed. Plain repository paths must
        # resolve to committed files.
        if (
            "://" in item
            or "PR #" in item
            or "issue #" in item.lower()
            or "SHA-256" in item
            or item.startswith("workflow run ")
            or item.startswith("NOTE:")
            or item.startswith("HOLD:")
        ):
            continue
        candidate = root / item
        if not candidate.is_file():
            findings.append(
                Finding(
                    "ERROR",
                    item_label,
                    f"repository evidence path is missing: {item}",
                )
            )
    return findings


def validate_receipt_structure(
    root: Path,
    expected_paper_id: str,
    path: Path,
) -> tuple[dict[str, Any] | None, list[Finding]]:
    rel = path.relative_to(root).as_posix()
    try:
        data = load_json(path)
    except ValueError as exc:
        return None, [Finding("ERROR", rel, str(exc))]
    if not isinstance(data, dict):
        return None, [Finding("ERROR", rel, "receipt top level must be an object")]

    findings: list[Finding] = []
    findings += require(
        data.get("schema_version") == SCHEMA_VERSION,
        rel,
        "unexpected schema_version",
    )
    findings += require(
        data.get("paper_id") == expected_paper_id,
        rel,
        "paper_id does not match filename or index entry",
    )
    receipt_date = data.get("receipt_date")
    findings += require(
        isinstance(receipt_date, str) and bool(DATE_RE.fullmatch(receipt_date)),
        rel,
        "receipt_date must be YYYY-MM-DD",
    )
    findings += require(
        data.get("status") in ALL_STATUSES,
        rel,
        "invalid publication-gate status",
    )
    findings += require(
        data.get("release_target")
        in {"public_technical_review", "archival_release", "journal_submission"},
        rel,
        "invalid release_target",
    )

    source = data.get("source_identity")
    if not isinstance(source, dict) or not source:
        findings.append(Finding("ERROR", rel, "source_identity must be an object"))
    else:
        findings += require(
            source.get("repository") == "novakprotocol/N-Human-AI-Mathematics",
            f"{rel}.source_identity",
            "unexpected repository",
        )
        manifest = source.get("package_sha256") or source.get("manifest_sha256")
        findings += require(
            isinstance(manifest, str) and bool(SHA64_RE.fullmatch(manifest)),
            f"{rel}.source_identity",
            "package or manifest SHA-256 is required",
        )

    gates = data.get("gates")
    if not isinstance(gates, dict):
        return data, findings + [Finding("ERROR", rel, "gates must be an object")]
    for name in sorted(REQUIRED_GATES - set(gates)):
        findings.append(Finding("ERROR", rel, f"missing mandatory gate: {name}"))

    for name in sorted(REQUIRED_GATES & set(gates)):
        gate = gates[name]
        label = f"{rel}.gates.{name}"
        if not isinstance(gate, dict):
            findings.append(Finding("ERROR", label, "gate must be an object"))
            continue
        findings += require(
            gate.get("status") in {"PASS", "HOLD"},
            label,
            "gate status must be PASS or HOLD",
        )
        findings.extend(validate_evidence_paths(root, label, gate.get("evidence")))

    limitations = data.get("limitations")
    findings += require(
        isinstance(limitations, list) and bool(limitations),
        rel,
        "limitations must be a nonempty array",
    )
    return data, findings


def validate_pass_receipt(
    root: Path,
    paper_id: str,
    path: Path,
) -> list[Finding]:
    rel = path.relative_to(root).as_posix()
    data, findings = validate_receipt_structure(root, paper_id, path)
    if data is None:
        return findings

    findings += require(
        data.get("status") in PASS_STATUSES,
        rel,
        "public paper lacks a PASS publication-gate status",
    )
    source = data.get("source_identity", {})
    if isinstance(source, dict):
        commit_values = [value for key, value in source.items() if "commit" in key]
        findings += require(
            any(
                isinstance(value, str) and bool(SHA40_RE.fullmatch(value))
                for value in commit_values
            ),
            f"{rel}.source_identity",
            "at least one exact 40-character commit is required",
        )

    gates = data.get("gates", {})
    if not isinstance(gates, dict):
        return findings
    for name in sorted(REQUIRED_GATES):
        gate = gates.get(name, {})
        if isinstance(gate, dict):
            findings += require(
                gate.get("status") == "PASS",
                f"{rel}.gates.{name}",
                "public release requires every gate to be PASS",
            )

    proof = gates.get("proof", {}) if isinstance(gates.get("proof"), dict) else {}
    findings += require(
        proof.get("universal_claims_have_complete_human_proofs") is True,
        f"{rel}.gates.proof",
        "universal claims must have complete human proofs",
    )
    findings += require(
        proof.get("finite_claims_exhaustively_verified_or_not_applicable") is True,
        f"{rel}.gates.proof",
        "finite claims must be exhaustively verified or explicitly not applicable",
    )

    hostile = (
        gates.get("hostile_review", {})
        if isinstance(gates.get("hostile_review"), dict)
        else {}
    )
    findings += require(
        hostile.get("blocking_findings_open") == 0,
        f"{rel}.gates.hostile_review",
        "hostile review has unresolved blocking findings",
    )

    prior = (
        gates.get("prior_art_search", {})
        if isinstance(gates.get("prior_art_search"), dict)
        else {}
    )
    findings += require(
        prior.get("search_completed_to_declared_scope") is True,
        f"{rel}.gates.prior_art_search",
        "prior-art search is incomplete",
    )
    findings += require(
        prior.get("final_delta_search_completed") is True,
        f"{rel}.gates.prior_art_search",
        "final pre-release delta search is incomplete",
    )
    findings += require(
        prior.get("final_delta_search_date") == data.get("receipt_date"),
        f"{rel}.gates.prior_art_search",
        "final delta search must be completed on the receipt date",
    )
    findings += require(
        prior.get("historical_priority")
        in {"unestablished", "externally_established"},
        f"{rel}.gates.prior_art_search",
        "historical-priority value is invalid or overclaimed",
    )

    independent = (
        gates.get("independent_challenge", {})
        if isinstance(gates.get("independent_challenge"), dict)
        else {}
    )
    findings += require(
        independent.get("structurally_independent_internal_route") is True,
        f"{rel}.gates.independent_challenge",
        "structurally independent internal challenge route is missing",
    )

    clean = (
        gates.get("clean_execution", {})
        if isinstance(gates.get("clean_execution"), dict)
        else {}
    )
    findings += require(
        clean.get("fresh_checkout_or_clean_copy") is True,
        f"{rel}.gates.clean_execution",
        "fresh-checkout or clean-copy execution is missing",
    )
    findings += require(
        clean.get("completed_without_timeout") is True,
        f"{rel}.gates.clean_execution",
        "required execution did not complete without timeout",
    )
    findings += require(
        clean.get("partial_runs_accepted") is False,
        f"{rel}.gates.clean_execution",
        "partial runs may not be accepted",
    )
    findings += require(
        clean.get("deterministic_receipt_present") is True,
        f"{rel}.gates.clean_execution",
        "deterministic completion receipt is missing",
    )

    provenance = (
        gates.get("provenance", {})
        if isinstance(gates.get("provenance"), dict)
        else {}
    )
    for field, message in (
        ("source_identity_locked", "source identity is not locked"),
        ("sha256_manifest_present", "SHA-256 manifest is missing"),
        ("versioned_tag_present", "versioned tag is missing"),
        ("release_record_present", "release record is missing"),
    ):
        findings += require(
            provenance.get(field) is True,
            f"{rel}.gates.provenance",
            message,
        )

    owner = (
        gates.get("owner_authorization", {})
        if isinstance(gates.get("owner_authorization"), dict)
        else {}
    )
    findings += require(
        owner.get("package_specific_authorization") is True,
        f"{rel}.gates.owner_authorization",
        "package-specific owner authorization is missing",
    )
    return findings


def validate(root: Path) -> list[Finding]:
    findings: list[Finding] = []
    for required in sorted(REQUIRED_REPOSITORY_FILES):
        if not (root / required).is_file():
            findings.append(
                Finding("ERROR", required, "mandatory publication-gate file is missing")
            )

    schema_path = root / "schemas" / "publication-gate.schema.json"
    if schema_path.is_file():
        try:
            schema = load_json(schema_path)
        except ValueError as exc:
            findings.append(
                Finding("ERROR", schema_path.relative_to(root).as_posix(), str(exc))
            )
        else:
            if (
                not isinstance(schema, dict)
                or schema.get("title")
                != "N Human-LLM Mathematics Publication Gate Receipt"
            ):
                findings.append(
                    Finding(
                        "ERROR",
                        schema_path.relative_to(root).as_posix(),
                        "unexpected publication-gate schema",
                    )
                )

    index_path = root / "research-index.json"
    try:
        index = load_json(index_path)
    except ValueError as exc:
        return findings + [Finding("ERROR", "research-index.json", str(exc))]
    papers = index.get("papers") if isinstance(index, dict) else None
    if not isinstance(papers, list):
        return findings + [
            Finding("ERROR", "research-index.json", "papers must be an array")
        ]

    indexed_ids: set[str] = set()
    public_ids: set[str] = set()
    for position, paper in enumerate(papers):
        label = f"research-index.json.papers[{position}]"
        if not isinstance(paper, dict):
            findings.append(Finding("ERROR", label, "paper must be an object"))
            continue
        paper_id = paper.get("id")
        if not isinstance(paper_id, str) or not PAPER_ID_RE.fullmatch(paper_id):
            findings.append(
                Finding("ERROR", label, f"invalid paper id: {paper_id!r}")
            )
            continue
        indexed_ids.add(paper_id)
        if paper.get("state") in PUBLIC_STATES:
            public_ids.add(paper_id)
            receipt = root / "reports" / "publication-gates" / f"{paper_id}.json"
            if not receipt.is_file():
                findings.append(
                    Finding(
                        "ERROR",
                        receipt.relative_to(root).as_posix(),
                        "public paper is missing its mandatory publication-gate receipt",
                    )
                )
            else:
                findings.extend(validate_pass_receipt(root, paper_id, receipt))

    receipt_dir = root / "reports" / "publication-gates"
    if receipt_dir.is_dir():
        for receipt in sorted(receipt_dir.glob("*.json")):
            if receipt.stem not in indexed_ids:
                findings.append(
                    Finding(
                        "ERROR",
                        receipt.relative_to(root).as_posix(),
                        "receipt paper is absent from research-index.json",
                    )
                )
                continue
            if receipt.stem in public_ids:
                continue
            data, receipt_findings = validate_receipt_structure(
                root, receipt.stem, receipt
            )
            findings.extend(receipt_findings)
            if data is None:
                continue
            findings += require(
                data.get("status") == "HOLD",
                receipt.relative_to(root).as_posix(),
                "unreleased paper receipt must remain HOLD",
            )
            gates = data.get("gates")
            if isinstance(gates, dict):
                findings += require(
                    any(
                        isinstance(gate, dict) and gate.get("status") == "HOLD"
                        for gate in gates.values()
                    ),
                    receipt.relative_to(root).as_posix(),
                    "HOLD receipt must identify at least one blocking gate",
                )
    return findings


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--root",
        type=Path,
        default=Path(__file__).resolve().parents[1],
    )
    parser.add_argument("--json-output", type=Path)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = args.root.resolve()
    findings = validate(root)
    errors = [item for item in findings if item.level == "ERROR"]
    result = {
        "schema_version": "n.human_llm_mathematics.publication_gate_validation.v1",
        "root": "<repo>",
        "result": "PASS" if not errors else "FAIL",
        "error_count": len(errors),
        "findings": [asdict(item) for item in findings],
    }
    if args.json_output:
        args.json_output.parent.mkdir(parents=True, exist_ok=True)
        args.json_output.write_text(
            json.dumps(result, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
    for item in findings:
        print(f"{item.level}: {item.path}: {item.message}")
    print(
        json.dumps(
            {"result": result["result"], "error_count": len(errors)},
            sort_keys=True,
        )
    )
    return 0 if not errors else 1


if __name__ == "__main__":
    sys.exit(main())
