# HINC-001 claim matrix

## Controlling status

```text
controlling manuscript:          manuscript/HINC-001_REVISED_MANUSCRIPT.md
paper state:                     candidate technical-review package
self-contained revised proof:   yes
bounded Lean verification:      yes
full manuscript Lean proof:     no
external specialist review:     pending
historical priority:             unestablished
peer reviewed:                   no
public switch readiness:         ready after final repository checks
public visibility:               not yet activated
```

The pre-review four-part manuscript is preserved for provenance but is not controlling.

## Structure convention

A **binary Gerstenhaber endomorphism** is unital, base-linear, degree-preserving, cup-product-preserving, and preserving the binary degree-minus-one Gerstenhaber bracket.

No preservation of a BV operator, restricted power, Gerstenhaber square beyond the binary bracket, brace algebra, or full `E_2` structure is claimed.

---

## C-01 — characteristic-two Hochschild foundation

**Claim.** For `D=F[epsilon]/(epsilon^2)` over a field of characteristic two,

```text
HH*(D,D) = D[u]
```

with

```text
[xu^i,yu^j]
  = (i x partial(y) + j y partial(x))u^(i+j-1).
```

**Status:** self-contained human proof integrated into the revised manuscript; external review pending; not formalized in the current Lean package.

## C-02 — even algebra presentation

**Claim.**

```text
E = F + uD[u] = F[r,s]/(s^2),
r=u,
s=epsilon u,
[r,s]=r.
```

**Status:** human proof integrated; external review pending.

## C-03 — even coefficient classification

**Claim.** A homogeneous generator assignment

```text
r -> lambda r + beta s
s -> eta r + delta s
```

satisfies the algebra and generator-bracket equations exactly when

```text
beta=0
eta^2=0
lambda(delta-1)=0.
```

**Status:** human proof, finite/symbolic controls, and bounded public Lean PASS.

## C-04 — even global endomorphism classification

**Claim.** The normalized even coefficients determine all binary Gerstenhaber endomorphisms of `E_R` over arbitrary commutative characteristic-two base algebras.

**Status:** revised human proof complete through the integrated generator-to-global lemma; coefficient layer formally verified; full theorem not yet formalized; external audit pending.

## C-05 — even affine monoid scheme

**Claim.** The functor is represented by

```text
Spec F[lambda,delta,eta]/(eta^2,lambda(delta-1))
```

with composition

```text
(lambda,delta,eta)(lambda',delta',eta')
 = (lambda lambda',delta delta',lambda eta' + delta' eta).
```

**Status:** explicit representability construction and revised human proof supplied; coefficient equations and composition law formally verified.

**Framing:** this is constrained upper-triangular matrix multiplication. As a scheme it is `C x alpha_2`; it is not a direct-product monoid scheme.

## C-06 — odd algebra presentation

**Claim.**

```text
O = D + F epsilon u + u^2D[u]
```

has the stated presentation on `epsilon,a,b,c`.

**Status:** complete human normal-form proof integrated into the revised manuscript; Lean formalization and external audit pending.

## C-07 — odd coefficient classification

**Claim.** The most general homogeneous candidate reduces exactly to

```text
epsilon -> lambda epsilon
a       -> mu a
b       -> p b
c       -> rho c
```

with

```text
p=lambda rho
rho=lambda p^2
lambda(mu-1)=0
rho(mu-1)=0.
```

**Status:** human proof, finite/symbolic controls, and bounded public Lean PASS.

## C-08 — odd global endomorphism classification

**Claim.** The normalized odd coefficients determine all binary Gerstenhaber endomorphisms of `O_R` over arbitrary commutative characteristic-two base algebras.

**Status:** revised human proof complete through the odd normal form and generator-to-global lemma; coefficient layer formally verified; full theorem not yet formalized; external audit pending.

## C-09 — odd affine monoid scheme and clopen split

**Claim.** The odd functor is represented by the stated coordinate ring with coordinatewise composition. The group-like idempotent

```text
z=lambda^3 rho
```

splits the representing scheme into a torus unit component and a crossing ideal.

**Status:** revised human proof integrated; internal polynomial checks passed; outside the current Lean scope.

**Pointwise qualification:** for disconnected bases, an `R`-point may select the two clopen components over different clopen pieces of `Spec R`; one must not use a naive all-rings set disjoint union.

## C-10 — common reduced crossing

