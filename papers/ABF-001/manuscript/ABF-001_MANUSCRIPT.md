# Affine Restriction Moment Kernels and Radical Incidence Geometry of a Vectorial Boolean Map

## A punctured 9-flat, bidual moment fibers, and an almost-disjoint binary symmetric matrix pencil

**Paper ID:** ABF-001
**Author:** Matthew S. Novak
**Research mode:** human-led, LLM-assisted
**Release:** candidate manuscript for public technical review
**Date:** 28 July 2026

## Abstract

Let $F:\mathbb F_2^n\to\mathbb F_2^m$ be a vectorial Boolean function, let $H_q$ be an affine hyperplane, and let $v\ne0$ be an output mask. Write $g_{v,q}$ for the restriction of $v\cdot F$ to $H_q$. We give a self-contained moment-kernel certificate for its algebraic degree. If $U_r(q)$ denotes the span of the vector moments of orders at most $r$, then

$$
\deg g_{v,q}\le n-r-2
\quad\Longleftrightarrow\quad
v\in U_r(q)^\perp.
$$

The same equations, viewed in the affine-hyperplane parameter $q$, form a linear kernel. This yields two fibers of one incidence relation: an annihilator fiber in output-mask space and a kernel fiber in affine-parameter space. The order-zero case gives an explicit top-layer signature and a punctured-kernel theorem. The order-one case gives a symmetric $17\times17$ binary moment matrix for each scalar projection.

We apply the certificate to a fully specified reduced map $F:\mathbb F_2^{16}\to\mathbb F_2^8$. Among all 131,070 affine hyperplanes, exactly 130,559 vectorial restrictions have degree 15 and exactly 511 have degree 14; none has lower degree. The 511 exceptional parameters are the nonzero points of a 9-dimensional kernel. For the 255 nonzero scalar masks, the order-one matrices have ranks 13, 14, 15, 16, and 17 with multiplicities 2, 15, 74, 112, and 52. The 203 singular masks yield 469 nonzero radical incidences on 467 affine parameters. After identifying one duplicated one-dimensional radical, there are 202 distinct nonzero radical subspaces. The mask-intersection graph is $K_3\sqcup200K_1$, while the mask-parameter incidence graph is a forest with 201 components: 200 stars and one ten-vertex tree.

A fresh NumPy implementation and a separately written integer/bitset implementation reproduce the truth-table identity, the vectorial restriction spectrum, the rank histogram, the 469-edge atlas, the unique triple-covered parameter, and the corrected 202-subspace count. The final release also records a completed standalone exhaustive control over all 65,536 maps $\mathbb F_2^3\to\mathbb F_2^2$: 5,505,024 direct degree-versus-moment comparisons, with zero mismatches. Historical evidence additionally records a byte-identical C reconstruction. This is a methods-and-instance contribution. It is not a claim of a full-width cryptographic weakness, global historical priority, peer review, or complete proof-assistant verification.

## 1. Scope

The paper has two layers.

1. **General method.** A Reed-Muller duality argument converts affine-restriction degree thresholds into moment vanishing, then into output annihilators and affine-parameter kernels.
2. **Exact finite instance.** The complete restriction and radical geometry of a specified 16-to-8 map is classified and independently reproduced.

The finite map is the one-bit reduced block-to-fixed-state map used in the N-MathLab black-box research lane. Its truth table consists of 65,536 output bytes with SHA-256 identity

```text
2a861e09dcb5b00e208ede53e1b29615a5309389a83da40f81d663ec760e7e52
```

No claim is made about collision resistance, preimage resistance, authentication, keys, or security of a full-width standardized construction.

### 1.1 Consolidation rule

ABF-001 consolidates the earlier affine-hyperplane spectrum result and the later bidual radical-incidence analysis. The earlier v30 theorem remains provenance; it is not a separate simultaneous submission. This avoids splitting one mathematical development into overlapping papers.

### 1.2 Principal contributions

- a self-contained moment-kernel theorem for scalar restrictions of vectorial Boolean functions;
- the two-sided incidence interpretation $v\in U_r(q)^\perp\Longleftrightarrow q\in\ker\Phi_{r,v}$;
- an explicit order-zero affine signature and punctured-kernel formula;
- an order-one symmetric moment pencil;
- the exact 130,559 / 511 / 0 vectorial hyperplane spectrum;
- the exact five-profile scalar restriction census;
- the rank distribution $13^2,14^{15},15^{74},16^{112},17^{52}$ for the 255 nonzero pencil members;
- a corrected distinction between 203 singular mask-indexed radicals and 202 distinct radical subspaces;
- a complete 469-edge, 201-component incidence forest;
- fresh independent computational reproduction and fail-closed evidence identities.

