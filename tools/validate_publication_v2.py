#!/usr/bin/env python3
"""Run the publication validator with the current full-Lean status vocabulary."""

from __future__ import annotations

import sys

import validate_publication as base


base.SCAN_EXCLUDED_PATHS = frozenset(
    {
        "tools/validate_publication.py",
        "tools/validate_publication_v2.py",
        "tools/validate_public_release.py",
        "tools/validate_public_release_v2.py",
        "tools/validate_public_state.py",
        "tools/Invoke-PublicSwitchPreflight.ps1",
        "tools/validate_full_lean_portfolio.py",
        "tools/validate_status_consistency.py",
        "tools/validate_learning_page.py",
    }
)

base.VALID_STATES = frozenset(
    set(base.VALID_STATES)
    | {
        "public_archive_full_lean_requalification_hold",
        "private_full_lean_completion_hold",
        "blocked_until_papers_1_3_full_pass",
        "teaching_preview_blocked_until_papers_1_3_full_pass",
    }
)


if __name__ == "__main__":
    sys.exit(base.main())
