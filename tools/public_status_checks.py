#!/usr/bin/env python3
"""Shared public-status validation helpers for the corrected review state."""

from __future__ import annotations

import json
import re
import subprocess
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable


PUBLIC_REPOSITORY = "novakprotocol/N-Human-AI-Mathematics"
CANONICAL_STATE: dict[str, dict[str, Any]] = {
    "HINC-001": {
        "research_state": "active_review",
        "portfolio_public_state": "ACTIVE_PUBLIC_CANDIDATE_TECHNICAL_REVIEW",
        "matrix_public_state": "ACTIVE_PUBLIC_CANDIDATE_TECHNICAL_REVIEW",
        "formal_state": "PARTIAL_PASS",
        "status_formal_state": "PARTIAL_PASS_BOUNDED_LEAN_VERIFICATION",
        "bounded_formal_scope": "bounded_Lean",
        "bounded_phrase": "bounded lean",
        "claim_map_complete": False,
        "full_manuscript_lean_verified": False,
        "external_specialist_review": "pending",
        "external_review": "pending",
        "historical_priority": "not_established",
        "research_historical_priority": "unestablished",
        "peer_review": "not_submitted",
        "journal_status": "not_submitted",
        "public_release_authorized": True,
        "active_public_review_authorized": True,
        "limitations_confirmed": True,
    },
    "ABF-001": {
        "research_state": "active_review",
        "portfolio_public_state": "ACTIVE_PUBLIC_CANDIDATE_TECHNICAL_REVIEW",
        "matrix_public_state": "ACTIVE_PUBLIC_CANDIDATE_TECHNICAL_REVIEW",
        "formal_state": "PARTIAL_PASS",
        "status_formal_state": "PARTIAL_PASS_BOUNDED_A01_LEAN_VERIFICATION",
        "bounded_formal_scope": "bounded_A01_Lean",
        "bounded_phrase": "bounded a01 lean",
        "compiled_bounded_lane": "A01",
        "compiled_lane": "A01",
        "a02_a06_status": "incomplete",
        "claim_map_complete": False,
        "full_manuscript_lean_verified": False,
        "external_specialist_review": "pending",
        "external_review": "pending",
        "historical_priority": "not_established",
        "research_historical_priority": "unestablished",
        "peer_review": "not_submitted",
        "journal_status": "not_submitted",
        "public_release_authorized": True,
        "active_public_review_authorized": True,
        "limitations_confirmed": True,
    },
    "FSG-001": {
        "research_state": "hold",
        "portfolio_public_state": "PRIVATE_CANDIDATE_MATHEMATICAL_BLOCKER_HOLD",
        "matrix_public_state": "PRIVATE_CANDIDATE_MATHEMATICAL_BLOCKER_HOLD",
        "formal_state": "HOLD_MATHEMATICAL_BLOCKER",
        "private_candidate": True,
        "mathematical_blocker": True,
        "public_theorem_package_released": False,
        "public_release_authorized": False,
        "full_manuscript_lean_verified": False,
    },
    "ACM-001": {
        "research_state": "hold",
        "portfolio_public_state": "HOLD_PENDING_CONSOLIDATION",
        "matrix_public_state": "HOLD_PENDING_CONSOLIDATION",
        "formal_state": "HOLD_PENDING_CONSOLIDATION",
        "controlling_manuscript_complete": False,
        "public_release_authorized": False,
        "full_manuscript_lean_verified": False,
    },
}

TEXT_STATUS_EXPECTED: dict[str, dict[str, str]] = {
    "HINC-001": {
        "paper_id": "HINC-001",
        "public_state": "active_review",
        "formal_state": "PARTIAL_PASS",
        "bounded_formal_scope": "bounded_Lean",
        "claim_map_complete": "false",
        "full_manuscript_lean_verified": "false",
        "external_specialist_review": "pending",
        "historical_priority": "not_established",
        "peer_review": "not_submitted",
        "journal_status": "not_submitted",
        "public_release_authorized": "true",
    },
    "ABF-001": {
        "paper_id": "ABF-001",
        "public_state": "active_review",
        "formal_state": "PARTIAL_PASS",
        "bounded_formal_scope": "bounded_A01_Lean",
        "compiled_lane": "A01",
        "a02_a06_status": "incomplete",
        "claim_map_complete": "false",
        "full_manuscript_lean_verified": "false",
        "external_specialist_review": "pending",
        "historical_priority": "not_established",
        "peer_review": "not_submitted",
        "journal_status": "not_submitted",
        "public_release_authorized": "true",
    },
    "FSG-001": {
        "paper_id": "FSG-001",
        "public_state": "hold",
        "private_candidate": "true",
        "mathematical_blocker": "true",
        "public_theorem_released": "false",
        "correction_status": "private_correction_under_internal_review",
        "external_review": "not_started",
        "formal_status": "HOLD_MATHEMATICAL_BLOCKER",
        "public_release_authorized": "false",
    },
    "ACM-001": {
        "paper_id": "ACM-001",
        "public_state": "hold",
        "manuscript_complete": "false",
        "claim_map_complete": "false",
        "full_manuscript_lean_verified": "false",
        "public_theorem_released": "false",
        "public_release_authorized": "false",
    },
}

CONTROLLED_JSON_FILES = (
    "research-index.json",
    "formal-verification-status.json",
    "PAPER_1_3_FULL_LEAN_STATUS.json",
    "papers/HINC-001/STATUS.json",
    "papers/ABF-001/STATUS.json",
    "reports/publication-gates/HINC-001.json",
    "reports/publication-gates/ABF-001.json",
)