## 2. Preliminaries

### 2.1 Boolean functions and algebraic degree

A scalar Boolean function on $d$ variables is represented uniquely by its algebraic normal form

$$
g(y)=\bigoplus_{I\subseteq[d]} a_I\prod_{i\in I}y_i.
$$

Its algebraic degree is the maximum $|I|$ for which $a_I=1$. A vectorial Boolean function $F:\mathbb F_2^n\to\mathbb F_2^m$ has scalar components

$$
f_v(x)=v\cdot F(x),\qquad 0\ne v\in\mathbb F_2^m.
$$

The degree of $F$ is the maximum degree of its nonzero scalar components. We use the standard extended conventions $\deg(0)=-\infty$, $\operatorname{RM}(s,d)=\{0\}$ for $s<0$, and $\operatorname{RM}(s,d)$ equal to the full Boolean function space for $s\ge d$. Under these conventions, the Reed-Muller duality statement below and the moment criterion remain valid for every $r\ge0$.

### 2.2 Affine-hyperplane parameters

Write

$$
q=(\beta,a)\in\mathbb F_2^{n+1},
$$

where $a\in\mathbb F_2^n$. Define

$$
h_q(x)=\beta\oplus a\cdot x.
$$

When $a\ne0$, $h_q$ is the indicator of the affine hyperplane

$$
H_q=\{x:a\cdot x=\beta\oplus1\}.
$$

The zero parameter represents the empty set. The parameter $(1,0)$ represents the whole domain and is not a hyperplane.

### 2.3 Vector moments

For $J\subseteq[n]$, put $x_J=\prod_{j\in J}x_j$ and define

$$
\mu_J(q)=\bigoplus_{x\in\mathbb F_2^n}x_JF(x)h_q(x)\in\mathbb F_2^m.
$$

For $r\ge0$, define the vector-moment span

$$
U_r(q)=\operatorname{span}\{\mu_J(q):|J|\le r\}.
$$

For fixed $v\ne0$, define the scalar moment map

$$
\Phi_{r,v}(q)=\big(v\cdot\mu_J(q)\big)_{|J|\le r}.
$$

Because $h_q(x)$ is linear in $q$, every $\mu_J(q)$ and every $\Phi_{r,v}(q)$ is linear in $q$.

## 3. Moment-kernel theorem

Let $H_q$ have dimension $d=n-1$. Choose any affine identification $H_q\cong\mathbb F_2^d$. The scalar restriction $g_{v,q}$ is a Boolean function on $d$ variables.

### Theorem 1. Moment criterion

For every $r\ge0$,

$$
\deg(g)\le d-r-1
$$

if and only if

$$
\bigoplus_{y\in\mathbb F_2^d}y_Ig(y)=0
\qquad\text{for every }|I|\le r.
$$

#### Proof

The Boolean functions of degree at most $s$ form the Reed-Muller code $\operatorname{RM}(s,d)$. Under the standard dot product on truth tables,

$$
\operatorname{RM}(r,d)^\perp=\operatorname{RM}(d-r-1,d).
$$

The monomials $y_I$ with $|I|\le r$ span $\operatorname{RM}(r,d)$. Therefore $g$ has degree at most $d-r-1$ exactly when its truth table is orthogonal to every such monomial. The displayed XOR sums are those inner products. $\square$

### Theorem 2. Bidual moment incidence

For every valid affine hyperplane $H_q$, every nonzero output mask $v$, and every $r\ge0$,

$$
\deg g_{v,q}\le n-r-2
\quad\Longleftrightarrow\quad
v\in U_r(q)^\perp
\quad\Longleftrightarrow\quad
q\in\ker\Phi_{r,v}.
$$

#### Proof

The restrictions to $H_q$ of the ambient affine coordinate functions $1,x_1,\dots,x_n$ span the affine functions on $H_q$. Their products of degree at most $r$ span $\operatorname{RM}(r,n-1)$. The scalar moments $v\cdot\mu_J(q)$ are therefore precisely the inner products in Theorem 1. Their simultaneous vanishing says that $v$ annihilates the span $U_r(q)$. Viewed as equations in $q$, the same vanishing says that $q$ lies in the kernel of $\Phi_{r,v}$. $\square$

### Corollary 3. Fiber count

Let $\rho_r(q)=\dim U_r(q)$. The number of nonzero scalar components satisfying the degree bound on $H_q$ is

