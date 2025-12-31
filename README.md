# Receipts-Native Standard

**The canonical definition of receipts-native architecture.**

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
[![Working Group](https://img.shields.io/badge/Working%20Group-Recruiting-blue.svg)](./RECRUITING.md)

---

## What is Receipts-Native?

**Receipts-native architecture** makes cryptographic receipts the primary data structure, not secondary logging. Every operation returns `(result, receipt)` where receipts form a Merkle-linked chain to genesis.

**The test:** Can you reconstruct system state from `receipts.jsonl` alone? If no → not receipts-native.

**Why it matters:** Accountability becomes *architectural* (cannot build without) rather than *operational* (added after).

---

## Quick Links

| Resource | Description |
|----------|-------------|
| [**DEFINITION.md**](./DEFINITION.md) | The formal v1.1 standard |
| [**Working Group**](./working-group/) | Charter, members, roadmap |
| [**RECRUITING.md**](./RECRUITING.md) | Join the steering committee |
| [**ProofPack**](https://github.com/northstaraokeystone/ProofPack) | Reference implementation |

---

## Six Core Principles

| # | Principle | Test |
|---|-----------|------|
| 1 | **Native Provenance** | Receipt is PRIMARY output |
| 2 | **Cryptographic Lineage** | Trace any receipt to genesis |
| 3 | **Verifiable Causality** | Audit without source code access |
| 4 | **Query-as-Proof** | Proofs derived, not stored |
| 5 | **Thermodynamic Governance** | Entropy conservation verified |
| 6 | **Receipts-Gated Progress** | No receipt → StopRule exception |

Pass all 6 → receipts-native. Fail any → receipts-augmented.

---

## Reference Implementation

[**ProofPack**](https://github.com/northstaraokeystone/ProofPack) demonstrates receipts-native compliance for government fraud detection:

- **147 Medicare fraud cases:** 100% recall, 0% false positives
- **Compression-based detection:** Physics decides, not heuristics
- **Production-ready:** Built and deployed

---

## Working Group

We're building the receipts-native category with a working group from day zero.

### Current State (Honest)

| Metric | Status |
|--------|--------|
| Steering members | 1 (founder) |
| Open seats | 6 |
| First meeting | February 2025 |

### Open Seats

We're recruiting experts in:
- ZK/Cryptography
- Enterprise Compliance
- Government/Defense
- Healthcare/FDA
- Autonomous Systems
- Open Source Infrastructure

**[Apply to join →](./RECRUITING.md)**

---

## Repository Structure

```
receipts-native-standard/
├── README.md                    # You are here
├── DEFINITION.md                # The formal standard (v1.1)
├── CHANGELOG.md                 # Version history
├── LICENSE                      # CC-BY-4.0
├── RECRUITING.md                # Join the working group
├── working-group/
│   ├── CHARTER.md               # Governance model
│   ├── MEMBERS.md               # Current + recruiting
│   ├── ROADMAP.md               # 12-month plan
│   ├── CONTRIBUTION_GUIDE.md    # How to contribute
│   └── meetings/                # Meeting notes
├── metrics/
│   └── CURRENT_STATE.md         # Honest adoption tracking
├── pilots/
│   ├── TARGET_LIST.md           # Pilot pipeline
│   └── templates/               # Outreach materials
└── .github/
    └── ISSUE_TEMPLATE/          # Working group applications
```

---

## Get Started

### Implement the Standard

1. Read [DEFINITION.md](./DEFINITION.md)
2. Review [ProofPack](https://github.com/northstaraokeystone/ProofPack) as reference
3. Run compliance tests against your system
4. Add your implementation to [MEMBERS.md](./working-group/MEMBERS.md)

### Contribute to the Standard

1. Read [CONTRIBUTION_GUIDE.md](./working-group/CONTRIBUTION_GUIDE.md)
2. Open issues for proposals
3. Join the working group

### Join the Working Group

1. Review [CHARTER.md](./working-group/CHARTER.md)
2. Check open seats in [RECRUITING.md](./RECRUITING.md)
3. Apply via GitHub issue template

---

## Why This Matters

**The standards vacuum:** "Receipts-native" is used by 5+ builders (Hackett MetaOS, Brevis, Miden, idOS, Keystone) with zero canonical definition—until now.

**The opportunity:** Most category creators (HashiCorp, Stripe) built tech first, then standards emerged. We're doing it reverse: **standard → working group → ecosystem**.

**The proof:** ProofPack already works. Now we're building the category.

---

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

## License

This work is licensed under [CC-BY-4.0](./LICENSE). You are free to share and adapt with attribution.

---

## Contact

- **GitHub Issues:** Questions, proposals, applications
- **Working Group:** Monthly meetings (starting February 2025)
- **Founder:** Matthew Cook, Keystone Research Lab

---

**If you can disable receipts and still operate → not receipts-native.**
**If system halts without receipts → receipts-native.**
**The substrate decides.**