CONTROLLED_TEXT_FILES = (
    "README.md",
    "STATUS.md",
    "START_HERE.md",
    "RESEARCH_INDEX.md",
    "AGENTS.md",
    "PUBLIC_REVIEW_RELEASE.md",
    "PUBLICATION_WORKFLOW.md",
    "FULL_LEAN_VERIFICATION_PROGRAM.md",
    "FULL_LEAN_RELEASE_STANDARD.md",
    "PUBLIC_REVIEW_FORMALIZATION_HOLD_2026-07-29.md",
    "FSG_001_PUBLIC_TEACHING_HOLD_2026-07-29.md",
    "docs/index.html",
    "docs/learn.html",
)

TEXT_SUFFIXES = {
    ".md",
    ".txt",
    ".json",
    ".yml",
    ".yaml",
    ".cff",
    ".py",
    ".ps1",
    ".sh",
    ".cmd",
    ".html",
    ".css",
    ".js",
    ".xml",
    ".toml",
}

APPROVED_PUBLIC_REPOSITORIES = {
    PUBLIC_REPOSITORY.casefold(),
    "novakprotocol/novak-sdt".casefold(),
}


@dataclass(frozen=True)
class Finding:
    level: str
    path: str
    message: str
    category: str = "validation"


def load_json(root: Path, relative: str) -> Any:
    return json.loads((root / relative).read_text(encoding="utf-8"))


def require(condition: bool, path: str, message: str, category: str) -> list[Finding]:
    return [] if condition else [Finding("ERROR", path, message, category)]


def text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def fold(value: Any) -> str:
    return str(value).casefold()




def status_control_findings(relative: str, data: dict[str, Any], paper_id: str) -> list[Finding]:
    expected = CANONICAL_STATE[paper_id]
    controls = data.get("status_controls")
    if not isinstance(controls, dict):
        return [Finding("ERROR", relative, f"{paper_id} status_controls block missing", "per_file_state_mismatch")]

    exact_keys: dict[str, Any] = {
        "public_state": expected["research_state"],
        "formal_state": expected["formal_state"],
        "bounded_formal_scope": expected["bounded_formal_scope"],
        "claim_map_complete": expected["claim_map_complete"],
        "full_manuscript_lean_verified": expected["full_manuscript_lean_verified"],
        "external_specialist_review": expected["external_specialist_review"],
        "historical_priority": expected["historical_priority"],
        "peer_review": expected["peer_review"],
        "journal_status": expected["journal_status"],
        "public_release_authorized": expected["public_release_authorized"],
        "limitations_confirmed": expected["limitations_confirmed"],
    }
    if paper_id == "ABF-001":
        exact_keys["compiled_lane"] = expected["compiled_lane"]
        exact_keys["a02_a06_status"] = expected["a02_a06_status"]

    findings: list[Finding] = []
    for key, expected_value in exact_keys.items():
        findings += require(controls.get(key) == expected_value, relative, f"{paper_id} status_controls.{key} mismatch", "per_file_state_mismatch")
    return findings

