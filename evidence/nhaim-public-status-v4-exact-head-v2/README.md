# NHAIM Public Status V4 Exact-Head Evidence Package V2

This directory is the V2 evidence-package repair for PR #60. It is an evidence-package integrity repair only.

- V1 evidence is preserved byte-for-byte in `evidence/nhaim-public-status-v4-exact-head-v1/`.
- V1 package-integrity audit failed with `EXACT_HEAD_EVIDENCE_INVALID`.
- V2 replaces V1 for evidence-package integrity.
- The immutable execution target remains unchanged.

Execution target head:
dda1d03bc54f52261e27b60642a314748b94a8d6

PR branch:
fix/restore-hinc-abf-active-fsg-math-hold-v1

Parent evidence commit:
aeffea46500d813629193b8ade7033b1fbc30e2a

Historical V1 receipt SHA-256 preserved:
c92df77215ca7cc166cfb3cc4f2957701946310f8407c25184a3b5ab19cc2ef5

## Verdict

- Source PR #60 remained open, draft, mergeable, unmerged, and exact-head pinned during the identity gate.
- Detached worktree execution target: `dda1d03bc54f52261e27b60642a314748b94a8d6`.
- Detached HEAD proof: `git symbolic-ref -q HEAD` exited nonzero; `git branch --show-current` was empty; `git rev-parse --abbrev-ref HEAD` returned `HEAD`.
- Local exact-head suite: PASS.
- HINC boundary: bounded Lean only, PASS.
- ABF boundary: bounded A01 Lean only, PASS.
- FSG boundary: private hold.
- ACM boundary: hold.
- Hosted workflows: five required runs, six jobs, all exact-head PASS.
- Checkout snippets are embedded in `hosted-workflow-ledger-v2.json`; there is no separate checkout-snippet file reference.
- Manifest verification: all entries checked, mismatches 0.
- Control-character scan: unexpected findings 0.
- Theorem source changed: false.
- Formal source changed: false.
- Repository visibility changed: false.
- Pages disabled: false.
- Merge performed: false.
- Release action: false.

## Files

- `exact-head-author-receipt-v2.json` - deterministic V4.1 receipt.
- `local-complete-execution-v2.log` - complete local command log with stdout, stderr, and exit codes.
- `hosted-workflow-ledger-v2.json` - hosted workflow/job/artifact ledger with embedded checkout snippets.
- `command-ledger-v2.txt` - concise command ledger.
- `worktree-creation-and-cleanup-v2.log` - worktree creation, detached-state, cleanup, and absence proof.
- `SHA256SUMS.txt` - SHA-256 manifest generated from final file bytes.
