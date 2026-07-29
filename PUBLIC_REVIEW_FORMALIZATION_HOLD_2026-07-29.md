# Public formalization hold — 29 July 2026

## Status correction

The owner has adopted a stricter release rule: every retained mathematical claim must be covered by compiled Lean before a theorem package is described as active.

Accordingly:

```text
HINC-001  public historical artifact; full-Lean requalification hold
ABF-001   public historical artifact; full-Lean requalification hold
FSG-001   private; full-Lean completion hold
ACM-001   consolidation hold; work does not advance until papers 1–3 align
```

This is a status correction, not a retraction of a demonstrated counterexample. The existing HINC-001 and ABF-001 releases are preserved for provenance, including their exact bounded formal evidence and limitations. They are no longer represented as active packages while complete manuscript formalization remains open.

## Current formal facts

- HINC-001 has two substantial bounded Lean PASS scopes, but its complete revised manuscript is not formalized.
- ABF-001 has a bounded A01 Lean PASS, but A02–A06 and the complete manuscript are not formalized.
- FSG-001 has a successful exact-head Lean bootstrap for its Fibonacci and literal-graph foundations, but F01–F07 and the complete manuscript are not formalized.

## Release requirement

Each package must independently reach:

- zero unmapped mathematical claims;
- zero unresolved formal claims;
- zero `sorry`, `admit`, project-result axioms, or `sorryAx`;
- clean immutable Lean build PASS;
- complete claim-to-declaration and manuscript-fidelity PASS;
- deterministic source, evidence, and release manifests;
- final prior-art and hostile review at the frozen head;
- exact owner authorization.

No new paper package will be activated until this standard is met. Historical priority, peer review, journal acceptance, and significance remain separate questions that Lean cannot establish.