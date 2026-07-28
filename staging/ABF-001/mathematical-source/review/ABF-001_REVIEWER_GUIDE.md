# ABF-001 Reviewer Guide

## Purpose

This guide directs independent reviewers to the load-bearing claims, evidence routes, and known limitations of ABF-001.

## Suggested review sequence

1. Read the abstract, Sections 2-5, and the claim ledger.
2. Check the Reed-Muller degree threshold in Theorem 1.
3. Check the affine-coordinate spanning argument in Theorem 2.
4. Recompute the order-zero signature formula.
5. Run the primary verifier and six focused tests.
6. Run the independent bitset verifier.
7. Compare the two edge-atlas SHA-256 identities.
8. Inspect the corrected indexed-versus-distinct radical count.
9. Search for prior equivalent results under alternate terminology.

## Principal claims to challenge

| Claim | Failure mode to seek |
|---|---|
| Moment criterion | off-by-one degree threshold or incomplete monomial span |
| Bidual incidence | affine-coordinate convention error or nonlinearity in q |
| Punctured kernel | invalid parameter retained or valid parameter omitted |
| Symmetric pencil | matrix indexing error, asymmetry, or wrong kernel interpretation |
| 511 exceptional hyperplanes | rank/nullity or invalid-parameter counting error |
| Rank histogram | truth-table or elimination error |
| 469-edge double count | disagreement between mask-first and hyperplane-first routes |
| 202 distinct subspaces | unrecognized additional duplicate or intersection |
| Forest census | missed cycle or component |

## Evidence hierarchy

```text
human proof
    + fresh NumPy implementation
    + separately written bitset implementation
    + historical separately written C implementation
    + exhaustive small-universe controls
    + deterministic hashes
```

This hierarchy is substantial internal evidence. It is not external validation.

## Corrected finite statement

The exact wording is:

> The 255 nonzero masks contain 203 singular mask-indexed radicals representing 202 distinct nonzero radical subspaces. The only duplicate is the line `119d5`, shared by masks `8a` and `9b`.

Do not shorten this to “203 distinct radicals.”

## Review dispositions

Use one or more of:

- confirmed for stated scope;
- clarification required;
- proof gap;
- computational discrepancy;
- earlier equivalent theorem;
- known consequence;
- counterexample;
- scope reduction;
- suitable after revision;
- unsuitable for publication.

## Claim boundaries

ABF-001 is not peer reviewed, proof-assistant verified, independently externally reproduced, historically first, or a full-width cryptographic result.
