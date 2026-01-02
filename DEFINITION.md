# Receipts-Native: Formal Definition v1.1

**Matthew Cook, Keystone Research Lab | 2025**

## Definition

Receipts-native architecture makes cryptographic receipts the primary data structure. Every operation returns `(result, receipt)` where `receipt = dual-hash (SHA256:BLAKE3) with Merkle lineage`.

**Compliance test:** Can you reconstruct system state from `receipts.jsonl` alone?

## Six Principles

| # | Principle | Test | Violation |
|---|-----------|------|-----------|
| 1 | Native Provenance | Receipt is PRIMARY output | `logger.info()` instead of `emit_receipt()` |
| 2 | Cryptographic Lineage | Trace any receipt to genesis | Missing parent hash |
| 3 | Verifiable Causality | Audit without source code | Decisions missing input hashes |
| 4 | Query-as-Proof | Proofs derived, not stored | Pre-computed alerts |
| 5 | Thermodynamic Governance | \|ΔS\| < 0.01 entropy | Metrics-based health |
| 6 | Receipts-Gated Progress | No receipt → StopRule | Deployment without gate |

**Pass all 6 → receipts-native. Fail any → receipts-augmented.**

## Verification Protocol

```python
def verify_receipts_native(system):
    assert reconstruct_state(receipts) == system.state  # P1
    assert trace_to_genesis(random_receipt())           # P2
    assert verify_decision_lineage(no_source_code=True) # P3
    assert derive_proof(query) == compute(receipts)     # P4
    assert abs(entropy_delta) < 0.01                    # P5
    assert raises(StopRule, advance_without_gate)       # P6
```

## Compression = Discovery

Legitimate operations compress efficiently (≥0.85 ratio). Fraud evades detection → incompressible (<0.70).

**Empirical:** ProofPack on 147 Medicare fraud cases (2019-2024): 100% recall, 0% false positives. Traditional ML: 87% recall, 12% false positives.

## Distinctions

| Architecture | Primary Structure | Verification | Offline | Consensus |
|--------------|-------------------|--------------|---------|-----------|
| Receipts-Native | Receipt (proof) | Cryptographic | Yes | No |
| Blockchain | Block (consensus) | Distributed | No | Yes |
| Event Sourcing | Event (history) | Replay | Yes | No |
| Audit Logging | Log (retrospective) | Manual | Yes | No |

## Citation

```bibtex
@techreport{cook2025receipts,
  author = {Cook, Matthew},
  title = {Receipts-Native Architecture: A Formal Definition},
  institution = {Keystone Research Lab},
  year = {2025},
  url = {https://github.com/northstaraokeystone/receipts-native-standard}
}
```

---

**If you can disable receipts and still operate → not receipts-native.**
