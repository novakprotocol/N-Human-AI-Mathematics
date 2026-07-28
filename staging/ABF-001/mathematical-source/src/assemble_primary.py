#!/usr/bin/env python3
"""Reassemble the exact ABF-001 primary verifier from a gzip/base64 bundle."""
from __future__ import annotations
import base64, gzip, hashlib, json
from pathlib import Path
ROOT = Path(__file__).resolve().parent
BUNDLE = ROOT / "_primary_bundle"
TARGET = ROOT / "abf001_verifier.py"
def main() -> int:
    manifest = json.loads((BUNDLE / "manifest.json").read_text(encoding="utf-8"))
    encoded = "".join((ROOT.parent / item["path"]).read_text(encoding="ascii") for item in manifest["parts"])
    data = gzip.decompress(base64.b64decode(encoded))
    actual = hashlib.sha256(data).hexdigest()
    if len(data) != manifest["target_bytes"] or actual != manifest["target_sha256"]:
        raise SystemExit(f"primary source identity mismatch: {len(data)} {actual}")
    TARGET.write_bytes(data)
    print(f"assembled {TARGET} ({len(data)} bytes, sha256={actual})")
    return 0
if __name__ == "__main__":
    raise SystemExit(main())
