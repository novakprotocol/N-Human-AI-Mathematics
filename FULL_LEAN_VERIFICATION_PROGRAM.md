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

# Full-Portfolio Lean Verification Program

The full-portfolio Lean program remains a gold-standard improvement program for
HINC-001, ABF-001, and any future public theorem package. It is not a
retroactive withdrawal rule for the already released HINC-001 and ABF-001
candidate-review packages.

## Current Public/Private States

```text
HINC-001  active public candidate technical review
          formal status: PARTIAL_PASS / bounded Lean verification
          full manuscript Lean verified: no

ABF-001   active public candidate technical review
          formal status: PARTIAL_PASS / bounded A01 Lean verification
          full manuscript Lean verified: no

FSG-001   private candidate
          public state: HOLD -- MATHEMATICAL BLOCKER
          mathematical state: C06 / main theorem item (v) false as written
          no public theorem package released
          public theorem package released: no
          public release authorized: no

ACM-001   hold pending consolidation
```

## FULL_PASS Gate

A paper reaches `FULL_PASS` only when every retained theorem, lemma, equation,
structural equivalence, exact finite classification, boundary case, and imported
mathematical dependency used by the controlling manuscript maps to compiled Lean
declarations or exact documented imported theorems, with zero unresolved formal
scope.

Required gates include:

1. frozen source identity;
2. complete claim inventory;
3. complete claim-to-Lean map;
4. zero placeholders or project-result axioms;
5. literal manuscript-object fidelity;
6. exact finite-universe certification where finite classification is claimed;
7. clean immutable build;
8. axiom and trusted-code audit;
9. independent manuscript-to-formal-statement fidelity review;
10. machine receipt with `FULL_PASS`.

Any missing condition leaves the result at `PARTIAL_PASS`, `HOLD`, `BLOCKED`, or
`FAIL`. No rounding up is allowed.

## Allowed and Forbidden Wording

For HINC-001 and ABF-001, public wording may say:

- active public candidate technical review;
- `PARTIAL_PASS`;
- bounded Lean verification, with the exact bounded scope;
- full manuscript not fully formalized;
- external review pending;
- historical priority unestablished.

For non-`FULL_PASS` manuscripts, public wording must not say:

- fully Lean verified;
- fully formalized;
- every claim is machine checked;
- peer reviewed;
- externally reproduced;
- historically first;
- journal accepted.

For FSG-001, public wording must say private candidate and mathematical blocker.
It must not publish private source paths, branch names, private PR links, the
corrected formula, or any statement implying that the private correction has
passed review.