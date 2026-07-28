# ABF-001 proof map

## Dependency graph

```text
Boolean ANF and affine hyperplanes
        ↓
Reed-Muller duality RM(r,d)^perp = RM(d-r-1,d)
        ↓
Moment criterion on an affine hyperplane
        ↓
Bidual incidence theorem
        ├── order 0: top-layer signature and punctured kernel
        └── order 1: symmetric moment matrix and radical kernel
                ↓
Specified truth table identity
                ↓
Vector spectrum + scalar rank/profile classification
                ↓
Radical arrangement + incidence forest
```

## Load-bearing nodes

### P1. Affine coordinate spanning
The restrictions of `1,x1,...,xn` to a hyperplane span its affine functions. Products through order `r` span `RM(r,n-1)`.

### P2. Reed-Muller duality
Extended Reed-Muller convention: `RM(s,d)={0}` for `s<0`, the full Boolean function space for `s>=d`, and `degree(0)=-infinity`. With this convention, the criterion is valid for every nonnegative moment order.

The threshold `degree <= n-r-2` is exactly orthogonality to `RM(r,n-1)`.

### P3. Linearity in the affine parameter
The hyperplane indicator is linear in `q`, making each moment map linear.

### P4. Symmetry of the order-one pencil
The matrix entries are sums of `z_i z_j(v·F)`, so `B_v=B_v^T` and `Phi_{1,v}(q)=B_vq`.

### P5. Finite source identity
Every numerical claim depends on the exact 65,536-byte truth table with SHA-256 `2a861e09dcb5b00e208ede53e1b29615a5309389a83da40f81d663ec760e7e52`.

## Hostile-review targets

1. Check the Reed-Muller threshold indexing.
2. Check that ambient coordinate products span all required hyperplane monomials.
3. Check the affine-parameter convention and exclusion of empty/whole-domain parameters.
4. Recompute the duplicate radical for masks `8a` and `9b`.
5. Recompute the five profile counts and 469-edge double count.
6. Search for an earlier equivalent moment-incidence theorem under different terminology.
7. Exhaustively compare direct restriction degree with moment vanishing over all maps `GF(2)^3 -> GF(2)^2`.
8. Flip one source truth-table bit and require the source-identity gate to reject it.

## Formal status

The proof is self-contained at the human level. No ABF-001 theorem has yet been formalized in a proof assistant.