$$
2^{m-\rho_r(q)}-1.
$$

### Corollary 4. Double counting

Let $\mathcal Q$ be the valid affine-hyperplane parameters. Then

$$
\sum_{q\in\mathcal Q}\big(2^{m-\rho_r(q)}-1\big)
=
\sum_{v\ne0}|\ker\Phi_{r,v}\cap\mathcal Q|.
$$

Both sides count the same incidence set.

## 4. The order-zero signature and punctured kernel

Assume $F$ has maximum degree $n$. Write its vectorial ANF as

$$
F(x)=\bigoplus_{I\subseteq[n]}c_Ix_I,
$$

with nonzero full coefficient $c=c_{[n]}$. Let $c_j$ be the coefficient of the degree-$(n-1)$ monomial missing $x_j$, and put $m_j=c_j\oplus c$. Define

$$
M(a)=\bigoplus_{j=1}^na_jm_j.
$$

### Theorem 5. Affine top-layer signature

For the hyperplane $a\cdot x=b$,

$$
R(a,b)=M(a)\oplus(b\oplus1)c
$$

is the degree-$(n-1)$ coefficient of the vectorial restriction. Equivalently,

$$
R(a,b)=\bigoplus_{x:a\cdot x=b}F(x).
$$

Thus the restriction has degree at most $n-2$ exactly when $R(a,b)=0$.

#### Proof

The hyperplane indicator is $1\oplus a\cdot x\oplus b$. The XOR of $F$ over the full domain is $c$. Multiplication by $x_j$ merges the degree-$n$ monomial with the degree-$(n-1)$ monomial missing $x_j$, giving $m_j$. Expanding the indicator gives the formula. $\square$

### Corollary 6. Punctured kernel

In translated coordinates $q=(a,\beta)$ with $\beta=b\oplus1$, define

$$
N(a,\beta)=M(a)\oplus\beta c.
$$

The valid hyperplanes whose restrictions have degree at most $n-2$ are exactly the nonzero vectors $q$ satisfying

$$
N(q)=0,\qquad q\ne0.
$$

If $\operatorname{rank}N=s$, their number is $2^{n+1-s}-1$.

## 5. The order-one symmetric moment pencil

Let

$$
z(x)=(1,x_1,\dots,x_n)^T.
$$

For each nonzero output mask $v$, define the $(n+1)\times(n+1)$ matrix

$$
B_v=\bigoplus_x (v\cdot F(x))z(x)z(x)^T.
$$

The matrix is symmetric. For every affine parameter $q$,

$$
\Phi_{1,v}(q)=B_vq.
$$

Consequently, valid hyperplanes on which $v\cdot F$ has degree at most $n-3$ are exactly the nonzero valid points in $\ker B_v$.

## 6. The specified 16-to-8 map

For the finite benchmark,

$$
n=16,\qquad m=8.
$$

The full degree-16 coefficient is

```text
f3
```

and the sixteen degree-15 coefficients are

```text
47 c3 5c f4 20 97 6c 33 4c d2 d2 7d 89 3e bb 10
```

The augmented signature matrix has rank 8, so its kernel has dimension 9.

## 7. Complete vectorial restriction spectrum

### Theorem 7

Among all

$$
2(2^{16}-1)=131{,}070
$$

valid affine hyperplanes,

| Restricted vectorial degree | Hyperplanes |
|---:|---:|
| 15 | 130,559 |
| 14 | 511 |
| 13 or lower | 0 |

The 511 degree-14 hyperplanes are the nonzero points of a 9-dimensional kernel. They split into 256 linear hyperplanes and 255 non-linear affine hyperplanes.

## 8. Scalar moment profiles

For each hyperplane, put $\rho_r(q)=\dim U_r(q)$ for $r=0,1,2$. Exactly five triples $(\rho_0,\rho_1,\rho_2)$ occur.

| Profile | Hyperplanes | Degree-15 masks | Degree-14 masks | Degree-13 masks |
|---|---:|---:|---:|---:|
| $(0,7,8)$ | 3 | 0 | 254 | 1 |
| $(0,8,8)$ | 508 | 0 | 255 | 0 |
| $(1,6,8)$ | 1 | 128 | 124 | 3 |
| $(1,7,8)$ | 463 | 128 | 126 | 1 |
| $(1,8,8)$ | 130,095 | 128 | 127 | 0 |

No valid hyperplane admits a nonzero scalar projection of degree 12 or below. Summing the fibers gives

