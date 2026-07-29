# Bootstrap correction ledger

This ledger preserves bootstrap failures separately from successful evidence. A failed attempt is not rewritten as a pass, and an operational correction is not represented as mathematical review.

## BSTR-CORR-001 â€” wrong repository and unavailable shell

**Observed:** the initializer was invoked from a nonpublic local source directory, and the machine did not provide `pwsh`.

**Effect:** execution stopped before the publication export was located.

**Correction:** the guarded bootstrap now resolves `private research source`, verifies its `origin`, and invokes Windows PowerShell 5.1 through `powershell.exe`.

**Status:** resolved.

## BSTR-CORR-002 â€” expected GitHub probe promoted to a terminating error

**Observed:** `gh repo view novakprotocol/N-Human-AI-Mathematics` correctly returned not found, but Windows PowerShell 5.1 promoted the diagnostic stream to `NativeCommandError` while the global error preference was `Stop`.

**Effect:** execution stopped before repository creation.

**Correction:** native commands are now evaluated by their exit status under a locally controlled error preference; expected negative probes are captured, while unexpected nonzero exits remain fatal.

**Correcting commit:** private correction identity redacted; provenance retained outside the public repository.

**Status:** resolved.

## BSTR-CORR-003 â€” validator matched its own embedded MIT-license signature

**Observed:** the full local materialization reached the publication validator after pinned private research source and Lean sources were copied. The validator reported:

```text
ERROR: tools/validate_publication.py:101: forbidden blanket MIT license text
```

The repository did not contain a blanket MIT license. The checker had scanned the literal detection signature embedded in its own source.

**Effect:** validation failed closed; no standalone GitHub repository was created during that attempt.

**Correction:** the validator now:

- excludes only `tools/validate_publication.py` from content-signature scanning;
- records that exact exclusion in the machine-readable validation inventory;
- constructs the MIT detection signature from source fragments;
- continues scanning every manuscript, evidence file, formal source, workflow, status record, rights file, and other tool;
- rejects unsafe source-manifest target traversal in addition to the prior checks.

The replacement validator was compiled and exercised against three controls before commit:

1. a complete synthetic publication tree passed;
2. the actual MIT grant sentence in another file failed;
3. an unsafe `../` manifest target failed.

**Correcting commit:** private correction identity redacted; provenance retained outside the public repository.

**Status:** resolved by the successful complete rerun below.

## Successful guarded bootstrap

A complete Windows PowerShell 5.1 rerun used a private bootstrap source whose exact identity is redacted from the public repository.

The run:

- authenticated the `novakprotocol` GitHub account;
- fetched the current private research source bootstrap source with its exact identity withheld from public source;
- created a detached worktree;
- materialized the manuscript and verifier sources from a private research source with the private commit withheld;
- materialized the Lean sources from `novak-sdt` commit `d7751d1de76253407016ef4bf92738cffa800e82`;
- completed publication validation with zero errors and zero warnings;
- created `novakprotocol/N-Human-AI-Mathematics` as a private repository;
- pushed default branch `main`;
- verified the final repository identity, visibility, and default branch;
- removed the dedicated bootstrap worktree after success.

Exact result:

```text
bootstrap receipt:           PASS
publication validation:      PASS
validation errors:           0
validation warnings:         0
standalone initial commit:   e378c773f7c54b375fdd208961f77702b1aadd05
repository visibility:       PRIVATE
default branch:              main
public release authorized:   no
blanket repository license:  no
created UTC:                 2026-07-26T00:04:30.6333559Z
```

The controlling evidence is preserved in:

- `BOOTSTRAP_RECEIPT.json`;
- `reports/publication-validation.json`.

## Hosted runner status

Earlier GitHub-hosted bootstrap attempts ended before usable step lists, logs, or artifacts were exposed. They remain classified as **hosted initialization failures with cause unclassified**. They are not rewritten as source passes or source failures.

The successful guarded local run above is the controlling bootstrap acceptance record. It is operational evidence, not independent mathematical review.

## Current merge and release boundary

- private source bootstrap reference: identifier withheld
- standalone repository created: **yes**
- standalone visibility: **private**
- standalone default branch: **main**
- bootstrap and validation receipts: **PASS**
- public release authorized: **no**
- blanket repository license applied: **no**
- external mathematical review supplied by this correction process: **no**

The bootstrap line is operationally complete. Public visibility, journal submission, novelty promotion, and peer-review status remain separate governed decisions.
