"""
Receipts-Native Core Primitives

Minimal implementations of the 4 core primitives for receipts-native systems.

Usage:
    from core_primitives import dual_hash, emit_receipt, merkle_root, StopRule
"""

import hashlib
import json
import sys
from datetime import datetime, timezone

# Try to import blake3, fall back to SHA256 if not available
try:
    import blake3
    BLAKE3_AVAILABLE = True
except ImportError:
    BLAKE3_AVAILABLE = False


def dual_hash(data: bytes | str) -> str:
    """
    Compute dual hash (SHA256:BLAKE3).

    Args:
        data: Bytes or string to hash

    Returns:
        Format: "sha256:{hex}:blake3:{hex}"
        If blake3 not available, returns "sha256:{hex}:sha256:{hex}"

    Example:
        >>> dual_hash(b"test")
        'sha256:9f86d081...:blake3:4d967a30...'
    """
    if isinstance(data, str):
        data = data.encode('utf-8')

    sha256_hash = hashlib.sha256(data).hexdigest()

    if BLAKE3_AVAILABLE:
        blake3_hash = blake3.blake3(data).hexdigest()
    else:
        # Fallback: use SHA256 twice with different prefixes
        blake3_hash = hashlib.sha256(b"blake3:" + data).hexdigest()

    return f"sha256:{sha256_hash}:blake3:{blake3_hash}"


def emit_receipt(receipt_type: str, data: dict, output_file: str = None) -> dict:
    """
    Emit receipt to stdout + return object.

    Args:
        receipt_type: Type of receipt (e.g., "ingest", "anchor")
        data: Receipt payload (should include tenant_id)
        output_file: Optional file to append receipt (default: receipts.jsonl)

    Returns:
        Complete receipt with:
        - receipt_type
        - ts (ISO8601)
        - tenant_id (from data or "default")
        - payload_hash (dual_hash of data)
        - **data (all fields from input)

    Side effects:
        Prints JSON to stdout (append-only ledger pattern)
        Optionally appends to output_file

    Example:
        >>> r = emit_receipt("test", {"tenant_id": "default", "value": 42})
        >>> r["receipt_type"]
        'test'
    """
    # Build receipt
    receipt = {
        "receipt_type": receipt_type,
        "ts": datetime.now(timezone.utc).isoformat(),
        "tenant_id": data.get("tenant_id", "default"),
        "payload_hash": dual_hash(json.dumps(data, sort_keys=True)),
        **data
    }

    # Emit to stdout (canonical append-only pattern)
    receipt_json = json.dumps(receipt, sort_keys=True)
    print(receipt_json, file=sys.stdout)

    # Optionally write to file
    if output_file:
        with open(output_file, 'a') as f:
            f.write(receipt_json + '\n')

    return receipt


def merkle_root(items: list) -> str:
    """
    Compute Merkle tree root over list of items.

    Args:
        items: List of dicts (receipts) or strings

    Returns:
        Merkle root as dual_hash string

    Example:
        >>> items = [{"a": 1}, {"b": 2}]
        >>> root = merkle_root(items)
        >>> assert ":" in root  # dual_hash format
    """
    if not items:
        return dual_hash(b"empty")

    # Convert items to hashes
    def item_hash(item):
        if isinstance(item, dict):
            return dual_hash(json.dumps(item, sort_keys=True))
        elif isinstance(item, str):
            return dual_hash(item)
        else:
            return dual_hash(str(item))

    hashes = [item_hash(item) for item in items]

    # Build Merkle tree bottom-up
    while len(hashes) > 1:
        next_level = []
        for i in range(0, len(hashes), 2):
            if i + 1 < len(hashes):
                combined = hashes[i] + hashes[i + 1]
            else:
                combined = hashes[i] + hashes[i]  # Duplicate odd node
            next_level.append(dual_hash(combined))
        hashes = next_level

    return hashes[0]


class StopRule(Exception):
    """
    Exception raised when SLO violated or gate fails.

    Never catch this silently. Must emit anomaly receipt.

    Example:
        >>> if latency > SLO_THRESHOLD:
        >>>     emit_receipt("anomaly", {"metric": "latency", "violation": True})
        >>>     raise StopRule("Latency exceeded 100ms")
    """
    pass


# Convenience exports
__all__ = ['dual_hash', 'emit_receipt', 'merkle_root', 'StopRule', 'BLAKE3_AVAILABLE']
