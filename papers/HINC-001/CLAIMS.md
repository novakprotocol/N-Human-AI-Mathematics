# HINC-001 Claim Matrix

## Controlling status

```text
paper state:                    private candidate under hostile review
public release:                 blocked
peer reviewed:                  no
external specialist review:    pending
historical priority:            unestablished
explicit counterexample found: no
```

The pre-review manuscript must be read together with:

- `HOSTILE_REVIEW_2026-07-27.md`;
- `MANUSCRIPT_ERRATA_2026-07-27.md`;
- `FOUNDATIONAL_HOCHSCHILD_DERIVATION_2026-07-27.md`;
- `GENERATOR_TO_GLOBAL_LEMMA_2026-07-27.md`;
- `ODD_PRESENTATION_NORMAL_FORM_2026-07-27.md`.

## Structure convention

A **binary Gerstenhaber endomorphism** in HINC-001 means a map that is:

```text
unital
base-linear
degree-preserving
cup-product-preserving
binary Gerstenhaber-bracket-preserving
```

No preservation of a BV operator, restricted power, Gerstenhaber square, brace algebra, or full `E_2` structure is claimed.

---

## C-01 — Ambient characteristic-two Hochschild algebra

**Claim.** For `D=F[epsilon]/(epsilon^2)` over a field of characteristic two, normalized Hochschild cochains give

```text
HH*(D,D) = D[u]
```

with the bracket

```text
[xu^i,yu^j]
  = (i x partial(y) + j y partial(x))u^(i+j-1).
```

**Status:** human proof supplied in `FOUNDATIONAL_HOCHSCHILD_DERIVATION_2026-07-27.md`; external review pending; not formalized in the current Lean package.

**Not claimed:** preservation or classification of additional positive-characteristic Hochschild operations.

## C-02 — Even algebra presentation

**Claim.** The even algebra is

```text
E = F + uD[u]
  = F[r,s]/(s^2),
r=u,
s=epsilon u,
[r,s]=r.
```

**Status:** direct algebraic consequence of C-01; human proof supplied; external review pending.

## C-03 — Even coefficient classification

**Claim.** A homogeneous generator candidate

```text
r -> lambda r + beta s,
s -> eta r + delta s
```

satisfies the generator relation/bracket equations exactly when

```text
beta=0,
eta^2=0,
lambda(delta-1)=0.
```

**Status:** human proof complete; finite/symbolic controls passed; bounded public Lean PASS.

## C-04 — Even global endomorphism classification

**Claim.** The normalized even coefficient data determine all binary Gerstenhaber endomorphisms of `E` over arbitrary commutative characteristic-two base algebras.

**Status:** candidate theorem. Coefficient classification formally verified; generator-to-global human proof now supplied; Lean integration and external specialist audit pending.

## C-05 — Even affine monoid scheme

**Claim.** The candidate endomorphism functor is represented by

```text
Spec F[lambda,delta,eta]/(eta^2,lambda(delta-1))
```

with composition

```text
(lambda,delta,eta)(lambda',delta',eta')
  = (lambda lambda',delta delta',lambda eta' + delta' eta).
```

**Status:** coefficient equations and composition law formally verified; complete representability proof remains prose and must be expanded before release.

**Framing:** the multiplication is constrained upper-triangular matrix multiplication. As a scheme it is `C × alpha_2`; not as a monoid scheme.

## C-06 — Odd algebra presentation

**Claim.** The odd algebra

```text
O = D + F epsilon u + u^2 D[u]
```

has the displayed presentation on `epsilon,a,b,c`.

**Status:** the relations are direct; presentation completeness is now human-proved by the normal form in `ODD_PRESENTATION_NORMAL_FORM_2026-07-27.md`; Lean formalization and external audit pending.

## C-07 — Odd coefficient classification

**Claim.** The most general homogeneous generator candidate reduces exactly to

```text
epsilon -> lambda epsilon,
a       -> mu a,
b       -> p b,
c       -> rho c,
```

with

```text
p=lambda rho,
rho=lambda p^2,
lambda(mu-1)=0,
rho(mu-1)=0.
```

**Status:** human proof complete; finite/symbolic controls passed; bounded public Lean PASS.

## C-08 — Odd global endomorphism classification

**Claim.** The normalized odd coefficient data determine all binary Gerstenhaber endomorphisms of `O` over arbitrary commutative characteristic-two base algebras.

**Status:** candidate theorem. Coefficient classification formally verified; odd presentation and generator-to-global human proofs supplied; Lean integration and external audit pending.

## C-09 — Odd affine monoid scheme and clopen split

