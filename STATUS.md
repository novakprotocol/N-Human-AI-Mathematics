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

# Repository Status

## Owner Clarification -- 29 July 2026

```text
repository_name:                 N-Human-AI-Mathematics
public_title:                    N Human-LLM Mathematics
repository_role:                 public candidate-review and reproduction layer
repository:                      novakprotocol/N-Human-AI-Mathematics
visibility:                      public
status_effective_date:           2026-07-29
active_public_candidate_review:  HINC-001, ABF-001
fully_lean_verified_manuscripts: none
private_candidate_hold:          FSG-001 -- mathematical blocker
consolidation_hold:              ACM-001
blanket_license_applied:         false
peer_reviewed:                   false
journal_submitted:               false
DOI_assigned:                    false
historical_priority:             unestablished
specific_model_disclosed:        false
specific_provider_disclosed:     false
```

PR #57 is preserved in history, but its interpretation that HINC-001 and
ABF-001 became inactive historical artifacts is superseded by the owner
clarification recorded here.

## Current Paper States

1. `HINC-001` -- **ACTIVE PUBLIC CANDIDATE TECHNICAL REVIEW**. Formal status:
   `PARTIAL_PASS` / bounded Lean verification. The full manuscript is not fully
   formalized. External review is pending. Historical priority is unestablished.
2. `ABF-001` -- **ACTIVE PUBLIC CANDIDATE TECHNICAL REVIEW**. Formal status:
   `PARTIAL_PASS` / bounded A01 Lean verification. The full manuscript is not
   fully formalized. External review is pending. Historical priority is
   unestablished.
3. `FSG-001` -- **PRIVATE CANDIDATE; HOLD -- MATHEMATICAL BLOCKER**. A
   universal arithmetic criterion in the private candidate manuscript has a
   confirmed counterexample: C06 / main theorem item (v) is false as written.
   The private correction is under internal review. No public FSG theorem
   package has been released, and no public FSG release is authorized.
4. `ACM-001` -- **HOLD PENDING CONSOLIDATION**.

## Full-Lean Boundary

Full-manuscript Lean verification remains the gold-standard improvement
program. It is required before any manuscript may be described as `FULL_PASS`,
fully Lean verified, or fully formalized.

That gold-standard program does not retroactively withdraw the already public
HINC-001 and ABF-001 candidate-review packages. Those packages may remain active
for public technical review only with their exact bounded formal status and
limitations stated next to the review status.

Lean does not establish novelty, significance, external correctness, peer
review, journal acceptance, or historical priority. Those remain separate gates.
