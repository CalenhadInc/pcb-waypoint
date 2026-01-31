# Design Review Changes - January 2026

## Overview
This document captures critical design issues identified during review and the recommended changes to be applied to the schematic.

---

## Critical Issues Summary

| # | Component | Issue | Priority | Status |
|---|-----------|-------|----------|--------|
| 1 | Q1 (Transistor) | Replace BJT with MOSFET | High | Pending |
| 2 | Q1 Gate | Add pull-down resistor | High | Pending |
| 3 | C15 | Unreasonably large, relocate or remove | Medium | Pending |
| 4 | Accelerometer INT | Floating interrupt line | High | Pending |
| 5 | SW1 | No debouncing circuit | Medium | Pending |
| 6 | Accelerometer Power | VDD not connected, C29 wrong | Critical | Pending |
| 7 | U3 (LDO) | Currently doing nothing | Critical | Pending |
| 8 | Battery Connector | Missing or misplaced | Critical | Pending |
| 9 | D2 (Schottky) | Remove - battery sees high voltage | Critical | Pending |
| 10 | J2 | Wrong connector type/placement | High | Pending |

---

## Detailed Issue Analysis

### Issue 1: Q1 Transistor - Replace with MOSFET

**Current State:**
- Part: MMBT3904TT1G (NPN BJT)
- Package: SC-75-3 (SOT-23 variant)
- Function: Buzzer driver switch

**Problem:**
- BJT requires continuous base current to stay on
- Less efficient for switching applications
- Voltage drop across collector-emitter

**Recommended Change:**
- Replace with: **BS170** (N-Channel MOSFET)
- Package: SOT-23 (SMD version: BS170F or 2N7002)
- Reason: Gate-driven (voltage controlled), lower on-resistance, more efficient for switching

**Alternative Parts (SMD):**
| Part Number | Package | Vds | Rds(on) | Notes |
|-------------|---------|-----|---------|-------|
| 2N7002 | SOT-23 | 60V | 2-5Ω | Very common, cheap |
| BS170F | SOT-23 | 60V | 1.2Ω | Direct BS170 SMD equivalent |
| DMN2056U | SOT-23 | 20V | 0.1Ω | Low Rds(on), higher current |
| AO3400 | SOT-23 | 30V | 0.03Ω | Excellent for switching |

**Recommendation:** Use **2N7002** or **AO3400** for availability and cost.

---

### Issue 2: MOSFET Gate Pull-Down Resistor

**Current State:**
- No pull-down on transistor base/gate
- Gate may float during MCU reset/boot

**Problem:**
- Floating gate can cause undefined buzzer behavior during power-up
- MOSFET gate has high impedance - susceptible to noise

**Recommended Change:**
- Add **10kΩ pull-down resistor** from MOSFET gate to GND
- Designator: R_GATE (new component)
- Package: 0402 or 0603

**Circuit Update:**
```
P0.17 (nRF52840) ──[1k]──┬── MOSFET Gate
                         │
                        [10k]
                         │
                        GND
```

---

### Issue 3: C15 Capacitor - Too Large

**Current State:**
- C15: 10uF, 0805 package
- Location: Unknown/unspecified in current docs

**Problem:**
- 10uF is excessive for most bypass/decoupling applications
- May be placed incorrectly

**Recommended Change - Option A (Remove):**
- Remove C15 entirely if not needed for specific function

**Recommended Change - Option B (Relocate):**
- Move C15 to VBAT input of AP2112K-3.3 LDO
- Provides bulk capacitance for battery input filtering
- Helps with transient response during load changes

**Decision:** Relocate to LDO VBAT input or remove entirely.

---

### Issue 4: Accelerometer Interrupt Floating

**Current State:**
- LIS2DH12TR INT1 connected to P0.11 (nRF52840)
- No pull-up/pull-down resistor specified
- Design spec mentions "R_ACC1: 10k (optional)" but may not be implemented

**Problem:**
- LIS2DH12 interrupt pins are **open-drain** outputs
- Without pull-up, the line will float when not actively driven low
- Causes undefined readings, potential false triggers, increased power consumption