**Claim.** The odd candidate functor is represented by the stated coefficient ring with coordinatewise composition. The idempotent

```text
z=lambda^3 rho
```

splits it into a torus unit component and a crossing ideal.

**Status:** candidate scheme-level theorem; algebraic identities internally reproduced; not included in the current Lean scope; external review pending.

**Framing:** describe this as adjoining a separate clopen unit component, not as a novel generic “unit-doubling” mechanism.

## C-10 — Common reduced crossing

**Claim.** The even reduction and odd nonunit component have the common commutative crossing

```text
C = Spec F[x,y]/(x(y-1))
```

with coordinatewise multiplication.

**Status:** exact internally reproduced algebraic consequence; external review pending.

## C-11 — Even universal noncommutativity

**Claim.** The even monoid has commutator defect

```text
(x+y)e' + (x'+y')e,
```

and is noncommutative over suitable square-zero test algebras even though the square-zero coordinate vanishes over fields.

**Status:** bounded Lean PASS for the defect formula and commutativity criterion; exact example supplied.

## C-12 — Scheme-theoretic center

**Claim.** The center is the constant finite étale two-point scheme cut out by

```text
e=0,
x=y,
x(x-1)=0.
```

**Status:** sufficient equations and idempotent consequence have bounded Lean PASS; complete equality as a center subfunctor remains outside the current Lean scope and requires specialist review.

**Pointwise wording:** on connected bases the points are zero and identity; disconnected bases allow idempotent mixtures.

## C-13 — Even unit-group commutator

**Claim.** The unit group has law

```text
(a,c)(b,d)=(ab,ad+c)
```

and commutator

```text
(1,(a+1)d+(b+1)c).
```

**Status:** bounded Lean PASS with explicit inverse witnesses.

## C-14 — Derived subgroup and abelianization

**Claim.** The fppf-derived subgroup is `alpha_2` and the abelianization is `G_m`.

**Status:** candidate group-scheme consequence. The pointwise commutator formula is verified; the scheme-image, fppf-sheaf image, closure, and quotient conventions require external audit and formalization.

## C-15 — Idempotent schemes

**Claim.** The even and odd idempotent schemes have the stated components, including one nonreduced `alpha_2` component in the even case and reduced finite components in the odd case.

**Status:** exact internally reproduced polynomial classification; external review pending.

## C-16 — Tangent, connectedness, and component claims

**Claim.** The manuscript’s dimension, tangent-space, reduction, connectedness, and clopen-component calculations follow from the displayed coordinate rings.

**Status:** exact internally reproduced commutative-algebra consequences; external review pending.

## C-17 — Finite-Artin counts

**Claim.** Over `R_n=F_2[t]/(t^n)`, the stated formulas for the crossing, square-zero elements, and even/odd monoids hold.

**Status:** exact finite formulas with computational controls. They support consistency and do not prove arbitrary-base classification.

## C-18 — Finite-field points and zeta functions

**Claim.** The stated finite-field point counts and zeta functions follow from the reduction and clopen split.

**Status:** exact internally reproduced. The even nilpotent thickening is invisible to field-valued points by construction; this is an illustration, not a new general arithmetic principle.

## C-19 — MCRC application

**Claim.** The private MCRC family supplies examples of the two abstract parity types.

**Status:** separate application claim. It is not needed for the standalone HINC theorem and should move to an appendix or companion note.

## C-20 — Historical priority

**Claim allowed.** A broad primary-source and exact-form search did not locate the complete paired HINC classification.

**Status:** historical priority unestablished.

**Not allowed:** “first,” “nobody has done this,” “globally novel,” or equivalent wording before qualified source-level review.

---

## Formal verification boundary

The current Lean package verifies:

- crossing and skew-extension multiplication laws;
- exact commutativity defect and criterion;
- sufficient center equations and one idempotent consequence;
- unit-group commutator formula;
- even and odd coefficient equations iff their normal forms;
- normalized composition closure, identity, and associativity;
- odd normalized commutativity.

It does not yet formalize:

- the characteristic-two Hochschild derivation;
- the even or odd presented algebras;
- the odd normal-form theorem;
- generator-to-global binary-bracket preservation;
- complete representability;
- clopen decomposition;
- complete center equality;
- fppf-derived subgroup or abelianization;
- the full manuscript.

## Publication boundary

```text
candidate mathematics:             yes
strong internal evidence:          yes
bounded formal verification:       yes
complete manuscript formalization: no
external correctness review:       no
external reproduction:             no
historical priority established:   no
peer reviewed:                      no
public release completed:          no; private draft only
```

Any status upgrade must identify the exact new source, proof, execution, reviewer, or formal environment and the precise claims affected.
