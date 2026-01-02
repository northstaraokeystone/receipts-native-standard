# Starter Kit

## Quick Start

```bash
pip install -r requirements.txt
python example_usage.py      # generates receipts.jsonl
pytest test_compliance.py -v # 6/6 tests pass
```

## Files

| File | Purpose |
|------|---------|
| `core_primitives.py` | dual_hash, emit_receipt, merkle_root, StopRule |
| `test_compliance.py` | 6 principle tests |
| `example_usage.py` | Working example |

## Use in Your Project

```bash
cp core_primitives.py your_project/
cp test_compliance.py your_project/tests/
pytest tests/test_compliance.py -v
```
