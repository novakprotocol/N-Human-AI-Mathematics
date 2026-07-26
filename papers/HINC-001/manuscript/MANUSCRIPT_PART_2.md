## 4. The odd endomorphism monoid

The relevant homogeneous pieces are

\[
O_0=R\,1\oplus R\,\epsilon,
\quad
O_1=R\,a,
\quad
O_2=R\,b\oplus R\,\epsilon b,
\quad
O_3=R\,c\oplus R\,\epsilon c.
\]

A general unital graded map begins as

\[
\begin{aligned}
\phi(\epsilon)&=x+\lambda\epsilon,\\
\phi(a)&=\mu a,\\
\phi(b)&=p b+q\epsilon b,\\
\phi(c)&=\rho c+\sigma\epsilon c.
\end{aligned}
\]

No coefficient is assumed invertible.

### Lemma 4.1 -- bracket equations

Preserving the generator bracket table yields

\[
x=0,
\qquad
\lambda(\mu-1)=0,
\qquad
\rho(\mu-1)=0,
\qquad
\sigma=0,
\]

and

\[
p=\lambda\rho,
\qquad
q=0.
\]

#### Proof

From `[a,\epsilon]=\epsilon`,

\[
[\mu a,x+\lambda\epsilon]
=\mu\lambda\epsilon
=x+\lambda\epsilon,
\]

so `x=0` and `\lambda(\mu-1)=0`.

From `[a,c]=c`,

\[
[\mu a,\rho c+\sigma\epsilon c]
=\mu\rho c
=\rho c+\sigma\epsilon c,
\]

so `\rho(\mu-1)=0` and `\sigma=0`.

Finally, `[c,\epsilon]=b` gives

\[
[\rho c,\lambda\epsilon]
=\lambda\rho b
=p b+q\epsilon b,
\]

and hence `p=\lambda\rho`, `q=0`.  The remaining generator brackets are then automatic. QED.

### Lemma 4.2 -- algebra equations

After Lemma 3.1, the defining algebra relations are equivalent to

\[
\rho=\lambda p^2.
\]

#### Proof

The only remaining nonautomatic relation is `ac=\epsilon b^2`:

\[
\phi(a)\phi(c)=\mu\rho\,\epsilon u^4,
\qquad
\phi(\epsilon)\phi(b)^2
=\lambda p^2\,\epsilon u^4.
\]

By Lemma 3.1, `\rho(\mu-1)=0`, so `\mu\rho=\rho`; hence the relation is precisely `\rho=\lambda p^2`.

The relation `ab=\epsilon c` becomes `\mu p=\lambda\rho`; this follows from `p=\lambda\rho` and `\lambda(\mu-1)=0`.  The relation `c^2=b^3` follows because

\[
\rho=\lambda p^2
\quad\Longrightarrow\quad
\rho^2=\lambda^2p^4,
\]

while

\[
p=\lambda\rho
\quad\Longrightarrow\quad
p^3=\lambda^3\rho^3;
\]

more directly, substituting `p=\lambda\rho` into `\rho=\lambda p^2` gives
`\rho=\lambda^3\rho^2`, and multiplying by `\rho` yields
`\rho^2=\lambda^3\rho^3=p^3`. QED.

### Theorem 4.3 -- complete odd endomorphism functor

For every commutative `F`-algebra `R`, `\mathcal O(R)` consists exactly of the diagonal maps

\[
\epsilon\mapsto\lambda\epsilon,
\qquad
a\mapsto\mu a,
\qquad b\mapsto p b,
\qquad c\mapsto\rho c,
\]

such that

\[
p=\lambda\rho,
\qquad
\rho=\lambda p^2,
\qquad
\lambda(\mu-1)=0,
\qquad
\rho(\mu-1)=0.
\]

Composition is coordinatewise:

\[
(\lambda,\mu,p,\rho)
(\lambda',\mu',p',\rho')
=
(\lambda\lambda',\mu\mu',pp',\rho\rho').
\]

