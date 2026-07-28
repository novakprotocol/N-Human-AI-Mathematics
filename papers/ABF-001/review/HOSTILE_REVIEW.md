# ABF-001 hostile-review report

## Verdict

**Conditional release for public technical review.** The mathematical core survives the internal hostile review, subject to external specialist review and the explicit claim boundaries below.

## Corrections integrated

1. The proof of the moment criterion is rewritten using Reed-Muller duality instead of relying on a named prior project theorem.
2. The earlier statement “203 radical subspaces” is corrected. There are 203 singular mask-indexed radicals but 202 distinct subspaces because masks `8a` and `9b` share one line.
3. The exact consequence `K3 ⊔ 200 K1` for the mask-intersection graph is recorded.
4. The established prior-art territory is expanded to include 2025–2026 affine-stability and Reed-Muller-subcode work.
5. Cryptographic and historical-priority wording is narrowed.

## No counterexample found

No contradiction was found in the top-layer formula, moment-kernel equivalence, rank histogram, five hyperplane profiles, 469-edge double count, or forest census.

## Remaining external gates

- Boolean-functions specialist review;
- symmetric-bilinear-form specialist review;
- independent reproduction;
- proof-assistant formalization;
- final historical-equivalence assessment.
