# Design Changes Comparison: Before vs After

*Review Date: January 31, 2026*

This document provides a side-by-side comparison of the original design versus the recommended changes from the design review.

---

## Summary Table

| Area | Original Design | Proposed Change | Impact |
|------|-----------------|-----------------|--------|
| Q1 Buzzer Driver | MMBT3904 (BJT) | 2N7002/AO3400 (MOSFET) | Better efficiency |
| Q1 Gate/Base | No pull-down | 10kΩ pull-down | Prevents floating |
| C15 | 10µF general bypass | Remove or move to LDO VBAT | Correct placement |
| Accelerometer INT | Floating (open-drain) | 10kΩ pull-up to VDD | Proper signal integrity |
| SW1 Debounce | 100nF (τ=1ms) | Consider 1µF (τ=10ms) | Better debouncing |
| Accelerometer VDD | Floating/wrong | Connect to 3.3V rail | **Critical fix** |
| U3 LDO | Not connected properly | Full connection to power rails | **Critical fix** |
| Battery Connector | Missing/misplaced J2 | Add proper JST-PH connector | **Critical fix** |
| D2 Schottky | SS14 backfeed protection | **Remove entirely** | **Safety critical** |
| Power Architecture | Diode OR-ing (dangerous) | Load switch or power MUX | **Safety critical** |

---

## 1. Buzzer Driver (Q1)

### BEFORE
```
Component: MMBT3904TT1G
Type: NPN Bipolar Junction Transistor (BJT)
Package: SC-75-3 (SOT-23 variant)

Circuit:
P0.17 ──[1kΩ]──► Base
                  │
           Collector ── Buzzer+ ── 3.3V
                  │
            Emitter ── GND

Characteristics:
- Requires base current (~1mA) to drive
- VCE(sat) ~0.2V voltage drop
- Current gain dependent on temperature
```

### AFTER
```
Component: 2N7002 or AO3400
Type: N-Channel Enhancement MOSFET
Package: SOT-23

Circuit:
P0.17 ──[1kΩ]──┬── Gate
               │
             [10kΩ] (pull-down)
               │
              GND

           Drain ── Buzzer+ ── 3.3V
             │
          Source ── GND

Characteristics:
- Voltage-driven (no gate current)
- RDS(on) < 0.1Ω (minimal voltage drop)
- Faster switching
- Temperature stable
```

### BOM Change
| Before | After |
|--------|-------|
| MMBT3904TT1G, $0.02 | 2N7002, $0.02 |
| - | 10kΩ 0402 resistor, $0.001 |

---

## 2. Capacitor C15

### BEFORE
```
Component: C15
Value: 10µF
Package: 0805
Location: Unspecified/general bypass
Purpose: Unknown
```

### AFTER - Option A (Remove)
```
Component: C15
Status: REMOVED
Reason: Excessive value, not needed at current location
```

### AFTER - Option B (Relocate)
```
Component: C15
Value: 10µF
Package: 0805
Location: AP2112K VIN pin (VBAT input)
Purpose: Input bulk capacitance for LDO

Connection:
VBAT ───┬─── AP2112K VIN
        │
      [10µF] C15
        │
       GND
```

---

## 3. Accelerometer Interrupt (INT1)

### BEFORE
```
LIS2DH12TR Pin 4 (INT1)
Connection: Direct to P0.11 (nRF52840)
Pull-up/Pull-down: None

Problem: Open-drain output floats high-impedance
when not active, causing:
- Undefined logic levels
- False interrupts
- Increased power consumption
```

### AFTER
```
LIS2DH12TR Pin 4 (INT1)
Connection: P0.11 (nRF52840) via pull-up

Circuit:
         3.3V
           │
        [10kΩ] R_ACC_PU (new)
           │
INT1 ──────┴─────► P0.11

Behavior:
- Idle: Line pulled HIGH by resistor
- Active: LIS2DH12 pulls LOW (open-drain)
- Clean digital signal transitions
```

### BOM Change
| Before | After |
|--------|-------|
| (none) | 10kΩ 0402 resistor, $0.001 |

---

## 4. Button Debouncing (SW1)

### BEFORE
```
SW1: B3FS-1050P
Pull-up: 10kΩ to VDD
Debounce Cap: 100nF

Time Constant: τ = 10kΩ × 100nF = 1ms
Typical bounce time: 5-50ms

Status: May be insufficient for aggressive button use
```