**Claim.** The even reduction and odd nonunit component have the common commutative crossing

```text
C = Spec F[x,y]/(x(y-1)).
```

**Status:** exact algebraic consequence with internal reproduction; external review pending.

## C-11 — even universal noncommutativity

**Claim.** The even monoid has commutativity defect

```text
(x+y)e' + (x'+y')e
```

and is noncommutative over suitable square-zero test algebras even though the square-zero coordinate vanishes over fields.

**Status:** bounded Lean PASS for the defect formula and criterion; explicit witness supplied.

## C-12 — scheme-theoretic center

**Claim.**

```text
Z_sch(M_E) = Spec F[z]/(z(z-1))
```

embedded by `z -> (z,z,0)`. Therefore

```text
Z_sch(M_E)(R) = {(e,e,0): e^2=e in R}.
```

**Status:** complete revised human proof supplied; sufficient equations and idempotent consequence have bounded Lean PASS; complete subfunctor equality is not yet formalized.

**Pointwise warning:** the abstract center of `M_E(R)` can be larger than the `R`-points of the scheme-theoretic center.

## C-13 — even unit-group commutator

**Claim.**

```text
(a,c)(b,d)=(ab,ad+c)
[(a,c),(b,d)]=(1,(a+1)d+(b+1)c).
```

**Status:** bounded Lean PASS with inverse witnesses.

## C-14 — fppf-derived subgroup and abelianization

**Claim.** Under the stated fppf-sheaf convention,

```text
[G_E,G_E]_fppf = alpha_2
G_E^ab = G_m.
```

**Status:** expanded human proof integrated into the revised manuscript; commutator formula formally verified; fppf image argument not yet formalized; external specialist audit pending.

## C-15 — idempotent schemes

**Claim.** The even idempotent scheme has two reduced points and one `alpha_2` component; the odd idempotent scheme has four reduced points.

**Status:** revised human proof and exact internal polynomial classification; external review pending.

## C-16 — geometry and tangent claims

**Claim.** The stated reduction, connectedness, normalization, component, and tangent-space calculations follow from the coordinate rings.

**Status:** exact commutative-algebra consequences with internal reproduction; external review pending.

## C-17 — finite Artin counts

**Claim.** Over `R_n=F_2[t]/(t^n)`, the stated crossing, square-zero, monoid, and idempotent formulas hold.

**Status:** exact formulas with independent computational controls; they do not prove the arbitrary-base classification.

## C-18 — finite-field points and zeta functions

**Claim.** The stated finite-field point counts and zeta functions follow from the reduction and clopen split.

**Status:** exact. Equality of the even scheme and reduction point counts illustrates the standard invisibility of nilpotent thickening to field-valued points.

## C-19 — private MCRC application

**Claim.** The private MCRC program supplies examples of the two abstract parity types.

**Status:** separate application claim, not required for HINC-001. It is omitted from the controlling core proof and may be treated in a companion note.

## C-20 — historical priority

**Allowed statement.** A broad exact-form and primary-source search did not locate the complete paired classification.

**Status:** historical priority unestablished.

**Not allowed:** “first,” “nobody has done this,” “globally novel,” or equivalent wording before qualified source-level review.

---

## Formal verification boundary

The current Lean package verifies:

- crossing and skew-extension multiplication laws;
- exact commutativity defect and criterion;
- sufficient center equations and an idempotent consequence;
- the unit-group commutator formula;
- even and odd coefficient equations iff their normal forms;
- normalized composition closure, identity, associativity, and odd commutativity.

It does not yet formalize:

- the characteristic-two Hochschild derivation;
- the presented source algebras;
- the odd normal-form theorem;
- generator-to-global bracket preservation;
- the complete natural representability bijections;
- complete center equality;
- the clopen split as a functorial scheme statement;
- the fppf-derived subgroup argument;
- the full revised manuscript.

## Publication boundary

```text
candidate mathematics:                yes
self-contained revised human proof:  yes
strong internal evidence:             yes
bounded formal verification:          yes
complete manuscript formalization:    no
external correctness review:          pending
external reproduction:                pending
historical priority established:      no
peer reviewed:                         no
public technical-review package:      ready after final repository checks
public visibility:                     private until owner switch
```

Public release, when activated, must use **candidate technical review** language and display every pending gate above. It would solicit external review; it would not claim that review has already occurred.
