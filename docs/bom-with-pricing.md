# Bill of Materials with Pricing

## Optimized BOM - nRF52840 + SX1262 PCB

### Cost Optimizations Applied
- Removed LTC4412 ideal diode controller (using Schottky diode instead)
- Using DRV2603 instead of DRV2605L for haptics
- Using cheaper TCXO alternative (YXC/TXC vs EPSON)

---

## ICs & Active Components

| Qty | Ref | Component | Part Number | Package | Recommended Source |
|-----|-----|-----------|-------------|---------|-------------------|
| 1 | U1 | MCU | NRF52840-QIAA-R | QFN-73 | LCSC / Utsource |
| 1 | U2 | LoRa Transceiver | SX1262IMLTRT | QFN-24 | LCSC |
| 1 | U3 | 3.3V LDO | AP2112K-3.3TRG1 | SOT-23-5 | LCSC |
| 1 | U4 | Battery Charger | MCP73831T-2ACI/OT | SOT-23-5 | LCSC |
| 1 | U5 | Haptic Driver | DRV2603RUNR | SON-8 | LCSC / DigiKey |
| 1 | D1 | ESD Protection | USBLC6-2P6 | SOT-666 | LCSC |
| 1 | D2 | Schottky Diode | SS14 | SMA | LCSC |

---

## Crystals & Oscillators

| Qty | Ref | Component | Part Number | Package | Recommended Source |
|-----|-----|-----------|-------------|---------|-------------------|
| 1 | Y1 | 32MHz Crystal | NX2016SA-32MHZ-EXS00A | 2016 | LCSC |
| 1 | Y2 | 32.768kHz Crystal | ABS07-32.768KHZ-T | 3215 | LCSC |
| 1 | Y3 | 32MHz TCXO | YXC YSO110TR / TXC 7Q-32.000MBG-T | 2016 | LCSC |

---

## Connectors

| Qty | Ref | Component | Part Number | Package | Recommended Source |
|-----|-----|-----------|-------------|---------|-------------------|
| 1 | J1 | USB-C | USB4105-GF-A | 16-pin SMD | LCSC |
| 1 | J2 | Battery JST | B2B-PH-K-S(LF)(SN) | 2-pin TH | LCSC |
| 1 | J3 | U.FL Antenna | U.FL-R-SMT-1(10) | SMD | LCSC |
| 1 | J4 | SWD Header | 20021121-00006C4LF | 6-pin 1.27mm | LCSC |
| 1 | J5 | Expansion Header | 640456-8 | 8-pin 2.54mm | LCSC |
| 1 | J6 | LRA Connector | 2.54-2P-LT | 2-pin 2.54mm | LCSC |

---

## Capacitors

| Qty | Ref | Value | Package | Notes |
|-----|-----|-------|---------|-------|
| 6 | C1,C2,C3,C4,C15,C19 | 10uF | 0805 | Decoupling |
| 2 | C9,C10 | 4.7uF | 1206 | Bulk capacitors |
| 2 | C11,C12 | 18pF | 0402 | 32MHz crystal load |
| 2 | C13,C14 | 12.5pF | 0402 | 32.768kHz crystal load |
| 7 | C5,C6,C7,C8,C16,C18,C20 | 100nF | 0805/0402 | Decoupling |
| 1 | C17 | 2.2pF | 0402 | RF matching |

---

## Resistors

| Qty | Ref | Value | Package | Notes |
|-----|-----|-------|---------|-------|
| 1 | R1 | 2k | 0603 | MCP73831 PROG (500mA) |
| 2 | R6,R7 | 5.1k | 0603 | USB-C CC pulldowns |
| 2 | R9,R10 | 0 ohm | 0603 | Antenna selection jumpers |
| 2 | R2,R3 | 1k | 0603 | LED current limiting |
| 1 | R11 | 1k | 0603 | Buzzer base resistor |
| 1 | R12 | 1k | 0603 | DIO1 series resistor |
| 4 | R4,R5,R8,R13 | 10k | 0603 | Pull-up resistors |
| 2 | R14,R15 | 4.7k | 0603 | I2C pull-ups |

---

## Inductors

