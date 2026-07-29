# ABF-001 formal-verification boundary

## Current status

```text
proof assistant:                 Lean 4.30.0 with Mathlib 4.30.0
bounded formal PASS:             yes — A01 bidual moment-kernel bridge
full-manuscript formal PASS:     no
human proof:                     complete candidate
computational verification:      extensive
```

The compiled A01 lane establishes the abstract linear-algebra bridge used by the
manuscript's bidual incidence relation:

```text
an output functional annihilates every displayed moment generator
iff it annihilates their generated span
iff the compatible affine-parameter moment map sends q to zero.
```

Exact source:

```text
papers/ABF-001/formal/ABF/MomentKernel.lean
```

The validated build rejects `sorry`, `admit`, project `axiom` declarations, and
`sorryAx`. It records the exact Lean toolchain, Mathlib request, Lake manifest,
source declarations, build log, and bounded receipt.

## Not yet formalized

```text
A02  Reed–Muller duality and the degree/coefficient criterion
A03  affine-hyperplane coordinates and complete moment-space construction
A04  order-zero signature and rank-one radical classification
A05  order-one alternating matrix pencil and affine-parameter identity
A06  proof-connected finite 16-to-8 atlas and every declared census value
```

The A01 PASS does **not** prove the general Reed–Muller moment criterion, the
complete finite classification, the exact incidence counts, or historical
priority. Those remain governed by the human proof and computational evidence
until their own declarations compile.

## Next formalization order

Reed–Muller duality; affine-hyperplane coordinates; complete moment spaces; the
degree-drop criterion; order-zero signature; order-one matrix identity; and
proof-connected finite rank/kernel certificates for the declared atlas.

Computational PASS receipts are not proof-assistant proofs. ABF-001 is a
partially formalized candidate manuscript, not a fully Lean-verified manuscript.
