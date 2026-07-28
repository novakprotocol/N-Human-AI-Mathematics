# Private website preview — blocker resolution ledger

This file preserves the hostile-review website blockers and records their disposition. The current controlling readiness record is:

- [`../PUBLIC_SWITCH_READINESS.md`](../PUBLIC_SWITCH_READINESS.md)

## Resolved before the final switch

1. **Public-release language above the fold** — replaced with private public-switch preview language.
2. **Search indexing during private review** — `noindex,nofollow,noarchive,nosnippet` retained.
3. **Draft links** — branch-pinned to `release/public-review-v1`.
4. **Mobile navigation** — available without JavaScript.
5. **Substantive content without JavaScript** — all mathematical and status content is static HTML.
6. **Status visualization** — explicitly labeled as status, not evidence.
7. **Evidence separation** — human proof, internal computation, bounded Lean verification, external review, and historical priority are displayed separately.
8. **Falsification and downgrade routes** — counterexample, proof-gap, prior-art, and reproduction channels are specified.
9. **Human + LLM boundary** — category-level disclosure is explicit and is not mathematical evidence or independent attestation.
10. **Release state** — repository remains private; public switch readiness is machine-readable and fail-closed.
11. **Repository-name/public-title mismatch** — the repository slug is treated as a legacy technical identifier; the public title is `N Human–LLM Mathematics`.
12. **Controlling manuscript** — the site links to `HINC-001_REVISED_MANUSCRIPT.md`, not the superseded four-part source.
13. **Citation warning** — the site states that HINC-001 is not established or peer reviewed.
14. **Pages deployment** — a separate post-switch workflow requires public visibility, exact owner confirmation, public-state validation, and HINC tests before deployment.

## Remaining post-launch scientific work

The following remain pending by design and are objectives of public technical review:

- external algebraic-monoid and Gerstenhaber review;
- independent reproduction;
- historical-equivalence review;
- optional independent formalization of the unformalized manuscript nodes;
- journal submission and peer review, if pursued later.

These do not prevent an honest public **candidate technical-review** release because they are displayed as pending and are not claimed as completed.

## Current release boundary

```text
repository visibility:       private
candidate package:           complete
public switch ready:         true
PR merge:                    pending final green checks
Pages deployment:            staged but not executed
public release:              not yet activated
peer reviewed:               no
historical priority:         unestablished
```
