---
title: "MCRC Hidden Infinitesimal Noncommutativity"
subtitle: "Specialist Review, Reproducibility, and Submission-Control Packet"
author:
  - "[Author Name]"
date: "24 July 2026"
abstract: |
  This packet accompanies the standalone manuscript on two explicit graded Gerstenhaber endomorphism monoid schemes. It isolates the proof risks, exact claim boundary, reproducibility route, formalization obligations, venue positioning, and submission gates. It is a review-control document, not a substitute for the manuscript.
---

# Status at a glance

| Gate | Status |
|---|---|
| Standalone coefficient proof | Written |
| Standalone local verifier | PASS |
| Deterministic evidence certificate | Present |
| Manuscript and cover letter | Prepared |
| Specialist equivalence review | Pending |
| Proof-assistant verification | Pending |
| Immutable hosted PASS | Not obtained |
| Worldwide priority | Not established |
| Public submission authorization | Hold |

> **Controlling formulation.** Reduced points can report that every visible unit is central while the universal symmetry group scheme has trivial center and a nontrivial infinitesimal derived subgroup.

## Referee guide and proof map

### One-sentence theorem

Two explicit graded Gerstenhaber algebras have endomorphism monoid schemes built from one crossing core: one by a nonreduced skew `alpha_2` thickening, the other by a reduced clopen unit doubling; the even reduced points appear commutative although the universal unit group has trivial center and derived subgroup `alpha_2`.

### Logical dependency map

1. Define `D=F[epsilon]/(epsilon^2)` and the bracket on `D[u]`.
2. Define the subalgebras `E=F+uD[u]` and `O=D+F epsilon u+u^2D[u]`.
3. Solve the coefficient equations for all graded strict endomorphisms of `E`.
4. Solve the coefficient equations for all graded strict endomorphisms of `O`.
5. Derive the odd group-like idempotent and clopen decomposition.
6. Identify the shared crossing core.
7. Prove the even center and unit-group commutator theorems.
8. Compute idempotents, normalization, tangents, and point counts.

The MCRC family is not required for steps 1-8.

### Highest-risk proof points

#### A. Odd coefficient elimination

Check that the algebra and bracket relations force every endomorphism to be diagonal and impose exactly

```text
p=lambda*rho
rho=lambda*p^2
lambda(mu-1)=0
rho(mu-1)=0.
```

#### B. Arbitrary-base interpretation

Check that coefficient comparison is valid over an arbitrary commutative `F`-algebra, including nonreduced rings. No field-only diagonalization may be used.

#### C. Odd clopen split

Check that `z=lambda^3*rho` is group-like and idempotent and that the two quotient ideals give exactly `G_m` and the crossing core.

#### D. Scheme-theoretic center

Check the universal quantifier over all base changes. The proof uses the test points `(0,1,0)` and `(0,0,t)` after adjoining `t^2=0`.

#### E. Derived subgroup

Check that all commutators lie in `alpha_2` and that every `alpha_2` point is obtained fppf-locally as a commutator after adjoining a unit `t` with `t+1` invertible.

#### F. Unit doubling

Check that the componentwise rules define a monoid scheme and match the odd coefficient model over arbitrary base algebras, not only fields or connected Artin rings.

### Questions for a specialist

1. Is the complete theorem already a direct specialization of a known result on endomorphism schemes of graded Poisson or Gerstenhaber algebras?
2. Is "unit doubling" standard under another name?
3. Is the derived-subgroup statement best phrased as an fppf sheaf-theoretic derived subgroup, schematic closure of commutators, or both?
4. Should the standalone paper retain the MCRC application or move it to a final remark?
5. Is Semigroup Forum or Journal of Pure and Applied Algebra the stronger editorial fit?

### Evidence boundary

Computations test formulas and falsify common mistakes. They are not used as substitutes for universal proofs.

## Claim boundary

### Supported

- The two Gerstenhaber algebras are explicitly defined inside `HH*(F[epsilon]/epsilon^2)`.
- Complete coefficient classifications are written over arbitrary commutative characteristic-two base algebras.
- The even and odd endomorphism functors are represented by the stated affine monoid schemes.
- The common crossing-core theorem and both modification constructions are proved.
- The even monoid center is zero plus identity.
- The even unit group has trivial center, derived subgroup `alpha_2`, and abelianization `G_m`, with the derived statement understood fppf-sheaf-theoretically.
- Idempotent, component, normalization, tangent, finite-field count, and zeta formulas are written.
- Multiple local executable challenge routes agree with zero recorded discrepancies.
- A new standalone verifier executed successfully in a fresh local process.

### Not supported

- Worldwide historical novelty.
- Publication priority.
- Peer-review acceptance.
- Proof-assistant verification.
- Independent external institutional replication.
- A successful immutable GitHub-hosted execution.
- Public release authorization.
- Claims about arbitrary Hochschild cohomology rings beyond the two explicit strict images.
- Claims that computational enumeration substitutes for universal proof.

### Safe public wording

> We give a self-contained candidate classification of two explicit graded Gerstenhaber endomorphism monoid schemes. The formulas are supported by all-base coefficient proofs and several independent computational challenge routes. A targeted search found no exact indexed match, but historical priority remains under specialist review.

