# Repository Status

## Current lifecycle state

```text
repository_name: N-Human-AI-Mathematics
repository_role: curated publication and external-review layer
staging_location: novakprotocol/N-MathLab
intended_public_location: novakprotocol/N-Human-AI-Mathematics
current_visibility: not yet created as a standalone repository
public_release_authorized: false
```

## What is complete

- Repository name, purpose, and separation from the private laboratory are fixed.
- Human-readable and AI-readable evidence rules are defined.
- Strict machine-readable research-index and paper-status schemas are included.
- Structured counterexample, proof-gap, prior-art, and reproduction workflows are defined.
- A dependency-free publication validator and GitHub validation workflow are included.
- A one-click PowerShell materialization script creates the clean private repository from exact source commits.
- The first paper identifier is fixed as `HINC-001`.
- The HINC standalone manuscript, review packet, verifier, tests, and receipt sources are mapped at immutable N-MathLab commit `e6adac212150177d4afa56e643d37533a208693c`.
- The existing HINC algebraic kernel has a public hosted Lean PASS.
- The principal even and odd coefficient classifications and normalized monoid laws have a second public hosted Lean PASS.
- The first failed principal-classification run, repair, rerun, source hashes, axiom report, and artifact identities are preserved.

## Formal verification checkpoint

```text
base run:                    30119931881
base artifact SHA-256:       63b2b160da40f722818820679da7c9d22eb7640694e48a5abc08fccf78f47133
classification run:          30174213006
classification job:          89720259114
classification artifact:     8623775718
classification SHA-256:      56267aba47fd67e94be5842057aaec5bd0718829e860af212eedcdb43efbb084
classification artifact hash:2dee88b9a248dee8719c27aa23a27ca3281e697cf67202bb50c1fe60a4809dc9
sorryAx:                     absent
```

## What remains before the standalone repository can be public

1. Create `novakprotocol/N-Human-AI-Mathematics` as a **private** repository.
2. Run `tools/Initialize-N-Human-AI-Mathematics.ps1` to import the clean bootstrap and materialize `HINC-001` from exact sources.
3. Run repository validation and inspect the generated receipt.
4. Review all materialized manuscript references and third-party notices.
5. Obtain at least one qualified outside algebra/monoid review.
6. Complete a focused historical-equivalence review.
7. Decide whether to formalize the generator-to-global Gerstenhaber-preservation theorem before submission.
8. Obtain explicit owner authorization before changing visibility to public.

## Current paper states

| Paper | Statement/proof | Internal reproduction | Formal proof | External review | Public state |
|---|---|---|---|---|---|
| `HINC-001` | Complete candidate manuscript | Passed for declared finite/symbolic routes | Base kernel PASS; principal coefficient classifications PASS; full manuscript incomplete | Pending | Private staging |
| `ABF-001` | Exact finite theorem complete | Python/C/small-universe controls passed | Pending | Pending | Hold |
| `FSG-001` | Candidate all-parameter theorem package | Multiple internal routes passed | Pending | Pending | Hold |
| `ACM-001` | Exact finite code/matroid classification | Multiple internal routes passed | Pending | Pending | Hold |

## Claim boundary

The existence of this bootstrap does not establish correctness, novelty, publication priority, peer-review acceptance, or importance of any paper. It establishes a controlled publication architecture and records exact internal and formal evidence for the declared scopes.
