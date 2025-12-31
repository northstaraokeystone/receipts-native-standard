"""
Receipts-Native Example Usage

Demonstrates core primitives in action.

Run:
    python example_usage.py

Output:
    Creates receipts.jsonl with receipts from this demo
"""

from core_primitives import dual_hash, emit_receipt, merkle_root, StopRule


def main():
    print("=== Receipts-Native Example ===\n")

    # Example 1: dual_hash
    print("1. Dual Hash:")
    h = dual_hash(b"Hello, receipts-native!")
    print(f"   Hash: {h[:60]}...\n")

    # Example 2: emit_receipt (genesis)
    print("2. Emit Genesis Receipt:")
    r1 = emit_receipt("genesis", {
        "tenant_id": "demo",
        "message": "First receipt"
    }, output_file="receipts.jsonl")
    print(f"   Receipt type: {r1['receipt_type']}")
    print(f"   Timestamp: {r1['ts']}\n")

    # Example 3: emit_receipt with lineage
    print("3. Emit Child Receipt (with parent_hash):")
    r2 = emit_receipt("child", {
        "tenant_id": "demo",
        "message": "Second receipt",
        "parent_hash": r1["payload_hash"]
    }, output_file="receipts.jsonl")
    print(f"   Parent hash: {r2['parent_hash'][:40]}...\n")

    # Example 4: Merkle root over receipts
    print("4. Compute Merkle Root:")
    receipts = [r1, r2]
    root = merkle_root(receipts)
    print(f"   Root: {root[:60]}...\n")

    # Example 5: Emit anchor receipt
    print("5. Emit Anchor Receipt:")
    anchor = emit_receipt("anchor", {
        "tenant_id": "demo",
        "merkle_root": root,
        "receipt_count": len(receipts)
    }, output_file="receipts.jsonl")
    print(f"   Anchored {anchor['receipt_count']} receipts\n")

    # Example 6: StopRule on violation
    print("6. StopRule on Violation:")
    try:
        # Simulate SLO violation
        latency = 150  # ms
        SLO_THRESHOLD = 100  # ms

        if latency > SLO_THRESHOLD:
            emit_receipt("anomaly", {
                "tenant_id": "demo",
                "metric": "latency",
                "actual": latency,
                "threshold": SLO_THRESHOLD
            }, output_file="receipts.jsonl")
            raise StopRule(f"Latency {latency}ms exceeds {SLO_THRESHOLD}ms")
    except StopRule as e:
        print(f"   StopRule raised: {e}\n")

    print("=== Demo Complete ===")
    print("Check receipts.jsonl for emitted receipts")


if __name__ == "__main__":
    main()