#### Proof

Necessity is Lemmas 3.1 and 3.2.  Conversely, the displayed equations preserve every defining algebra relation and the complete generator bracket table.  Coordinatewise composition follows from diagonality, and the equations are stable under that composition. QED.

### Corollary 4.4 -- coordinate bialgebra

The odd endomorphism functor is represented by

\[
M_O=\operatorname{Spec}A_O,
\]

where

\[
A_O=
\frac{F[\lambda,\mu,p,\rho]}
{(p-\lambda\rho,
\rho-\lambda p^2,
\lambda(\mu-1),
\rho(\mu-1))}.
\]

All four coordinates are group-like for the monoid comultiplication:

\[
\Delta(x)=x\otimes x
\quad
(x\in\{\lambda,\mu,p,\rho\}),
\]

and the counit takes each coordinate to `1`.

Eliminating `p` gives

\[
A_O\cong
\frac{F[\lambda,\mu,\rho]}
{(\lambda(\mu-1),
\rho(\mu-1),
\rho(1-\lambda^3\rho))}.
\]

## 5. The odd clopen split

Define

\[
z=\lambda^3\rho\in A_O.
\]

### Lemma 5.1

The element `z` is a group-like idempotent:

\[
z^2=z,
\qquad
\Delta(z)=z\otimes z,
\qquad
\varepsilon(z)=1.
\]

#### Proof

The eliminated relation `\rho=\lambda^3\rho^2` gives

\[
\lambda^3\rho=\lambda^6\rho^2,
\]

which is `z=z^2`.  Group-likeness follows because both `\lambda` and `\rho` are group-like. QED.

### Theorem 5.2 -- clopen decomposition

There is a canonical decomposition of affine monoid schemes

\[
M_O\cong G\sqcup C,
\]

where

\[
G=V(z-1)\cong\mathbf G_m
\]

and

\[
C=V(z)
\cong
\operatorname{Spec}F[\lambda,\mu]/(\lambda(\mu-1)).
\]

The component `G` is exactly the unit group of `M_O`.  The component `C` is a clopen two-sided ideal.

#### Proof

An idempotent in a commutative ring splits its spectrum, so

\[
A_O\cong A_O/(z)\times A_O/(z-1).
\]

On `z=0`, the relation

\[
\rho(1-z)=0
\]

forces `\rho=0`, and then `p=\lambda\rho=0`.  The only remaining equation is `\lambda(\mu-1)=0`, yielding `C`.

On `z=1`, `\lambda` and `\rho` are units.  Hence `\mu=1`, and with `t=\lambda^{-1}` one obtains

\[
\lambda=t^{-1},
\qquad p=t^2,
\qquad \rho=t^3.
\]

Thus the component is `\mathbf G_m` and consists of the previously classified automorphisms.

Since `z(xy)=z(x)z(y)`, multiplying by a point of `C` keeps the product in `C`; hence `C` is a two-sided ideal. QED.

### Proposition 5.3 -- the collapse component has a local identity

The point

\[
e=(\lambda,\mu,p,\rho)=(1,1,0,0)
\]

is a central idempotent and is the identity element of the monoid `C`.  Therefore `C` is a unital monoid scheme in its own right.

#### Proof

Composition on `M_O` is coordinatewise.  For a point of `C`, the last two coordinates vanish, so multiplying by `e` fixes all four coordinates.  The whole monoid is commutative, hence `e` is central. QED.

### Corollary 5.4 -- reducedness and connected components

The monoid `M_O` is reduced and commutative.  It has two connected components:

1. the irreducible torus `G\cong\mathbf G_m`;
2. the connected crossing `C`, which has two irreducible affine-line components.

#### Proof

The coordinate ring of `G` is a Laurent polynomial ring.  In the polynomial ring `F[\lambda,\mu]`,

