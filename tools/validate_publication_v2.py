#!/usr/bin/env python3
"""Run the publication validator for the corrected current public-review state."""

from __future__ import annotations

import sys

import validate_publication as base


# Do not reintroduce obsolete current states such as full_lean_requalification_hold.
base.SCAN_EXCLUDED_PATHS = frozenset()
base.VALID_STATES = frozenset({"active_review", "hold", "archived_case_study", "rejected", "superseded", "published"})


if __name__ == "__main__":
    sys.exit(base.main())