| Scalar restricted degree | Pairs $(v,q)$ |
|---:|---:|
| 15 | 16,711,552 |
| 14 | 16,710,829 |
| 13 | 469 |
| 12 or below | 0 |

## 9. Rank spectrum of the symmetric pencil

For the 255 nonzero output masks, the matrices $B_v$ have the following ranks.

| Rank | Matrices | Radical dimension | Nonzero radical points per matrix |
|---:|---:|---:|---:|
| 13 | 2 | 4 | 15 |
| 14 | 15 | 3 | 7 |
| 15 | 74 | 2 | 3 |
| 16 | 112 | 1 | 1 |
| 17 | 52 | 0 | 0 |

Thus 203 masks give singular matrices, and the total number of mask-indexed nonzero radical incidences is

$$
2\cdot15+15\cdot7+74\cdot3+112\cdot1=469.
$$

## 10. Corrected radical geometry

The earlier v32 wording described 203 nonzero radical subspaces. The exact computation distinguishes two counts:

- **203 singular output masks**, each with a mask-indexed radical;
- **202 distinct nonzero radical subspaces**, because masks `8a` and `9b` have the same one-dimensional radical.

This correction changes no incidence edge, rank, hyperplane profile, degree count, or forest component. It only removes an ambiguity between an indexed family and its set of distinct members.

### Theorem 8. Almost-disjoint arrangement

The 203 mask-indexed radicals contain 469 nonzero point incidences but cover 467 distinct affine parameters. There is one multiply covered parameter,

```text
q* = 119d5
normal = 8cea
hyperplane offset = 0
```

and its annihilator line has nonzero masks

```text
11 8a 9b
```

The radicals for `8a` and `9b` are the same one-dimensional subspace generated by $q^*$. This subspace lies in the higher-dimensional radical for mask `11`. After identifying the duplicate line, the 202 distinct radicals have exactly one nontrivial containment; every other pair of distinct radicals intersects only at zero.

The graph on the 203 singular masks, joining two masks when their radicals meet nontrivially, is

$$
K_3\sqcup200K_1.
$$

## 11. Incidence forest

Form the bipartite graph with singular output masks on the left, covered nonzero affine parameters on the right, and radical incidences as edges. It has

```text
203 left vertices
467 right vertices
469 edges
201 connected components
```

Every component is a tree. The component census is

| Component | Count |
|---|---:|
| $K_{1,15}$ | 2 |
| $K_{1,7}$ | 14 |
| $K_{1,3}$ | 74 |
| $K_{1,1}$ | 110 |
| Exceptional ten-vertex tree | 1 |

The exceptional component consists of masks `11`, `8a`, and `9b`; the shared parameter `119d5`; and six additional leaves incident only to mask `11`.

## 12. Verification

### 12.1 Fresh primary implementation

The fresh standalone NumPy verifier included with this release reconstructs the truth table and reproduces:

- truth-table SHA-256 `2a861e09...e7e52`;
- vector spectrum `130559 / 511 / 0`;
- signature rank 8 and augmented kernel dimension 9;
- rank histogram `2,15,74,112,52`;
- 469 mask-first and hyperplane-first edges;
- edge-atlas SHA-256 `95d64917...742fa`;
- five hyperplane profiles;
- 201 forest components;
- 203 mask-indexed radicals and 202 distinct radical subspaces;
- the unique duplicate line for `8a` and `9b`.

Six focused tests pass. The fresh evidence identity is

```text
ebf4d164512339f4cf3fb14d22b7ba98253ad0726f4b5258ef5f52b2d17e34a9
```

### 12.2 Separately written bitset implementation

A second implementation uses Python integer bitsets and the standard library only. It does not import the NumPy verifier. It independently reproduces the truth-table hash, signature rank, 511 exceptions, rank histogram, 469-edge atlas, 467 covered parameters, 203 mask-indexed radicals, 202 distinct subspaces, and the unique `119d5` triple point. Its evidence identity is

```text
c47b5a4b3e7c12e2c42da27ce0d2da440adfcce1ae82906d862e2eaf9904c96b
```

### 12.3 Complete small-universe control and historical native route

The final package contains a standalone direct restriction-ANF versus ambient-moment verifier. It exhaustively processes all 65,536 functions $\mathbb F_2^3\to\mathbb F_2^2$, all 14 affine hyperplanes, all three nonzero output masks, and moment orders zero and one. This gives 5,505,024 exact comparisons and zero mismatches.

The N-MathLab record additionally contains:

- a separately written C reconstruction;
- byte-identical Python/C edge CSVs with SHA-256 `95d64917...742fa`;
- a one-bit truth-table tamper that changes the rank distribution and is rejected.

