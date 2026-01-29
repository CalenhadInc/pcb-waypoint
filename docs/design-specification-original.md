# nRF52840 + SX1262 PCB Design Specification (ORIGINAL)

## Status: Original Full-Featured Design
This is the initial design before cost optimizations were applied.
See `design-specification.md` for the optimized version.
See `decision-log.md` for trade-off analysis.

---

## Board Parameters
- **Dimensions:** 46mm x 62mm
- **Layers:** 2-layer FR4
- **Thickness:** 1.6mm
- **Copper:** 1oz (35um)
- **Finish:** HASL or ENIG
- **Min trace/space:** 0.15mm / 0.15mm (6mil)

---

## Power Architecture (Original - Full Featured)

### Block Diagram

```
USB-C 5V ──┬── [MCP73831] ── LiPo+
           │        │
           │    [LiPo 3.7V]
           │        │
           └────────┴── [LTC4412 Ideal Diode] ── [AP2112K-3.3] ── 3.3V Rail
                                                       │
                                             ┌─────────┴─────────┐
                                             ↓                   ↓
                                        nRF52840             SX1262
```

### Power Components (Original)

| Component | Part Number | Package | Function | Cost |
|-----------|-------------|---------|----------|------|
| LDO | AP2112K-3.3TRG1 | SOT-23-5 | 3.3V @ 600mA | $0.10 |
| Charger | MCP73831T-2ACI/OT | SOT-23-5 | 500mA charge | $0.50 |
| **Ideal Diode** | **LTC4412MPS6#TRPBF** | SOT-23-6 | USB/Battery switching | **$6.99** |
| Battery connector | B2B-PH-K-S(LF)(SN) | 2-pin TH | JST-PH LiPo | $0.15 |
| USB-C | USB4105-GF-A | 16-pin SMD | USB 2.0 receptacle | $0.80 |
| ESD protection | USBLC6-2P6 | SOT-666 | USB ESD | $0.10 |

### LTC4412 Connections

| Pin | Name | Connection |
|-----|------|------------|
| 1 | GND | Ground |
| 2 | SENSE | USB VBUS (through sense resistor) |
| 3 | GATE | P-FET gate (external MOSFET) |
| 4 | CTL | Control input (tie to GND for auto) |
| 5 | STAT | Status output (optional, to GPIO) |
| 6 | VIN | USB VBUS |

**Note:** LTC4412 requires external P-FET (e.g., SI2301) for load switching.

---

## nRF52840 Section

### Part: nRF52840-QIAA-R7 (QFN-73, 7x7mm)

*Same as optimized version - no changes*

### Crystal Oscillators

| Function | Part | Frequency | Package | Cost |
|----------|------|-----------|---------|------|
| HF Crystal | NX2016SA-32M-EXS00A-CS08760 | 32.000 MHz | 2.0x1.6mm | $0.25 |
| LF Crystal | ABS07-32.768KHZ-7-T | 32.768 kHz | 3.2x1.5mm | $0.30 |

### nRF52840 Pin Assignments

**SX1262 SPI (Port 1):**

| Signal | Pin | GPIO |
|--------|-----|------|
| SX_NSS | 43 | P1.10 |
| SX_SCK | 44 | P1.11 |
| SX_MOSI | 45 | P1.12 |
| SX_MISO | 46 | P1.13 |
| SX_BUSY | 47 | P1.14 |
| SX_DIO1 | 48 | P1.15 |
| SX_RESET | 9 | P1.06 |

**USB:**

| Signal | Pin | GPIO |
|--------|-----|------|
| USB D- | 33 | D- |
| USB D+ | 34 | D+ |

**User Interface:**

| Signal | Pin | GPIO |
|--------|-----|------|
| LED1 (Green) | 15 | P0.13 |
| LED2 (Red) | 16 | P0.14 |
| BUTTON1 | 17 | P0.15 |
| BUTTON2 | 20 | P0.16 |

**Haptic (I2C for DRV2605L):**

| Signal | Pin | GPIO |
|--------|-----|------|
| SDA | 4 | P0.26 |
| SCL | 5 | P0.27 |
| HAPTIC_EN | 7 | P0.04 |

