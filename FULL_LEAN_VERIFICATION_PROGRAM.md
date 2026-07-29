# Full-portfolio Lean verification program

## Owner-selected standard

The portfolio now uses one fail-closed gold standard for the mathematical claims
presented on the public research and learning pages:

> A paper may be described as **fully Lean-verified** only when every theorem,
> lemma, structural equivalence, finite classification, and imported mathematical
> dependency used by its controlling manuscript has an exact compiled declaration
> or an explicitly identified imported theorem, with a complete claim-to-
> declaration map and no unresolved formal scope.

This policy does not retroactively relabel bounded verification as full proof. It
also does not withdraw HINC-001 or ABF-001 from public technical review. Their
current public packages remain valid under their stated bounded boundaries while
the stronger formalization program proceeds.

FSG-001 and ACM-001 are not eligible for a new public mathematical release under
this owner-selected standard until their complete controlling manuscripts satisfy
the gold gate.

## What Lean can and cannot establish

Lean can kernel-check formal statements, definitions, reductions, calculations,
and proofs inside an exact toolchain and dependency graph. It can also check a
finite classification when the declared finite universe and the computation are
connected to a proof-producing or kernel-evaluated declaration.

Lean does not by itself establish:

- that the formal statement faithfully captures the intended prose theorem;
- historical priority or worldwide novelty;
- significance or publication value;
- independent reproduction;
- peer review, journal acceptance, or correctness of external factual claims.

Those remain separate review gates.

## Mandatory gold gate

For each paper `P`, the formal receipt must establish all of the following:

1. **Exact source identity** — controlling manuscript, formal source commit,
   Lean toolchain, Lake version, Mathlib revision, and dependency manifest.
2. **Complete claim map** — every mathematical claim in the controlling
   manuscript maps to one or more compiled declarations or to an exact imported
   theorem with its use documented.
3. **No placeholders** — zero `sorry`, zero `admit`, zero project `axiom`
   declarations used to assume a project result, and no `sorryAx` in the build.
4. **Axiom report** — every remaining kernel axiom dependency is recorded and
   compared against an explicit allowlist.
5. **Literal-source bridge** — formalization begins from the paper's actual
   objects and hypotheses, not merely from a downstream matrix, count, or normal
   form that assumes the difficult bridge.
6. **Universal/finite separation** — universal theorems receive universal
   proofs; finite claims receive complete exact finite declarations over the
   stated universe. Numerical spot checks are never substituted for a universal
   proof.
7. **Clean immutable build** — a fresh exact-head build completes without
   timeout, skipped required declaration, missing log, or accepted partial
   output.
8. **Fidelity review** — a human mathematical reviewer checks that formal
   statements match the controlling manuscript and that no hypothesis or
   conclusion was weakened silently.
9. **Machine-readable receipt** — result `FULL_PASS`, unresolved claim count
   zero, and `full_manuscript_lean_verified: true`.

Any missing condition leaves the result at `PARTIAL`, `BOOTSTRAP`, `HOLD`, or
`FAIL`; it may not be rounded up.

## Current portfolio status

### HINC-001

```text
public state:                     active candidate technical review
proof-assistant project:          Lean 4.30.0 / Mathlib 4.30.0
compiled Lean boundary:           H01 algebraic kernel
                                  H02 coefficient classification
                                  H03 dual-number Hochschild foundation
full revised manuscript:          not formalized
formal status:                    PARTIAL_PASS
fully Lean-verified:              no
```

The compiled H03 lane establishes the square-zero generator, characteristic-two
boundary cancellation, represented normalized-differential vanishing, represented
cup associativity, and the epsilon-coefficient product rule. It does not yet
construct the complete normalized cochain complex, insertion operation, closed
Gerstenhaber bracket formula, or generator-to-global extension.

The remaining formal lanes are the complete normalized Hochschild/bracket
calculation, complete source algebras, odd presentation normal form,
generator-to-global bracket extension, natural representability, coordinate
bialgebras, clopen decomposition, complete scheme centers, fppf-derived
subgroup/abelianization, and the remaining geometric and arithmetic consequences.

### ABF-001

```text
public state:                     active candidate technical review
proof-assistant project:          Lean 4.30.0 / Mathlib 4.30.0
compiled Lean boundary:           A01 bidual moment-kernel bridge
human proof:                      complete candidate
computational evidence:           extensive
formal status:                    PARTIAL_PASS
fully Lean-verified:              no
```

The compiled A01 lane proves the abstract equivalence between annihilating the
moment generators, annihilating their generated span, and lying in the kernel of
a compatible affine-parameter moment map. It does not prove the Reed--Muller
degree criterion or the finite atlas.

The remaining formal order is Reed--Muller duality, affine-hyperplane
coordinates, complete moment spaces, the degree-drop criterion, order-zero
signature, order-one matrix identity, and proof-connected finite rank/kernel
certificates for the complete declared atlas.

### FSG-001

```text
public state:                     private release-edge teaching preview
formal project:                   private gold-standard bootstrap
compiled complete manuscript:     no
clean immutable execution:        not yet passed
formal status:                    BOOTSTRAP_COMPILE_PENDING
fully Lean-verified:              no
public mathematical release:      HOLD
```

The required lanes are Fibonacci/Lucas identities; literal graph, boundary cases,
connectedness, and reduced Laplacian; integral graph-to-3x3 cokernel equivalence;
trees, forests, gluing, and resistance; all Smith determinantal divisors; chip-
class signature and original-vertex firing equivalence; and the complete
arithmetic/CRT/density layer for every claim retained in the manuscript.

### ACM-001

```text
public state:                     teaching preview / consolidation hold
controlling manuscript:           absent
proof-assistant project:          absent
formal status:                    BLOCKED_BY_CONSOLIDATION
fully Lean-verified:              no
public mathematical release:      HOLD
```

Formal work begins only after one controlling manuscript, exact map/source
identity, complete finite-result ledger, and claim map are frozen. The expected
lanes are the ANF coefficient code, support floor, all generalized support
weights, minimizer uniqueness and non-nesting, matroid translation, and exact
automorphism/stabilizer classification.

## Public wording rule

Until a paper has a `FULL_PASS` receipt, public wording must use one of these
bounded forms:

- `bounded Lean verification`;
- `selected declarations compile in Lean`;
- `formalization in progress`;
- `not fully formalized`;
- `no proof-assistant verification`.

The phrases `formally proved`, `fully formalized`, `Lean-verified manuscript`,
and `all claims machine-checked` are prohibited for a non-`FULL_PASS` paper.

## Release decision

```text
HINC-001: remain active with bounded H01-H03 formal PASS
ABF-001:  remain active with bounded A01 formal PASS
FSG-001:  HOLD under the selected full-Lean gold standard
ACM-001:  HOLD pending consolidation and full formalization
```

This policy changes no theorem, source identity, release asset, or historical-
priority conclusion. It strengthens future release language and acceptance.