**Recommended Change:**
- Add **10kΩ pull-up resistor** from INT1 to VDD (3.3V)
- Designator: R_ACC_PU (or R_ACC1 if using existing designator)
- Package: 0402

**Circuit Update:**
```
              VDD (3.3V)
                │
              [10k] R_ACC_PU
                │
LIS2DH12 INT1 ──┴── P0.11 (nRF52840)
```

**Reference:** LIS2DH12 Datasheet Section 7.3 - "INT1 and INT2 are open-drain outputs"

---

### Issue 5: SW1 Button Debouncing

**Current State:**
- SW1: B3FS-1050P tactile switch
- 10k pull-up to VDD
- 100nF debounce cap (mentioned in design spec)

**Problem:**
- Depending on user interaction frequency, current debouncing may be insufficient
- Mechanical switches bounce for 5-50ms typically

**Recommended Change:**
- Verify 100nF capacitor is actually implemented
- Consider RC time constant: τ = R × C = 10kΩ × 100nF = 1ms
- For aggressive debouncing, increase to: **1µF** (τ = 10ms)

**Alternative Hardware Debounce Circuit:**
```
         VDD (3.3V)
           │
         [10k]
           │
SW1 ───────┼───────[1k]────── GPIO
           │         │
        [100nF]    [100nF]
           │         │
          GND       GND
```

**Note:** Software debouncing in firmware is also effective and saves components.

---

### Issue 6: Accelerometer Power Not Connected (CRITICAL)

**Current State:**
- LIS2DH12TR power pins may be floating
- C29 may be connected incorrectly

**Problem:**
- Accelerometer will not function without proper power connections
- **This is a critical error preventing the sensor from working**

**Required Connections (per LIS2DH12 datasheet):**
| Pin | Name | Required Connection |
|-----|------|---------------------|
| 1 | VDD | 3.3V |
| 5 | VDD_IO | 3.3V (can be same as VDD) |
| 3, 7, 12 | GND | Ground |

**Bypass Capacitors Required:**
- VDD: 100nF to GND (close to pin)
- VDD_IO: 100nF to GND (close to pin)

**Recommended Fix:**
1. Verify VDD and VDD_IO are connected to 3.3V rail
2. Verify all GND pins are connected
3. Check C29 placement - should be on VDD or VDD_IO, not floating
4. Add proper bypass capacitors if missing

---

### Issue 7: U3 (AP2112K LDO) Doing Nothing (CRITICAL)

**Current State:**
- U3: AP2112K-3.3TRG1 (3.3V LDO)
- Apparently not connected properly in schematic

**Problem:**
- LDO is the primary 3.3V power supply
- **Without this working, nothing on the board will function**

**Required Connections (per AP2112K datasheet):**
| Pin | Name | Connection |
|-----|------|------------|
| 1 | VIN | Input voltage (VBAT or USB 5V) |
| 2 | GND | Ground |
| 3 | EN | Enable (tie to VIN for always-on, or GPIO for power control) |
| 4 | NC | No connection |
| 5 | VOUT | 3.3V output rail |

**Bypass Capacitors Required:**
- VIN: 10µF ceramic to GND
- VOUT: 10µF ceramic to GND

**Recommended Fix:**
1. Connect VIN to power source (battery via protection circuit or USB)
2. Connect EN to VIN (or add enable control)
3. Connect VOUT to 3.3V net
4. Verify bypass capacitors are in place

---

### Issue 8: Battery Connector Missing (CRITICAL)

**Current State:**
- J2: B2B-PH-K-S(LF)(SN) - JST-PH 2-pin connector
- Design spec says this is the battery connector
- Reviewer indicates it's either missing or misplaced

**Problem:**
- Without battery connector, device cannot be powered by LiPo battery
- J2 may be at top of board (wrong location per reviewer)

**Recommended Fix:**
1. Verify J2 exists in schematic with correct pinout
2. Relocate to appropriate position near power management section
3. Ensure proper connections:
   - Pin 1: VBAT (positive)
   - Pin 2: GND (negative)

