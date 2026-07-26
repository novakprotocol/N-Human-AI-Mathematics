## 11. Independent reconstruction and falsification

Finite computation does not replace the all-base proof.  It is used here to challenge the coefficient elimination, monoid laws, component split, and idempotent geometry through structurally different implementations.

### 11.1 Operation-level Python route

The independent Python implementation imports neither the closed-form endomorphism module nor the preceding automorphism-scheme packet.  It:

1. constructs `R_n` directly as bit-polynomial rings;
2. constructs sparse monomials `\epsilon^e u^j` in the dual-polynomial model;
3. implements cup products and the characteristic-two bracket;
4. inserts every general homogeneous generator image;
5. checks the complete defining algebra relations and generator bracket table;
6. compares the accepted set with an independently coded normal form;
7. computes products, component indicators, and idempotents directly.

The recorded audit is:

```text
even orders:              1 through 4
odd orders:               1 through 3
general candidates:       2,183,568
formula mismatches:                0
idempotent-count mismatches:       0
component-indicator failures:      0
result:                         PASS
```

### 11.2 Separately written C coefficient route

The C program does not call either Python implementation.  It implements truncated-ring multiplication, the direct coefficient equations, the proposed normal forms, component indicators, and idempotence checks.

```text
even orders:              1 through 6
odd orders:               1 through 4
general candidates:     288,444,816
accepted candidates:          2,841
idempotents:                     49
formula mismatches:               0
component failures:               0
result:                         PASS
```

### 11.3 Exact Groebner-ideal route

A third implementation uses exact polynomial ideals over `GF(2)`.  It verifies:

1. equality of the direct even coefficient ideal and the even normal-form ideal;
2. equality of the direct odd coefficient ideal and the odd normal-form ideal;
3. equality of the eliminated odd ideal with the intersection of the two clopen component ideals;
4. idempotence of `z=\lambda^3\rho` modulo the odd ideal;
5. exact decomposition of the even idempotent ideal into two reduced points and one `\alpha_2` component;
6. exact decomposition of the odd idempotent ideal into four reduced point ideals.

All six symbolic checks pass.

### 11.4 Semantic negative controls

The packet rejects altered statements including:

- the even monoid is reduced;
- the even monoid is commutative;
- the odd monoid is noncommutative;
- the odd unit group is not a connected component;
- the odd `\epsilon` translation survives;
- the odd degree-two or degree-three nilpotent shear survives;
- the even idempotent scheme is reduced;
- the odd collapse component is unrelated to the even reduction.

### 11.5 Standalone common-core verifier

A fourth implementation was written from scratch for the consolidated paper. It imports none of the earlier MCRC, Hochschild, endomorphism, or common-core modules. It directly implements `F_2[t]/(t^n)`, the crossing core, the bilateral skew product, and the unit-doubling product.

It passed five focused tests and audited orders `n=1,2,3,4`, checking closure, identities, associativity, the universal commutator-defect formula, the collapse morphism, and deterministic certificate generation. An independent SymPy route checked the core closure identity, skew associativity/coassociativity, the commutator formula, reducedness of the two-point center, finite-field count formulas, and tangent-dimension assertions.

```text
result: PASS
finite failures: 0
symbolic failures: 0
evidence SHA-256: 20d883988da7818f73de0b4ccab68bc7adea5097a4af7a6ef5a72c23b4e1ea4b
```

## 12. Relation to established theory and priority boundary

The surrounding frameworks are established and are not claimed as new.

1. Rittatore and Brion develop the structure of algebraic monoids and the openness of their unit groups.
2. Brion proves that the idempotent scheme of a commutative algebraic semigroup is finite and reduced. This is consistent with the reduced four-point odd idempotent scheme; the even monoid is noncommutative and has an `alpha_2` idempotent component.
3. Perepechko proves that every affine algebraic monoid can occur as the endomorphism monoid of a finite-dimensional nonassociative algebra. Thus the existence of endomorphism monoids with exotic geometry is not itself new.
4. Scheme-theoretic automorphism groups of graded algebras are an active established framework; Elduque develops this viewpoint for gradings over arbitrary fields.
5. Koenig-Nagase and Hermann provide the stratifying-ideal and Gerstenhaber-functorial machinery relevant to the MCRC origin of `E` and `O`.
6. The dual-number Hochschild Gerstenhaber algebra and deformation interpretation of low-degree Hochschild cohomology are classical.

