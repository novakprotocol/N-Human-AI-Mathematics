#!/usr/bin/env python3
"""Run the corrected public-review validator with the v2 tool inventory."""

from __future__ import annotations

import sys

import validate_public_release as base


base.REQUIRED_FILES = set(base.REQUIRED_FILES) | {
    "tools/validate_publication_v2.py",
    "tools/validate_public_release_v2.py",
    "tools/validate_public_state.py",
}


if __name__ == "__main__":
    sys.exit(base.main())