# Repository status

## Full-Lean requalification hold

```text
repository_name:             N-Human-AI-Mathematics
public_title:                N Human-LLM Mathematics
repository_role:             curated candidate-review and reproduction layer
repository:                  novakprotocol/N-Human-AI-Mathematics
visibility:                  public
status_effective_date:       2026-07-29
active_theorem_packages:     none
public_archives_on_hold:     HINC-001, ABF-001
private_completion_hold:     FSG-001
blocked_next_package:        ACM-001
full_Lean_required:          true
blanket_license_applied:     false
peer_reviewed:               false
journal_submitted:           false
DOI_assigned:                false
historical_priority:         unestablished
specific_model_disclosed:    false
specific_provider_disclosed: false
```

The owner now requires every retained mathematical claim in a theorem package to map to compiled Lean before that package is classified as active. See `FULL_LEAN_RELEASE_STANDARD.md` and `PUBLIC_REVIEW_FORMALIZATION_HOLD_2026-07-29.md`.

## Papers 1–3

1. `HINC-001` — public historical artifact; `PARTIAL_PASS`; full-Lean requalification hold.
2. `ABF-001` — public historical artifact; `PARTIAL_PASS`; full-Lean requalification hold.
3. `FSG-001` — private; exact-head Fibonacci/graph bootstrap PASS; full F01–F07 completion hold.
4. `ACM-001` — blocked until papers 1–3 reach the same complete professional state.

## Formal boundary

HINC-001 and ABF-001 have genuine bounded Lean results. FSG-001 has a genuine exact-head bootstrap build. None currently has a complete manuscript claim-to-declaration map with zero unresolved formal claims. Therefore none is currently an active theorem package under the owner-selected standard.

## Release condition

A paper may return to active public technical review only when its exact frozen source has:

- every retained mathematical claim inventoried and mapped to compiled declarations or exact imported theorems;
- zero unresolved claims, `sorry`, `admit`, project-result axioms, or `sorryAx`;
- literal-source fidelity and complete boundary-case coverage;
- a clean immutable build with logs, manifests, axiom reports, and hashes;
- an independent manuscript-to-Lean fidelity review;
- exact owner authorization for the final source, package, tag, release, and site wording.

Lean does not establish novelty, significance, external correctness, peer review, journal acceptance, or historical priority. Those remain separate gates.