def reconcile_json_surface(root: Path, relative: str) -> list[Finding]:
    findings: list[Finding] = []
    data = load_json(root, relative)

    if relative == "research-index.json":
        papers = {item.get("id"): item for item in data.get("papers", []) if isinstance(item, dict)}
        findings += require(data.get("release_channel") == "public_review", relative, "current release channel must be public_review", "current_release_channel")
        findings += require(data.get("public_release_authorized") is True, relative, "existing public HINC/ABF review releases must remain authorized", "publication_state")
        for paper_id, expected in CANONICAL_STATE.items():
            record = papers.get(paper_id, {})
            findings += require(record.get("state") == expected["research_state"], relative, f"{paper_id} state mismatch", "per_file_state_mismatch")
            findings += require(record.get("peer_review") == "not_submitted", relative, f"{paper_id} must not claim completed peer review", "peer_review_overclaim")
            findings += require(record.get("historical_priority") == expected.get("research_historical_priority", "unestablished"), relative, f"{paper_id} must not claim historical priority", "historical_priority_overclaim")
            if paper_id in {"HINC-001", "ABF-001"}:
                formal = record.get("formal_verification", {})
                findings += require(isinstance(formal, dict), relative, f"{paper_id} formal_verification must be structured", "formal_state")
                if isinstance(formal, dict):
                    findings += require(formal.get("status") == "PARTIAL_PASS", relative, f"{paper_id} formal state must be PARTIAL_PASS", "formal_state")
                    findings += require(formal.get("claim_map_complete") is False, relative, f"{paper_id} claim map must remain incomplete", "full_lean_overclaim")
                    findings += require(formal.get("full_manuscript") == "not_fully_formalized", relative, f"{paper_id} full manuscript must remain incomplete", "full_lean_overclaim")
                    if paper_id == "ABF-001":
                        completed = " ".join(map(str, formal.get("completed_lanes", [])))
                        open_lanes = " ".join(map(str, formal.get("open_lanes", [])))
                        findings += require("A01" in completed and all(f"A0{i}" not in completed for i in range(2, 7)), relative, "ABF compiled bounded lane must be A01 only", "formal_state")
                        findings += require(all(f"A0{i}" in open_lanes for i in range(2, 7)), relative, "ABF A02-A06 lanes must remain incomplete", "full_lean_overclaim")
            if paper_id == "FSG-001":
                formal = record.get("formal_verification", {})
                findings += require(record.get("state") == "hold", relative, "FSG public state must remain hold", "fsg_hold")
                findings += require(isinstance(formal, dict), relative, "FSG formal_verification must be structured", "fsg_hold")
                if isinstance(formal, dict):
                    findings += require(formal.get("status") == "HOLD_MATHEMATICAL_BLOCKER", relative, "FSG must remain on mathematical hold", "fsg_hold")
                    findings += require(bool(formal.get("mathematical_blocker")), relative, "FSG mathematical blocker must remain explicit", "fsg_hold")
                    findings += require(formal.get("public_theorem_package_released") is False, relative, "FSG public theorem package must remain unreleased", "fsg_release")
                    findings += require(formal.get("public_release_authorized") is False, relative, "FSG public release must remain unauthorized", "fsg_release")
            if paper_id == "ACM-001":
                formal = record.get("formal_verification", {})
                findings += require(record.get("state") == "hold", relative, "ACM public state must remain hold", "acm_hold")
                findings += require(isinstance(formal, dict), relative, "ACM formal_verification must be structured", "acm_hold")
                if isinstance(formal, dict):
                    findings += require(formal.get("controlling_manuscript_present") is False, relative, "ACM controlling manuscript must remain incomplete", "acm_hold")

    elif relative == "formal-verification-status.json":
        portfolio = data.get("portfolio", {})
        findings += require(data.get("active_public_candidate_review_packages") == ["HINC-001", "ABF-001"], relative, "active candidate-review package list mismatch", "publication_state")
        findings += require(data.get("papers_with_full_pass") == [], relative, "no paper may be listed as FULL_PASS", "full_lean_overclaim")
        findings += require(data.get("fsg_public_release_authorized") is False, relative, "FSG release must remain unauthorized", "fsg_release")
        for paper_id, expected in CANONICAL_STATE.items():
            record = portfolio.get(paper_id, {})
            findings += require(record.get("public_state") == expected["portfolio_public_state"], relative, f"{paper_id} public state mismatch", "per_file_state_mismatch")
            findings += require(record.get("formal_status") == expected["formal_state"], relative, f"{paper_id} formal state mismatch", "formal_state")
            findings += require(record.get("full_manuscript_lean_verified") is False, relative, f"{paper_id} must not claim full Lean verification", "full_lean_overclaim")
            if paper_id in {"HINC-001", "ABF-001"}:
                findings += require(record.get("external_review") == "pending", relative, f"{paper_id} external review must remain pending", "peer_review_overclaim")
                findings += require(record.get("historical_priority") == "unestablished", relative, f"{paper_id} historical priority must remain unestablished", "historical_priority_overclaim")
        fsg = portfolio.get("FSG-001", {})
        findings += require(fsg.get("public_theorem_package_released") is False, relative, "FSG public theorem package must remain unreleased", "fsg_release")
        findings += require(fsg.get("public_mathematical_release_authorized") is False, relative, "FSG public release must remain unauthorized", "fsg_release")
        acm = portfolio.get("ACM-001", {})
        findings += require(acm.get("controlling_manuscript_present") is False, relative, "ACM controlling manuscript must remain incomplete", "acm_hold")

    elif relative == "PAPER_1_3_FULL_LEAN_STATUS.json":
        papers = data.get("papers", {})
        findings += require(data.get("global_state") == "HINC_ABF_ACTIVE_REVIEW_FSG_MATHEMATICAL_HOLD", relative, "global state mismatch", "publication_state")
        findings += require(data.get("fsg_public_release_authorized") is False, relative, "FSG public release must remain unauthorized", "fsg_release")
        for paper_id, expected in CANONICAL_STATE.items():
            record = papers.get(paper_id, {})
            findings += require(record.get("public_artifact_state") == expected["matrix_public_state"], relative, f"{paper_id} matrix state mismatch", "per_file_state_mismatch")
            findings += require(record.get("formal_status") == expected["formal_state"], relative, f"{paper_id} matrix formal state mismatch", "formal_state")
            findings += require(record.get("full_manuscript_lean_verified") is False, relative, f"{paper_id} must not claim full Lean verification", "full_lean_overclaim")
        findings += require(papers.get("FSG-001", {}).get("public_theorem_package_released") is False, relative, "FSG public theorem package must remain unreleased", "fsg_release")
        findings += require(papers.get("ACM-001", {}).get("controlling_manuscript_present") is False, relative, "ACM controlling manuscript must remain incomplete", "acm_hold")

    elif relative in {"papers/HINC-001/STATUS.json", "papers/ABF-001/STATUS.json"}:
        paper_id = "HINC-001" if "HINC-001" in relative else "ABF-001"
        expected = CANONICAL_STATE[paper_id]
        release = data.get("release", {})
        formal = data.get("formal_verification", {})
        review = data.get("review", {})
        findings += require(release.get("public_authorized") is True, relative, f"{paper_id} public review must remain authorized", "publication_state")
        findings += require(release.get("channel") == "public_review", relative, f"{paper_id} channel must be public_review", "current_release_channel")
        findings += require(formal.get("status") == expected["status_formal_state"], relative, f"{paper_id} bounded formal state mismatch", "formal_state")
        findings += require(formal.get("full_manuscript_lean_verified") is False, relative, f"{paper_id} must not claim full Lean verification", "full_lean_overclaim")
        findings += require(formal.get("claim_map_complete") is False, relative, f"{paper_id} claim map must remain incomplete", "full_lean_overclaim")
        findings += require(review.get("external") == "pending", relative, f"{paper_id} external specialist review must remain pending", "peer_review_overclaim")
        findings += require(review.get("peer_review") in {"not submitted", "not_submitted"}, relative, f"{paper_id} must not claim peer review", "peer_review_overclaim")
        findings += require("unestablished" in fold(review.get("historical_priority", "")), relative, f"{paper_id} historical priority must remain unestablished", "historical_priority_overclaim")
        findings.extend(status_control_findings(relative, data, paper_id))

    elif relative in {"reports/publication-gates/HINC-001.json", "reports/publication-gates/ABF-001.json"}:
        paper_id = "HINC-001" if "HINC-001" in relative else "ABF-001"
        findings += require(data.get("status") == "PASS_PUBLIC_TECHNICAL_REVIEW", relative, f"{paper_id} gate must remain candidate technical-review PASS", "publication_state")
        limitations = " ".join(map(str, data.get("limitations", []))).casefold()
        findings += require("not fully lean verified" in limitations or "not fully lean" in limitations, relative, f"{paper_id} gate must keep full-Lean limitation", "full_lean_boundary")
        findings += require("peer review" in limitations, relative, f"{paper_id} gate must keep peer-review limitation", "peer_review_boundary")

    return findings


