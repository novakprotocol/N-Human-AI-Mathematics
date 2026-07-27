# Characteristic-Two Hochschild Foundation for HINC-001

## Status

```text
purpose:                     self-contained foundation for the ambient ring and bracket
base field:                  arbitrary field F of characteristic two
algebra:                     D = F[epsilon]/(epsilon^2)
structure proved here:       cup product and binary Gerstenhaber bracket
restricted/BV/E2 structure: not classified here
external specialist review: pending
```

This note removes an avoidable foundational dependency from HINC-001. It derives the exact Hochschild ring and bracket convention used by the paper from normalized Hochschild cochains.

## 1. Normalized cochains

Write

```text
D = F 1 + F epsilon,
epsilon^2 = 0,
bar D = D / F 1 = F epsilon.
```

For every `n >= 0`, the normalized Hochschild cochains are

```text
C^n(D,D) = Hom_F((bar D)^(tensor n), D).
```

Since `bar D` is one-dimensional, evaluation on

```text
epsilon tensor ... tensor epsilon
```

identifies `C^n(D,D)` with `D`. For `x in D`, let `c_{n,x}` denote the normalized cochain satisfying

```text
c_{n,x}(epsilon,...,epsilon) = x.
```

For `n=0`, this is simply the element `x in D`.

## 2. The differential vanishes

Evaluate the Hochschild differential of `c_{n,x}` on `n+1` copies of `epsilon`.

Every interior term contains a product `epsilon^2` and is zero. The two boundary terms are

```text
epsilon x + x epsilon = 2 epsilon x = 0
```

because `D` is commutative and `char F = 2`.

Therefore the normalized Hochschild differential is identically zero. Hence

```text
HH^n(D,D) = C^n(D,D) = D
```

in every degree.

## 3. Cup product

For normalized cochains,

```text
(c_{i,x} cup c_{j,y})(epsilon,...,epsilon) = xy.
```

Let `u = [c_{1,1}]`. Then

```text
[c_{n,x}] = x u^n,
```

and cup product gives an isomorphism of graded `F`-algebras

```text
HH^*(D,D) = D[u],
|epsilon| = 0,
|u| = 1.
```

Because the base characteristic is two, graded commutativity does not force `u^2` to vanish.

## 4. Circle products

Write an element `y in D` uniquely as

```text
y = y_0 + y_1 epsilon.
```

Define the `F`-derivation

```text
partial(1) = 0,
partial(epsilon) = 1.
```

Thus `partial(y) = y_1`.

Consider insertion of `c_{j,y}` into `c_{i,x}`. A normalized cochain vanishes when any input is the scalar unit. Therefore, when the output `y_0 + y_1 epsilon` is inserted, only the `epsilon` part survives. Each admissible insertion contributes

```text
x partial(y).
```

There are `i` insertion positions. All Koszul signs become `+1` in characteristic two. Hence

```text
c_{i,x} circle c_{j,y}
  = i x partial(y) c_{i+j-1,1}.
```

Interchanging the cochains gives

```text
c_{j,y} circle c_{i,x}
  = j y partial(x) c_{i+j-1,1}.
```

## 5. Gerstenhaber bracket

The Gerstenhaber bracket is the graded commutator of the circle product. In characteristic two, subtraction and the sign factor both reduce to addition. Therefore

```text
[x u^i, y u^j]
  = (i x partial(y) + j y partial(x)) u^(i+j-1),
```

where the integers `i` and `j` act through their parity in `F`.

This is exactly the bracket used throughout HINC-001.

## 6. Immediate generator checks

For the even generators

```text
r = u,
s = epsilon u,
```

one obtains

```text
s^2 = 0,
[r,s] = r,
[r,r] = [s,s] = 0.
```

For the odd generators

```text
a = epsilon u,
b = u^2,
c = u^3,
```

one obtains

```text
[a,epsilon] = epsilon,
[c,epsilon] = b,
[a,c] = c,
[a,b] = 0,
[b,c] = 0,
```

with the remaining generator brackets determined by characteristic-two graded symmetry and the displayed formula.

## 7. Scope boundary

This derivation proves the graded-commutative cup product and the binary degree-minus-one Gerstenhaber bracket used by HINC-001.

It does **not** claim that the classified endomorphisms preserve:

- a Batalin–Vilkovisky operator;
- a restricted `p`-power operation;
- a Gerstenhaber squaring operation beyond the binary bracket;
- the brace algebra on cochains;
- the full `E_2` or `B_infinity` structure.

The revised manuscript must call its maps **binary Gerstenhaber endomorphisms** or give an equivalent explicit definition.

## 8. External-source boundary

Published work establishes the broader Hochschild ring, Gerstenhaber, BV, and positive-characteristic restricted-operation frameworks. This note is included because the exact dual-number, characteristic-two formula is short enough to prove directly and should not be hidden behind a citation whose hypotheses or conventions differ.
