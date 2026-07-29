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

FSG-001 is blocked independently by a confirmed mathematical counterexample in
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