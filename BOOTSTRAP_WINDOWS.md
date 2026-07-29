# Windows Bootstrap Note

This file is retained as historical bootstrap documentation for the original public repository setup.
It is not an executable public release instruction.

## Current Boundary

The repository `novakprotocol/N-Human-AI-Mathematics` is already public. Current status is governed by `STATUS.md`, `research-index.json`, and the publication/status validators in `tools/`.

Private lab repository locations, local filesystem paths, private branch names, private manuscript paths, and private review links are intentionally omitted from this public note.

## Current Public State

```text
HINC-001  active public candidate technical review; PARTIAL_PASS / bounded Lean verification
ABF-001   active public candidate technical review; PARTIAL_PASS / bounded A01 Lean verification
FSG-001   private candidate; HOLD -- MATHEMATICAL BLOCKER; no public theorem package released
ACM-001   hold pending consolidation
```

This note does not authorize a visibility change, GitHub Pages change, release, tag, theorem-source change, FSG release, or publication action.

## Validation

Use the repository validators instead of the historical bootstrap command sequence:

```powershell
python tools/validate_public_state.py --root .
python tools/validate_status_consistency.py --root .
python tools/validate_learning_page.py .
python tools/validate_publication.py --root . --allow-public
python tools/validate_publication_v2.py --root . --allow-public
python tools/validate_publication_gate.py --root .
python tools/validate_public_release.py --root .
python tools/validate_public_release_v2.py --root .
```