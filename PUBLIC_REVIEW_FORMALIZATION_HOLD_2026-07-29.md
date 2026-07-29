<!--
NHAIM_STATUS_BLOCK_V1
HINC-001:
  public_state: active_review
  formal_state: PARTIAL_PASS
  full_manuscript_lean_verified: false
  external_review: pending
  historical_priority: not_established
  peer_review: not_submitted
  release_authorized: true
ABF-001:
  public_state: active_review
  formal_state: PARTIAL_PASS
  compiled_lane: A01
  a02_a06_status: incomplete
  full_manuscript_lean_verified: false
  external_review: pending
  historical_priority: not_established
  peer_review: not_submitted
  release_authorized: true
FSG-001:
  public_state: hold
  private_candidate: true
  mathematical_blocker: true
  public_theorem_package_released: false
  release_authorized: false
ACM-001:
  public_state: hold
  controlling_manuscript_complete: false
  release_authorized: false
END_NHAIM_STATUS_BLOCK_V1
-->

# Public Formalization Hold Record -- 29 July 2026

This file is preserved as the PR #57 full-Lean policy record. Its status
interpretation has been superseded by the 29 July 2026 owner clarification:
HINC-001 and ABF-001 are not inactive or withdrawn. They remain active public
candidate technical-review packages with exact bounded formal-verification
statements.

The full-manuscript Lean program remains active as a gold-standard improvement
program:

- `FULL_PASS` requires complete retained manuscript claim-to-Lean coverage;
- bounded Lean PASS must not be described as full-manuscript verification;
- manuscript-to-formal-statement fidelity remains a separate required gate;
- Lean does not establish peer review, historical priority, journal acceptance,
  external reproduction, novelty, significance, or prose correctness.

## Corrected Current State

```text
HINC-001  active public candidate technical review
          PARTIAL_PASS / bounded Lean verification
          full manuscript not fully formalized
          external review pending
          historical priority unestablished

ABF-001   active public candidate technical review
          PARTIAL_PASS / bounded A01 Lean verification
          full manuscript not fully formalized
          external review pending
          historical priority unestablished

FSG-001   private candidate
          HOLD -- MATHEMATICAL BLOCKER
          C06 / main theorem item (v) false as written
          private correction under internal review
          no public theorem package released
          no public release authorized

ACM-001   hold pending consolidation
```

## Supersession Boundary

PR #57 is not deleted or rewritten. The public interpretation that HINC-001 and
ABF-001 are historical artifacts on inactive full-Lean requalification hold is
superseded. The prohibition on claiming complete Lean verification is preserved.