STATUS_BLOCK_RE = re.compile(r"NHAIM_STATUS_BLOCK_V1\s*(.*?)\s*END_NHAIM_STATUS_BLOCK_V1", re.DOTALL)


def parse_status_block(body: str) -> dict[str, dict[str, str]]:
    match = STATUS_BLOCK_RE.search(body)
    if not match:
        return {}
    current: str | None = None
    parsed: dict[str, dict[str, str]] = {}
    for raw_line in match.group(1).splitlines():
        line = raw_line.strip()
        if not line:
            continue
        if line.endswith(":") and line[:-1] in TEXT_STATUS_EXPECTED:
            current = line[:-1]
            parsed[current] = {}
            continue
        if current and ":" in line:
            key, value = line.split(":", 1)
            parsed[current][key.strip()] = value.strip()
    return parsed


def block_status_findings(relative: str, body: str) -> list[Finding]:
    findings: list[Finding] = []
    matches = STATUS_BLOCK_RE.findall(body)
    findings += require(len(matches) == 1, relative, "exactly one NHAIM_STATUS_BLOCK_V1 block is required", "per_file_state_mismatch")
    parsed = parse_status_block(body)
    for paper_id, expected in TEXT_STATUS_EXPECTED.items():
        actual = parsed.get(paper_id)
        if actual is None:
            findings.append(Finding("ERROR", relative, f"{paper_id} status block missing", "per_file_state_mismatch"))
            continue
        unexpected = sorted(set(actual) - set(expected))
        if unexpected:
            findings.append(Finding("ERROR", relative, f"{paper_id} status block has unknown keys {unexpected}", "per_file_state_mismatch"))
        for key, expected_value in expected.items():
            findings += require(actual.get(key) == expected_value, relative, f"{paper_id} status block {key} mismatch", "per_file_state_mismatch")
    return findings


def negated_context(body: str, start: int, end: int) -> bool:
    left = max(body.rfind(".", 0, start), body.rfind(";", 0, start))
    right_candidates = [idx for idx in (body.find(".", end), body.find(";", end)) if idx != -1]
    right = min(right_candidates) if right_candidates else min(len(body), end + 80)
    window = body[left + 1:right].casefold()
    negators = (
        "not ", "no ", "never ", "without ", "must not", "does not", "do not",
        "is not", "are not", "unestablished", "forbidden", "absent", "disabled",
        "paused", "withheld", "superseded", "no claim", "not claimed", "not established",
    )
    return any(marker in window for marker in negators)


def add_pattern_findings(relative: str, body: str, patterns: Iterable[tuple[re.Pattern[str], str, str]], findings: list[Finding]) -> None:
    for pattern, category, message in patterns:
        for match in pattern.finditer(body):
            if not negated_context(body, match.start(), match.end()):
                findings.append(Finding("ERROR", relative, message, category))