\[
(\lambda(\mu-1))
=(\lambda)\cap(\mu-1),
\]

an intersection of two prime ideals.  Hence the coordinate ring of `C` is reduced.  The coordinatewise monoid law is commutative.  The two affine lines of `C` meet at `(0,1)`, so `C` is connected. QED.

## 6. One crossing core and two parity modifications

Put

\[
C=\operatorname{Spec}A_C,
\qquad
A_C=F[x,y]/(x(y-1)),
\]

with coordinatewise multiplication

\[
(x,y)(x',y')=(xx',yy').
\]

The defining equation is stable because

\[
xx'(yy'-1)=xx'\bigl(y(y'-1)+(y-1)\bigr)=0.
\]

The identity is `(1,1)` and the unit group is

\[
G=D(x)=V(y-1)\cap D(x)\cong\mathbf G_m.
\]

Geometrically, `C` is two affine lines meeting at `(0,1)`.

### Theorem 6.1 - even parity is a bilateral square-zero skew extension

There is an isomorphism of schemes

\[
M_E\cong C\times\alpha_2.
\]

Under this identification, multiplication is

\[
(x,y,e)(x',y',e')
=(xx',yy',xe'+y'e).
\]

Equivalently, the nilpotent coordinate is skew primitive:

\[
\Delta(e)=x\otimes e+e\otimes y.
\]

#### Proof

The coordinate algebra of `M_E` is

\[
A_C[e]/(e^2)=A_C\otimes_F F[e]/(e^2),
\]

which gives the scheme product. The composition formula from Theorem 3.3 gives the displayed multiplication. Associativity follows from

\[
(xx')e''+y''(xe'+y'e)
=xx'e''+xy''e'+y'y''e
\]

and

\[
x(x'e''+y''e')+(y'y'')e
=xx'e''+xy''e'+y'y''e.
\]

The same identity is coassociativity of the displayed coproduct. QED.

The multiplication is not the direct-product law on `C x alpha_2`: the square-zero direction has unequal left and right weights. The commutativity defect is

\[
\Omega((x,y,e),(x',y',e'))
=(x+y)e'+(x'+y')e.
\]

The matrix model

\[
(x,y,e)\longmapsto
\begin{pmatrix}x&e\\0&y\end{pmatrix}
\]

makes the skew multiplication immediate.

### Theorem 6.2 - odd parity is unit doubling

Let `G_new` be a second copy of `G`. Define

\[
\operatorname{Dbl}_G(C)=G_{\mathrm{new}}\sqcup C
\]

with the group law on `G_new`, the original monoid law on `C`, and cross action

\[
u\cdot(x,y)=(ux,y).
\]

Then

\[
M_O\cong\operatorname{Dbl}_G(C).
\]

#### Proof

The group-like idempotent in Theorem 5.2 splits `M_O` into the global unit component and the collapse component. The latter is `C`. A global unit with parameter `u` acts on a collapse point by multiplying its `x`-coordinate by `u` and leaving `y` fixed, which is precisely multiplication by the original unit `(u,1)` in `C`. These componentwise rules agree with the definition of `Dbl_G(C)`. QED.

There is a unital collapse morphism

\[
q:M_O\longrightarrow C
\]

that is the identity on the core and identifies `G_new` with the original unit subgroup. The inclusion `C\to M_O` is a section as a semigroup scheme, but not as a unital monoid scheme: the identity of `C` becomes only a local identity inside the clopen ideal.

### Unified parity statement

\[
\boxed{\text{even = common crossing + infinitesimal skew thickening}}
\]

\[
\boxed{\text{odd = common crossing + discrete clopen unit doubling}}
\]

| property | even | odd |
|---|---|---|
| connected | yes | no |
| reduced | no | yes |
| commutative | no | yes |
| role of `C` | reduction | clopen two-sided ideal |
| extra state | `alpha_2` direction | new `G_m` component |
