#!/usr/bin/env python3
"""Run the publication validator without scanning validator vocabularies as release prose."""

from __future__ import annotations

import sys

import validate_publication as base


base.SCAN_EXCLUDED_PATHS = frozenset(
    {
        "tools/validate_publication.py",
        "tools/validate_publication_v2.py",
        "tools/validate_public_release.py",
        "tools/validate_public_state.py",
    }
)


if __name__ == "__main__":
    sys.exit(base.main())
