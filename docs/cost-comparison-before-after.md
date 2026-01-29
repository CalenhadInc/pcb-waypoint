# Cost Comparison: Before vs After Trade-offs

## Executive Summary

| Volume | Original Design | Optimized Design | Savings | % Saved |
|--------|-----------------|------------------|---------|---------|
| 1 | $30.18 | $18.73 | $11.45 | 38% |
| 100 | $22.09 | $12.71 | $9.38 | 42% |
| 1,000 | $16.80 | $9.08 | $7.72 | 46% |
| 10,000 | $13.15 | $6.96 | $6.19 | 47% |

---

## Trade-offs Applied

| Change | Original | Optimized | Savings @1 | Savings @1000 |
|--------|----------|-----------|------------|---------------|
| Power management | LTC4412 ($6.99) | SS14 Schottky ($0.02) | $6.97 | $6.97 |
| Haptic driver | DRV2605L ($1.15) | DRV2603 ($0.55) | $0.60 | $0.60 |
| TCXO | EPSON ($2.50) | YXC/TXC ($0.45) | $2.05 | $2.05 |
| Sourcing | DigiKey | LCSC | $1.83 | $4.10 |
| **Component savings** | | | **$11.45** | **$13.72** |

---

## Detailed Breakdown: 1 Unit (Prototype)

### BOM Cost

| Component | Original | Optimized | Savings |
|-----------|----------|-----------|---------|
| nRF52840-QIAA-R | $5.47 (DigiKey) | $3.09 (LCSC) | $2.38 |
| SX1262IMLTRT | $5.89 (DigiKey) | $1.62 (LCSC) | $4.27 |
| LTC4412MPS6 | $6.99 | - | $6.99 |
| SS14 Schottky | - | $0.02 | -$0.02 |
| DRV2605LDGSR | $1.15 | - | $1.15 |
| DRV2603RUNR | - | $0.55 | -$0.55 |
| EPSON TCXO | $2.50 | - | $2.50 |
| YXC TCXO | - | $0.80 | -$0.80 |
| AP2112K-3.3 | $0.10 | $0.10 | $0.00 |
| MCP73831 | $0.50 | $0.50 | $0.00 |
| USBLC6-2P6 | $0.10 | $0.10 | $0.00 |
| Crystals (2) | $0.55 | $0.55 | $0.00 |
| Connectors | $2.10 | $2.10 | $0.00 |
| Passives | $0.48 | $0.48 | $0.00 |
| LEDs, Buttons | $0.46 | $0.46 | $0.00 |
| LRA Motor | $1.00 | $1.00 | $0.00 |
| **BOM Total** | **$27.29** | **$11.37** | **$15.92** |

### Total Unit Cost (1 pc)

| Category | Original | Optimized |
|----------|----------|-----------|
| BOM | $27.29 | $11.37 |
| PCB (5pc min) | $2.00 | $2.00 |
| Assembly | $5.00 | $5.00 |
| Shipping | $0.89 | $0.36 |
| **Total** | **$35.18** | **$18.73** |

**Savings: $16.45 (47%)**

---

## Detailed Breakdown: 100 Units

### BOM Cost

| Component | Original | Optimized | Savings |
|-----------|----------|-----------|---------|
| nRF52840-QIAA-R | $4.38 | $2.80 | $1.58 |
| SX1262IMLTRT | $4.71 | $1.45 | $3.26 |
| LTC4412MPS6 | $5.50 | - | $5.50 |
| SS14 Schottky | - | $0.015 | -$0.015 |
| DRV2605LDGSR | $0.95 | - | $0.95 |
| DRV2603RUNR | - | $0.65 | -$0.65 |
| EPSON TCXO | $1.80 | - | $1.80 |
| YXC TCXO | - | $0.60 | -$0.60 |
| Other components | $2.56 | $2.56 | $0.00 |
| **BOM Total** | **$19.90** | **$8.08** | **$11.82** |

### Total Unit Cost (100 pcs)

| Category | Original | Optimized |
|----------|----------|-----------|
| BOM | $19.90 | $8.08 |
| PCB | $0.80 | $0.80 |
| Assembly | $2.50 | $2.50 |
| Shipping/unit | $0.89 | $0.33 |
| **Total/unit** | **$24.09** | **$11.71** |

| | Original | Optimized |
|---|----------|-----------|
| **100 Unit Total** | **$2,409** | **$1,171** |
| **Savings** | | **$1,238** |

---

## Detailed Breakdown: 1,000 Units

### BOM Cost

| Component | Original | Optimized | Savings |
|-----------|----------|-----------|---------|
| nRF52840-QIAA-R | $3.83 | $2.36 | $1.47 |
| SX1262IMLTRT | $4.12 | $1.30 | $2.82 |
| LTC4412MPS6 | $4.50 | - | $4.50 |
| SS14 Schottky | - | $0.01 | -$0.01 |
| DRV2605LDGSR | $0.80 | - | $0.80 |
| DRV2603RUNR | - | $0.55 | -$0.55 |
| EPSON TCXO | $1.20 | - | $1.20 |
| YXC TCXO | - | $0.45 | -$0.45 |
| Other components | $2.15 | $2.15 | $0.00 |
| **BOM Total** | **$16.60** | **$6.82** | **$9.78** |