### AFTER (if needed)
```
SW1: B3FS-1050P
Pull-up: 10kΩ to VDD
Debounce Cap: 1µF (increased from 100nF)

Time Constant: τ = 10kΩ × 1µF = 10ms
Coverage: Handles most mechanical bounce

Alternative: Implement software debouncing
- Sample at 10ms intervals
- Require 2-3 consecutive readings
- No additional hardware cost
```

---

## 5. Accelerometer Power (CRITICAL)

### BEFORE
```
LIS2DH12TR Power Connections:
- VDD (Pin 1): FLOATING or incorrectly connected
- VDD_IO (Pin 5): Unknown
- C29: Connected incorrectly

Status: WILL NOT FUNCTION
```

### AFTER
```
LIS2DH12TR Power Connections:
- VDD (Pin 1): 3.3V rail
- VDD_IO (Pin 5): 3.3V rail
- GND (Pins 3, 7, 12): Ground plane

Bypass Capacitors:
- C_ACC1: 100nF, VDD to GND (close to pin 1)
- C_ACC2: 100nF, VDD_IO to GND (close to pin 5)

Schematic:
       3.3V ────┬──────────┬─── VDD (Pin 1)
                │          │
              [100nF]      └─── VDD_IO (Pin 5)
                │                   │
               GND              [100nF]
                                    │
                                   GND
```

---

## 6. LDO Power Supply U3 (CRITICAL)

### BEFORE
```
U3: AP2112K-3.3TRG1
Status: Not properly connected
Result: No 3.3V power to any components

Board will not power on.
```

### AFTER
```
U3: AP2112K-3.3TRG1

Connections:
┌─────────────────────────────────┐
│  Pin 1 (VIN)  ◄── VBAT/USB     │
│  Pin 2 (GND)  ◄── Ground       │
│  Pin 3 (EN)   ◄── VIN (always on) │
│  Pin 4 (NC)   ── No connection │
│  Pin 5 (VOUT) ──► 3.3V Rail    │
└─────────────────────────────────┘

Bypass Capacitors:
- VIN: 10µF ceramic to GND
- VOUT: 10µF ceramic to GND

Schematic:
VBAT ──┬──[10µF]──┬── GND
       │          │
       └───► VIN  │
             EN ──┘
             │
           VOUT ──┬──[10µF]──┬── GND
                  │          │
                  └─────────►│ 3.3V Rail
```

---

## 7. Battery Connector (CRITICAL)

### BEFORE
```
J2: B2B-PH-K-S(LF)(SN)
Type: JST-PH 2-pin
Location: Top of board (reviewer comment)
Status: Either missing, misplaced, or wrong type

Issues:
- May not be connected to power circuit
- Placement may interfere with RF
- May be in inaccessible location
```

### AFTER
```
J2: B2B-PH-K-S(LF)(SN) (or add new J7)
Type: JST-PH 2-pin (correct for LiPo)
Location: Bottom edge, near power management

Connections:
  J2 Pin 1 (VBAT+) ──► Battery positive rail
  J2 Pin 2 (GND)   ──► Ground plane

Placement Guidelines:
- Near MCP73831 charger IC
- Away from RF sections (>10mm)
- Accessible from board edge
- Orientation for easy battery insertion
```

---

## 8. Power Architecture (SAFETY CRITICAL)

### BEFORE
```
                    ┌─────────────────┐
USB 5V ─────────────┤                 │
                    │    SS14 (D2)    ├──► LDO VIN
VBAT (3.7V) ────────┤   (Schottky)    │
                    └─────────────────┘

Problem:
- USB 5V - 0.5V diode drop = 4.5V appears on VBAT line
- LiPo max voltage: 4.2V
- BATTERY DAMAGE / FIRE HAZARD
```

### AFTER - Option A (Load Switch)
```
                    ┌──────────────────────────────────┐
                    │                                  │
USB 5V ─────────────┼──► MCP73831 ──► Battery        │
                    │        │                        │
                    │   [USB Detect]                  │
                    │        │                        │
                    │        ▼                        │
                    │   ┌─────────┐                   │
USB 5V ─────────────┼───┤ P-FET   ├───┐              │
                    │   │ Switch  │   │              │
                    │   └─────────┘   │              │
                    │                 ├──► LDO ──► 3.3V
VBAT ───────────────┼─────────────────┘              │
                    │                                │
                    └──────────────────────────────────┘

Operation:
- USB connected: P-FET ON, USB powers system
- USB disconnected: P-FET OFF, battery powers system
- Battery never sees USB voltage
```

