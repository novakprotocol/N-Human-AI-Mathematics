# Repository Status

## Current lifecycle state

```text
repository_name:             N-Human-AI-Mathematics
repository_role:             curated public-review and external-review layer
repository:                  novakprotocol/N-Human-AI-Mathematics
release_channel:             public review
release_version:             0.1.0-public-review
release_date:                2026-07-27
default_branch:              main
standalone_repository:       created
initial_curated_commit:      e378c773f7c54b375fdd208961f77702b1aadd05
bootstrap_source_commit:     9dc69542fb2b089a4cef5ea3c425d82bb705d4dd
bootstrap_result:            PASS
publication_validation:      PASS
public_release_authorized:   true
blanket_license_applied:     false
peer_reviewed:               false
journal_submitted:           false
historical_priority:         unestablished
openai_endorsement:          not claimed
```

The GitHub repository may remain private until the release branch is merged and the owner performs the final visibility change. The status above describes the authorized release state being frozen by `release/public-review-v1`.

## What is complete

- The standalone GitHub repository exists and `main` is the default branch.
- The initial curated repository was created from pinned N-MathLab and `novak-sdt` commits.
- `BOOTSTRAP_RECEIPT.json` records `PASS`.
- The initial publication validation recorded zero errors and zero warnings.
- Repository purpose and separation from the private laboratory are fixed.
- Human-readable and AI-readable evidence rules are defined.
- Machine-readable research-index and paper-status schemas are included.
- Counterexample, proof-gap, prior-art, and reproduction workflows are defined.
- A dependency-free publication validator and GitHub validation workflow are included.
- The human–AI collaboration record and prior-art boundary are public-review source files.
- The public-source audit found no indexed personal Windows path, known GitHub token pattern, private-key header, blanket MIT grant sentence, or private chat transcript.
- The HINC bibliography metadata was checked against primary publication or preprint records and corrected where needed.
- The first complete paper package is fixed as `HINC-001`.
- The HINC standalone manuscript, review packet, verifier, tests, and receipts were materialized from immutable N-MathLab commit `e6adac212150177d4afa56e643d37533a208693c`.
- The HINC formal sources were materialized from immutable `novak-sdt` commit `d7751d1de76253407016ef4bf92738cffa800e82`.
- The HINC algebraic kernel has a public hosted Lean PASS.
- The principal even and odd coefficient classifications and normalized monoid laws have a second public hosted Lean PASS.
- Failed bootstrap and formal-proof attempts, their causes, and their repairs remain preserved separately from successful evidence.
- Matthew S. Novak authorized public-review release on 27 July 2026.

## Public-review release record

```text
release declaration:          PUBLIC_REVIEW_RELEASE.md
human-AI record:              HUMAN_AI_COLLABORATION_RECORD.md
human-AI prior art:           HUMAN_AI_MATHEMATICS_PRIOR_ART.md
open challenge:               OPEN_REVIEW_CHALLENGE.md
machine-readable audit:       reports/public-release-audit-2026-07-27.json
complete released package:    HINC-001
indexed hold packages:        ABF-001, FSG-001, ACM-001
DOI:                          none
journal venue:                none
```

Public review is not peer review. It opens the source and evidence to challenge while preserving unresolved scientific gates.

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

## What remains after public release

### HINC-001 scientific review

1. Obtain qualified outside algebra/monoid review.
2. Complete a focused source-level historical-equivalence review.
3. Resolve any counterexample, proof-gap, prior-art, or reproduction reports.
4. Decide whether to formalize generator-to-global Gerstenhaber preservation before journal submission.
5. Freeze a separate reviewed archival or journal-submission identity.
6. Record DOI, venue, peer review, or acceptance only after those events occur.

### Additional paper packages

1. Convert `ABF-001` into the complete public package format.
2. Convert `FSG-001` into the complete public package format.
3. Consolidate the ANF code/matroid line into `ACM-001` and create its public package.

These tasks may proceed in parallel with new research in N-MathLab.

## Current paper states

| Paper | Statement/proof | Internal reproduction | Formal proof | External review | Public state |
|---|---|---|---|---|---|
| `HINC-001` | Complete candidate manuscript | Passed for declared finite/symbolic routes | Base kernel PASS; principal coefficient classifications PASS; full manuscript incomplete | Pending | Public review package |
| `ABF-001` | Exact finite theorem complete | Python/C/small-universe controls passed | Pending | Pending | Indexed hold; package not released |
| `FSG-001` | Candidate all-parameter theorem package | Multiple internal routes passed | Pending | Pending | Indexed hold; package not released |
| `ACM-001` | Exact finite code/matroid classification | Multiple routes passed for merged scope | Pending | Pending | Indexed hold; consolidation pending |

## Claim boundary

The repository establishes a controlled, inspectable public-review architecture and evidence of a sustained human-led, ChatGPT-assisted research process. It does not establish mathematical correctness, worldwide novelty, publication priority, peer-review acceptance, importance, OpenAI endorsement, or full formal verification of any manuscript.
