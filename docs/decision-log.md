# Design Decision Log

## Overview

This document tracks the original design options, adapted choices, and trade-offs made during the nRF52840 + SX1262 PCB design process.

---

## Decision 1: PCB Layer Count

| Option | Cost | Performance | Chosen |
|--------|------|-------------|--------|
| **2-layer** | ~$0.50/unit | Adequate for this design | YES |
| 4-layer | ~$1.50/unit | Better RF, easier routing | NO |

**Trade-off:** 2-layer saves ~$1/unit but requires more careful RF layout. Acceptable for this board size and complexity.

**Mitigation:** Maximize ground pour on bottom layer, use ground stitching vias around RF sections.

---

## Decision 2: Power Management Architecture

### Original Option: LTC4412 Ideal Diode Controller

| Spec | Value |
|------|-------|
| Part | LTC4412MPS6#TRPBF |
| Cost | $6.99/unit |
| Function | Automatic USB/battery switching with near-zero voltage drop |
| Pros | Seamless power switching, no power loss |
| Cons | Expensive, adds complexity |

### Adapted Option: Separate Rails (No Diode)

| Spec | Value |
|------|-------|
| Part | None (D2 removed) |
| Cost | $0.00/unit |
| Function | USB charges battery only, system runs from battery |
| Pros | Safe, simple, no voltage drop |
| Cons | System always runs from battery (even when USB connected) |

**Decision: Remove D2, use separate rails**

**Trade-off Analysis:**
- Saves: **$6.99/unit** ($6,990 at 1000 units) vs LTC4412
- No voltage drop on battery path
- USB 5V only goes to charger (MCP73831), never to system
- Battery (3.0-4.2V) directly powers LDO
- Eliminates safety hazard (original D2 design allowed 4.5V on battery)

**Why D2 was removed (Jan 2026 review):**
The original SS14 Schottky design had a critical bug - J2 (battery connector) was on the VBUS net, meaning battery saw USB 5V directly. This was a safety hazard. Rather than fix the diode placement, we switched to separate rails architecture which is simpler and inherently safe.

**Power Architecture:**
```
USB 5V ──► MCP73831 (charger) ──► Battery (J2)
                                      │
                                      ▼
                                  AP2112K (LDO) ──► 3.3V
```

---

## Decision 3: Haptic Driver

### Original Option: DRV2605L (Full-featured)

| Spec | Value |
|------|-------|
| Part | DRV2605LDGSR |
| Cost | $1.15/unit |
| Interface | I2C |
| Features | Auto-resonance, 123 built-in effects, closed-loop |
| Pros | Best haptic quality, easy software integration |
| Cons | Higher cost, requires I2C setup |

### Adapted Option: DRV2603 (Open-loop)

| Spec | Value |
|------|-------|
| Part | DRV2603RUNR |
| Cost | $0.55/unit (est.) |
| Interface | PWM + EN pin |
| Features | Open-loop drive, basic operation |
| Pros | Cheaper, simpler PWM control |
| Cons | No auto-resonance, must tune frequency manually |

### Alternative Considered: ERM Motor + Transistor

| Spec | Value |
|------|-------|
| Parts | 2N7002 + ERM motor |
| Cost | $0.15/unit |
| Interface | GPIO + PWM |
| Features | Simple DC motor drive |
| Pros | Cheapest, simplest |
| Cons | Buzzy feel, slower response, less precise |

**Decision: DRV2603 (middle ground)**

**Trade-off Analysis:**
- DRV2605L → DRV2603 saves: **$0.60/unit**
- Loses: Auto-resonance tracking, effect library
- Keeps: LRA support, decent haptic quality

**When to reconsider:**
- Need premium haptics → use DRV2605L
- Need cheapest possible → use ERM + transistor

---

## Decision 4: TCXO Selection

### Original Option: EPSON X1G0042110003

| Spec | Value |
|------|-------|
| Part | X1G0042110003 |
| Cost | $2.50/unit |
| Stability | ±2.5ppm |
| Pros | High quality, well-documented |
| Cons | Expensive, extended part on LCSC |

### Adapted Option: YXC/TXC Generic TCXO

| Spec | Value |
|------|-------|
| Part | YXC YSO110TR or TXC 7Q-32.000MBG-T |
| Cost | $0.45-0.80/unit |
| Stability | ±2.5ppm |
| Pros | Much cheaper, same specs |
| Cons | Less documentation, verify footprint |

**Decision: Use cheaper TCXO**

**Trade-off Analysis:**
- Saves: **$1.70-2.05/unit**
- Risk: Slightly less documentation, may need footprint verification
- Mitigation: Order samples first, verify SX1262 lock and frequency accuracy

---

## Decision 5: Battery Charger IC

### Original Option: MCP73831

