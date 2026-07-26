# Teaching handout: a hidden wiggle that ordinary points cannot see

## The lowest-level picture

Imagine a machine with two visible knobs. Ordinary tests record how the knobs scale. In the even case there is also a microscopic wiggle that squares to zero. On normal number systems that wiggle is forced to be zero, so the machine looks ordinary.

Under an infinitesimal microscope, the wiggle appears. It interacts differently from the left and the right, so the symmetry machine is not commutative.

## The common crossing

Both cases share the same basic shape:

```text
one horizontal line
one vertical line
meeting at one point
```

Algebraically:

```text
x(y-1)=0.
```

The even case adds a square-zero shadow to the crossing. The odd case adds a separate copy of the invertible part.

## Even case

```text
(x,y,e)(x',y',e')=(xx',yy',x e'+y' e)
```

The tiny coordinate `e` is treated differently from the left and the right. That asymmetry causes hidden noncommutativity.

## Odd case

The odd case has no infinitesimal shadow. Instead it has a separate component containing all global units. The original crossing remains as an ideal with its own local identity.

## The surprise

Over a field, the tiny coordinate is always zero. Every visible unit appears to commute with every other unit.

But as a scheme, the even unit group has:

```text
trivial center
derived subgroup alpha_2
abelianization G_m
```

So ordinary points say "everything is central," while the universal object says "only the identity is central."

## Why tests are not enough

Millions of finite checks can catch implementation errors and false formulas. They cannot prove a statement for every commutative base algebra. The paper therefore contains coefficient proofs, and the programs are challenge routes rather than substitutes.

## Quick comparison

| Question | Even case | Odd case |
|---|---|---|
| Shared visible core | crossing | crossing |
| Extra structure | square-zero shadow | separate unit component |
| Reduced? | no | yes |
| Commutative? | no | yes |
| What ordinary fields see | only scaling | only scaling |
| What the microscope sees | hidden shear and commutators | no hidden shear |

## What has been checked

- complete coefficient proofs are written over arbitrary characteristic-two base algebras;
- independent Python, C, symbolic, and standalone routes agree in their audited ranges;
- deterministic evidence hashes are recorded;
- manuscript, referee guide, reproducibility instructions, and formalization plan are prepared.

## What remains before a public claim

- specialist equivalence and correctness review;
- proof-assistant verification of the small universal proof kernel;
- a fresh immutable hosted execution that records steps and logs;
- final authorship, disclosure, venue-template, and submission decisions.

## One-sentence result

> Reduced points can report ΓÇ£commutative and centralΓÇ¥ while the universal symmetry scheme says the opposite.