**Debug/Programming (SWD):**

| Signal | Pin | GPIO |
|--------|-----|------|
| SWDIO | 26 | SWDIO |
| SWDCLK | 25 | SWDCLK |
| RESET | 18 | P0.18 |

---

## SX1262 Section

### Part: SX1262IMLTRT (QFN-24, 4x4mm)

### Clock: 32MHz TCXO (Original - Premium)

| Part | Package | Stability | Voltage | Cost |
|------|---------|-----------|---------|------|
| **EPSON X1G0042110003** | 2.5x2.0mm | ±2.5ppm | 1.8V (from DIO3) | **$2.50** |

*TCXO controlled by DIO3 - configure in software*

### Antenna Matching Network (915 MHz)

| Ref | Value | Package | Notes |
|-----|-------|---------|-------|
| C_MATCH1 | 3.0pF | 0402 | Series to antenna |
| L_MATCH1 | 6.8nH | 0402 | Shunt to GND |
| C_MATCH2 | 3.3pF | 0402 | Shunt to GND |

---

## Haptic Feedback Section (Original - Full Featured)

### Driver: DRV2605L (Closed-loop with effects library)

| Spec | Value |
|------|-------|
| Part | **DRV2605LDGSR** |
| Package | WSON-10 (3x3mm) |
| Interface | I2C |
| Features | Auto-resonance tracking, 123 haptic effects library |
| Supply | 2.5V - 5.5V (use 3.3V) |
| Output | Up to 300mA peak |
| **Cost** | **$1.15** |

### DRV2605L Connections

| Pin | Name | Connection |
|-----|------|------------|
| 1 | VDD | 3.3V |
| 2 | GND | Ground |
| 3 | SDA | nRF52840 P0.26 |
| 4 | SCL | nRF52840 P0.27 |
| 5 | EN | nRF52840 P0.04 |
| 6 | IN/TRIG | NC (using I2C mode) |
| 7 | OUT+ | LRA+ |
| 8 | OUT- | LRA- |
| 9 | REG | 1uF to GND |
| 10 | VDD | 3.3V |

### LRA Motor

| Part | Size | Resonant Freq | Cost |
|------|------|---------------|------|
| Jinlong G0832012D | 8x3.2mm | 235 Hz | $1.00 |

### DRV2605L Software Features

Built-in effect library includes:
- Effect 1: Strong click (100%)
- Effect 7: Soft bump (60%)
- Effect 14: Sharp tick
- Effect 27: Short double click
- Effect 47: Buzz (1 sec)
- ...and 118 more effects

Typical I2C sequence:
```
1. Set EN high
2. Write mode register (0x01) to exit standby
3. Write waveform register (0x04) with effect number
4. Write GO register (0x0C) to trigger
```

---

## User Interface (Original)

### LEDs

| Ref | Color | Part Number | Resistor | Cost |
|-----|-------|-------------|----------|------|
| LED1 | Green | 150060VS75000 (Wurth) | 1k (0402) | $0.03 |
| LED2 | Red | 150060RS75000 (Wurth) | 1k (0402) | $0.03 |

### Buttons (Original - 2 buttons)

| Ref | Function | Part Number | Cost |
|-----|----------|-------------|------|
| SW1 | User button | B3FS-1050P | $0.20 |
| **SW2** | **Reset button** | B3FS-1050P | **$0.20** |

*10k pull-up resistors (0402) to 3.3V, 100nF debounce caps*

---

## Connectors

### Programming Header (2x3, 1.27mm pitch)

```
+---+---+
|VCC|SWD|  1: VCC (3.3V)
+---+---+  2: SWDIO
|GND|CLK|  3: GND
+---+---+  4: SWDCLK
|GND|RST|  5: GND
+---+---+  6: RESET
```

**Part:** Amphenol 20021121-00006C4LF

### Expansion Header (1x8, 2.54mm pitch)