**Physical Location Recommendation:**
- Near charger IC (MCP73831)
- Near power input section
- Away from RF sections

---

### Issue 9: D2 (Schottky Diode) - Remove (CRITICAL)

**Current State:**
- D2: SS14 Schottky diode
- Used for "battery backfeed protection"
- Connected between USB/Battery and LDO input

**Problem:**
- With current design, battery may see high voltage:
  - USB provides 5V
  - SS14 forward voltage drop: ~0.3-0.5V
  - Battery would see: 5V - 0.5V = **4.5V on VBAT**
- **LiPo batteries should NEVER exceed 4.2V**
- This is a safety hazard - could damage battery or cause fire

**Recommended Fix:**
- **Remove D2 completely**
- Implement proper power path management:

**Option A: Load Switch (Recommended)**
```
USB 5V ──[Load Switch]──┬── LDO VIN
                        │
VBAT ──[Ideal Diode]────┘
```
- Use P-FET load switch controlled by USB detection
- Battery only powers system when USB disconnected

**Option B: Power MUX IC**
- Use dedicated power MUX like TPS2113A
- Automatically switches between USB and battery
- Prevents backfeed

**Option C: Separate Rails (Simplest)**
```
USB 5V ──────────────────► Charger (MCP73831) ──► Battery
                              │
VBAT ────────────────────────►─┴─► LDO ──► 3.3V
```
- USB only charges battery
- System always runs from battery
- Battery provides stable input to LDO

---

### Issue 10: J2 Connector Placement/Type

**Current State:**
- J2: B2B-PH-K-S(LF)(SN) at "top of board"
- Reviewer indicates this is wrong

**Problem:**
- Either wrong connector type for battery
- Or placed in wrong location (RF interference, accessibility)

**Recommended Fix:**
1. Confirm J2 purpose (battery vs expansion)
2. If battery connector:
   - Use JST-PH 2-pin (current part is correct)
   - Relocate to bottom/edge near power section
3. If expansion connector:
   - Add separate battery connector
   - Designate new part (e.g., J7)

---

## Additional Observations

### Power Architecture Review Needed
The current power architecture has fundamental issues:
1. D2 allows dangerous voltage to battery
2. U3 (LDO) not properly connected
3. No clear power path from USB/Battery to 3.3V rail

**Recommended Power Architecture:**
```
USB 5V ──┬──► MCP73831 (Charger) ──► LiPo Battery
         │
         └──► [USB Detection]
                    │
                    ▼
         ┌─────────[P-FET Switch]─────────┐
         │                                │
USB 5V ──┤                                ├──► AP2112K ──► 3.3V Rail
         │                                │
VBAT ────┴────────────────────────────────┘
```

### Component Verification Needed
The following components should be verified in the schematic:
- [ ] All capacitor connections (C1-C29)
- [ ] All resistor values and placements
- [ ] Power rail connectivity
- [ ] Ground plane connectivity

---

## Change Implementation Checklist

### Phase 1: Critical Fixes (Required for Board to Function)
- [ ] Fix U3 (LDO) connections
- [ ] Fix accelerometer power (VDD, VDD_IO)
- [ ] Remove D2, implement proper power path
- [ ] Verify/add battery connector

### Phase 2: Important Improvements
- [ ] Replace Q1 with MOSFET
- [ ] Add MOSFET gate pull-down
- [ ] Add accelerometer INT1 pull-up
- [ ] Relocate/remove C15

### Phase 3: Enhancements
- [ ] Review button debouncing
- [ ] Verify J2 placement
- [ ] Add test points for debugging

---

## References

- LIS2DH12TR Datasheet: ST Microelectronics
- AP2112K Datasheet: Diodes Incorporated
- MCP73831 Datasheet: Microchip Technology
- nRF52840 Product Specification: Nordic Semiconductor
- BS170/2N7002 Datasheet: ON Semiconductor / various

---

*Document created: January 31, 2026*
*Status: Pending schematic implementation*