The candidate contribution is the explicit pair and its complete all-base classification:

- one crossing core appearing as the even reduction and odd collapse component;
- a bilateral skew `alpha_2` thickening versus a clopen unit doubling;
- a monoid whose reduced points are commutative while its universal center is only zero and identity;
- a unit group whose field-valued points are all central but whose group-scheme center is trivial and whose derived subgroup is `alpha_2`;
- exact idempotent, normalization, tangent, point-count, and zeta fingerprints;
- several structurally independent computational challenge routes.

A targeted indexed search through algebraic-monoid, automorphism-scheme, endomorphism-scheme, Gerstenhaber, and Hochschild literature found no exact occurrence of this complete pair of formulas or the common-core interpretation. This is a negative search, not proof of worldwide historical priority. Equivalent results may occur under different generators or as an unstated specialization of a general theorem.

The defensible label is:

```text
standalone explicit classification with plausible publication value,
pending specialist equivalence review and formal verification.
```

## 13. Evidence boundary and next gates

Supported by the present packet:

- complete coefficient proofs over arbitrary commutative characteristic-two base algebras;
- explicit coordinate bialgebras and composition laws;
- common-core, hidden-center, derived-subgroup, component, normalization, tangent, and zeta calculations;
- Python, C, Groebner, finite-Artin, and standalone common-core challenge routes;
- deterministic evidence identities and semantic negative controls;
- a self-contained formulation independent of acceptance of the MCRC parent theorem.

Not established:

- worldwide historical novelty or publication priority;
- proof-assistant verification;
- independent external institutional replication;
- successful immutable hosted execution in GitHub Actions;
- peer-review acceptance;
- authorization for public release.

The remaining high-value gates are:

1. specialist review of the functor-of-points and common-core isomorphisms;
2. formalization of the coefficient classification, skew coproduct, center, derived subgroup, and clopen split;
3. a source-level MathSciNet/zbMATH/thesis search by a domain expert;
4. execution from an immutable fresh clone in an environment that records actual steps and logs;
5. editorial review of whether the MCRC application belongs in this paper or a companion note.

## References

1. M. Brion, *On algebraic semigroups and monoids*, in **Algebraic Monoids, Group Embeddings, and Algebraic Combinatorics**, Fields Institute Communications 71, Springer, 2014; arXiv:1208.0675.
2. M. Brion, *On algebraic semigroups and monoids, II*, Semigroup Forum 88 (2014), 250-272; arXiv:1303.3955.
3. A. Rittatore, *Algebraic monoids and group embeddings*, Transformation Groups 3 (1998), 375-396; arXiv:math/9802073.
4. A. Perepechko, *Affine algebraic monoids as endomorphisms' monoids of finite-dimensional algebras*, Proceedings of the American Mathematical Society 137 (2009), 3301-3305; arXiv:0809.2356.
5. S. Koenig and H. Nagase, *Hochschild cohomology and stratifying ideals*, Journal of Pure and Applied Algebra 213 (2009), 886-891. DOI: 10.1016/j.jpaa.2008.10.012.
6. R. Hermann, *Monoidal Categories and the Gerstenhaber Bracket in Hochschild Cohomology*, Memoirs of the American Mathematical Society 243 (2016), no. 1151; arXiv:1411.0836.
7. A. Elduque, *Automorphism group schemes and Weyl groups of gradings*, arXiv:2507.12321, revised 2026.
8. M. Gerstenhaber, *The cohomology structure of an associative ring*, Annals of Mathematics 78 (1963), 267-288.
9. M. Gerstenhaber, *On the deformation of rings and algebras*, Annals of Mathematics 79 (1964), 59-103.
