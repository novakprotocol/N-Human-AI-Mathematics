# Repository status

## Current lifecycle state

```text
repository_name:             N-Human-AI-Mathematics
public_title:                N Human–LLM Mathematics
repository_role:             curated candidate-review and reproduction layer
repository:                  novakprotocol/N-Human-AI-Mathematics
visibility:                  private
release_channel:             private staging
candidate_version:           0.1.0-public-review-candidate
default_branch:              main
release_branch:              release/public-review-v1
public_release_authorized:   false
public_switch_ready:         true
visibility_switch_executed:  false
Pages_deployment_executed:   false
blanket_license_applied:     false
peer_reviewed:               false
journal_submitted:           false
historical_priority:         unestablished
specific_model_disclosed:    false
specific_provider_disclosed: false
```

The package is prepared so that the remaining release operation is an owner-controlled switch: merge the validated release branch into private `main`, validate `main`, change visibility, activate Pages, and verify the live release.

## What is complete

- The standalone private repository exists with `main` as the default branch.
- The guarded bootstrap and initial publication validation passed.
- Human-readable and machine-readable evidence rules are defined.
- Counterexample, proof-gap, prior-art, and reproduction channels are defined.
- No blanket MIT license is applied.
- The public wording is category-level **Human-led, LLM-assisted**; no specific model or provider is disclosed.
- The 2026-07-27 hostile review found no explicit counterexample to the controlling coefficient systems.
- HINC-001 now has one controlling consolidated manuscript:

```text
papers/HINC-001/manuscript/HINC-001_REVISED_MANUSCRIPT.md
```

- The consolidated manuscript integrates:
  - the characteristic-two normalized Hochschild derivation;
  - complete even and odd source presentations;
  - the odd normal-form theorem;
  - generator-to-global binary-bracket preservation;
  - explicit natural representability;
  - corrected cross-references and terminology;
  - the center subfunctor and pointwise-center distinction;
  - disconnected-base clopen language;
  - the fppf-derived-subgroup argument;
  - idempotent, geometric, finite-field, and finite-Artin results;
  - current computational, formal, and historical-priority boundaries.
- The HINC algebraic kernel has a public hosted Lean PASS.
- The principal even and odd coefficient classifications and normalized monoid laws have a second public hosted Lean PASS.
- Failed bootstrap, formal-proof, test-harness, and publication attempts remain preserved separately from successful evidence.
- The publication order remains HINC-001, ABF-001, FSG-001, ACM-001.

## Formal verification checkpoint

```text
base run:                     30119931881
base artifact SHA-256:        63b2b160da40f722818820679da7c9d22eb7640694e48a5abc08fccf78f47133
classification run:           30174213006
classification job:           89720259114
classification artifact:      8623775718
classification SHA-256:       56267aba47fd67e94be5842057aaec5bd0718829e860af212eedcdb43efbb084
classification artifact hash: 2dee88b9a248dee8719c27aa23a27ca3281e697cf67202bb50c1fe60a4809dc9
sorryAx:                      absent
```

These receipts cover the listed algebraic kernel and coefficient-classification declarations only. The full revised manuscript is not formally verified and is not described as such.

## Current paper states

| Paper | Mathematical state | External review | First-launch state |
|---|---|---|---|
| `HINC-001` | Self-contained revised candidate classification; internal evidence and bounded Lean scopes passed | Pending and requested | Complete candidate technical-review package |
| `ABF-001` | Exact finite theorem package preserved | Pending | Index entry only; next package |
| `FSG-001` | Candidate all-parameter theorem package preserved | Pending | Hold |
| `ACM-001` | Exact finite code/matroid line preserved | Pending | Hold pending consolidation |

## Why external review remains pending

Public technical review is intended to obtain:

1. outside algebraic-monoid and Gerstenhaber review;
2. independent reproduction;
3. source-level historical-equivalence analysis;
4. optional independent formalization of unformalized proof nodes.

Those are not blockers to honestly releasing a **candidate technical-review package**, provided they remain visibly pending. They remain blockers to claiming external validation, peer review, journal acceptance, or historical priority.

## Final switch gates

Before the repository becomes public, all of the following must pass in one controlled sequence:

1. release-branch CI;
2. repository privacy, rights, citation, and withheld-identity scans;
3. HINC standalone tests;
4. website static and accessibility checks;
5. branch merge into private `main`;
6. fresh validation of private `main`;
7. public visibility change and metadata re-read;
8. GitHub Pages activation and live-site verification;
9. public-review tag, release, and checksum receipt;
10. structured review-channel creation.

See [`PUBLIC_SWITCH_READINESS.md`](PUBLIC_SWITCH_READINESS.md).

## Claim boundary

The repository establishes a controlled candidate-review architecture and strong internal evidence for HINC-001. It does not establish complete formal verification, outside correctness review, outside reproduction, worldwide novelty, publication priority, peer-review acceptance, journal submission, DOI assignment, security impact, or a specific model/provider identity.
