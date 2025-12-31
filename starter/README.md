# Receipts-Native Starter Kit

Get started building receipts-native systems in 5 minutes.

I built this starter kit (along with everything else here) by orchestrating agentic teams—one human, multiple LLMs. It's battle-tested against my production systems.

## What's Included

- `core_primitives.py` - Core functions (dual_hash, emit_receipt, merkle, StopRule)
- `test_compliance.py` - Automated compliance tests (6 principles)
- `example_usage.py` - Working example showing all primitives
- `requirements.txt` - Dependencies (blake3, pytest)

## Quick Start

```bash
# Install dependencies
pip install -r requirements.txt --break-system-packages

# Run example
python example_usage.py

# Expected output: receipts.jsonl with 5+ receipts

# Run compliance tests
pytest test_compliance.py -v

# Expected: 6/6 tests pass
```

## Core Primitives

### dual_hash(data: bytes) -> str
Returns `sha256:...:blake3:...` format

### emit_receipt(receipt_type: str, data: dict) -> dict
Emits receipt to stdout + returns receipt object

### merkle_root(items: list) -> str
Computes Merkle tree root over items

### StopRule(Exception)
Exception raised when SLO violated

## Compliance Tests

The 6 tests verify your system follows receipts-native principles:

1. `test_p1_native_provenance` - Receipts as primary output
2. `test_p2_cryptographic_lineage` - Parent hash chains
3. `test_p3_verifiable_causality` - Input receipt references
4. `test_p4_query_as_proof` - Derive, don't store
5. `test_p5_thermodynamic_governance` - Entropy conservation
6. `test_p6_receipts_gated_progress` - Gates + StopRule

## Integration

To add to your project:

```bash
# Copy primitives
cp starter/core_primitives.py your_project/src/

# Copy compliance tests
cp starter/test_compliance.py your_project/tests/

# Run tests against your implementation
pytest tests/test_compliance.py -v
```

## Learn More

- [Full Standard](../DEFINITION.md)
- [Working Group](../working-group/)
- [Reference Implementation: ProofPack](https://github.com/northstaraokeystone/ProofPack)
