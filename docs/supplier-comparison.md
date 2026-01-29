# Supplier Comparison - Key Components

## nRF52840-QIAA-R (MCU)

### Price Comparison

| Supplier | Type | 1 pc | 100 pc | 1,000 pc | 10,000 pc | Stock |
|----------|------|------|--------|----------|-----------|-------|
| **LCSC** | Authorized | $3.09 | $2.85 | $2.50 | $2.20 | 914 |
| **Utsource** | Broker | $2.62 | $2.40 | $2.36 | RFQ | Yes |
| **Win-Source** | Broker | ~$2.50 | RFQ | RFQ | RFQ | Yes |
| DigiKey | Authorized | $5.47 | $4.38 | $3.83 | $3.35 | 8,000+ |
| Mouser | Authorized | $5.47 | $4.38 | $3.83 | RFQ | 6,000+ |
| Arrow | Authorized | $5.15 | $4.12 | $3.61 | RFQ | Yes |

### Recommendation
- **Prototype:** LCSC ($3.09)
- **Production:** Utsource/LCSC ($2.36-2.50)
- **Risk-averse:** DigiKey ($3.83 but guaranteed genuine)

### Links
- LCSC: https://www.lcsc.com/product-detail/C190794.html
- DigiKey: https://www.digikey.com/en/products/detail/nordic-semiconductor-asa/NRF52840-QIAA-R/7725407
- Utsource: https://www.utsource.net/itm/p/8406894.html
- Octopart: https://octopart.com/nrf52840-qiaa-r-nordic+semiconductor-76957979

---

## SX1262IMLTRT (LoRa Transceiver)

### Price Comparison

| Supplier | Type | 1 pc | 100 pc | 1,000 pc | 10,000 pc | Stock |
|----------|------|------|--------|----------|-----------|-------|
| **LCSC** | Authorized | $1.62 | $1.45 | $1.30 | $1.10 | 1,892 |
| Alibaba | Wholesale | $1.50 | ~$1.20 | RFQ | RFQ | Varies |
| DigiKey | Authorized | $5.89 | $4.71 | $4.12 | $3.60 | 3,000+ |
| Mouser | Authorized | $5.89 | $4.71 | $4.12 | RFQ | 2,500+ |
| Arrow | Authorized | $6.52 | $5.20 | $4.43 | RFQ | Yes |
| Future | Authorized | $4.13 | $3.50 | $2.80 | RFQ | 3,000+ |

### Recommendation
- **All volumes:** LCSC ($1.30-1.62) - significantly cheaper than alternatives
- LCSC pricing is 60-75% lower than DigiKey/Mouser

### Links
- LCSC: https://www.lcsc.com/product-detail/C191341.html
- DigiKey: https://www.digikey.com/en/products/detail/semtech-corporation/SX1262IMLTRT/8564369
- Alibaba: https://www.alibaba.com/product-detail/SX1262IMLTRT-QFN-24-22dBm-Long-range_1601498969915.html
- Octopart: https://octopart.com/sx1262imltrt-semtech-78879753

---

## Combined Savings: LCSC vs DigiKey

### At 1,000 Units

| Component | DigiKey | LCSC | Savings |
|-----------|---------|------|---------|
| nRF52840 | $3.83 | $2.50 | $1.33 |
| SX1262 | $4.12 | $1.30 | $2.82 |
| **Per Unit** | $7.95 | $3.80 | **$4.15** |
| **1,000 Units** | $7,950 | $3,800 | **$4,150** |

### At 10,000 Units

| Component | DigiKey | LCSC | Savings |
|-----------|---------|------|---------|
| nRF52840 | $3.35 | $2.20 | $1.15 |
| SX1262 | $3.60 | $1.10 | $2.50 |
| **Per Unit** | $6.95 | $3.30 | **$3.65** |
| **10,000 Units** | $69,500 | $33,000 | **$36,500** |

---

## Risk Assessment

### LCSC
- **Risk Level:** Low
- **Pros:** Authorized distributor, good QC, JLCPCB integration
- **Cons:** Shipping from China (5-10 days), stock fluctuations
- **Recommendation:** Safe for production use

### Utsource / Win-Source
- **Risk Level:** Medium
- **Pros:** Lower prices, large inventory
- **Cons:** Broker (not direct from manufacturer), verify authenticity
- **Recommendation:** Request COC (Certificate of Conformance), test samples first

### AliExpress / Alibaba
- **Risk Level:** Medium-High
- **Pros:** Lowest prices
- **Cons:** Counterfeit risk, inconsistent quality, no warranty
- **Recommendation:** Only for non-critical prototypes, always test thoroughly

### DigiKey / Mouser / Arrow
- **Risk Level:** None
- **Pros:** Guaranteed authentic, same-day shipping, excellent support
- **Cons:** Higher prices
- **Recommendation:** Use when authenticity is critical or speed is essential

---

## Counterfeit Detection Tips

### For nRF52840
1. Check laser marking quality and font
2. Verify QFN package dimensions (7x7mm exactly)
3. Program and check Device ID matches Nordic database
4. Test BLE/USB functionality

### For SX1262
1. Verify QFN-24 package (4x4mm)
2. Check marking "SX1262" on top
3. Test RF output power (+22dBm spec)
4. Verify SPI communication and register values

---

## Order Strategy

### For 100 Units (Pilot Run)
```
1. Order from LCSC
2. Pay for expedited shipping
3. Inspect and test 10% of ICs before assembly
4. Keep DigiKey as backup source
```

### For 1,000+ Units (Production)
```
1. Split order: 70% LCSC, 30% backup source
2. Request lot/date code consistency
3. Incoming inspection procedure
4. Maintain 2-week safety stock
```

### For 10,000+ Units (Scale)
```
1. Request direct quotes from Nordic and Semtech
2. Negotiate pricing through distribution agreement
3. Consider consignment inventory at CM
4. Establish secondary source qualification
```

---

## Contact Information

### LCSC Electronics
- Website: https://www.lcsc.com
- Support: service@lcsc.com
- MOQ: Usually 1 pc

### Utsource
- Website: https://www.utsource.net
- Support: sales@utsource.net
- MOQ: Varies by part

### DigiKey
- Website: https://www.digikey.com
- Support: 1-800-344-4539
- MOQ: Usually 1 pc

### Nordic Semiconductor (Direct)
- Website: https://www.nordicsemi.com
- Sales: sales@nordicsemi.no
- MOQ: Typically 1,000+ for direct pricing

### Semtech (Direct)
- Website: https://www.semtech.com
- Distribution: Through authorized channels
- MOQ: Typically 3,000+ reels