### Total Unit Cost (1,000 pcs)

| Category | Original | Optimized |
|----------|----------|-----------|
| BOM | $16.60 | $6.82 |
| PCB | $0.50 | $0.50 |
| Assembly | $1.20 | $1.20 |
| Shipping/unit | $0.50 | $0.20 |
| **Total/unit** | **$18.80** | **$8.72** |

| | Original | Optimized |
|---|----------|-----------|
| **1,000 Unit Total** | **$18,800** | **$8,720** |
| **Savings** | | **$10,080** |

---

## Detailed Breakdown: 10,000 Units

### BOM Cost

| Component | Original | Optimized | Savings |
|-----------|----------|-----------|---------|
| nRF52840-QIAA-R | $3.35 | $2.00 | $1.35 |
| SX1262IMLTRT | $3.60 | $1.10 | $2.50 |
| LTC4412MPS6 | $3.80 | - | $3.80 |
| SS14 Schottky | - | $0.008 | -$0.008 |
| DRV2605LDGSR | $0.65 | - | $0.65 |
| DRV2603RUNR | - | $0.45 | -$0.45 |
| EPSON TCXO | $0.90 | - | $0.90 |
| YXC TCXO | - | $0.35 | -$0.35 |
| Other components | $1.70 | $1.70 | $0.00 |
| **BOM Total** | **$14.00** | **$5.61** | **$8.39** |

### Total Unit Cost (10,000 pcs)

| Category | Original | Optimized |
|----------|----------|-----------|
| BOM | $14.00 | $5.61 |
| PCB | $0.35 | $0.35 |
| Assembly | $0.60 | $0.60 |
| Shipping/unit | $0.20 | $0.10 |
| **Total/unit** | **$15.15** | **$6.66** |

| | Original | Optimized |
|---|----------|-----------|
| **10,000 Unit Total** | **$151,500** | **$66,600** |
| **Savings** | | **$84,900** |

---

## Savings Visualization

```
Savings by Volume:

1 unit:      $11.45  ████
100 units:   $1,238  ████████
1,000 units: $10,080 ████████████████████████████████
10,000:      $84,900 ████████████████████████████████████████████████████
```

---

## Cost Per Unit Comparison Chart

```
$/unit
$35 |■ Original
$30 |■
$25 |■
$20 |    ■
$19 |□         ■
$15 |□              ■
$12 |    □
$10 |
$9  |         □
$7  |              □
$5  |
    +----+--------+----------+------------
        1      100      1,000      10,000
              Volume (units)

■ = Original Design
□ = Optimized Design
```

---

## Break-Even Analysis

At what volume do the optimizations pay for the trade-offs?

| Trade-off | Impact | Break-even |
|-----------|--------|------------|
| SS14 vs LTC4412 | 8% battery life | Saves $6.97 from unit 1 |
| DRV2603 vs DRV2605L | Manual tuning ~2hrs dev time | ~$0.60 × 100 = $60 covers dev time |
| Generic TCXO | Test samples first ~$20 | ~$2.05 × 10 = $20.50 covers testing |
| LCSC vs DigiKey | 5-10 day lead time | Immediate savings, plan ahead |

**All trade-offs pay for themselves within the first 10-100 units.**

---

## Cumulative Savings Over Product Lifetime

| Cumulative Units | Original Cost | Optimized Cost | Total Saved |
|------------------|---------------|----------------|-------------|
| 100 | $2,409 | $1,171 | $1,238 |
| 500 | $11,245 | $5,155 | $6,090 |
| 1,000 | $18,800 | $8,720 | $10,080 |
| 5,000 | $81,500 | $36,100 | $45,400 |
| 10,000 | $151,500 | $66,600 | $84,900 |
| 25,000 | $356,250 | $156,500 | $199,750 |
| 50,000 | $687,500 | $298,000 | $389,500 |

---

## Summary: What You Get for the Trade-offs

| You Give Up | You Save |
|-------------|----------|
| 8% battery capacity | $84,900 at 10k units |
| Auto-resonance haptics | Simpler firmware, fewer components |
| EPSON brand TCXO | Same performance, lower cost |
| Same-day shipping | 5-10 day lead time (plan ahead) |

**Bottom line:** Trade-offs are minor, savings are substantial. Optimized design recommended for all volumes.

---

## Files Reference

| File | Description |
|------|-------------|
| `design-specification-original.md` | Original full-featured design |
| `design-specification.md` | Optimized design (recommended) |
| `decision-log.md` | Detailed trade-off analysis |
| `bom-with-pricing.md` | Optimized BOM with part numbers |
| `cost-analysis.md` | Volume pricing breakdown |
| `supplier-comparison.md` | Sourcing options |
| `cost-comparison-before-after.md` | This file |
