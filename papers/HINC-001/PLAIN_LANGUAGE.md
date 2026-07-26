# HINC-001 in Plain Language

## The basic question

Suppose a mathematical object has a collection of symmetry-like transformations. We want to know:

- what all of those transformations are;
- how they compose;
- whether their composition is commutative;
- which transformations commute with everything;
- whether ordinary numerical points reveal the complete structure.

The paper studies this question for two explicit graded algebraic objects in characteristic two.

## The shared crossing

Both transformation systems contain the same reduced equation:

```text
x(y - 1) = 0.
```

A product is zero when at least one factor is zero, so the equation describes two branches:

```text
x = 0       or       y = 1.
```

These two branches meet at `(x,y) = (0,1)`. Geometrically, that is a crossing.

## The even object: a hidden infinitesimal direction

The even transformation system adds a coordinate `e` satisfying:

```text
e² = 0.
```

A nonzero quantity whose square is zero is called **nilpotent** or **infinitesimal**. Ordinary fields do not contain nonzero square-zero elements, so ordinary field-valued points force `e = 0`.

The multiplication is:

```text
(x,y,e)(x',y',e') = (xx', yy', x e' + y' e).
```

The last coordinate treats the left and right factors differently. Consequently, changing the order can change the answer.

For example, over a ring with a nonzero square-zero element `t`, take:

```text
p = (1,1,t)
q = (0,1,0).
```

Then:

```text
pq = (0,1,t)
qp = (0,1,0),
```

so `pq != qp`.

But over an ordinary field, `t` must equal zero. The visible field-valued multiplication then looks commutative. This is the hidden-infinitesimal effect.

## The odd object: a visible separate component

The odd transformation system does not use the same hidden skew direction. Instead, it is reduced and commutative and contains an additional separate unit component.

The rough comparison is:

| Even | Odd |
|---|---|
| Hidden square-zero thickening | Separate visible unit component |
| Connected | Disconnected |
| Nonreduced | Reduced |
| Universally noncommutative | Commutative |
| Difference disappears on ordinary field points | Difference visible as a separate component |

## Why ordinary points can mislead

A scheme is not determined only by its points over fields. It also remembers how it behaves over rings containing nilpotent elements.

Testing only ordinary fields is like testing a three-dimensional object only through a shadow that removes one direction. The shadow can be accurate for what it shows and still omit a structural feature.

The paper's central lesson is:

> To answer a universal question about commutativity or the center, one must inspect the complete functor of points, including nonreduced test rings—not only ordinary field-valued points.

## What is classified

The paper claims complete formulas for strict graded Gerstenhaber endomorphisms of two explicit algebras.

For the even object, every endomorphism is represented by three coefficients:

```text
(lambda, delta, eta)
```

satisfying:

```text
eta² = 0
lambda(delta - 1) = 0.
```

For the odd object, the paper derives a diagonal normal form with its own coefficient equations and a commutative composition law.

From those classifications, the manuscript derives:

- representing affine monoid schemes;
- the common crossing core;
- connected components;
- units and idempotents;
- scheme-theoretic centers;
- commutator and derived-subgroup behavior;
- reduced geometry and normalization;
- finite-field point counts and zeta functions.

## What Lean has verified

A public hosted Lean build verifies a bounded central kernel:

- the crossing multiplication laws;
- the square-zero skew multiplication laws;
- the exact formula measuring noncommutativity;
- the equivalence between commutativity and zero defect;
- sufficient center equations;
- the affine commutator formula.

A second Lean file encodes the principal even and odd coefficient classifications and their composition laws. Its first hosted run exposed a proof-engineering failure in one extensionality lemma. That failure was preserved, the proof was repaired explicitly, and a new immutable run is required before this expanded scope can be called proof-assistant verified.

## What remains open

The following are not yet externally settled:

- whether every manuscript proof is correct;
- whether a known general theorem already contains the classification;
- whether the historical novelty boundary is accurate;
- whether the complete generator-to-global Gerstenhaber-preservation argument is formalized;
- whether the paper will be accepted for publication.

## Why publish the package before those questions are closed?

A clean review package lets specialists answer those questions against exact source and evidence. The purpose is not to declare victory. The purpose is to make the claim falsifiable, reproducible, and reviewable.
