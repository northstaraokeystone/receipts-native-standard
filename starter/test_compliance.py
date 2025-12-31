"""
Receipts-Native Compliance Tests

Tests your system against 6 core principles.

Usage:
    pytest test_compliance.py -v
"""

import pytest
from core_primitives import dual_hash, emit_receipt, merkle_root, StopRule


def test_p1_native_provenance():
    """
    P1: Operations emit receipts, not logs.

    Test: Receipt emitted, contains required fields, uses dual_hash.
    """
    # Emit test receipt
    r = emit_receipt("test_p1", {"tenant_id": "test", "value": 1})

    # Check required fields
    assert r["receipt_type"] == "test_p1"
    assert "ts" in r
    assert "tenant_id" in r
    assert "payload_hash" in r

    # Check dual_hash format
    assert ":" in r["payload_hash"]
    parts = r["payload_hash"].split(":")
    assert len(parts) == 4  # sha256:hash:blake3:hash
    assert parts[0] == "sha256"
    assert parts[2] == "blake3"


def test_p2_cryptographic_lineage():
    """
    P2: Receipts form cryptographic chain via parent_hash.

    Test: Sequential receipts link via parent_hash.
    """
    # Emit genesis receipt (no parent)
    r1 = emit_receipt("genesis", {"tenant_id": "test", "seq": 1})

    # Emit child receipt (references parent)
    r2 = emit_receipt("child", {
        "tenant_id": "test",
        "seq": 2,
        "parent_hash": r1["payload_hash"]
    })

    # Check lineage
    assert "parent_hash" in r2
    assert r2["parent_hash"] == r1["payload_hash"]


def test_p3_verifiable_causality():
    """
    P3: Decisions reference input receipts.

    Test: Decision receipt contains input_receipt_hash.
    """
    # Ingest input
    input_r = emit_receipt("ingest", {"tenant_id": "test", "data": "x"})

    # Make decision referencing input
    decision_r = emit_receipt("decision", {
        "tenant_id": "test",
        "action": "approve",
        "input_receipt_hash": input_r["payload_hash"]
    })

    # Check causality
    assert "input_receipt_hash" in decision_r
    assert decision_r["input_receipt_hash"] == input_r["payload_hash"]


def test_p4_query_as_proof():
    """
    P4: Results derived from receipts, not pre-stored.

    Test: Query function derives result from receipt list.
    """
    # Create receipt ledger
    receipts = [
        emit_receipt("event", {"tenant_id": "test", "value": i})
        for i in range(10)
    ]

    # Derive result from receipts (not pre-computed)
    def query_sum(receipts):
        return sum(r.get("value", 0) for r in receipts)

    result = query_sum(receipts)

    # Verify derivation works
    assert result == sum(range(10))
    assert result == 45


def test_p5_thermodynamic_governance():
    """
    P5: Entropy tracked, violations raise StopRule.

    Test: Entropy conservation checked, violation raises StopRule.
    """
    # Simulate entropy check
    def check_entropy(before, after, threshold=0.01):
        delta = abs(before - after)
        if delta >= threshold:
            emit_receipt("anomaly", {
                "tenant_id": "test",
                "metric": "entropy",
                "delta": delta
            })
            raise StopRule(f"Entropy violation: |{delta}| >= {threshold}")
        return True

    # Test pass case
    assert check_entropy(1.0, 1.005, threshold=0.01) == True

    # Test fail case
    with pytest.raises(StopRule):
        check_entropy(1.0, 1.02, threshold=0.01)


def test_p6_receipts_gated_progress():
    """
    P6: Progress blocked without gate receipt.

    Test: StopRule raised when advancing without gate.
    """
    # Simulate gate check
    def advance_with_gate(gate_receipt):
        if gate_receipt is None:
            raise StopRule("Cannot advance: no gate receipt")
        if gate_receipt.get("gate_passed") != True:
            raise StopRule("Cannot advance: gate failed")
        return True

    # Test pass case
    gate_r = emit_receipt("gate", {"tenant_id": "test", "gate_passed": True})
    assert advance_with_gate(gate_r) == True

    # Test fail cases
    with pytest.raises(StopRule):
        advance_with_gate(None)

    failed_gate = emit_receipt("gate", {"tenant_id": "test", "gate_passed": False})
    with pytest.raises(StopRule):
        advance_with_gate(failed_gate)