| Qty | Ref | Value | Package | Notes |
|-----|-----|-------|---------|-------|
| 1 | L1 | 4.7nH | 0402 | RF matching |
| 1 | L2 | 10uH | 0805 | nRF52840 DC-DC (if needed) |

---

## Other Components

| Qty | Ref | Component | Part Number | Package |
|-----|-----|-----------|-------------|---------|
| 2 | LED1,LED2 | LED Green/Red | 150060xS75000 | 0603 |
| 1 | SW1 | Push Button | B3FS-1050P | 6x6mm |
| 5 | TP1-TP5 | Test Point | Generic | SMD pad |
| 1 | M1 | LRA Motor | Jinlong G0832012D | 8mm coin |

---

## Pricing by Volume

### Per-Unit Component Costs

| Component | 1 pc | 100 pcs | 1,000 pcs | 10,000 pcs |
|-----------|------|---------|-----------|------------|
| NRF52840-QIAA-R | $3.10 | $2.80 | $2.36 | $2.00 |
| SX1262IMLTRT | $1.62 | $1.45 | $1.30 | $1.10 |
| AP2112K-3.3TRG1 | $0.10 | $0.08 | $0.06 | $0.05 |
| MCP73831T-2ACI/OT | $0.50 | $0.40 | $0.32 | $0.25 |
| DRV2603RUNR | $0.80 | $0.65 | $0.55 | $0.45 |
| USBLC6-2P6 | $0.10 | $0.07 | $0.05 | $0.04 |
| SS14 | $0.02 | $0.015 | $0.01 | $0.008 |
| 32MHz Crystal | $0.25 | $0.18 | $0.13 | $0.10 |
| 32.768kHz Crystal | $0.30 | $0.22 | $0.15 | $0.12 |
| 32MHz TCXO | $0.80 | $0.60 | $0.45 | $0.35 |
| USB-C Connector | $0.80 | $0.55 | $0.40 | $0.35 |
| JST Battery | $0.15 | $0.10 | $0.08 | $0.06 |
| U.FL Connector | $0.50 | $0.35 | $0.25 | $0.20 |
| SWD Header | $0.40 | $0.30 | $0.22 | $0.18 |
| 8-pin Header | $0.20 | $0.15 | $0.10 | $0.08 |
| LRA Connector | $0.05 | $0.03 | $0.02 | $0.015 |
| Capacitors (all 20) | $0.28 | $0.18 | $0.12 | $0.08 |
| Resistors (all 15) | $0.15 | $0.10 | $0.06 | $0.04 |
| Inductor 4.7nH | $0.05 | $0.03 | $0.02 | $0.015 |
| LEDs (2) | $0.06 | $0.04 | $0.03 | $0.02 |
| Buttons (2) | $0.40 | $0.24 | $0.16 | $0.12 |
| Test Points (5) | $0.10 | $0.06 | $0.04 | $0.03 |
| LRA Motor | $1.00 | $0.70 | $0.50 | $0.40 |
| **BOM TOTAL** | **$11.73** | **$9.41** | **$7.38** | **$6.01** |

---

## Supplier Recommendations

### Primary: LCSC Electronics
- Best pricing for most components
- Ships from China (5-10 days to US/EU)
- JLCPCB integration for assembly

### Secondary: DigiKey / Mouser
- Faster shipping (same day)
- Guaranteed authentic parts
- Higher prices but reliable

### For High Volume (1000+): Request Quotes From
- Utsource (nRF52840)
- Arrow Electronics (SX1262)
- Future Electronics
- Direct from Nordic/Semtech

---

## LCSC Part Numbers (for JLCPCB Assembly)

| Component | LCSC Part # |
|-----------|-------------|
| NRF52840-QIAA-R | C190794 |
| SX1262IMLTRT | C191341 |
| AP2112K-3.3TRG1 | C51118 |
| MCP73831T-2ACI/OT | C14879 |
| USBLC6-2P6 | C558442 |
| USB4105-GF-A | C2688138 |
| B2B-PH-K-S | C131337 |
| 20021121-00006C4LF | C178291 |
| X1G0042110003 (TCXO) | C3013793 |
| 2.54-2P-LT | C722697 |
| LTC4412MPS6#TRPBF | C688483 (REMOVED - using D2 Schottky instead) |
