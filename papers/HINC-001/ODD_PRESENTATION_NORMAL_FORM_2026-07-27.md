# Odd-Algebra Presentation and Normal Form

## Status

```text
object:                    O = D + F epsilon u + u^2 D[u]
base field:                characteristic two
presentation proof:        supplied below
computational checks:      previously passed
Lean formalization:        pending
external specialist audit: pending
```

## 1. Claimed presentation

Let

```text
D = F[epsilon]/(epsilon^2),
a = epsilon u,
b = u^2,
c = u^3.
```

The odd algebra is

```text
O = D + F epsilon u + u^2 D[u]
```

inside `D[u]`.

The proposed abstract presentation has generators

```text
epsilon, a, b, c
```

and relations

```text
epsilon^2 = 0,
epsilon a = 0,
a^2 = 0,
ab = epsilon c,
ac = epsilon b^2,
c^2 = b^3.
```

## 2. Spanning normal form

Using `c^2=b^3`, every polynomial in `b,c` reduces to

```text
f(b) + c g(b).
```

Multiplication by `epsilon` gives

```text
epsilon h(b) + epsilon c k(b).
```

Any word containing `a` reduces as follows:

- `epsilon a=0` and `a^2=0` remove words containing `epsilon a` or two copies of `a`;
- for `m>=1`,

```text
a b^m = epsilon c b^(m-1);
```

- for `m>=0`,

```text
a c b^m = epsilon b^(m+2).
```

Therefore every element has a representative of the form

```text
f(b) + c g(b) + epsilon h(b) + epsilon c k(b) + tau a,
```

where `f,g,h,k in F[b]` and `tau in F`.

## 3. Linear independence after mapping into `D[u]`

Under the proposed map,

```text
b^m             -> u^(2m),
c b^m           -> u^(2m+3),
epsilon b^m     -> epsilon u^(2m),
epsilon c b^m   -> epsilon u^(2m+3),
a                 -> epsilon u.
```

These monomials are pairwise distinct members of the standard `F`-basis

```text
{u^n, epsilon u^n : n>=0}
```

of `D[u]`.

They are exactly the basis elements belonging to

```text
D + F epsilon u + u^2 D[u]:
```

- degree zero contributes `1,epsilon`;
- degree one contributes only `epsilon u`;
- every degree at least two contributes `u^n` and `epsilon u^n`.

Hence the spanning normal form is unique. The proposed relations generate the full kernel, and the presentation is complete.

## 4. Consequence for HINC-001

A homogeneous generator assignment that satisfies these algebra relations defines a unique graded algebra endomorphism of `O`.

Combined with the generator-to-global bracket lemma and the complete generator bracket table, this supplies the missing human proof that the normalized odd coefficient data determine global **binary Gerstenhaber endomorphisms**.

## 5. Remaining boundary

The proof above should still be:

- checked by an external algebra specialist;
- formalized in Lean alongside the presented algebra;
- incorporated into the consolidated manuscript rather than left only as an addendum.
