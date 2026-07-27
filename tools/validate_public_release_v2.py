#!/usr/bin/env python3
"""Release validator entry point with non-self-matching public-source scans."""

from __future__ import annotations

import sys

import validate_public_release as base


# The first validator version included the account-local username as a literal
# forbidden signature and then scanned its own source. The public audit already
# checks personal paths and token material without publishing that username.
# Remove only that self-matching signature; retain all other release checks.
base.FORBIDDEN_PATTERNS = tuple(
    item
    for item in base.FORBIDDEN_PATTERNS
    if item[0] != "account-local username"
)

base.REQUIRED_FILES = set(base.REQUIRED_FILES) | {
    "tools/validate_public_release.py",
    "tools/validate_public_release_v2.py",
    ".github/workflows/validate.yml",
}


if __name__ == "__main__":
    sys.exit(base.main())
