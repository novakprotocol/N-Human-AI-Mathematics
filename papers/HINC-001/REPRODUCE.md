# Reproducing HINC-001

## Two independent goals

The package has two distinct reproduction routes:

1. **computational formula checking** for finite Artin rings and symbolic identities;
2. **proof-assistant compilation** for the formally encoded algebraic scope.

Neither route replaces the human proof of the complete arbitrary-base manuscript.

## Source identities

### Standalone manuscript and Python verifier

```text
repository: novakprotocol/N-MathLab
commit:     e6adac212150177d4afa56e643d37533a208693c
PR:         #406
```

### Base formal kernel

```text
compiled source commit: 8ccf90b05a0ab4fb45774e9dd8ba7b3c9a59cd8c
public checker:          novakprotocol/novak-sdt PR #57
```

### Principal classification formal source

```text
N-MathLab PR:            #416
public checker:          novakprotocol/novak-sdt PR #58
```

## Route A — Standalone Python verifier

### Requirements

```text
Python 3.11 or later
SymPy 1.14.0
```

### Commands from the source packet root

```bash
python -m pip install 'sympy==1.14.0'
PYTHONPATH=src python -m unittest discover -s tests -v
PYTHONPATH=src python src/standalone_common_core_verifier.py \
  --maximum-order 4 \
  --output evidence/standalone-certificate.reproduced.json
```

Compare the reproduced certificate:

```bash
cmp evidence/standalone-certificate.json \
    evidence/standalone-certificate.reproduced.json
sha256sum -c evidence/SHA256SUMS.code.txt
```

Expected controlling evidence identity:

```text
20d883988da7818f73de0b4ccab68bc7adea5097a4af7a6ef5a72c23b4e1ea4b
```

### What Route A checks

- crossing-core closure;
- even skew closure and associativity;
- skew-primitive coassociativity;
- universal commutator-defect formula;
- odd unit-doubling closure and associativity;
- multiplicativity of the collapse map;
- deterministic certificate generation;
- finite-field point-count formulas;
- reduced-center polynomial on the declared finite route;
- tangent-dimension assertions;
- semantic mutations intended to make the checker fail.

### Route A limitations

It does not prove arbitrary-base coefficient comparison, representability, the full scheme-theoretic center, or the fppf-derived subgroup by finite enumeration.

## Route B — Base Lean kernel

The controlling public run already completed.

```text
Lean:                 4.30.0
Mathlib:              v4.30.0
workflow run:         30119931881
workflow job:         89569737408
artifact:             8606983225
artifact SHA-256:     63b2b160da40f722818820679da7c9d22eb7640694e48a5abc08fccf78f47133
result:               PASS
sorryAx:              absent
```

Local commands after checking out the exact source:

```bash
cd formal/hinc-lean-kernel-v1
lake update
lake exe cache get
lake build
lake env lean HINC/Core.lean
```

Verify that the displayed axiom report contains no `sorryAx`.

## Route C — Principal classification Lean gate

The expanded checker compiles `HINC/Classification.lean` and records the coefficient-classification axiom report.

The first hosted run failed at one extensionality proof because recursive simplification exceeded Lean's recursion depth. The failure is preserved as:

```text
run:       30173789803
job:       89719185539
artifact:  8623660266
```

The proof was repaired with explicit field substitutions. Use the current PR #58 status and its latest immutable artifact rather than assuming the rerun passed.

When the gate passes, the local reproduction route is:

```bash
cd formal/hinc-lean-kernel-v1
lake update
lake exe cache get
lake build
lake env lean HINC/Classification.lean
```

## Independent reproduction recommendations

A strong outside reproduction should do at least one of the following:

- rederive the even and odd coefficient equations without reading the expected normal forms;
- implement the functor-of-points equations in a different computer algebra system;
- formalize the generator-to-global sufficiency theorem independently;
- reproduce finite Artin-ring tests without importing the primary module;
- verify the scheme center and clopen split using direct coordinate-ring calculations.

## Reporting discrepancies

Do not edit expected hashes or source until the discrepancy is understood. Report:

```text
exact source commit
commands
environment
first differing theorem/test/output
complete logs
whether the difference is mathematical, implementation, or environment-related
```

A mismatch is a valid scientific result.
