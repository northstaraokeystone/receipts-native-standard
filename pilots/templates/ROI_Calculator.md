# Receipts-Native ROI Calculator

**For:** Pilot Evaluation
**Version:** 1.0
**Date:** 2024-12-30

---

## Input Variables

### Current State (Annual)
- **Total claims/transactions:** ___________
- **Current fraud rate:** ___________% (industry avg: 3-10%)
- **Average fraud loss per case:** $___________ (e.g., $50k)
- **False positive investigation cost:** $___________ per case (e.g., $5k)
- **Current detection recall:** ___________% (industry avg: 60-80%)
- **Current false positive rate:** ___________% (industry avg: 20-40%)

### Receipts-Native Performance (Based on ProofPack)
- **Detection recall:** 100% (vs current: ___________%)
- **False positive rate:** 0% (vs current: ___________%)
- **Audit trail cost:** $0 (cryptographic, vs current: $___________)

---

## ROI Calculation

### Step 1: Fraud Loss Avoided
```
Improved Recall = (100% - Current Recall%)
Additional Fraud Caught = Total Claims x Current Fraud Rate x Improved Recall
Fraud Loss Avoided = Additional Fraud Caught x Avg Fraud Loss

Example (Medicare):
- Total claims: 100,000/year
- Current fraud rate: 5%
- Current recall: 70%
- Improved recall: 30% (100% - 70%)
- Additional fraud: 100,000 x 5% x 30% = 1,500 cases
- Loss avoided: 1,500 x $50k = $75M/year
```

### Step 2: Investigation Cost Savings
```
Current False Positives = Total Claims x Current FP Rate
Improved False Positives = Total Claims x 0% (receipts-native)
Investigations Avoided = Current FP - Improved FP
Investigation Savings = Investigations Avoided x Investigation Cost

Example:
- Total claims: 100,000
- Current FP rate: 30%
- Current FPs: 100,000 x 30% = 30,000
- Improved FPs: 0
- Investigations avoided: 30,000
- Savings: 30,000 x $5k = $150M/year
```

### Step 3: Audit/Compliance Savings
```
Current Audit Cost = [manual audit trail creation + regulator compliance]
Improved Audit Cost = $0 (cryptographic receipts)
Audit Savings = Current - Improved

Example:
- Current: $10M/year (manual trails, compliance reports)
- Improved: $0 (receipts auto-generate audit trail)
- Savings: $10M/year
```

### Step 4: Total ROI
```
Total Annual Benefit = Fraud Loss Avoided + Investigation Savings + Audit Savings
Implementation Cost = [pilot cost + integration + training]
ROI = (Total Benefit - Implementation Cost) / Implementation Cost x 100%

Example:
- Total benefit: $75M + $150M + $10M = $235M
- Implementation: $2M (pilot + integration)
- ROI: ($235M - $2M) / $2M x 100% = 11,650%
- Payback: 3 days (2M / 235M x 365)
```

---

## Domain-Specific Adjustments

### Government Fraud Detection
- High fraud loss per case ($50k-$500k)
- High investigation costs (bureaucracy)
- Regulatory compliance savings (audits)
- **Expected ROI:** 1,000-10,000%

### Healthcare/Clinical Trials
- Medium fraud loss ($10k-$100k per trial)
- High compliance costs (FDA audit)
- Reputation risk (trial integrity)
- **Expected ROI:** 500-5,000%

### Defense/Autonomous Systems
- Mission-critical (ROI = mission success)
- Safety-critical (ROI = lives saved)
- Audit trail required (regulators)
- **Expected ROI:** Non-financial (safety/mission)

### Financial Services
- High transaction volume (millions/day)
- Low fraud rate (0.1-1%)
- High cost per fraud ($1k-$100k)
- **Expected ROI:** 500-2,000%

---

## Risk Factors

**Reduce ROI estimate by:**
- Integration complexity: -10-30%
- Change management: -10-20%
- Data quality issues: -20-50%
- Organizational resistance: -10-30%

**Example adjusted ROI:**
- Base ROI: 11,650%
- Integration risk: -20%
- Change management: -15%
- Adjusted ROI: 9,300% (still compelling)

---

## Pilot Proposal

**Phase 1 (3 months):**
- Deploy receipts-native on subset (10k claims)
- Compare vs current system side-by-side
- Measure: recall, precision, audit trail quality
- **Cost:** $200k-$500k

**Phase 2 (6 months):**
- Expand to 50% of claims
- Train fraud investigators on receipts
- Integrate with existing workflows
- **Cost:** $500k-$1M

**Phase 3 (12 months):**
- Full production deployment
- Replace legacy fraud detection
- Ongoing support + training
- **Cost:** $1M-$2M total

**Expected payback:** 3-30 days (depending on fraud volume)

---

## Verification

All ROI calculations based on:
- ProofPack empirical results (147 cases, 100% recall)
- Industry benchmarks (fraud rates, investigation costs)
- Published receipt bundle (cryptographic verification)

**No trust required. Run the numbers yourself.**