These are internal project reproductions, not external institutional validation.

## 13. Prior-art boundary

Several surrounding frameworks are established.

1. Algebraic-degree stability under affine restrictions is an active theory for Boolean and vectorial Boolean functions.
2. Affine-hyperplane restrictions and output projections are used in trim spectra and APN classification.
3. Reed-Muller duality, affine-space sums, and subcodes provide a general language for moment vanishing.
4. Linear spaces of symmetric bilinear forms, rank distributions, radicals, and partial-spread phenomena are established subjects.

ABF-001 does not claim to invent those subjects. Its defensible candidate contribution is their explicit integration into a two-sided affine moment certificate together with the complete, reproducible finite geometry of the specified map.

A systematic search to the declared 28 July 2026 scope covered arXiv, publisher/DOI metadata, IACR ePrint discovery surfaces, HAL, Zenodo, books, theses, public repositories, and public mathematical-index surfaces. The closest work treats affine-restriction degree stability, vectorial trims, affine-subspace sums and Reed-Muller subcodes, or rank/radical geometry of bilinear-form spaces. No exact indexed match was located for the combined numerical packet: the truth-table identity, punctured 9-flat, rank histogram, five moment profiles, unique parameter `119d5`, corrected 202-subspace arrangement, and 201-component forest. Search absence does not establish worldwide priority.

## 14. Usefulness

The method can be used to:

- replace exhaustive restriction-ANF calculations with small linear maps;
- compute exact affine restriction spectra;
- classify which scalar projections collapse on each affine relation;
- construct affine-equivalence fingerprints;
- screen reduced cryptographic components for degree loss under guessed linear constraints;
- produce compact certificates that can be independently recomputed;
- translate restriction questions into finite incidence geometry and symmetric-form rank data.

These uses do not imply a security weakness. A reduced benchmark may illuminate methods without transferring conclusions to a full construction.

## 15. Claim boundaries

### Established inside the recorded model

- the general moment-kernel equivalence;
- the top-layer affine signature and punctured-kernel formula;
- the order-one symmetric moment pencil;
- the complete vectorial and scalar finite spectra;
- the rank histogram and five moment profiles;
- the 469-edge incidence set;
- the corrected 203-indexed / 202-distinct radical counts;
- the $K_3\sqcup200K_1$ mask-intersection graph;
- the 201-component bipartite forest;
- fresh independent computational reproduction.

### Not established

- proof-assistant verification of the general theorem;
- independent external or institutional reproduction;
- worldwide historical priority;
- peer-review acceptance or journal publication;
- a full-width collision, preimage, key recovery, or authentication bypass;
- security or insecurity of a standardized full-width construction.

## 16. Conclusion

Affine-restriction degree drops can be viewed from either side of a bilinear incidence relation. Hyperplanes determine vector-moment spans and output annihilators; output masks determine linear moment kernels in affine-parameter space. For the specified 16-to-8 map, this framework yields a complete vectorial spectrum, five scalar moment profiles, an eight-dimensional symmetric pencil, and a nearly disjoint radical geometry. The corrected finite classification contains 203 singular mask-indexed radicals but 202 distinct radical subspaces, with all overlap concentrated at one parameter. The result is exact and reproducible within the recorded model, while its broader priority and significance remain questions for external specialist review.

## References

1. C. Carlet, S. Feukoua, and A. Sălăgean, “The stability of the algebraic degree of Boolean functions when restricted to affine spaces,” *Designs, Codes and Cryptography* 93 (2025), 4799–4832. DOI: 10.1007/s10623-025-01702-z.
2. C. Carlet, S. Feukoua, and A. Sălăgean, “On the algebraic degree stability of vectorial Boolean functions when restricted to affine subspaces,” arXiv:2504.03307 (2025).
3. C. Beierle, G. Leander, and L. Perrin, “Trims and extensions of quadratic APN functions,” *Designs, Codes and Cryptography* 90 (2022), 1009–1036. DOI: 10.1007/s10623-022-01024-4.
4. R. Gow, “Rank-related dimension bounds for subspaces of symmetric bilinear forms,” arXiv:1602.03077 (2016).
5. P. Heering, C. Kaspers, and V. Taranchuk, “On Reed-Muller subcodes, Grassmannian partitions and sum-free functions,” arXiv:2605.22958 (2026).
6. F. J. MacWilliams and N. J. A. Sloane, *The Theory of Error-Correcting Codes*, North-Holland, 1977.