## Reproducibility guide

### Minimal standalone route

Requirements:

```text
Python 3.11 or later
SymPy 1.14.0
```

From the packet root:

```bash
python -m pip install 'sympy==1.14.0'
PYTHONPATH=src python -m unittest discover -s tests -v
PYTHONPATH=src python src/standalone_common_core_verifier.py \
  --maximum-order 4 \
  --output evidence/standalone-certificate.reproduced.json
```

Then compare:

```bash
cmp evidence/standalone-certificate.json \
    evidence/standalone-certificate.reproduced.json
sha256sum -c evidence/SHA256SUMS.code.txt
```

### What the standalone route checks

- crossing-core closure;
- even skew closure and associativity;
- skew-primitive coassociativity;
- universal commutator-defect formula;
- odd unit-doubling closure and associativity;
- multiplicativity of the collapse map;
- deterministic certificate generation;
- finite-field point-count formulas;
- two-point reduced center polynomial;
- tangent-dimension assertions.

### Evidence identity

```text
standalone certificate evidence SHA-256:
20d883988da7818f73de0b4ccab68bc7adea5097a4af7a6ef5a72c23b4e1ea4b
```

### Larger parent routes

The parent project records additional operation-level Python, independent C, and exact Groebner routes. Their identities and execution receipts are preserved separately. The standalone route is intentionally independent and smaller so a referee can read it in one sitting.

### Failure policy

Any mismatch must be recorded as a scientific failure. Do not regenerate expected hashes after a mismatch without first identifying and documenting the mathematical or implementation change.

## Proof-assistant formalization blueprint

### Recommended strategy

Formalize the standalone Gerstenhaber-algebra theorem first. Treat the MCRC origin as a separate downstream development.

A system with strong commutative-algebra support is preferable. Lean 4 with Mathlib is a plausible choice, but the plan is system-neutral.

### Phase 1 - algebraic data

1. Define a characteristic-two commutative base ring.
2. Define the graded algebra `D[u]` with `epsilon^2=0`.
3. Define the bracket formula on homogeneous monomials.
4. Prove graded antisymmetry, Jacobi, and Leibniz identities.
5. Define subalgebras `E` and `O` and their finite generator presentations.

### Phase 2 - endomorphism normal forms

6. Represent a general degree-preserving generator map for `E`.
7. Prove relation preservation iff `beta=0`, `eta^2=0`, and `lambda(delta-1)=0`.
8. Derive the composition law and bialgebra formulas.
9. Represent a general homogeneous generator map for `O`.
10. Prove all off-diagonal coefficients vanish.
11. Prove the four diagonal equations are necessary and sufficient.
12. Derive coordinatewise composition.

### Phase 3 - geometry and monoids

13. Define the crossing monoid `C`.
14. Prove closure, associativity, identity, and unit subgroup.
15. Prove `M_E` is a scheme product with `alpha_2` and a skew monoid product.
16. Prove the odd group-like idempotent and clopen decomposition.
17. Define unit doubling and prove `M_O` is isomorphic to it.
18. Prove the collapse morphism and nonunital section statement.

### Phase 4 - centers and idempotents

19. Formalize the universal center functor.
20. Prove `Z(M_E)={0,1}`.
21. Define `G_E=alpha_2 semidirect G_m` and prove the commutator formula.
22. Prove the center is trivial.
23. Prove the fppf-derived subgroup is `alpha_2` and the abelianization is `G_m`.
24. Compute both idempotent schemes.

### Phase 5 - arithmetic geometry

25. Prove normalization of the crossing.
26. Compute tangent dimensions at the crossing and identities.
27. Prove finite-field point counts and zeta functions.

### Formalization acceptance gate

No theorem should be marked formalized until the build is pinned, runs from a fresh checkout, and contains no `sorry`, admitted axioms, or imported computational certificates as proof terms.

## Related work and priority assessment

### Established frameworks

#### Algebraic monoids

Rittatore and Brion provide foundational structure theory, including openness of unit groups. Brion also proves that the idempotent scheme of a commutative algebraic semigroup is finite and reduced.

#### Endomorphism monoids

Perepechko proves that every affine algebraic monoid can be realized as the endomorphism monoid of a finite-dimensional nonassociative algebra. Therefore the mere occurrence of a nonreduced or disconnected endomorphism monoid is not new.

#### Scheme-theoretic automorphisms of graded structures

Elduque develops automorphism group schemes of gradings over arbitrary fields, confirming that functor-of-points and group-scheme methods are established and active in graded algebra.

#### Hochschild and Gerstenhaber structure

Koenig-Nagase establish long exact Hochschild sequences for stratifying ideals. Hermann establishes compatibility of Gerstenhaber structures under suitable structure-preserving functors and Morita invariance. The dual-number Hochschild algebra and Gerstenhaber deformation theory are classical.

### Search target

The search looked for the complete combination:

