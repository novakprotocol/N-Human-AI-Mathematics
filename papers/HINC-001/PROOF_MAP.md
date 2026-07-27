# HINC-001 proof map

## Controlling source

The controlling proof is the consolidated manuscript:

```text
manuscript/HINC-001_REVISED_MANUSCRIPT.md
```

The hostile-review addenda remain provenance and review records; they are no longer substitutes for an integrated manuscript.

## Structure convention

The classified maps are **binary Gerstenhaber endomorphisms**: unital, base-linear, degree-preserving, cup-product-preserving, and preserving the binary degree-minus-one bracket.

No BV, restricted-power, brace, Gerstenhaber-square beyond the binary bracket, or full `E_2` preservation is claimed.

---

## Foundation chain

```text
F0  normalized cochains of D=F[epsilon]/(epsilon^2) in characteristic two
        ↓
F1  zero differential, cup algebra D[u], explicit binary bracket
        ↓
F2  explicit subalgebras E and O
        ↓
F3  complete algebra presentations
        ↓
F4  general homogeneous generator images
        ↓
F5  polynomial relation and generator-bracket equations
        ↓
F6  generator-to-global biderivation lemma
        ↓
F7  natural arbitrary-base endomorphism classifications
        ↓
F8  affine coefficient schemes, polynomial composition, bialgebras
        ↓
F9  common core, centers, units, clopen split, idempotents, and counts
```

### F0–F1 — ambient Hochschild structure

The revised manuscript proves directly:

```text
HH*(D,D)=D[u]
[xu^i,yu^j]=(i x partial(y)+j y partial(x))u^(i+j-1).
```

**Human proof:** complete.  
**Lean:** not formalized.  
**External review:** pending.

### F2–F3 — source algebras

Even:

```text
E=F+uD[u]=F[r,s]/(s^2)
[r,s]=r.
```

Odd:

```text
O=D+F epsilon u+u^2D[u]
```

with complete normal form

```text
f(b)+c g(b)+epsilon h(b)+epsilon c k(b)+tau a.
```

**Human proof:** complete.  
**Lean:** not formalized.  
**External review:** pending.

### F6 — generator-to-global theorem

The revised manuscript proves that a unital graded algebra homomorphism preserving brackets on homogeneous algebra generators preserves the bracket globally, by induction through the two biderivation identities.

**Human proof:** complete.  
**Lean:** not formalized.  
**External review:** pending.

### F8 — representability

The revised manuscript explicitly:

1. chooses finite homogeneous generator-image coefficient spaces;
2. imposes polynomial algebra and bracket equations;
3. proves a natural base-wise bijection using F3 and F6;
4. derives polynomial composition;
5. identifies the coordinate bialgebras.

**Human proof:** complete.  
**Lean:** coefficient equations and normalized composition only.  
**External review:** pending.

---

## Even classification chain

```text
r -> lambda r + beta s
s -> eta r + delta s
```

- `s^2=0` gives `eta^2=0`.
- `[r,s]=r` gives `beta=0` and `lambda(delta-1)=0`.
- F6 extends generator-table preservation globally.
- Composition is

```text
(lambda,delta,eta)(lambda',delta',eta')
 = (lambda lambda',delta delta',lambda eta'+delta' eta).
```

The representing ring is

```text
F[lambda,delta,eta]/(eta^2,lambda(delta-1)).
```

The multiplication is constrained upper-triangular matrix multiplication. As schemes,

```text
M_E = C x alpha_2,
```

but this is not a direct-product monoid law.

### Even proof status

| Node | Human proof | Internal computation | Lean | External review |
|---|---|---|---|---|
| Algebra presentation | Complete | Checked | Not formalized | Pending |
| Coefficient equations | Complete | Checked | Hosted PASS | Pending |
| Generator-to-global | Complete | Supporting checks | Not formalized | Pending |
| Composition | Complete | Checked | Hosted PASS | Pending |
| Representability | Complete | Symbolic checks | Partial | Pending |
| Common-core scheme statement | Complete | Checked | Multiplication kernel PASS | Pending |
| Center equality | Complete | Finite/symbolic checks | Sufficient equations only | Pending |
| Unit commutator | Complete | Checked | Hosted PASS | Pending |
| fppf-derived subgroup | Complete paper proof | Commutator checked | Not formalized | Pending |