def text_status_findings(relative: str, body: str) -> list[Finding]:
    lower = body.casefold()
    findings: list[Finding] = []
    findings.extend(block_status_findings(relative, body))

    exact_forbidden = (
        ("no active theorem packages", "obsolete_current_state"),
        ("active theorem status suspended", "obsolete_current_state"),
        ("historical public artifact only", "obsolete_current_state"),
        ("historical artifacts only", "obsolete_current_state"),
        ("full_lean_requalification_hold", "obsolete_current_state"),
        ("full-lean requalification hold", "obsolete_current_state"),
        ("full_pass sole active", "obsolete_current_state"),
        ("hold pending full lean", "obsolete_current_state"),
        ("zero blocking findings", "fsg_blocker_contradiction"),
        ("zero open blocking findings", "fsg_blocker_contradiction"),
        ("fsg-001 correction has passed", "fsg_correction_overclaim"),
        ("fsg-001 is ready for public theorem release", "fsg_release"),
        ("all claims are machine checked", "full_lean_overclaim"),
        ("peer reviewed: yes", "peer_review_overclaim"),
        ("peer_reviewed = true", "peer_review_overclaim"),
        ("peer reviewed</span><strong>yes", "peer_review_overclaim"),
        ("world-first", "historical_priority_overclaim"),
    )
    always_forbidden = {
        "no active theorem packages",
        "active theorem status suspended",
        "historical public artifact only",
        "historical artifacts only",
        "full_lean_requalification_hold",
        "full-lean requalification hold",
        "full_pass sole active",
        "hold pending full lean",
        "zero blocking findings",
        "zero open blocking findings",
        "fsg-001 correction has passed",
    }
    for phrase, category in exact_forbidden:
        index = lower.find(phrase)
        if index == -1:
            continue
        local = body[max(0, index - 120): min(len(body), index + len(phrase) + 120)].casefold()
        historical_exception = "superseded" in local and category == "obsolete_current_state"
        if phrase in always_forbidden:
            if not historical_exception:
                findings.append(Finding("ERROR", relative, f"forbidden current-status wording: {phrase}", category))
        elif not negated_context(body, index, index + len(phrase)):
            findings.append(Finding("ERROR", relative, f"forbidden current-status wording: {phrase}", category))

    hinc_patterns = (
        (re.compile(r"\bHINC-001\b[^.\n]{0,120}\b(?:withdrawn|inactive|suspended|retired)\b", re.IGNORECASE), "obsolete_current_state", "HINC inactive or withdrawn contradiction"),
        (re.compile(r"\bHINC-001\b[^.\n]{0,160}\bhistorical\s+(?:public\s+)?artifact(?:\s+only)?\b", re.IGNORECASE), "obsolete_current_state", "HINC historical-artifact-only contradiction"),
        (re.compile(r"\bHINC-001\b[^.\n]{0,120}\bfully\s+(?:Lean\s+)?(?:verified|formalized)\b", re.IGNORECASE), "full_lean_overclaim", "HINC full-Lean overclaim"),
        (re.compile(r"\bHINC-001\b[^.\n]{0,160}\bfull\s+manuscript\b[^.\n]{0,80}\b(?:verified|formalized|machine\s+checked)\b", re.IGNORECASE), "full_lean_overclaim", "HINC full-manuscript overclaim"),
        (re.compile(r"\bHINC-001\b[^.\n]{0,160}\b(?:claim[- ]map\s+(?:is\s+)?complete|all\s+claims\s+(?:are\s+)?formally\s+mapped)\b", re.IGNORECASE), "full_lean_overclaim", "HINC claim-map completion overclaim"),
        (re.compile(r"\bHINC-001\b[^.\n]{0,160}\b(?:journal\s+accepted|accepted\s+for\s+publication)\b", re.IGNORECASE), "peer_review_overclaim", "HINC journal-acceptance overclaim"),
        (re.compile(r"\bHINC-001\b[^.\n]{0,160}\b(?:externally\s+(?:validated|reviewed|reproduced)|external\s+review\s+(?:complete|completed|passed))\b", re.IGNORECASE), "peer_review_overclaim", "HINC external-review overclaim"),
        (re.compile(r"\bHINC-001\b[^.\n]{0,120}\bpeer[- ]review(?:ed)?\b[^.\n]{0,60}\b(?:complete|completed|accepted|yes|true)\b", re.IGNORECASE), "peer_review_overclaim", "HINC peer-review overclaim"),
        (re.compile(r"\bHINC-001\b[^.\n]{0,160}\b(?:historically\s+first|first\s+result\s+of\s+its\s+kind|world[- ]first|historical\s+priority\s+(?:established|claimed|proved))\b", re.IGNORECASE), "historical_priority_overclaim", "HINC priority overclaim"),
    )
    abf_patterns = (
        (re.compile(r"\bABF-001\b[^.\n]{0,120}\b(?:withdrawn|inactive|suspended|retired)\b", re.IGNORECASE), "obsolete_current_state", "ABF inactive or withdrawn contradiction"),
        (re.compile(r"\bABF-001\b[^.\n]{0,160}\bhistorical\s+(?:public\s+)?artifact(?:\s+only)?\b", re.IGNORECASE), "obsolete_current_state", "ABF historical-artifact-only contradiction"),
        (re.compile(r"\bABF-001\b[^.\n]{0,120}\bfully\s+(?:Lean\s+)?(?:verified|formalized)\b", re.IGNORECASE), "full_lean_overclaim", "ABF full-Lean overclaim"),
        (re.compile(r"\bABF-001\b[^.\n]{0,160}\bfull\s+manuscript\b[^.\n]{0,80}\b(?:verified|formalized|machine\s+checked)\b", re.IGNORECASE), "full_lean_overclaim", "ABF full-manuscript overclaim"),
        (re.compile(r"\bABF-001\b[^.\n]{0,160}\b(?:claim[- ]map\s+(?:is\s+)?complete|all\s+claims\s+(?:are\s+)?formally\s+mapped)\b", re.IGNORECASE), "full_lean_overclaim", "ABF claim-map completion overclaim"),
        (re.compile(r"\bABF-001\b[^.\n]{0,200}\bA02\s*(?:-|through|to|\u2013)\s*A06\b[^.\n]{0,100}\b(?:complete|verified|passed|formalized)\b", re.IGNORECASE), "full_lean_overclaim", "ABF A02-A06 completion overclaim"),
        (re.compile(r"\bABF-001\b[^.\n]{0,200}\bcomplete\s+Boolean\s+atlas\b[^.\n]{0,100}\bformally\s+proved\b", re.IGNORECASE), "full_lean_overclaim", "ABF Boolean-atlas completion overclaim"),
        (re.compile(r"\bABF-001\b[^.\n]{0,160}\b(?:journal\s+accepted|accepted\s+for\s+publication)\b", re.IGNORECASE), "peer_review_overclaim", "ABF journal-acceptance overclaim"),
        (re.compile(r"\bABF-001\b[^.\n]{0,160}\b(?:externally\s+(?:validated|reviewed|reproduced)|external\s+review\s+(?:complete|completed|passed))\b", re.IGNORECASE), "peer_review_overclaim", "ABF external-review overclaim"),
        (re.compile(r"\bABF-001\b[^.\n]{0,120}\bpeer[- ]review(?:ed)?\b[^.\n]{0,60}\b(?:complete|completed|accepted|yes|true)\b", re.IGNORECASE), "peer_review_overclaim", "ABF peer-review overclaim"),
        (re.compile(r"\bABF-001\b[^.\n]{0,160}\b(?:historically\s+first|first\s+result\s+of\s+its\s+kind|world[- ]first|historical\s+priority\s+(?:established|claimed|proved))\b", re.IGNORECASE), "historical_priority_overclaim", "ABF priority overclaim"),
    )
    fsg_patterns = (
        (re.compile(r"\bFSG-001\b[^.\n]{0,120}\bactive\s+public\s+theorem\b", re.IGNORECASE), "fsg_release", "FSG active public theorem overclaim"),
        (re.compile(r"\bFSG-001\b[^.\n]{0,160}\b(?:corrected|repaired)\s+theorem\b[^.\n]{0,80}\b(?:established|passed|accepted|proved)\b", re.IGNORECASE), "fsg_correction_overclaim", "FSG corrected theorem overclaim"),
        (re.compile(r"\bFSG-001\b[^.\n]{0,120}\bzero\s+(?:open\s+)?block(?:er|ing\s+finding)s?\b", re.IGNORECASE), "fsg_blocker_contradiction", "FSG zero-blocker contradiction"),
        (re.compile(r"\bFSG-001\b[^.\n]{0,120}\bblocker\s+removed\b", re.IGNORECASE), "fsg_blocker_contradiction", "FSG blocker-removal contradiction"),
        (re.compile(r"\bFSG-001\b[^.\n]{0,120}\bexternally\s+(?:validated|reviewed|reproduced)\b", re.IGNORECASE), "peer_review_overclaim", "FSG external-review overclaim"),
        (re.compile(r"\bFSG-001\b[^.\n]{0,160}\bcorrection\s+passed\s+external\s+review\b", re.IGNORECASE), "peer_review_overclaim", "FSG correction external-review overclaim"),
        (re.compile(r"\bFSG-001\b[^.\n]{0,120}\bpublicly\s+released\b", re.IGNORECASE), "fsg_release", "FSG public-release overclaim"),
        (re.compile(r"\bFSG-001\b[^.\n]{0,160}\bpublic\s+release\s+ready\b", re.IGNORECASE), "fsg_release", "FSG public-release readiness overclaim"),
    )
    acm_patterns = (
        (re.compile(r"\bACM-001\b[^.\n]{0,120}\bactive\s+(?:public\s+)?theorem(?:\s+package)?\b", re.IGNORECASE), "acm_hold", "ACM active theorem package overclaim"),
        (re.compile(r"\bACM-001\b[^.\n]{0,120}\b(?:controlling\s+)?manuscript\b[^.\n]{0,80}\bcomplete\b", re.IGNORECASE), "acm_hold", "ACM manuscript completion overclaim"),
        (re.compile(r"\bACM-001\b[^.\n]{0,160}\bclaim[- ]map\s+(?:is\s+)?complete\b", re.IGNORECASE), "acm_hold", "ACM claim-map completion overclaim"),
        (re.compile(r"\bACM-001\b[^.\n]{0,160}\b(?:fully\s+Lean\s+verified|full\s+Lean\b[^.\n]{0,80}\bcomplete)\b", re.IGNORECASE), "full_lean_overclaim", "ACM full-Lean overclaim"),
    )
    add_pattern_findings(relative, body, hinc_patterns, findings)
    add_pattern_findings(relative, body, abf_patterns, findings)
    add_pattern_findings(relative, body, fsg_patterns, findings)
    add_pattern_findings(relative, body, acm_patterns, findings)
    return findings


