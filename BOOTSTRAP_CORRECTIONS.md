# Bootstrap correction ledger

This ledger preserves bootstrap failures separately from successful evidence. A failed attempt is not rewritten as a pass, and an operational correction is not represented as mathematical review.

## BSTR-CORR-001 — wrong repository and unavailable shell

**Observed:** the initializer was invoked from `N-LMS`, and the machine did not provide `pwsh`.

**Effect:** execution stopped before the publication export was located.

**Correction:** the guarded bootstrap now resolves `N-MathLab`, verifies its `origin`, and invokes Windows PowerShell 5.1 through `powershell.exe`.

**Status:** resolved in the bootstrap branch.

## BSTR-CORR-002 — expected GitHub probe promoted to a terminating error

**Observed:** `gh repo view novakprotocol/N-Human-AI-Mathematics` correctly returned not found, but Windows PowerShell 5.1 promoted the diagnostic stream to `NativeCommandError` while the global error preference was `Stop`.

**Effect:** execution stopped before repository creation.

**Correction:** native commands are now evaluated by their exit status under a locally controlled error preference; expected negative probes are captured, while unexpected nonzero exits remain fatal.

**Correcting commit:** `1d922ef9ad025967009df3b3048e9b3a4cb07d11`

**Status:** resolved.

## BSTR-CORR-003 — validator matched its own embedded MIT-license signature

**Observed:** the full local materialization reached the publication validator after pinned N-MathLab and Lean sources were copied. The validator reported:

```text
ERROR: tools/validate_publication.py:101: forbidden blanket MIT license text
```

The repository did not contain a blanket MIT license. The checker had scanned the literal detection signature embedded in its own source.

**Effect:** validation failed closed; no standalone GitHub repository was created.

**Correction:** the validator now:

- excludes only `tools/validate_publication.py` from content-signature scanning;
- records that exact exclusion in the machine-readable validation inventory;
- constructs the MIT detection signature from source fragments;
- continues scanning every manuscript, evidence file, formal source, workflow, status record, rights file, and other tool;
- rejects unsafe source-manifest target traversal in addition to the prior checks.

The replacement validator was compiled and exercised against three local controls before commit:

1. a complete synthetic publication tree passed;
2. the actual MIT grant sentence in another file failed;
3. an unsafe `../` manifest target failed.

**Correcting commit:** `87b57d54ed72a39c9607c2189dd0b45752924239`

**Status:** source corrected; complete real bootstrap rerun pending.

## Hosted runner status

GitHub-hosted attempts have ended before usable step lists, logs, or artifacts were exposed. They remain classified as **hosted initialization failures with cause unclassified**. They are not evidence that the bootstrap source passed or failed.

## Current merge and release boundary

- PR: `novakprotocol/N-MathLab#417`
- branch: `agent/n-human-ai-mathematics-publication-bootstrap-v1`
- standalone repository created: **no**
- public release authorized: **no**
- blanket repository license applied: **no**
- external mathematical review supplied by this correction process: **no**

The controlling next gate is one complete guarded Windows bootstrap producing both `BOOTSTRAP_RECEIPT.json` and `reports/publication-validation.json` with `PASS`, followed by verification that the new repository is private and its default branch is `main`.
