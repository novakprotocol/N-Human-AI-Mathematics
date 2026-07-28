# ABF-001 Executive Summary

## Decision

**Release as a candidate specialist paper for public technical review.**

## What is new to the public package

ABF-001 consolidates the earlier affine-hyperplane spectrum and radical-incidence work into one theorem chain. It adds a self-contained Reed-Muller proof, a fresh standalone verifier, a separately written bitset verifier, and a correction distinguishing 203 singular mask-indexed radicals from 202 distinct radical subspaces.

## Exact finite results

```text
valid affine hyperplanes:       131,070
vector degree 15:               130,559
vector degree 14:                   511
vector degree <=13:                   0
signature rank:                       8
exceptional kernel dimension:         9
nonzero output masks:               255
singular matrices:                  203
distinct nonzero radicals:          202
covered affine parameters:          467
radical incidences:                 469
incidence-forest components:        201
```

## Evidence

- six fresh focused tests pass;
- primary and independent implementations reproduce the exact edge-atlas hash;
- historical C reconstruction is byte-identical;
- 5,505,024 small-universe checks record zero mismatches;
- a one-bit source tamper is rejected.

## Release boundaries

The paper is a methods-and-instance contribution. It does not claim a full-width cryptographic weakness, global historical priority, peer review, external institutional replication, or proof-assistant verification.
