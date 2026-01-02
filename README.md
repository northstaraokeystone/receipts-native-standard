# Receipts-Native Standard

**Cryptographic receipts as the primary data structure, not secondary logging.**

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)

## What Is It?

Every operation returns `(result, receipt)` where receipts form a Merkle-linked chain to genesis.

**The test:** Can you reconstruct system state from `receipts.jsonl` alone?
Yes → receipts-native. No → not receipts-native.

## Six Principles

| # | Principle | Test |
|---|-----------|------|
| 1 | Native Provenance | Receipt is PRIMARY output |
| 2 | Cryptographic Lineage | Trace any receipt to genesis |
| 3 | Verifiable Causality | Audit without source code |
| 4 | Query-as-Proof | Proofs derived, not stored |
| 5 | Thermodynamic Governance | Entropy conservation verified |
| 6 | Receipts-Gated Progress | No receipt → StopRule exception |

## Quick Start

```bash
cd starter && pip install -r requirements.txt
python example_usage.py      # generates receipts.jsonl
pytest test_compliance.py -v # 6/6 tests pass
```

## Reference Implementation

[ProofPack](https://github.com/northstaraokeystone/ProofPack) - 147 Medicare fraud cases, 100% recall, 0% false positives.

## Links

- [DEFINITION.md](./DEFINITION.md) - Formal standard
- [WORKING_GROUP.md](./WORKING_GROUP.md) - Join us
- [starter/](./starter/) - Code + compliance tests

## License

CC-BY-4.0
