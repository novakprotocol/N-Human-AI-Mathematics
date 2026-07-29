# Full-portfolio Lean verification program

## Controlling rule

Effective 29 July 2026, the accountable owner requires a complete-manuscript Lean `FULL_PASS` before any theorem package is classified as active.

> A paper reaches `FULL_PASS` only when every retained theorem, lemma, equation, structural equivalence, exact finite classification, boundary case, and imported mathematical dependency used by the controlling manuscript maps to compiled Lean declarations or exact documented imported theorems, with zero unresolved formal scope.

The historical HINC-001 and ABF-001 public releases remain accessible for chronology, correction, and review. Their active theorem status is suspended while complete-manuscript requalification proceeds. FSG-001 remains private. ACM-001 remains blocked until papers 1–3 align.

This file and `FULL_LEAN_RELEASE_STANDARD.md` are controlling together. Where an older release record conflicts with them, the 29 July 2026 hold and correction records control current status.

## What Lean can and cannot establish

Lean can kernel-check formal statements, definitions, reductions, calculations, certificates, and proofs inside an exact toolchain and dependency graph. It can check a finite classification when the declared universe and computation are connected to proof-producing or kernel-evaluated declarations.

Lean does not by itself establish:

- that the encoded theorem faithfully matches the intended manuscript;
- historical priority or worldwide novelty;
- significance or publication value;
- independent outside reproduction;
- external correctness review;
- peer review or journal acceptance.

Those remain separate gates.

## Mandatory FULL_PASS gate

For each paper `P`, the accepted formal receipt must establish:

1. **Frozen source identity** — one controlling manuscript, formal source commit, Lean toolchain, Lake version, Mathlib revision, and committed dependency manifest.
2. **Complete claim inventory** — every retained theorem, lemma, corollary, formula, exact count, asymptotic statement, and boundary case has a stable claim ID.
3. **Complete claim map** — every claim maps to compiled declarations or exact imported theorems, with unresolved claims equal to zero.
4. **Literal-source bridge** — the formalization starts from the manuscript’s actual objects and hypotheses, not a downstream matrix, table, count, or normal form that assumes the hardest step.
5. **Universal/finite separation** — universal claims have universal proofs; finite claims cover the complete stated finite universe.
6. **No placeholders** — zero `sorry`, zero `admit`, zero project axioms used to assume project results, and no `sorryAx`.
7. **Axiom audit** — every exported theorem has a retained `#print axioms` report checked against an explicit allowlist.
8. **Trusted-code audit** — any use of `native_decide`, `bv_decide`, `trustCompiler`, `implemented_by`, `extern`, unsafe code, or custom metaprogramming is disclosed and bounded.
9. **Immutable build** — a fresh exact-head build uses the committed manifest and completes without timeout, skipped stage, or dependency mutation.
10. **Independent kernel validation** — controlling modules are replayed by the selected checker program and any required trusted-challenge comparison.
11. **Fidelity review** — a mathematically qualified reviewer compares manuscript and Lean definitions, hypotheses, quantifiers, boundary cases, and conclusions.
12. **Machine receipt** — result `FULL_PASS`, unresolved formal claims `0`, fidelity blockers `0`, and `full_manuscript_lean_verified: true`.

Any missing condition leaves the result at `PARTIAL_PASS`, `PARTIAL_BOOTSTRAP_PASS`, `HOLD`, `BLOCKED`, or `FAIL`. No rounding up is allowed.

## Current portfolio status

### HINC-001

```text
public state:                     historical public artifact
active theorem state:             suspended pending full Lean
compiled Lean lanes:              H01, H02, H03 bounded PASS
remaining lanes:                  H04–H09
formal status:                    PARTIAL_PASS
full manuscript Lean verified:    no
```

Required completion includes the complete normalized Hochschild cochain and Gerstenhaber-bracket construction, presented source algebras, odd normal form, generator-to-global extension, representability and bialgebras, complete scheme centers, clopen decomposition, fppf-derived subgroup and abelianization, and all retained geometric, idempotent, tangent, counting, and zeta consequences.

### ABF-001

```text
public state:                     historical public artifact
active theorem state:             suspended pending full Lean
compiled Lean lane:               A01 bidual moment-kernel bridge
remaining lanes:                  A02–A06
formal status:                    PARTIAL_PASS
full manuscript Lean verified:    no
```

Required completion includes Reed–Muller duality and the degree criterion; affine-hyperplane coordinates and complete moment spaces; order-zero signature and radical classification; order-one matrix-pencil identity; and a proof-connected complete 16-to-8 atlas from the exact map through all masks, restrictions, ranks, kernels, counts, and incidence data.

### FSG-001

```text
public state:                     private
bootstrap exact head:             462395ad89ee3fa20b1fccd4ecf86c15dd156879
compiled bootstrap:               Fibonacci foundation and literal adjacency
formal status:                    PARTIAL_BOOTSTRAP_PASS
remaining lanes:                  F01–F07
clean immutable execution:        not yet accepted
full manuscript Lean verified:    no
public mathematical release:      HOLD
```

Required completion includes complete Fibonacci and Lucas arithmetic; literal graph connectedness, degrees, and Laplacian; the integral graph-to-3×3 bridge; tree, forest, gluing, and resistance results; complete determinantal divisors and Smith factors; chip signatures and firing reconstruction; and the full valuation, CRT, torsion, Wall–Sun–Sun condition, and density layer. F03 and F05 are release-critical.

### ACM-001

```text
public state:                     teaching preview only
controlling manuscript:           absent
proof-assistant project:          absent
formal status:                    BLOCKED_BY_CONSOLIDATION
full manuscript Lean verified:    no
public mathematical release:      HOLD
```

ACM work begins only after papers 1–3 reach the same complete professional state and one ACM controlling manuscript, exact map identity, complete result ledger, overlap decision, correction ledger, and claim map are frozen.

## Public wording rule

Until a paper has `FULL_PASS`, public wording may say:

- `bounded Lean verification`;
- `selected declarations compile in Lean`;
- `partial formalization`;
- `formalization in progress`;
- `not fully formalized`;
- `historical public artifact on full-Lean requalification hold`.

For a non-`FULL_PASS` paper, the following are prohibited:

- `formally proved`;
- `fully formalized`;
- `Lean-verified manuscript`;
- `all claims machine checked`;
- `active theorem package` under the current owner rule.

## Release decision

```text
HINC-001: public archive; PARTIAL_PASS; active status suspended
ABF-001:  public archive; PARTIAL_PASS; active status suspended
FSG-001:  private; PARTIAL_BOOTSTRAP_PASS; HOLD
ACM-001:  BLOCKED until papers 1–3 reach FULL_PASS
```

This correction changes no theorem, historical source identity, or prior-art conclusion. It changes the current release classification and the work required before reactivation.