| Spec | Value |
|------|-------|
| Part | MCP73831T-2ACI/OT |
| Cost | $0.50/unit |
| Package | SOT-23-5 |
| Current | Programmable via resistor |
| Pros | Small, accurate, well-documented |

### Alternative Considered: TP4056

| Spec | Value |
|------|-------|
| Part | TP4056 |
| Cost | $0.15-0.30/unit |
| Package | SOP-8 (larger) |
| Current | Programmable via resistor |
| Pros | Cheaper, thermal regulation |
| Cons | Larger footprint |

**Decision: Keep MCP73831**

**Reasoning:** Small form factor matters for 46x62mm board. $0.20-0.35 savings not worth larger footprint.

**When to reconsider:** If board size increases or cost is extremely tight.

---

## Decision 6: Component Sourcing Strategy

### Option A: Authorized Only (DigiKey/Mouser)

| Aspect | Value |
|--------|-------|
| nRF52840 @ 1000 | $3.83 |
| SX1262 @ 1000 | $4.12 |
| Total for both | $7.95 |
| Risk | None - guaranteed genuine |
| Lead time | Same day shipping |

### Option B: LCSC (Authorized, China)

| Aspect | Value |
|--------|-------|
| nRF52840 @ 1000 | $2.50 |
| SX1262 @ 1000 | $1.30 |
| Total for both | $3.80 |
| Risk | Low - authorized distributor |
| Lead time | 5-10 days from China |

### Option C: Brokers (Utsource, AliExpress)

| Aspect | Value |
|--------|-------|
| nRF52840 @ 1000 | $2.36 |
| SX1262 @ 1000 | ~$1.20 |
| Total for both | ~$3.56 |
| Risk | Medium - verify authenticity |
| Lead time | 7-14 days |

**Decision: LCSC as primary source**

**Trade-off Analysis:**
- LCSC vs DigiKey saves: **$4.15/unit** on just these two ICs
- At 1000 units: **$4,150 saved**
- Risk is low (LCSC is authorized)
- Trade-off: Longer lead time, must plan ahead

---

## Decision 7: Antenna Implementation

### Option A: U.FL Connector Only

| Aspect | Value |
|--------|-------|
| Cost | $0.50 |
| Pros | Flexible, use any external antenna |
| Cons | Requires separate antenna purchase |

### Option B: PCB Antenna Only

| Aspect | Value |
|--------|-------|
| Cost | $0 (trace on PCB) |
| Pros | No extra parts, integrated |
| Cons | Fixed performance, takes board space |

### Option C: Both U.FL + PCB Antenna (with jumper)

| Aspect | Value |
|--------|-------|
| Cost | $0.50 + 0Ω resistors |
| Pros | Maximum flexibility |
| Cons | Slightly more complex |

**Decision: Both (Option C)**

**Reasoning:** U.FL for testing/certification, PCB antenna for production if adequate. 0Ω resistor jumpers allow selection.

---

## Decision 8: User Interface

### Buttons

| Original | Adapted |
|----------|---------|
| 2 buttons (User + Reset) | 2 buttons (kept) |
| Cost: $0.40 | Cost: $0.40 |

**Decision: Keep both buttons**

**Reasoning:** $0.20 savings not worth the usability trade-off. Reset button essential for:
- Quick reboot during development
- User recovery from crashes
- Bootloader entry (hold reset + power)

### LEDs

| Option | Cost | Decision |
|--------|------|----------|
| 2 LEDs (Green + Red) | $0.06 | Keep |
| 1 RGB LED | $0.15 | Not chosen |

**Reasoning:** Two discrete LEDs are simpler and cheaper than RGB.

---

## Summary: Total Optimization Savings

| Decision | Original | Adapted | Savings/Unit |
|----------|----------|---------|--------------|
| Power management | LTC4412 | Separate rails (no diode) | $6.99 |
| Haptic driver | DRV2603 | DRV2605L (kept) | -$0.60 |
| TCXO | EPSON | YXC/TXC | $1.70 |
| Sourcing (MCU+Radio) | DigiKey | LCSC | $4.15 |
| BLE Antenna | Linx ($4.21) | Johanson ($0.27) | $3.94 |
| Button | 2x | 2x (kept) | $0.00 |
| **TOTAL** | | | **$16.16** |

### Impact at Volume

| Volume | Savings |
|--------|---------|
| 100 units | $1,616 |
| 1,000 units | $16,160 |
| 10,000 units | $161,600 |

---

## Decisions NOT Changed (Kept Original)

| Component | Reason Kept |
|-----------|-------------|
| nRF52840 MCU | No viable alternative for BLE+USB+GPIO |
| SX1262 LoRa | Best in class for sub-GHz LoRa |
| MCP73831 charger | Small footprint worth the cost |
| AP2112K LDO | Cheap, reliable, right specs |
| USB-C connector | Standard, future-proof |
| LRA motor type | Better haptic feel than ERM |

