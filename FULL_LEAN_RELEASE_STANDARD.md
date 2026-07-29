<!--
NHAIM_STATUS_BLOCK_V1
HINC-001:
  paper_id: HINC-001
  public_state: active_review
  formal_state: PARTIAL_PASS
  bounded_formal_scope: bounded_Lean
  claim_map_complete: false
  full_manuscript_lean_verified: false
  external_specialist_review: pending
  historical_priority: not_established
  peer_review: not_submitted
  journal_status: not_submitted
  public_release_authorized: true
ABF-001:
  paper_id: ABF-001
  public_state: active_review
  formal_state: PARTIAL_PASS
  bounded_formal_scope: bounded_A01_Lean
  compiled_lane: A01
  a02_a06_status: incomplete
  claim_map_complete: false
  full_manuscript_lean_verified: false
  external_specialist_review: pending
  historical_priority: not_established
  peer_review: not_submitted
  journal_status: not_submitted
  public_release_authorized: true
FSG-001:
  paper_id: FSG-001
  public_state: hold
  private_candidate: true
  mathematical_blocker: true
  public_theorem_released: false
  correction_status: private_correction_under_internal_review
  external_review: not_started
  formal_status: HOLD_MATHEMATICAL_BLOCKER
  public_release_authorized: false
ACM-001:
  paper_id: ACM-001
  public_state: hold
  manuscript_complete: false
  claim_map_complete: false
  full_manuscript_lean_verified: false
  public_theorem_released: false
  public_release_authorized: false
END_NHAIM_STATUS_BLOCK_V1
-->

# Full-Lean Release Standard

Full-manuscript Lean verification is the repository's gold-standard improvement
program. It controls when a manuscript may be described as `FULL_PASS`, fully
Lean verified, or fully formalized.

It does **not** retroactively withdraw or deactivate already public
candidate-review packages that clearly state bounded formal-verification results
and open formal scope.

## FULL_PASS Requirement

A manuscript may be marked `FULL_PASS` only when one exact frozen source has:

1. every retained theorem, lemma, equation, exact count, classification, and
   boundary case inventoried with stable claim IDs;
2. every retained claim mapped to compiled Lean declarations or exact imported
   theorems whose hypotheses are explicitly discharged;
3. zero unresolved formal claims;
4. zero `sorry`, `admit`, project-result axioms, or `sorryAx`;
5. finite classifications connected to kernel-checked certificates or
   exhaustive decidable proofs over the exact declared universe;
6. literal-object fidelity between manuscript definitions and formal objects;
7. a pinned Lean, Lake, and Mathlib environment that builds from a clean
   immutable source checkout;
8. retained logs, manifests, source hashes, dependency records, and axiom
   reports;
9. independent manuscript-to-formal-statement fidelity review.

Any missing condition leaves the manuscript below `FULL_PASS`.

## Existing Public Candidate-Review Packages

HINC-001 and ABF-001 may remain active public candidate technical-review
packages with exact bounded statements:

```text
HINC-001  PARTIAL_PASS / bounded Lean verification
ABF-001   PARTIAL_PASS / bounded A01 Lean verification
```

Those statements do not claim that either full manuscript is fully formalized,
peer reviewed, externally reproduced, historically first, or journal accepted.

## FSG and Future Releases

FSG-001 is on HOLD -- MATHEMATICAL BLOCKER and is blocked independently by a confirmed mathematical counterexample in
the private candidate manuscript. No public FSG theorem package has been
released, and no public FSG release is authorized.

ACM-001 remains on hold pending consolidation.

Future packages require exact owner authorization and must pass their applicable
mathematical, review, provenance, rights, packaging, and release gates. If they
claim full-manuscript Lean verification, they must satisfy `FULL_PASS`.

## What Lean Cannot Establish

Lean does not establish historical priority, peer review, journal acceptance,
significance, external reproduction, accessibility, website behavior, or prose
quality. Those remain separate review and engineering gates.
