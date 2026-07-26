# HINC-001 Evidence Map

This document maps each major claim to its human proof, computational evidence, formal verification, and remaining review gate.

## Source identities

| Layer | Repository / source | Exact identity |
|---|---|---|
| Standalone manuscript and verifier | `novakprotocol/N-MathLab` PR #406 | `e6adac212150177d4afa56e643d37533a208693c` |
| Base Lean kernel source | public checker source | `8ccf90b05a0ab4fb45774e9dd8ba7b3c9a59cd8c` |
| Principal classification Lean source | `novakprotocol/novak-sdt` PR #58 | `d7751d1de76253407016ef4bf92738cffa800e82` |
| Clean publication staging | `novakprotocol/N-MathLab` export branch | current bootstrap branch head |

## Claim-to-evidence matrix

| Claim area | Human proof | Computation | Lean | Remaining gate |
|---|---|---|---|---|
| Crossing multiplication and geometry | Manuscript Parts 1–2 | Standalone verifier | Base hosted PASS | External algebraic-monoid review |
| Even square-zero skew multiplication | Manuscript Part 2 | Finite Artin and symbolic checks | Base hosted PASS | Scheme-level interpretation review |
| Exact commutativity defect | Manuscript Part 2 | Explicit counter-order witness | Base hosted PASS | None for formula; external significance review |
| Even coefficient normal form | Manuscript coefficient elimination | Symbolic and finite checks | Principal classification hosted PASS | Generator-to-global sufficiency and external review |
| Even normalized composition | Direct substitution proof | Standalone checks | Principal classification hosted PASS | Scheme representability review |
| Odd coefficient normal form | Manuscript arbitrary-base elimination | Finite and symbolic checks | Principal classification hosted PASS | Generator-to-global sufficiency and specialist audit |
| Odd normalized composition | Direct substitution proof | Standalone checks | Principal classification hosted PASS | Scheme representability review |
| Endomorphism functor representability | Manuscript coordinate-ring proof | Symbolic consistency only | Not formalized | External review and future Lean work |
| Common crossing core | Manuscript scheme isomorphism | Finite checks | Base crossing only | External equivalence review |
| Odd clopen unit split | Manuscript idempotent/quotient proof | Finite checks | Not formalized | High-priority specialist review |
| Complete even monoid center | Manuscript universal-point proof | Dual-number test points | Sufficient equations only | Complete formalization and external review |
| Unit-group derived subgroup | Manuscript commutator/fppf proof | Symbolic checks | Commutator formula only | Validate fppf formulation |
| Idempotents, tangents, counts, zeta | Manuscript corollaries | Standalone verifier | Not formalized | Secondary audit |
| MCRC application | Final manuscript application | Parent project checks | Not formalized | Keep logically separate from standalone theorem |

## Computational evidence

### Standalone route

```text
focused tests:                         5 PASS
primary local process:                    PASS
fresh copied workspace:                   PASS
finite Artin orders:                    1–4
finite failures:                           0
symbolic failures:                         0
duplicate certificate byte identity:   PASS
```

Controlling certificate SHA-256:

```text
20d883988da7818f73de0b4ccab68bc7adea5097a4af7a6ef5a72c23b4e1ea4b
```

### Base Lean receipt

```text
run:               30119931881
job:               89569737408
artifact:          8606983225
artifact SHA-256:  63b2b160da40f722818820679da7c9d22eb7640694e48a5abc08fccf78f47133
result:            PASS
sorryAx:           absent
```

### Principal classification Lean receipt

```text
run:                    30174213006
job:                    89720259114
artifact:               8623775718
artifact SHA-256:       2dee88b9a248dee8719c27aa23a27ca3281e697cf67202bb50c1fe60a4809dc9
Classification SHA-256:56267aba47fd67e94be5842057aaec5bd0718829e860af212eedcdb43efbb084
axiom report SHA-256:   dcd0bbefb6d88e0c70a57dabc0e45c408fe7998ace6b33e330f6f6d44fb5b7ce
result:                 PASS
sorryAx:                absent
```

## Preserved negative evidence

The first classification build failed at run `30173789803` because an extensionality proof exceeded Lean's recursion depth. The failure artifact `8623660266` is preserved. The proof was repaired with explicit field substitutions; the theorem statement did not change.

## Evidence not yet present

- an outside specialist correctness report;
- an outside independent implementation;
- source-level MathSciNet/zbMATH equivalence review;
- a generator-to-global Lean proof;
- formal representability and scheme-decomposition proofs;
- journal peer review;
- DOI release;
- owner authorization for public visibility.

## Interpretation

The formal and computational evidence substantially supports the coefficient calculations and algebraic kernel. The complete scheme-valued classification remains a candidate theorem until its remaining human and formal gates close.