def reconcile_text_surface(root: Path, relative: str) -> list[Finding]:
    return text_status_findings(relative, text(root / relative))


GITHUB_REPO_URL_RE = re.compile(r"https?://github\.com/([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)", re.IGNORECASE)
NOVAK_REPO_TOKEN_RE = re.compile(r"\bnovakprotocol/([A-Za-z0-9_.-]+)\b", re.IGNORECASE)
GENERIC_REPO_TOKEN_RE = re.compile(r"\b((?:example\.invalid|[a-z0-9_.-]+-sentinel)/(?:nonpublic|private|withheld|sentinel)[a-z0-9_.-]*)\b", re.IGNORECASE)
PRIVATE_REPOSITORY_SHORTHAND_RE = re.compile(r"\b[A-Z](?:-[A-Za-z0-9]+)*Lab\b")
PRIVATE_STYLE_PR_RE = re.compile(
    r"\b(?:private|nonpublic|withheld)\s+(?:lab|laboratory|repository|source|project)[^\n]{0,80}\b(?:PR|pull|issue)\b\s*(?:#?\d+|#[A-Z][A-Z0-9_-]*)\b"
    r"|\b(?:PR|pull|issue)\b\s*(?:#?\d+|#[A-Z][A-Z0-9_-]*)\b[^\n]{0,80}\b(?:private|nonpublic|withheld)\s+(?:lab|laboratory|repository|source|project)\b",
    re.IGNORECASE,
)
NONPUBLIC_PROJECT_PR_LINK_RE = re.compile(r"https?://(?:github\.com/)?[A-Za-z0-9_.-]+/(?:nonpublic|private|withheld|sentinel)[A-Za-z0-9_.-]+/(?:pull|issues?)/[A-Za-z0-9_-]+", re.IGNORECASE)
PRIVATE_BRANCH_RE = re.compile(r"\b(?:agent|fix|formal|private|nonpublic|withheld)/(?:private|nonpublic|withheld|fsg|sentinel|synthetic)[A-Za-z0-9._/-]*\b", re.IGNORECASE)
PRIVATE_PATH_RE = re.compile(r"\b(?:papers|manuscript|manuscripts|source|src|formal|review|reviews|evidence|artifact|artifacts|release)/(?:private|nonpublic|withheld|fsg|sentinel|synthetic)[A-Za-z0-9._/-]*\b", re.IGNORECASE)
PRIVATE_WINDOWS_PATH_RE = re.compile(r"[A-Za-z]:\\(?:[^\\\r\n]+\\)*(?:private|nonpublic|withheld|fsg|sentinel|synthetic)[^\\\r\n]*(?:\\[^\\\r\n]+)*", re.IGNORECASE)
HASH_RE = re.compile(r"\b[0-9a-f]{40}\b", re.IGNORECASE)
PRIVATE_HASH_CONTEXT_RE = re.compile(r"\b(?:private|nonpublic|internal source|private provenance|internal provenance|withheld)\b", re.IGNORECASE)
PUBLIC_HASH_CONTEXT_MARKERS = (
    "compiled source commit",
    "formal_source_commit",
    "immutable source",
    "merge commit",
    "novakprotocol/n-human-ai-mathematics",
    "novakprotocol/novak-sdt",
    "public checker",
    "public export",
    "release branch source commit",
    "source commit",
    "standalone initial commit",
)
SYNTHETIC_PRIVATE_HOST_RE = re.compile(r"\bexample\.invalid/(?:private|nonpublic|internal|withheld|sentinel)[A-Za-z0-9._/-]*", re.IGNORECASE)
DYNAMIC_REPO_URL_CONSTRUCTION_RE = re.compile(
    r"[\"']https?://github\.com/?[\"']\s*\+\s*[\"'][^\"']*(?:novakprotocol|nonpublic|private|withheld|sentinel|synthetic)[^\"']*[\"']"
    r"|[\"']https?://github\.com/novakprotocol/?[\"']\s*\+\s*[\"'][^\"']+[\"']",
    re.IGNORECASE,
)
DYNAMIC_PR_CONSTRUCTION_RE = re.compile(
    r"(?:private|nonpublic|withheld)[^\n]{0,120}(?:[\"'][^\"']*[\"']\s*\+\s*)+[\"'][^\"']*(?:PR|pull|issue|pull/)[^\"']*[\"']"
    r"|[\"'](?:private|nonpublic|withheld)[^\"']*[\"']\s*\+\s*[\"'][^\"']*(?:PR|pull|issue|pull/)[^\"']*[\"']",
    re.IGNORECASE,
)
DYNAMIC_BRANCH_CONSTRUCTION_RE = re.compile(r"[\"'](?:agent|fix|formal|private|nonpublic|withheld)/[\"']\s*\+\s*[\"'][^\"']*(?:private|nonpublic|withheld|fsg|sentinel|synthetic)[^\"']*[\"']", re.IGNORECASE)
DYNAMIC_PATH_CONSTRUCTION_RE = re.compile(r"[\"'](?:manuscript|manuscripts|source|evidence|artifact|artifacts)/[\"']\s*\+\s*[\"'][^\"']*(?:private|nonpublic|withheld|fsg|sentinel|synthetic)[^\"']*[\"']", re.IGNORECASE)


