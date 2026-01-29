# Cost Analysis - nRF52840 + SX1262 PCB

## Executive Summary

| Volume | Unit Cost | Total Project Cost |
|--------|-----------|-------------------|
| 1 | $18.53 | $18.53 |
| 100 | $12.59 | $1,259 |
| 1,000 | $9.00 | $9,000 |
| 10,000 | $6.90 | $69,000 |

---

## Detailed Cost Breakdown by Volume

### 1 Unit (Prototype)

| Category | Cost |
|----------|------|
| Components (BOM) | $11.53 |
| PCB (5 pcs min from JLCPCB) | $2.00 |
| Assembly (manual) | $5.00 |
| **Total per unit** | **$18.53** |

### 100 Units

| Category | Per Unit | Total |
|----------|----------|-------|
| Components (BOM) | $9.29 | $929 |
| PCB Fabrication | $0.80 | $80 |
| SMT Assembly | $2.50 | $250 |
| **Total** | **$12.59** | **$1,259** |

### 1,000 Units

| Category | Per Unit | Total |
|----------|----------|-------|
| Components (BOM) | $7.30 | $7,300 |
| PCB Fabrication | $0.50 | $500 |
| SMT Assembly | $1.20 | $1,200 |
| **Total** | **$9.00** | **$9,000** |

### 10,000 Units

| Category | Per Unit | Total |
|----------|----------|-------|
| Components (BOM) | $5.95 | $59,500 |
| PCB Fabrication | $0.35 | $3,500 |
| SMT Assembly | $0.60 | $6,000 |
| **Total** | **$6.90** | **$69,000** |

---

## Cost Drivers Analysis

### Major Cost Components (at 1,000 units)

| Component | Cost | % of BOM |
|-----------|------|----------|
| nRF52840 MCU | $2.36 | 32% |
| SX1262 LoRa | $1.30 | 18% |
| LRA Motor | $0.50 | 7% |
| DRV2603 Haptic | $0.55 | 8% |
| TCXO | $0.45 | 6% |
| All other | $2.14 | 29% |
| **Total BOM** | **$7.30** | **100%** |

```
BOM Cost Distribution (1000 units):

nRF52840    ████████████████  32%
SX1262      █████████         18%
Haptic+LRA  ████████          15%
TCXO        ███               6%
Other       ██████████████    29%
```

---

## Volume Discount Curve

```
Cost per Unit:

$19 |*
$18 |
$17 |
$16 |
$15 |
$14 |
$13 |  *
$12 |
$11 |
$10 |
$9  |      *
$8  |
$7  |          *
$6  |
    +--+----+------+--------
      1   100   1000   10000
           Volume
```

| Transition | Savings |
|------------|---------|
| 1 -> 100 | 32% reduction |
| 100 -> 1,000 | 29% reduction |
| 1,000 -> 10,000 | 23% reduction |

---

## Price Comparison: Authorized vs Broker Sources

### nRF52840-QIAA-R

| Source | Type | Price @1000 | Risk |
|--------|------|-------------|------|
| DigiKey | Authorized | $3.83 | None |
| LCSC | Authorized | $2.50 | Low |
| Utsource | Broker | $2.36 | Medium |
| AliExpress | Marketplace | $2.00 | High |

**Recommendation:** LCSC for best price/risk balance

### SX1262IMLTRT

| Source | Type | Price @1000 | Risk |
|--------|------|-------------|------|
| DigiKey | Authorized | $4.12 | None |
| Arrow | Authorized | $4.43 | None |
| LCSC | Authorized | $1.30 | Low |
| Alibaba | Wholesale | $1.20 | Medium |

**Recommendation:** LCSC - significantly cheaper and authorized

---

## Savings from Optimizations

### Changes Made

| Original | Optimized | Savings @1000 |
|----------|-----------|---------------|
| LTC4412 ($6.99) | SS14 Schottky ($0.01) | $6.98/unit |
| DRV2605L ($1.15) | DRV2603 ($0.55) | $0.60/unit |
| EPSON TCXO ($2.50) | YXC TCXO ($0.45) | $2.05/unit |
| **Total Savings** | | **$9.63/unit** |

At 1,000 units: **$9,630 saved**
At 10,000 units: **$96,300 saved**

---

## Manufacturing Options

### Option A: JLCPCB (China)

| Service | 100 units | 1,000 units | 10,000 units |
|---------|-----------|-------------|--------------|
| PCB Only | $80 | $500 | $3,500 |
| SMT Assembly | $250 | $1,200 | $6,000 |
| Lead Time | 7-10 days | 10-15 days | 15-20 days |

### Option B: PCBWay (China)

| Service | 100 units | 1,000 units | 10,000 units |
|---------|-----------|-------------|--------------|
| PCB Only | $90 | $550 | $3,800 |
| SMT Assembly | $280 | $1,300 | $6,500 |
| Lead Time | 7-10 days | 10-15 days | 15-20 days |

### Option C: US/EU CM (for 10k+)

| Service | 10,000 units |
|---------|--------------|
| Full turnkey | $8.50-10/unit |
| Lead Time | 4-6 weeks |
| Benefits | Local support, faster iteration |

---

## Retail Pricing Scenarios

Assuming target gross margin:

| Volume | Unit Cost | 50% Margin | 60% Margin | 70% Margin |
|--------|-----------|------------|------------|------------|
| 100 | $12.59 | $25.18 | $31.48 | $41.97 |
| 1,000 | $9.00 | $18.00 | $22.50 | $30.00 |
| 10,000 | $6.90 | $13.80 | $17.25 | $23.00 |

---

## Additional Costs (Not Included Above)

| Item | Estimated Cost | Notes |
|------|----------------|-------|
| FCC/CE Certification | $3,000-10,000 | Required for sale in US/EU |
| Enclosure/Case | $0.50-2.00/unit | Injection molded at volume |
| Packaging | $0.20-0.50/unit | Box, manual, accessories |
| Shipping (components) | 3-5% of BOM | DHL/FedEx from China |
| Import duties | 0-5% | Varies by country |
| Testing/QC | $0.10-0.30/unit | At CM or in-house |

### Fully Loaded Cost (10,000 units, estimated)

| Item | Per Unit |
|------|----------|
| BOM + PCB + Assembly | $6.90 |
| Enclosure | $1.00 |
| Packaging | $0.30 |
| Testing/QC | $0.20 |
| Shipping/Duties | $0.40 |
| **Landed Cost** | **$8.80** |

---

## Recommendations

### For Prototyping (1-10 units)
- Order from LCSC + JLCPCB
- Use SMT assembly service for QFN parts
- Budget: ~$20/unit

### For Small Batch (100 units)
- Full JLCPCB turnkey
- Order extra components for rework
- Budget: ~$13/unit

### For Production (1,000+ units)
- Request quotes from multiple CMs
- Lock in component pricing with distributor
- Consider consignment inventory
- Budget: ~$9/unit

### For Scale (10,000+ units)
- Direct quotes from Nordic/Semtech
- Contract manufacturing agreement
- Component buffer stock (8-12 weeks)
- Budget: ~$7/unit