```text
two explicit graded Gerstenhaber algebras
+ full arbitrary-base endomorphism monoid schemes
+ shared reducible crossing core
+ skew alpha_2 thickening versus clopen unit doubling
+ reduced points commutative but universal center {0,1}
+ field-valued units central but group-scheme center trivial
+ derived subgroup alpha_2 and abelianization G_m
+ explicit idempotent, tangent, point-count, and zeta phase
```

Exact phrases and structural variants were searched in arXiv, publisher pages, and citation trails around algebraic monoids, endomorphism schemes, automorphism group schemes, alpha-p extensions, and Gerstenhaber algebras.

### Result

No exact indexed occurrence of the complete theorem was located. The closest frameworks explain individual mechanisms but did not provide this pair or the common-core theorem in the searched sources.

This is not proof of historical absence. A specialist must still check:

- MathSciNet and zbMATH at source level;
- theses and proceedings;
- equivalent coordinate changes;
- general theorems on graded Poisson/Gerstenhaber endomorphism schemes;
- algebraic-monoid constructions equivalent to unit doubling.

### Defensible label

```text
plausible publication-grade explicit classification,
pending specialist equivalence and historical-priority review
```

## Venue matrix

### Recommended editorial order

| Rank | Venue | Fit | Main risk | Required edit |
|---:|---|---|---|---|
| 1 | Semigroup Forum | Strongest fit for explicit algebraic monoid structure, idempotents, units, and common-core construction | Gerstenhaber origin may look secondary or too specialized | Lead with monoid theorem; move MCRC/Hochschild application to final section |
| 2 | Journal of Pure and Applied Algebra | Strong fit if the Gerstenhaber-algebra classification and scheme representability are emphasized | Explicit example may be judged too narrow without broader structural framing | Stress universal functors, hidden center, and common-core construction |
| 3 | Algebras and Representation Theory | Reasonable if expanded toward Hochschild structure and graded-algebra symmetries | Monoid-scheme geometry may sit outside the journal's main center | Add more representation-theoretic motivation |
| 4 | Proceedings of the AMS | Attractive only for a sharply compressed theorem note | Current full paper likely exceeds the 15 printed-page limit | Produce a separate <=15-page core theorem and omit most evidence |

### Primary recommendation

**Semigroup Forum**, after specialist review, because the strongest theorem is now an explicit algebraic-monoid classification rather than an internal MCRC consequence.

### Secondary recommendation

**Journal of Pure and Applied Algebra**, particularly if the final title and introduction emphasize endomorphism schemes of graded Gerstenhaber algebras and the arbitrary-base coefficient method.

### Submission hold

Do not submit until:

1. a specialist validates the odd arbitrary-base normal form and common-core isomorphism;
2. the derived subgroup phrasing is finalized;
3. authorship and AI-assistance disclosures are approved;
4. the manuscript is anonymized if the selected venue requires it;
5. all references are checked against MathSciNet/zbMATH;
6. a clean immutable verification run is preserved or the absence is explicitly disclosed.

## Submission checklist

### Mathematical gates

- [ ] Specialist validates even coefficient classification.
- [ ] Specialist validates odd coefficient classification.
- [ ] Specialist validates common-core and unit-doubling isomorphism.
- [ ] Specialist validates universal center proof.
- [ ] Specialist validates fppf-derived subgroup statement.
- [ ] Related-work search checked in MathSciNet and zbMATH.
- [ ] Proof-assistant scope decided.

### Evidence gates

- [x] Standalone local verifier passes.
- [x] Deterministic certificate generated.
- [x] Source and evidence checksums recorded.
- [ ] Immutable fresh-clone execution produces logs and receipt.
- [ ] External reproduction by a second person or institution.

### Editorial gates

- [x] Standalone manuscript written.
- [x] MCRC dependency removed from theorem logic.
- [x] Cover letter drafted.
- [x] Referee guide drafted.
- [x] Claim boundary drafted.
- [x] Reproducibility guide drafted.
- [x] Formalization blueprint drafted.
- [x] Venue matrix drafted.
- [ ] Author names and affiliations confirmed.
- [ ] Corresponding author confirmed.
- [ ] Conflict-of-interest statement confirmed.
- [ ] AI/computational assistance disclosure approved.
- [ ] Journal template applied.
- [x] Double-anonymous copy prepared.
- [ ] Final language edit completed.

### Release gate

```text
CURRENT STATE: SPECIALIST PRE-SUBMISSION HOLD
```

## Authorship and computational-assistance disclosure template

The named human authors take full responsibility for the mathematical statements, proofs, source verification, citations, and submission decisions in this work.

Computational tools were used to enumerate finite test cases, perform symbolic ideal checks, generate deterministic evidence receipts, and format draft materials. Generative AI systems assisted with exploratory derivation, code drafting, exposition, document organization, and literature-query formulation. AI systems are not authors and did not independently certify correctness, novelty, or priority.

Before submission, the human authors must:

1. read and approve every theorem and proof;
2. independently verify all cited sources;
3. rerun or supervise all computational evidence;
4. comply with the selected journal's current disclosure policy;
5. ensure no confidential or third-party material is improperly included;
6. accept responsibility for errors and corrections.

**Journal-specific disclosure text:**  
[Insert the exact disclosure required by the selected venue.]