def line_number(body: str, offset: int) -> int:
    return body.count("\n", 0, offset) + 1


def line_text(body: str, offset: int) -> str:
    start = body.rfind("\n", 0, offset) + 1
    end = body.find("\n", offset)
    if end == -1:
        end = len(body)
    return body[start:end]


def private_hash_context_findings(relative: str, body: str) -> list[Finding]:
    findings: list[Finding] = []
    emitted: set[tuple[str, int]] = set()

    def emit(offset: int) -> None:
        line = line_number(body, offset)
        key = (relative, line)
        if key not in emitted:
            emitted.add(key)
            findings.append(Finding("ERROR", f"{relative}:{line}", "private-context exact source hash", "private_reference"))

    for match in HASH_RE.finditer(body):
        hash_line = line_text(body, match.start())
        if PRIVATE_HASH_CONTEXT_RE.search(hash_line):
            emit(match.start())
            continue
        paragraph_start = body.rfind("\n\n", 0, match.start()) + 2
        paragraph_end = body.find("\n\n", match.end())
        if paragraph_end == -1:
            paragraph_end = len(body)
        paragraph = body[paragraph_start:paragraph_end]
        folded_line = hash_line.casefold()
        folded_paragraph = paragraph.casefold()
        public_context = any(marker in folded_line or marker in folded_paragraph for marker in PUBLIC_HASH_CONTEXT_MARKERS)
        if PRIVATE_HASH_CONTEXT_RE.search(paragraph) and not public_context:
            emit(match.start())

    structured = re.compile(
        r"(?is)\b(?:source_classification|source_provenance|private_provenance|classification)\s*:\s*"
        r"(?:private|nonpublic|internal source|private provenance)\b.{0,250}?"
        r"\b(?:source_commit|commit|source_sha|sha)\s*:\s*\n?\s*([0-9a-f]{40})\b"
    )
    for match in structured.finditer(body):
        emit(match.start(1))
    return findings

def private_reference_findings(relative: str, body: str) -> list[Finding]:
    findings: list[Finding] = []
    for match in GITHUB_REPO_URL_RE.finditer(body):
        repo = match.group(1).casefold().removesuffix(".git")
        if repo not in APPROVED_PUBLIC_REPOSITORIES:
            findings.append(Finding("ERROR", f"{relative}:{line_number(body, match.start())}", "non-allowlisted project repository URL", "private_reference"))
    for match in NOVAK_REPO_TOKEN_RE.finditer(body):
        repo = f"novakprotocol/{match.group(1)}".casefold().removesuffix(".git")
        if repo not in APPROVED_PUBLIC_REPOSITORIES:
            findings.append(Finding("ERROR", f"{relative}:{line_number(body, match.start())}", "non-allowlisted novakprotocol repository reference", "private_reference"))
    for pattern, message in (
        (GENERIC_REPO_TOKEN_RE, "synthetic or nonpublic repository token"),
        (PRIVATE_REPOSITORY_SHORTHAND_RE, "private repository shorthand"),
        (PRIVATE_STYLE_PR_RE, "private-style PR or issue reference"),
        (NONPUBLIC_PROJECT_PR_LINK_RE, "nonpublic project PR or issue link"),
        (PRIVATE_BRANCH_RE, "private-style branch name"),
        (PRIVATE_PATH_RE, "private manuscript/source/evidence/artifact path"),
        (PRIVATE_WINDOWS_PATH_RE, "private-style local path"),
        (SYNTHETIC_PRIVATE_HOST_RE, "synthetic nonpublic host reference"),
        (DYNAMIC_REPO_URL_CONSTRUCTION_RE, "dynamically constructed nonallowlisted repository URL"),
        (DYNAMIC_PR_CONSTRUCTION_RE, "dynamically constructed private-style PR reference"),
        (DYNAMIC_BRANCH_CONSTRUCTION_RE, "dynamically constructed private-style branch"),
        (DYNAMIC_PATH_CONSTRUCTION_RE, "dynamically constructed private-style path"),
    ):
        for match in pattern.finditer(body):
            findings.append(Finding("ERROR", f"{relative}:{line_number(body, match.start())}", message, "private_reference"))
    findings.extend(private_hash_context_findings(relative, body))
    return findings

