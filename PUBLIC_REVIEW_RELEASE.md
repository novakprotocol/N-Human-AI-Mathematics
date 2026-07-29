# Public review release record

## Current controlling status — 29 July 2026

The 27–28 July 2026 HINC-001 and ABF-001 releases remain preserved as immutable historical public artifacts. The accountable owner has since adopted a stricter rule:

> Every retained mathematical claim in an active theorem package must be covered by compiled Lean, with a complete manuscript-to-declaration map and zero unresolved formal scope.

Accordingly, the current status is:

```text
HINC-001  public archive; full-Lean requalification hold
ABF-001   public archive; full-Lean requalification hold
FSG-001   private; full-Lean completion hold
ACM-001   blocked until papers 1–3 align
active theorem packages under the current rule: none
```

See:

- `FULL_LEAN_RELEASE_STANDARD.md`;
- `PUBLIC_REVIEW_FORMALIZATION_HOLD_2026-07-29.md`;
- `PAPER_1_3_FULL_LEAN_STATUS.json`.

This is a status correction, not a claim that a counterexample has been found. The prior artifacts remain readable for chronology, review, and correction. They MUST NOT be described as currently active or fully Lean-verified while requalification is incomplete.

## Historical release identity

```text
release channel:             public review
historical version:          0.1.0-public-review
initial release date:        2026-07-27
repository:                  novakprotocol/N-Human-AI-Mathematics
accountable owner:           Matthew S. Novak
AI assistance:               one or more large language models
specific model disclosed:    no
specific provider disclosed: no
blanket license:             none
DOI:                         not assigned
journal submission:          not initiated
peer-review status:          not peer reviewed
historical priority:         unestablished
```

## Historical public artifacts

### HINC-001

The historical HINC-001 package includes a self-contained human candidate manuscript, proof and claim maps, bounded Lean evidence, computational checks, prior-art boundaries, reproduction instructions, rights notices, and review channels.

Its bounded Lean scopes are genuine. The complete manuscript remains unformalized, including major Hochschild, source-algebra, global-preservation, representability, center, clopen, derived-subgroup, and downstream consequence claims.

Current status:

```text
formal status:  PARTIAL_PASS
active status:  SUSPENDED_PENDING_FULL_LEAN
```

### ABF-001

The historical ABF-001 package includes a complete human candidate manuscript, exhaustive finite evidence, independent internal implementations, mutation controls, provenance, reproduction instructions, and a bounded A01 Lean lane.

A02–A06 and the complete proof-connected finite atlas remain unformalized.

Current status:

```text
formal status:  PARTIAL_PASS
active status:  SUSPENDED_PENDING_FULL_LEAN
```

### FSG-001

FSG-001 is not publicly released as a theorem package. Its private exact-head Lean bootstrap compiles the Fibonacci foundation and literal graph adjacency, but the complete F01–F07 program remains open.

Current status:

```text
formal status:  PARTIAL_BOOTSTRAP_PASS
active status:  PRIVATE_FULL_LEAN_COMPLETION_HOLD
```

## Required reactivation gate

For each exact paper source:

1. freeze one controlling manuscript;
2. inventory every retained theorem, lemma, equation, classification, exact count, and boundary case;
3. map every item to compiled Lean declarations or exact imported theorems;
4. formalize from the literal manuscript objects;
5. eliminate `sorry`, `admit`, project-result axioms, and `sorryAx`;
6. connect finite computations to kernel-checked certificates or exhaustive decidable proofs;
7. build from a committed manifest in a fresh exact-head environment;
8. retain axiom reports, source hashes, logs, manifests, and deterministic bundles;
9. pass an independent manuscript-to-Lean fidelity review;
10. complete the remaining hostile, prior-art, rights, packaging, and owner-authorization gates.

Only then may the package return to active public technical review.

## Scientific-status boundaries

Lean verification does not establish:

- external specialist correctness review;
- independent outside reproduction;
- historical priority;
- novelty or significance;
- peer review;
- journal acceptance;
- DOI or archival status.

Those remain separate gates and must be described separately.

## Rights

Public visibility permits reading and review. It does not create a blanket open-source or open-content license. Unless a file-specific notice states otherwise:

```text
Copyright © 2026 Matthew S. Novak. All rights reserved.
```

See `RIGHTS_AND_LICENSING.md` and each paper’s terms files.

## Correction policy

Historical releases will not be silently rewritten. Any material correction, narrowing, supersession, formal completion, or withdrawal must identify the affected source, claim, evidence, impact, repaired source, and disposition.
