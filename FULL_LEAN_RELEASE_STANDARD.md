# Full-Lean release standard

Effective 29 July 2026, the accountable owner requires every retained mathematical claim in a released theorem package to be covered by compiled Lean before that package is treated as active.

## Required result

A paper may be marked `ACTIVE_PUBLIC_REVIEW` only when all of the following hold for one exact frozen source identity:

1. Every theorem, lemma, exact formula, classification, finite count, and mathematical corollary retained in the controlling manuscript has a stable claim ID.
2. Every retained claim maps to one or more compiled Lean declarations or to an exact imported Mathlib theorem whose hypotheses are explicitly discharged.
3. The map contains no `UNMAPPED`, `PARTIAL`, `ASSUMED`, or `COMPUTATION_ONLY` mathematical claim.
4. The project contains no `sorry`, `admit`, project `axiom` declaration standing in for a project result, or `sorryAx` dependency.
5. Universal claims are proved universally. Finite classifications are connected to kernel-checked certificates or exhaustive decidable proofs covering the exact declared universe.
6. The literal manuscript objects are connected to their formal representations; proving a simplified substitute is insufficient.
7. A pinned Lean, Lake, and Mathlib environment builds from a clean immutable source checkout.
8. The build emits an axiom report, source manifest, claim-map receipt, logs, deterministic evidence bundle, and SHA-256.
9. A human fidelity audit verifies that the compiled declarations express the manuscript claims without weakening or changing hypotheses.
10. The final source, package, manifest, tag, release target, and site wording receive exact owner authorization.

## Nonmathematical boundaries

Lean does not establish historical priority, peer review, journal acceptance, significance, accessibility, website behavior, or prose quality. Those remain separate review and engineering gates.

## Requalification rule

Existing public artifacts for HINC-001 and ABF-001 are preserved as historical records. Until they satisfy this standard, they are not described as active theorem packages; their status is `PUBLIC_ARCHIVE_FULL_LEAN_REQUALIFICATION_HOLD`.

FSG-001 remains private until it satisfies the same standard. ACM-001 and later packages may not advance to publication work until HINC-001, ABF-001, and FSG-001 are aligned at the same professional state.

## Fail-closed state

The only successful mathematical release state is:

```json
{
  "full_manuscript_lean_verified": true,
  "unmapped_mathematical_claims": 0,
  "unresolved_formal_claims": 0,
  "sorry_count": 0,
  "admit_count": 0,
  "project_axiom_count": 0,
  "sorryAx_present": false,
  "clean_immutable_build": "PASS",
  "claim_fidelity_review": "PASS",
  "public_release_authorized": true
}
```

Any missing field or lesser state is a release hold.