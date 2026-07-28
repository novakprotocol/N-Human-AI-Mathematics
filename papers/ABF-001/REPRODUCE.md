# Reproduce ABF-001

## Requirements

- Python 3.11 or newer
- NumPy

## Materialize the exact primary verifier

```bash
python src/assemble_primary.py
```

The assembler verifies the committed gzip/base64 bundle against the exact target SHA-256 before writing `src/abf001_verifier.py`.

## Primary verifier

```bash
python src/abf001_verifier.py --output-directory evidence/generated
```

Expected key output:

```text
truth_table_sha256 = 2a861e09dcb5b00e208ede53e1b29615a5309389a83da40f81d663ec760e7e52
edge_sha256 = 95d64917af27fa1b827bda0b82364dc6e69de6376ccb0ad81e12ab22b82742fa
vector spectrum = 130559 / 511 / 0
rank histogram = 13:2, 14:15, 15:74, 16:112, 17:52
```

## Independent bitset verifier

```bash
python src/abf001_independent_bitset.py --output-directory evidence/independent
```

This path uses no NumPy and does not import the primary verifier.

## Tests

```bash
python -m unittest discover -s tests -p 'test_*.py' -v
```

## Independence labels

- Primary NumPy route: internal implementation.
- Separate bitset route: separately written internal implementation.
- Historical C route: separately written internal native implementation.
- External reproduction: not yet completed.

A reproducer should record operating system, Python version, dependency versions, exact commit, commands, outputs, and file hashes.

## Complete small-universe control

```bash
python src/abf001_small_universe.py \
  --output evidence/receipts/small-universe-final.json
```

Expected: `5,505,024` comparisons and `0` failures.

## Tamper control

```bash
PYTHONPATH=src python src/abf001_tamper_control.py \
  --output evidence/receipts/tamper-control-final.json
```

Expected: the original truth-table SHA-256 matches and the one-bit-altered table is rejected.
