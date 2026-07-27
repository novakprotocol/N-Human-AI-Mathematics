# HINC-001 Proof Map

## Current use

This map reflects the 2026-07-27 hostile review. The preserved four-part manuscript predates several load-bearing clarifications. Read the controlling foundation and errata files before treating any downstream theorem as release-ready.

## Structure convention

The classified maps are **binary Gerstenhaber endomorphisms**:

```text
unital
base-linear
degree-preserving
cup-product-preserving
binary degree-minus-one bracket-preserving
```

No BV, restricted-power, Gerstenhaber-square, brace, or full `E_2` preservation is claimed.

---

## Foundation chain

```text
F0  normalized Hochschild cochains of D=F[epsilon]/epsilon^2 in char 2
        ↓
F1  zero differential, cup algebra D[u], explicit binary bracket
        ↓
F2  explicit subalgebras E and O inside D[u]
        ↓
F3  complete algebra presentations and generator bracket tables
        ↓
F4  general homogeneous generator images
        ↓
F5  coefficient equations
        ↓
F6  generator-to-global binary-bracket preservation
        ↓
F7  functorial endomorphism classifications
        ↓
F8  affine coefficient schemes and polynomial composition
        ↓
F9  geometry, centers, units, derived groups, idempotents, and counts
```

### F0–F1 — Ambient Hochschild structure

The exact characteristic-two derivation is now supplied in:

```text
FOUNDATIONAL_HOCHSCHILD_DERIVATION_2026-07-27.md
```

It is a human proof, not part of the current Lean package.

### F2–F3 — Source algebras

Even:

```text
E = F + uD[u] = F[r,s]/(s^2)
|r|=|s|=1
[r,s]=r
```

Odd:

```text
O = D + F epsilon u + u^2D[u]
```

with the displayed presentation on `epsilon,a,b,c`.

The odd presentation completeness is supplied by:

```text
ODD_PRESENTATION_NORMAL_FORM_2026-07-27.md
```

with unique normal form

```text
f(b)+c g(b)+epsilon h(b)+epsilon c k(b)+tau a.
```

### F6 — Generator-to-global theorem

The biderivation induction is supplied in:

```text
GENERATOR_TO_GLOBAL_LEMMA_2026-07-27.md
```

This closes the human proof route but remains unformalized and externally unaudited.

---

## Even classification chain

### E1 — General degree-one candidate

```text
r -> lambda r + beta s
s -> eta r + delta s
```

### E2 — Algebra relation

Preserving `s^2=0` gives

```text
eta^2=0.
```

Dependency: `r^2` spans a free base-ring summand.

### E3 — Bracket relation

Preserving `[r,s]=r` gives

```text
beta=0
lambda(delta-1)=0.
```

### E4 — Coefficient theorem

The generator equations are equivalent to the normal form. This is formally verified in the bounded Lean classification kernel.

### E5 — Global extension

The normal-form assignment preserves the algebra relation and complete generator bracket table. The generator-to-global lemma gives global binary-bracket preservation.

```text
human proof:        supplied
Lean formalization: pending
external audit:     pending
```

### E6 — Composition

```text
(lambda,delta,eta)(lambda',delta',eta')
 = (lambda lambda',delta delta',lambda eta'+delta' eta).
```

Closure, identity, and associativity are formally verified for normalized data.

### E7 — Representability

Candidate coefficient scheme:

```text
A_E = F[lambda,delta,eta]/(eta^2,lambda(delta-1)).
```

Required before release:

- define the coefficient affine space;
- impose all algebra and bracket equations;
- prove the natural base-wise bijection;
- derive polynomial composition and coordinate-bialgebra maps.

### E8 — Matrix and geometric interpretation

The multiplication is upper-triangular matrix multiplication:

```text
[x e]
[0 y]
```

with constraints

```text
x(y-1)=0,
e^2=0.
```

As schemes,

```text
M_E = C × alpha_2.
```

This is not a direct-product monoid law.

### E9 — Units and commutator

Unit law:

```text
(a,c)(b,d)=(ab,ad+c).
```

Commutator:

```text
(1,(a+1)d+(b+1)c).
```

The commutator formula has bounded Lean verification.

### E10 — Center and derived group

Candidate center equations:

```text
e=0,
x=y,
x(x-1)=0.
```

The center should be stated as the constant finite étale two-point scheme. The complete center equality and fppf-derived subgroup convention remain outside the current Lean scope and require specialist audit.

---

## Odd classification chain

### O1 — General homogeneous candidate

```text
epsilon -> x + lambda epsilon
a       -> mu a
b       -> p b + q epsilon b
c       -> rho c + sigma epsilon c.
```

### O2 — Bracket elimination

The generator bracket table gives

```text
x=q=sigma=0
p=lambda rho
lambda(mu-1)=0
rho(mu-1)=0.
```

### O3 — Algebra equation

The remaining relation gives

```text
rho=lambda p^2.
```

### O4 — Coefficient theorem

The direct generator equations are equivalent to the diagonal normal form. This is formally verified in the bounded Lean classification kernel.

### O5 — Global extension

The odd normal-form presentation plus the generator-to-global lemma gives the human proof of global binary-bracket preservation.

```text
human proof:        supplied
Lean formalization: pending
external audit:     pending
```

### O6 — Composition

Composition is coordinatewise on normalized data. Closure, identity, associativity, and commutativity are formally verified.

### O7 — Representability and clopen split

Candidate coordinate ring:

```text
F[lambda,mu,p,rho]/
(p-lambda rho,
 rho-lambda p^2,
 lambda(mu-1),
 rho(mu-1)).
```

The element

```text
z=lambda^3 rho
```

is idempotent and group-like, yielding a torus unit component and crossing ideal. This scheme-level decomposition is internally checked but not formally verified.

Use “adjoining a separate clopen unit component” rather than implying a new general doubling construction.

---

## Common-core synthesis

```text
Even reduction                  = crossing C
Odd nonunit clopen component   = crossing C
```

where

```text
C = Spec F[x,y]/(x(y-1))
```

with coordinatewise multiplication.

The candidate comparison is:

```text
Even: C with a skew square-zero direction
Odd:  C plus a separate clopen torus unit component
```

The general mechanisms are established. The candidate project contribution is the explicit Gerstenhaber-derived pair and exact common-core identification.

---

## Secondary consequences

The following depend on the global classifications and, where applicable, scheme-level conventions:

- idempotent schemes;
- center descriptions;
- derived subgroup and abelianization;
- tangent spaces;
- normalization;
- finite-Artin counts;
- finite-field counts and zeta functions;
- MCRC application.

A flaw in F0–F7 blocks all downstream consequences. A flaw only in E10 does not invalidate the coefficient classifications.

---

## Verification overlay

| Proof node | Human proof | Internal computation | Lean status | External review |
|---|---|---|---|---|
| Characteristic-two Hochschild foundation | Supplied in addendum | Generator table checked | Not formalized | Pending |
| Even algebra presentation | Complete | Checked | Not formalized | Pending |
| Odd algebra presentation | Normal-form proof supplied | Checked | Not formalized | Pending |
| Even coefficient equations | Complete | Checked | Public hosted PASS | Pending |
| Odd coefficient equations | Complete | Checked | Public hosted PASS | Pending |
| Generator-to-global lemma | Supplied in addendum | Partly checked | Not formalized | Pending |
| Even/odd normalized composition | Complete | Checked | Public hosted PASS | Pending |
| Representability/bialgebras | Candidate, needs expansion | Symbolic checks | Not formalized | Pending |
| Odd clopen split | Candidate | Checked in declared routes | Not formalized | Pending |
| Complete center equality | Candidate | Symbolic/finite checks | Partial kernel only | Pending |
| Derived subgroup/abelianization | Candidate | Commutator checked | Commutator formula only | Pending |

## Review priority

1. Characteristic-two normalized-bar and bracket derivation.
2. Odd presentation normal form.
3. Generator-to-global binary-bracket preservation.
4. Functorial representability and coordinate bialgebras.
5. Complete center subfunctor.
6. fppf-derived subgroup and abelianization.
7. Odd clopen split and common-core isomorphism.
8. Historical equivalence under different generators or matrix-monoid language.

## Release rule

Do not release the pre-review manuscript as controlling. First consolidate the foundation, presentation, global-extension, terminology, status, bibliography, and priority corrections into a new source identity; then rerun every evidence and rendering gate.
