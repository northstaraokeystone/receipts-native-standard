# Receipts-Native Architecture: Technical Overview

**For:** Technical Decision Makers
**Audience:** CTOs, Staff Engineers, Security Architects
**Duration:** 15-minute read

---

## How I Built This

I built ProofPack and this entire standard by orchestrating agentic teams—one human, multiple LLMs across different platforms. That's my secret sauce.

**The agents got me here. Now I need humans to scale the category.**

I'm recruiting domain experts for a working group: government procurement specialists, FDA regulatory experts, ZK cryptographers, enterprise compliance practitioners.

---

## Problem Statement

**Traditional accountability:**
- Logs (unverified, mutable)
- Metrics (no causality)
- Dashboards (no provenance)
- Black-box AI (unexplainable)

**Result:** Trust-based systems in zero-trust environments.

---

## Core Insight

**Compression = Discovery**

Legitimate operations follow compressible patterns.
Fraudulent operations must evade detection (incompressible).

**Compression ratio is objective fraud detector.**

---

## Architecture Principles

### 1. Native Provenance
**Pattern:** `emit_receipt()` replaces `logger.info()`

```python
# Before (trust-based)
logger.info("Fraud detected", case_id=123)

# After (receipts-native)
emit_receipt("fraud_detection", {
    "case_id": 123,
    "compression_ratio": 0.42,
    "threshold": 0.70,
    "input_receipt_hash": input_hash
})
```

**Result:** Every operation has cryptographic proof.

### 2. Cryptographic Lineage
**Pattern:** Receipts form Merkle-anchored chain

```python
receipt_n["parent_hash"] = receipt_{n-1}["payload_hash"]
merkle_root = merkle(all_receipts)
```

**Result:** Tamper-evident audit trail.

### 3. Verifiable Causality
**Pattern:** Decisions reference input receipts

```python
decision_receipt = {
    "action": "approve",
    "input_receipt_hash": ingest_hash,  # proves input
    "reasoning": "compression >= 0.70"
}
```

**Result:** Reconstruct decision chain without source code.

### 4. Query-as-Proof
**Pattern:** Derive results from receipts, don't pre-store

```python
# Before (gameable)
fraud_table.insert(case_id, is_fraud=True)

# After (provable)
def is_fraud(case_id):
    receipts = query_receipts(case_id)
    return derive_verdict(receipts)  # computed on-demand
```

**Result:** Impossible to game (no pre-stored results).

### 5. Thermodynamic Governance
**Pattern:** Entropy conservation as health metric

```python
if abs(entropy_before - entropy_after) >= 0.01:
    raise StopRule("Entropy violation")
```

**Result:** System health = physics, not guesswork.

### 6. Receipts-Gated Progress
**Pattern:** StopRule halts on SLO violation

```python
if latency > SLO_THRESHOLD:
    emit_receipt("anomaly", {...})
    raise StopRule("Latency exceeded")
```

**Result:** No silent failures.

---

## Implementation Stack

### Core Primitives
```python
dual_hash(data)          # SHA256:BLAKE3
emit_receipt(type, data) # Append to ledger
merkle_root(receipts)    # Batch anchoring
StopRule(Exception)      # SLO enforcement
```

### Storage
- **Receipts:** Append-only JSONL (receipts.jsonl)
- **Anchors:** Merkle roots (periodic batching)
- **Ledger:** PostgreSQL (queryable) or S3 (archival)

### Verification
```python
def verify_chain(receipts):
    for i, r in enumerate(receipts[1:], 1):
        assert r["parent_hash"] == receipts[i-1]["payload_hash"]
    return merkle_root(receipts)
```

---

## ProofPack Case Study

**Domain:** Medicare fraud detection
**Dataset:** 147 cases (10 fraud, 137 legit)
**Method:** Compression-based detection

**Implementation:**
1. Ingest claim -> emit `ingest_receipt`
2. Compress claim data
3. Calculate ratio -> emit `detect_receipt`
4. Compare to threshold (0.70)
5. Anchor batch -> emit `anchor_receipt`

**Results:**
- Recall: 100% (vs 60-80% industry)
- Precision: 100% (vs 40-60% industry)
- Audit trail: Full reconstruction from receipts
- Verification: Published receipt bundle

**Receipts emitted:**
- 147 ingest receipts (1 per claim)
- 147 detect receipts (1 per detection)
- 1 anchor receipt (Merkle root)
- Total: 295 receipts

**Receipt size:** ~1KB average
**Total ledger:** ~300KB for 147 cases
**Compression:** 99.7% (vs raw claim data)

---

## Integration Patterns

### Pattern 1: Side-by-Side
- Run receipts-native in parallel with legacy
- Compare results
- Build confidence before cutover

### Pattern 2: Shadow Mode
- Emit receipts, don't act on them
- Analyze receipt chain quality
- Validate before production

### Pattern 3: Hybrid
- Legacy system emits receipts retroactively
- Gradual migration to receipts-first
- Maintain continuity during transition

---

## Security Model

### Cryptographic Guarantees
- **Integrity:** Dual-hash (SHA256:BLAKE3)
- **Lineage:** Parent hash chains
- **Completeness:** Merkle roots
- **Non-repudiation:** Timestamped receipts

### Threat Model
| Attack | Defense |
|--------|---------|
| Receipt tampering | Merkle root breaks |
| Receipt deletion | Gaps in parent_hash chain |
| Replay attacks | Timestamp + nonce |
| Pre-computation | Query-as-proof (derive on-demand) |

### Zero Trust
No component trusted. All claims verified.
Regulators audit receipts, not systems.

---

## Performance Characteristics

**ProofPack benchmarks:**
- Receipt emission: <1ms
- Dual-hash: <0.5ms
- Merkle (1000 receipts): <10ms
- Chain verification: <5s per 10k receipts

**Scalability:**
- Receipts: Append-only (horizontal)
- Anchors: Periodic batching (configurable)
- Queries: Indexed by timestamp/type

**Storage:**
- ~1KB per receipt
- 1M receipts = ~1GB
- S3 archival: ~$0.02/GB/month

---

## Deployment Requirements

### Infrastructure
- **Runtime:** Python 3.10+ (or Rust for hotpath)
- **Storage:** PostgreSQL + S3
- **Dependencies:** blake3, pytest

### Integration
- **Existing logs:** Can emit receipts retroactively
- **APIs:** RESTful receipt query endpoints
- **Monitoring:** Receipt rate, chain health

### Compliance
- **NIST:** Cryptographic standards (SHA256, FIPS 180-4)
- **GDPR:** Receipt redaction support
- **SOC 2:** Full audit trail built-in

---

## Pilot Scope

**Recommended first deployment:**
- 10k-50k transactions
- 3-month pilot
- Side-by-side with legacy
- Assisted integration

**Success criteria:**
- Receipt chain integrity: 100%
- Detection accuracy: >= legacy + 10%
- Audit trail completeness: 100%
- False positive reduction: >=50%

**Deliverables:**
- Receipt ledger (verifiable)
- Performance metrics
- Integration runbook
- Training materials

---

## Next Steps

1. **Verify:** Download ProofPack receipt bundle, run verification
2. **Test:** Run starter kit compliance tests on your system
3. **Pilot:** Identify 10k-transaction pilot cohort
4. **Deploy:** 3-month assisted pilot

**All claims verifiable. No trust required.**

---

## References

- Standard: github.com/northstaraokeystone/receipts-native-standard
- ProofPack: github.com/northstaraokeystone/ProofPack
- Working Group: Launching Feb 2025
- Receipt Bundle: [Download link]

**Contact:** Matthew Cook, Keystone Research Lab
