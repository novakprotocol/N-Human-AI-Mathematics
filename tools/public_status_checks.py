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
        "bounded_phrase": "bounded lean",
        "full_manuscript_lean_verified": False,
        "active_public_review_authorized": True,
    },
    "ABF-001": {
        "research_state": "active_review",
        "portfolio_public_state": "ACTIVE_PUBLIC_CANDIDATE_TECHNICAL_REVIEW",
        "matrix_public_state": "ACTIVE_PUBLIC_CANDIDATE_TECHNICAL_REVIEW",
        "formal_state": "PARTIAL_PASS",
        "status_formal_state": "PARTIAL_PASS_BOUNDED_A01_LEAN_VERIFICATION",
        "bounded_phrase": "bounded a01 lean",
        "compiled_bounded_lane": "A01",
        "full_manuscript_lean_verified": False,
        "active_public_review_authorized": True,
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
            findings += require(record.get("historical_priority") == "unestablished", relative, f"{paper_id} must not claim historical priority", "historical_priority_overclaim")
            if paper_id in {"HINC-001", "ABF-001"}:
                formal = record.get("formal_verification", {})
                findings += require(formal.get("status") == "PARTIAL_PASS", relative, f"{paper_id} formal state must be PARTIAL_PASS", "formal_state")
                findings += require(formal.get("full_manuscript") == "not_fully_formalized", relative, f"{paper_id} full manuscript must remain incomplete", "full_lean_overclaim")
            if paper_id == "FSG-001":
                formal = record.get("formal_verification", {})
                findings += require(formal.get("status") == "HOLD_MATHEMATICAL_BLOCKER", relative, "FSG must remain on mathematical hold", "fsg_hold")
                findings += require(formal.get("public_theorem_package_released") is False, relative, "FSG public theorem package must remain unreleased", "fsg_release")
                findings += require(formal.get("public_release_authorized") is False, relative, "FSG public release must remain unauthorized", "fsg_release")
            if paper_id == "ACM-001":
                formal = record.get("formal_verification", {})
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
        findings += require(release.get("public_authorized") is True, relative, f"{paper_id} public review must remain authorized", "publication_state")
        findings += require(release.get("channel") == "public_review", relative, f"{paper_id} channel must be public_review", "current_release_channel")
        findings += require(formal.get("status") == expected["status_formal_state"], relative, f"{paper_id} bounded formal state mismatch", "formal_state")
        findings += require(formal.get("full_manuscript_lean_verified") is False, relative, f"{paper_id} must not claim full Lean verification", "full_lean_overclaim")
        findings += require(data.get("review", {}).get("peer_review") == "not submitted", relative, f"{paper_id} must not claim peer review", "peer_review_overclaim")

    elif relative in {"reports/publication-gates/HINC-001.json", "reports/publication-gates/ABF-001.json"}:
        paper_id = "HINC-001" if "HINC-001" in relative else "ABF-001"
        findings += require(data.get("status") == "PASS_PUBLIC_TECHNICAL_REVIEW", relative, f"{paper_id} gate must remain candidate technical-review PASS", "publication_state")
        limitations = " ".join(map(str, data.get("limitations", []))).casefold()
        findings += require("not fully lean verified" in limitations or "not fully lean" in limitations, relative, f"{paper_id} gate must keep full-Lean limitation", "full_lean_boundary")
        findings += require("peer review" in limitations, relative, f"{paper_id} gate must keep peer-review limitation", "peer_review_boundary")

    return findings


def text_status_findings(relative: str, body: str) -> list[Finding]:
    lower = body.casefold()
    findings: list[Finding] = []

    required = {
        "HINC-001": ("hinc-001", "active", "candidate", "partial_pass", "bounded"),
        "ABF-001": ("abf-001", "active", "candidate", "partial_pass", "bounded", "a01"),
        "FSG-001": ("fsg-001", "hold", "mathematical blocker", "no public"),
        "ACM-001": ("acm-001", "hold", "consolidation"),
    }
    for paper_id, phrases in required.items():
        missing = [phrase for phrase in phrases if phrase not in lower]
        findings += require(not missing, relative, f"{paper_id} text state is incomplete; missing {missing}", "per_file_state_mismatch")

    forbidden_patterns = (
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
    for phrase, category in forbidden_patterns:
        historical_pr57_record = (
            relative == "PUBLIC_REVIEW_FORMALIZATION_HOLD_2026-07-29.md"
            and category == "obsolete_current_state"
            and phrase in {"full-lean requalification hold", "full_lean_requalification_hold"}
            and "superseded" in lower
        )
        if phrase in lower and not historical_pr57_record:
            findings.append(Finding("ERROR", relative, f"forbidden current-status wording: {phrase}", category))

    overclaim_patterns = (
        (re.compile(r"\b(?:hinc-001|abf-001)\b[^.\n]{0,80}\bis\s+fully\s+lean\s+verified", re.IGNORECASE), "full_lean_overclaim", "fully Lean verified paper claim"),
        (re.compile(r"\b(?:hinc-001|abf-001)\b[^.\n]{0,80}\bis\s+fully\s+formalized", re.IGNORECASE), "full_lean_overclaim", "fully formalized paper claim"),
        (re.compile(r"\b(?:the\s+)?manuscripts\s+are\s+fully\s+formalized", re.IGNORECASE), "full_lean_overclaim", "fully formalized manuscript claim"),
    )
    for pattern, category, message in overclaim_patterns:
        if pattern.search(body):
            findings.append(Finding("ERROR", relative, message, category))

    return findings


def reconcile_text_surface(root: Path, relative: str) -> list[Finding]:
    return text_status_findings(relative, text(root / relative))


GITHUB_REPO_URL_RE = re.compile(r"https?://github\.com/([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)", re.IGNORECASE)
GENERIC_REPO_TOKEN_RE = re.compile(r"\b((?:example\.invalid|[a-z0-9_.-]+)/(?:nonpublic|private|withheld|sentinel)[a-z0-9_.-]*)\b")
PRIVATE_STYLE_PR_RE = re.compile(r"\b(?:private|nonpublic|withheld|fsg)[^\n]{0,80}\b(?:PR|pull|issue)\s*#?\d+\b|\b(?:PR|pull|issue)\s*#?\d+\b[^\n]{0,80}\b(?:private|nonpublic|withheld|fsg)\b", re.IGNORECASE)
PRIVATE_BRANCH_RE = re.compile(r"\b(?:agent|fix|formal)/(?:private|nonpublic|withheld|fsg)[A-Za-z0-9._/-]*\b", re.IGNORECASE)
PRIVATE_PATH_RE = re.compile(r"\b(?:papers|manuscript|source|src|formal|review|reviews|evidence|artifact|artifacts|release)/(?:private|nonpublic|withheld|fsg)[A-Za-z0-9._/-]*\b", re.IGNORECASE)
PRIVATE_WINDOWS_PATH_RE = re.compile(r"[A-Za-z]:\\(?:[^\\\r\n]+\\)*(?:private|nonpublic|withheld|fsg)[^\\\r\n]*(?:\\[^\\\r\n]+)*", re.IGNORECASE)
EXACT_HASH_CONTEXT_RE = re.compile(r"\b(?:private|nonpublic|withheld|fsg)[^\n]{0,80}\b[0-9a-f]{40}\b|\b[0-9a-f]{40}\b[^\n]{0,80}\b(?:private|nonpublic|withheld|fsg)\b", re.IGNORECASE)
SYNTHETIC_PRIVATE_HOST_RE = re.compile(r"\bexample\.invalid/(?:private|nonpublic|internal|withheld)[A-Za-z0-9._/-]*", re.IGNORECASE)


def private_reference_findings(relative: str, body: str) -> list[Finding]:
    findings: list[Finding] = []
    for match in GITHUB_REPO_URL_RE.finditer(body):
        repo = match.group(1).casefold()
        if repo not in APPROVED_PUBLIC_REPOSITORIES:
            line = body.count("\n", 0, match.start()) + 1
            findings.append(Finding("ERROR", f"{relative}:{line}", "non-allowlisted project repository URL", "private_reference"))
    for pattern, message in (
        (GENERIC_REPO_TOKEN_RE, "synthetic or nonpublic repository token"),
        (PRIVATE_STYLE_PR_RE, "private-style PR or issue reference"),
        (PRIVATE_BRANCH_RE, "private-style branch name"),
        (PRIVATE_PATH_RE, "private manuscript/source/evidence/artifact path"),
        (PRIVATE_WINDOWS_PATH_RE, "private-style local path"),
        (EXACT_HASH_CONTEXT_RE, "private-context exact source hash"),
        (SYNTHETIC_PRIVATE_HOST_RE, "synthetic nonpublic host reference"),
    ):
        for match in pattern.finditer(body):
            line = body.count("\n", 0, match.start()) + 1
            findings.append(Finding("ERROR", f"{relative}:{line}", message, "private_reference"))
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
    r'"scan_excluded_paths"\s*:\s*\[(?!\s*\])|SCAN_EXCLUDED_PATHS\s*=\s*(?!frozenset\(\)|set\(\)|\{\})',
    re.IGNORECASE,
)
HISTORICAL_MARKER_RE = re.compile(r"\b(?:HISTORICAL|SUPERSEDED|NO LONGER CURRENT|PRE[-_ ]?MAJOR[-_ ]?REPAIR|PRE[-_ ]?CORRECTION)\b", re.IGNORECASE)


def validator_workflow_exclusion_findings(relative: str, body: str) -> list[Finding]:
    findings: list[Finding] = []
    for match in SCAN_EXCLUSION_RE.finditer(body):
        context = body[max(0, match.start() - 240): min(len(body), match.end() + 360)]
        if HISTORICAL_MARKER_RE.search(context):
            continue
        line = body.count("\n", 0, match.start()) + 1
        findings.append(Finding("ERROR", f"{relative}:{line}", "active private-scan exclusion", "validator_workflow_exclusion"))
    return findings


def all_text_files(root: Path) -> list[Path]:
    paths: list[Path] = []
    skipped_dirs = {".git", ".lake", ".venv", "__pycache__", ".artifacts", "_mutation_work"}
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
        result = subprocess.run(
            ["git", "ls-files"],
            cwd=root,
            text=True,
            capture_output=True,
            check=True,
        )
    except subprocess.CalledProcessError:
        return all_text_files(root)
    paths = []
    for item in result.stdout.splitlines():
        path = root / item
        if path.is_file() and path.suffix.lower() in TEXT_SUFFIXES:
            paths.append(path)
    return paths


def changed_text_files(root: Path, base_ref: str = "origin/main") -> list[Path]:
    if not (root / ".git").exists():
        return [root / rel for rel in CONTROLLED_TEXT_FILES if (root / rel).is_file()]
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
