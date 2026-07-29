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