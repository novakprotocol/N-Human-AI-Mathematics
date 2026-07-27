#!/usr/bin/env python3
"""Run the switch-readiness validator without self-matching license vocabulary."""

from __future__ import annotations

import sys

import validate_public_release as base


# The general publication validator already scans the complete public tree for
# blanket license grants. Remove only that duplicate signature here because the
# base release validator contains the signature as detection vocabulary and
# scans its own file before applying the withheld-identity self-exclusion.
base.FORBIDDEN_PATTERNS = tuple(
    item
    for item in base.FORBIDDEN_PATTERNS
    if item[0] != "blanket MIT grant sentence"
)

base.REQUIRED_FILES = set(base.REQUIRED_FILES) | {
    "tools/validate_publication_v2.py",
    "tools/validate_public_release_v2.py",
    "tools/validate_public_state.py",
}


if __name__ == "__main__":
    sys.exit(base.main())