### AFTER - Option B (Battery-Only System Power)
```
USB 5V ──────────────────► MCP73831 ──► Battery
                                           │
                                           │
VBAT ◄─────────────────────────────────────┘
  │
  └──────────────────────► AP2112K ──► 3.3V

Operation:
- USB only charges battery (never powers system directly)
- System always runs from battery
- Simplest, most robust approach
- Battery acts as power filter
```

### D2 Status
| Before | After |
|--------|-------|
| SS14 Schottky installed | **REMOVED** |
| Creates safety hazard | Power path redesigned |

---

## Component Changes Summary

### Components to REMOVE
| Designator | Part | Reason |
|------------|------|--------|
| D2 | SS14 | Safety hazard - battery overvoltage |
| C15 | 10µF (optional) | Not needed at current location |

### Components to ADD
| Designator | Part | Value | Package | Purpose |
|------------|------|-------|---------|---------|
| R_GATE | Resistor | 10kΩ | 0402 | MOSFET gate pull-down |
| R_ACC_PU | Resistor | 10kΩ | 0402 | Accelerometer INT pull-up |

### Components to CHANGE
| Designator | Before | After | Reason |
|------------|--------|-------|--------|
| Q1 | MMBT3904 (BJT) | 2N7002 (MOSFET) | Better efficiency |

### Components to RELOCATE
| Designator | Before Location | After Location |
|------------|-----------------|----------------|
| C15 (if kept) | Unknown | LDO VIN input |
| J2 | Top of board | Near power section |

### Connections to FIX
| Net | Issue | Fix |
|-----|-------|-----|
| U3 VIN | Not connected | Connect to VBAT |
| U3 VOUT | Not connected | Connect to 3.3V rail |
| U3 EN | Unknown | Tie to VIN |
| U7/U8 VDD | Floating | Connect to 3.3V |
| U7/U8 VDD_IO | Floating | Connect to 3.3V |

---

## Cost Impact

| Change | Cost Impact |
|--------|-------------|
| Remove D2 (SS14) | -$0.02 |
| Change Q1 to 2N7002 | $0.00 (same price) |
| Add R_GATE (10kΩ) | +$0.001 |
| Add R_ACC_PU (10kΩ) | +$0.001 |
| **Net Change** | **-$0.018** |

*Note: These changes actually reduce BOM cost slightly while fixing critical issues.*

---

## Risk Assessment

### Before Changes
| Risk | Level | Consequence |
|------|-------|-------------|
| Battery damage | **CRITICAL** | Fire hazard, device destruction |
| Board won't power | **CRITICAL** | Non-functional device |
| Accelerometer fails | **HIGH** | Major feature loss |
| Buzzer unreliable | MEDIUM | Unpredictable alerts |

### After Changes
| Risk | Level | Consequence |
|------|-------|-------------|
| Battery damage | NONE | Properly protected |
| Board won't power | NONE | Correct connections |
| Accelerometer fails | NONE | Properly powered |
| Buzzer unreliable | NONE | Clean MOSFET switching |

---

## Implementation Priority

### Must Fix Before Fabrication
1. **Remove D2** - Safety critical
2. **Fix U3 connections** - Board won't work
3. **Fix accelerometer power** - Major feature
4. **Add/verify battery connector** - Power source

### Should Fix Before Fabrication
5. Replace Q1 with MOSFET
6. Add MOSFET pull-down
7. Add accelerometer INT pull-up
8. Review C15 placement

### Can Fix in Rev 2
9. Button debouncing improvements
10. Additional test points

---

## Files Reference

| Document | Purpose |
|----------|---------|
| `design-review-changes.md` | Detailed issue descriptions |
| `design-changes-comparison.md` | This file - before/after comparison |
| `design-specification.md` | Current design (needs updating) |
| `design-specification-original.md` | Original design reference |

---

*Comparison document created: January 31, 2026*
*Next step: Update design-specification.md with approved changes*