---

## Decision 9: BLE Chip Antenna

### Options Considered

| Option | Part Number | Cost | Notes |
|--------|-------------|------|-------|
| **Johanson** | 2450AT18A100E | $0.27 | Smallest, cheapest |
| Abracon | ACAG1204-2450-T | $0.62 | Mid-range |
| Linx | ANT-2.45-CHP-x | $4.21 | Most expensive |

**Decision: Johanson 2450AT18A100E**

**Reasoning:** Cheapest option at $0.27, well-documented, proven design. Requires pi-match network.

**Matching Network:**
- L2 = 2.7nH (series inductor)
- C28 = 1.0pF (shunt capacitor to GND)

---

## Decision 10: LIS2DH12 I2C Address

| Option | SA0 Pin | Address | Chosen |
|--------|---------|---------|--------|
| **Address 0x18** | GND | 0x18 | YES |
| Address 0x19 | VDD | 0x19 | NO |

**Decision: SA0 → GND (address 0x18)**

**Reasoning:** No conflict with DRV2605L which has fixed address 0x5A. Either address would work, but 0x18 is the default per datasheet.

---

## Decision 11: SX1262 DC-DC Inductor Value

| Original Value | Correct Value |
|----------------|---------------|
| 47nH (WRONG) | **6.8µH** |

**Decision: Corrected L_SX1 to 6.8µH**

**Critical Fix:** The schematic had 47nH which is completely wrong for the SX1262 DC-DC converter. Per Semtech reference design, must be 6.8µH.

**Recommended Part:** Murata LQH32CN6R8M23 (6.8µH, 0603, 700mA, 0.28Ω DCR)

---

## Decision 12: Haptic Driver (Revised)

**Note:** Decision 3 originally specified DRV2603, but schematic uses **DRV2605LDGS**.

| Aspect | DRV2603 | DRV2605L |
|--------|---------|----------|
| Interface | PWM | I2C |
| Auto-resonance | No | Yes |
| Effect library | No | 123 effects |
| Cost | $0.55 | $1.15 |

**Current Implementation: DRV2605LDGS (I2C)**

**Reasoning:** I2C interface simpler for nRF52840 (no dedicated PWM needed), built-in effects reduce firmware complexity.

---

## Decision 13: nRF52840 DC-DC Inductor

| Parameter | Requirement | Selected |
|-----------|-------------|----------|
| Value | 10µH ±20% | 10µH |
| DCR | <0.5Ω | 0.35Ω |
| Isat | >50mA | 150mA |
| Package | 0805 | 0805 |

**Selected Part:** Murata LQM21PN100MGRD

**Decision:** Added L_DCDC1 between DCC (pin B3) and DCCH (pin AB2).

**Reasoning:** Nordic reference design uses this exact part. Required for internal DC-DC converter to function - was missing from original schematic.

---

## Decision 14: DRV2605 REG Capacitor

| Parameter | Value |
|-----------|-------|
| Capacitance | 1µF |
| Package | 0402 |

**Selected Part:** Standard 1µF ceramic (C27)

**Decision:** Added C27 on DRV2605 REG pin (pin 1).

**Reasoning:** DRV2605L datasheet recommends 1µF capacitor on internal regulator output for stability. Was missing from original schematic.

---

## Decision 15: Component Reference Standardization

**Date:** February 2026

During design review, several components had descriptive names that were changed to standard numbering:

| Original | Standard | Function |
|----------|----------|----------|
| R_GATE | R20 | Q1 gate pull-down (10kΩ) |
| R_ACC1 | R21 | Accelerometer INT1 pull-up (10kΩ) |
| D3 | D2 | Buzzer flyback diode (1N4148W) |

**Context:**
- The original D2 (SS14 Schottky in power path) was removed entirely (see Decision 2)
- D3 (flyback diode) was renumbered to D2 to fill the gap
- R_GATE and R_ACC1 were given standard R## designators for consistency

**Reasoning:** Standard numbering makes BOM generation cleaner and avoids confusion with pick-and-place files.

---

## Future Optimization Opportunities

If further cost reduction needed:

| Opportunity | Potential Savings | Trade-off |
|-------------|-------------------|-----------|
| Remove haptics entirely | $1.55/unit | Lose haptic feedback |
| Use ERM instead of LRA | $0.50/unit | Buzzy feel, slower |
| Single LED | $0.03/unit | Less status indication |
| Remove test points | $0.10/unit | Harder debugging |
| Smaller USB-C (6-pin) | $0.30/unit | No USB data, power only |
| Remove expansion header | $0.20/unit | Less flexibility |