```
1: VCC (3.3V)
2: GND
3: SDA (P0.26)
4: SCL (P0.27)
5: TX (P0.06)
6: RX (P0.08)
7: GPIO (P0.04)
8: GPIO (P0.05)
```

---

## Original BOM Summary

| Qty | Reference | Value/Part | Package | Cost Each |
|-----|-----------|------------|---------|-----------|
| 1 | U1 | nRF52840-QIAA-R | QFN-73 | $3.10 |
| 1 | U2 | SX1262IMLTRT | QFN-24 | $4.15 |
| 1 | U3 | AP2112K-3.3TRG1 | SOT-23-5 | $0.10 |
| 1 | U4 | MCP73831T-2ACI/OT | SOT-23-5 | $0.50 |
| 1 | **U5** | **LTC4412MPS6#TRPBF** | SOT-23-6 | **$6.99** |
| 1 | **U6** | **DRV2605LDGSR** | WSON-10 | **$1.15** |
| 1 | D1 | USBLC6-2P6 | SOT-666 | $0.10 |
| 1 | Y1 | NX2016SA-32MHZ | 2016 | $0.25 |
| 1 | Y2 | ABS07-32.768KHZ-T | 3215 | $0.30 |
| 1 | **Y3** | **X1G0042110003 (EPSON)** | 2520 | **$2.50** |
| 1 | L1 | 4.7nH | 0402 | $0.05 |
| 1 | J1 | USB4105-GF-A | 16-pin SMD | $0.80 |
| 1 | J2 | B2B-PH-K-S | 2-pin TH | $0.15 |
| 1 | J3 | U.FL-R-SMT-1 | SMD | $0.50 |
| 1 | J4 | 20021121-00006C4LF | 6-pin 1.27mm | $0.40 |
| 1 | J5 | 640456-8 | 8-pin 2.54mm | $0.20 |
| 1 | J6 | 2.54-2P-LT | 2-pin 2.54mm | $0.05 |
| 2 | LED1,2 | 150060xS75000 | 0603 | $0.03 |
| **2** | **SW1,2** | **B3FS-1050P** | 6x6mm | **$0.20** |
| 1 | M1 | Jinlong G0832012D | 8mm coin | $1.00 |
| - | Capacitors | Various | 0402-0805 | $0.28 |
| - | Resistors | Various | 0402-0603 | $0.15 |

---

## Original Cost Summary

### Per-Unit BOM Cost (at 1 unit pricing)

| Category | Cost |
|----------|------|
| ICs (U1-U6, D1) | $16.09 |
| Crystals/Oscillators | $3.05 |
| Connectors | $2.10 |
| Passives | $0.48 |
| UI (LEDs, Buttons) | $0.46 |
| LRA Motor | $1.00 |
| **Total BOM** | **$23.18** |

### Comparison: Original vs Optimized

| Item | Original | Optimized | Savings |
|------|----------|-----------|---------|
| LTC4412 | $6.99 | $0.02 (SS14) | $6.97 |
| DRV2605L | $1.15 | $0.55 (DRV2603) | $0.60 |
| EPSON TCXO | $2.50 | $0.45 (YXC) | $2.05 |
| 2nd Button | $0.20 | $0 | $0.20 |
| DigiKey → LCSC | - | - | $4.15 |
| **BOM Total** | **$23.18** | **$11.53** | **$11.65** |

---

## When to Use Original Design

Consider the original full-featured design when:

1. **Battery life is critical** - LTC4412 eliminates diode voltage drop
2. **Premium haptic experience needed** - DRV2605L has better effects
3. **Tight RF timing required** - EPSON TCXO is more reliable
4. **Hardware reset button needed** - Some users prefer physical reset
5. **Budget is not primary concern** - Focus on features over cost

---

## Files Reference

| File | Description |
|------|-------------|
| `design-specification-original.md` | This file (original design) |
| `design-specification.md` | Optimized/final design |
| `decision-log.md` | Trade-off analysis for each change |
| `bom-with-pricing.md` | Optimized BOM with volume pricing |
| `cost-analysis.md` | Full cost breakdown |
| `supplier-comparison.md` | Component sourcing options |