def credential_findings(relative: str, body: str) -> list[Finding]:
    pieces = {
        "key_begin": "-----BEGIN ",
        "key_end": "PRIVATE KEY-----",
    }
    patterns = (
        ("GitHub token", re.compile(r"(?:gh[oprsu]_|github_pat_)[A-Za-z0-9_]{20,}")),
        ("private-key material", re.compile(re.escape(pieces["key_begin"]) + r"(?:RSA |EC |OPENSSH )?" + re.escape(pieces["key_end"]))),
        ("personal Windows path", re.compile(r"[A-Za-z]:(?:\\\\|\\)Users(?:\\\\|\\)[^\\\s\"]+", re.IGNORECASE)),
        ("personal POSIX path", re.compile(r"/(?:Users|home)/[^/\\\s\"]+", re.IGNORECASE)),
    )
    findings: list[Finding] = []
    for label, pattern in patterns:
        match = pattern.search(body)
        if match:
            line = body.count("\n", 0, match.start()) + 1
            findings.append(Finding("ERROR", f"{relative}:{line}", label, "credential_or_personal_path"))
    return findings

SCAN_EXCLUSION_RE = re.compile(
    r'"scan_excluded_paths"\s*:\s*\[(?!\s*\])|SCAN_EXCLUDED_PATHS\s*=\s*(?!\s*(?:frozenset\(\)|set\(\)|\{\}))',
    re.IGNORECASE,
)


def validator_workflow_exclusion_findings(relative: str, body: str) -> list[Finding]:
    findings: list[Finding] = []
    for match in SCAN_EXCLUSION_RE.finditer(body):
        line = body.count("\n", 0, match.start()) + 1
        findings.append(Finding("ERROR", f"{relative}:{line}", "active private-scan exclusion", "validator_workflow_exclusion"))
    return findings


def all_text_files(root: Path) -> list[Path]:
    paths: list[Path] = []
    skipped_dirs = {".git", ".lake", ".venv", "__pycache__", ".artifacts", "_mutation_work", "_schema_negative_work", "_internal_link_work"}
    for path in root.rglob("*"):
        relative_parts = path.relative_to(root).parts
        if any(part in skipped_dirs for part in relative_parts):
            continue
        if path.is_file() and path.suffix.lower() in TEXT_SUFFIXES:
            paths.append(path)
    return paths


def tracked_text_files(root: Path) -> list[Path]:
    if not (root / ".git").exists():
        return all_text_files(root)
    try:
        tracked = subprocess.run(
            ["git", "ls-files"],
            cwd=root,
            text=True,
            capture_output=True,
            check=True,
        )
        untracked = subprocess.run(
            ["git", "ls-files", "--others", "--exclude-standard"],
            cwd=root,
            text=True,
            capture_output=True,
            check=True,
        )
    except subprocess.CalledProcessError:
        return all_text_files(root)
    paths = []
    for item in [*tracked.stdout.splitlines(), *untracked.stdout.splitlines()]:
        path = root / item
        if path.is_file() and path.suffix.lower() in TEXT_SUFFIXES:
            paths.append(path)
    return sorted(set(paths))


def changed_text_files(root: Path, base_ref: str = "origin/main") -> list[Path]:
    if not (root / ".git").exists():
        return all_text_files(root)
    result = subprocess.run(
        ["git", "diff", "--name-only", f"{base_ref}...HEAD"],
        cwd=root,
        text=True,
        capture_output=True,
        check=True,
    )
    untracked = subprocess.run(
        ["git", "ls-files", "--others", "--exclude-standard"],
        cwd=root,
        text=True,
        capture_output=True,
        check=True,
    )
    paths = []
    for item in [*result.stdout.splitlines(), *untracked.stdout.splitlines()]:
        path = root / item
        if path.is_file() and path.suffix.lower() in TEXT_SUFFIXES:
            paths.append(path)
    return sorted(set(paths))


def scan_paths(root: Path, paths: Iterable[Path]) -> list[Finding]:
    findings: list[Finding] = []
    for path in sorted(paths):
        relative = path.relative_to(root).as_posix()
        try:
            body = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            findings.append(Finding("ERROR", relative, "text file is not UTF-8", "encoding"))
            continue
        findings.extend(credential_findings(relative, body))
        findings.extend(private_reference_findings(relative, body))
        findings.extend(validator_workflow_exclusion_findings(relative, body))
    return findings


def status_surface_findings(root: Path) -> list[Finding]:
    findings: list[Finding] = []
    for relative in CONTROLLED_JSON_FILES:
        path = root / relative
        findings += require(path.is_file(), relative, "required controlled JSON surface missing", "required_file")
        if path.is_file():
            findings.extend(reconcile_json_surface(root, relative))
    for relative in CONTROLLED_TEXT_FILES:
        path = root / relative
        findings += require(path.is_file(), relative, "required controlled text surface missing", "required_file")
        if path.is_file():
            findings.extend(reconcile_text_surface(root, relative))
    return findings