---

## Odd classification chain

```text
epsilon -> x + lambda epsilon
a       -> mu a
b       -> p b + q epsilon b
c       -> rho c + sigma epsilon c
```

The generator brackets give

```text
x=q=sigma=0
p=lambda rho
lambda(mu-1)=0
rho(mu-1)=0.
```

The remaining algebra relation gives

```text
rho=lambda p^2.
```

The normal-form theorem proves that the displayed source relations are complete. F6 then gives global bracket preservation. Composition is coordinatewise.

The representing ring is

```text
F[lambda,mu,p,rho]/
(p-lambda rho,
 rho-lambda p^2,
 lambda(mu-1),
 rho(mu-1)).
```

The group-like idempotent

```text
z=lambda^3 rho
```

splits the representing scheme into a torus unit component and a crossing ideal.

For connected bases, every point lies in one component. For disconnected bases, points may select components on complementary clopen pieces; the scheme split is not a naive all-rings set disjoint union.

### Odd proof status

| Node | Human proof | Internal computation | Lean | External review |
|---|---|---|---|---|
| Presentation normal form | Complete | Checked | Not formalized | Pending |
| Coefficient equations | Complete | Checked | Hosted PASS | Pending |
| Generator-to-global | Complete | Supporting checks | Not formalized | Pending |
| Composition | Complete | Checked | Hosted PASS | Pending |
| Representability | Complete | Symbolic checks | Partial | Pending |
| Group-like idempotent | Complete | Checked | Not formalized | Pending |
| Clopen scheme split | Complete | Checked | Not formalized | Pending |

---

## Common-core synthesis

```text
Even reduction                = crossing C
Odd nonunit clopen component = crossing C
```

where

```text
C=Spec F[x,y]/(x(y-1))
```

with coordinatewise multiplication.

The paired result is:

```text
Even: C plus a constrained skew square-zero direction.
Odd:  C plus a separate clopen torus unit component.
```

The general mechanisms are established. The candidate contribution is the explicit binary-Gerstenhaber-derived pair and exact common-core identification.

---

## Scheme-theoretic center and pointwise warning

The revised proof identifies

```text
Z_sch(M_E)=Spec F[z]/(z(z-1))
```

embedded by `z -> (z,z,0)`.

Thus

```text
Z_sch(M_E)(R)={(e,e,0):e^2=e}.
```

The abstract center of `M_E(R)` can be larger. This distinction is part of the controlling theorem and must remain visible in every summary.

---

## Evidence overlay

The current Lean package verifies the algebraic kernel, coefficient equations, normalized composition laws, commutativity defect, sufficient center equations, and unit-group commutator. It does not verify the full revised manuscript.

Finite Python, C, Gröbner, Artin-ring, and standalone common-core routes challenge the declared formulas. They are internal evidence, not external reproduction.

---

## Review priorities after public release

Public release is intended to obtain, not pre-claim:

1. an external check of the characteristic-two normalized-cochain derivation;
2. an external check of the odd presentation normal form;
3. an external check of generator-to-global preservation;
4. a scheme-theoretic audit of representability and the clopen split;
5. a center and fppf-derived-subgroup audit;
6. a source-level equivalence and historical-priority review;
7. independent reproduction or formalization of the presently unformalized nodes.

## Release rule

The candidate package may be made public only with:

- the consolidated revised manuscript as the controlling source;
- the exact formal-verification boundary displayed;
- external review and historical priority marked pending;
- no claim of peer review or journal acceptance;
- the repository privacy and identity scans passing;
- a final owner-controlled visibility switch.
