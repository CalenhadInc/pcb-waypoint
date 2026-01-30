# Component Placement Instructions by Reference Designator

Board: 46mm x 62mm (coordinate system: **0,0 at center**)
- **X range:** -23mm to +23mm
- **Y range:** -31mm to +31mm

---

## Step 1: Define Zone Boundaries

```
┌─────────────────────────────────────────────┐ Y=-31 (top edge)
│ ZONE 1: BLE ANTENNA KEEPOUT (15x5mm)       │
│ [X: -23 to -8mm, Y: -31 to -26mm]          │
├─────────────────────────────────────────────┤
│ ZONE 2: nRF52840 & Crystals                │
│ [X: -23 to -3mm, Y: -26 to -6mm]           │
├─────────────────────────────────────────────┤
│ ZONE 3: Power & USB                         │
│ [X: -3 to +23mm, Y: -31 to -6mm]           │
├─────────────────────────────────────────────┤
│ ZONE 4: SX1262 & RF Path                    │
│ [X: -23 to +2mm, Y: -6 to +9mm]            │
├─────────────────────────────────────────────┤
│ ZONE 5: Peripherals (Accel, Haptic)        │
│ [X: -3 to +23mm, Y: -6 to +14mm]           │
├─────────────────────────────────────────────┤
│ ZONE 6: User Interface (LED, SW, Buzzer)   │
│ [X: -23 to +7mm, Y: +14 to +31mm]          │
├─────────────────────────────────────────────┤
│ ZONE 7: LoRa ANTENNA KEEPOUT               │
│ [X: +7 to +23mm, Y: +19 to +31mm]          │
└─────────────────────────────────────────────┘ Y=+31 (bottom edge)
X=-23 (left edge)                    X=+23 (right edge)
```

---

## Step 2: Place Main ICs First

### **U1: NRF52840-QIAA-R (QFN-73, 7x7mm)**
- **Location:** ZONE 2, centered at X=-13mm, Y=-16mm
- **Orientation:** Pin 1 at top-left (mark with silkscreen dot)
- **Clearance:** 10mm radius around U1 center (no tall components)
- **Action:**
  1. Place U1 at (-13, -16)
  2. Add 9x thermal vias (0.3mm drill, 0.6mm pad) in 3x3 grid under center pad
  3. Via spacing: 2mm apart, centered under IC

### **U2: SX1262IMLTRT (QFN-24, 4x4mm)**
- **Location:** ZONE 4, centered at X=-13mm, Y=+1mm
- **Orientation:** Pin 1 (VDD_IN) at top-left
- **RF Path:** Orient so RFI_P/RFI_N (pins 22-23) face toward J3 (U.FL connector)
- **Action:**
  1. Place U2 at (-13, +1)
  2. Add 4x thermal vias (0.3mm drill) in 2x2 grid under center pad
  3. Via spacing: 1.5mm apart

### **U3: AP2112K-3.3TRG1 (SOT-23-5)**
- **Location:** ZONE 3, at X=+5mm, Y=-21mm
- **Orientation:** Pin 1 (VIN) facing left (toward power input)
- **Action:** Place U3 at (+5, -21)

### **U4: MCP73831T-2ACI/OT (SOT-23-5)**
- **Location:** ZONE 3, at X=+13mm, Y=-21mm
- **Orientation:** Pin 1 (STAT) at top-left
- **Action:** Place U4 at (+13, -21)

### **U5: DRV2605LDGSR (SON-8, 2x2mm) - Haptic Driver**
- **Location:** ZONE 6, at X=-13mm, Y=+19mm
- **Orientation:** Pin 1 (REG) at top-left
- **Near:** J6 (LRA motor connector)
- **Action:** Place U5 at (-13, +19)

### **U6: LIS2DH12TR (LGA-12, 2x2mm) - Accelerometer**
- **Location:** ZONE 5, at X=+2mm, Y=-1mm
- **Orientation:** Pin 1 at top-left, align with X/Y axes for proper motion sensing
- **Action:** Place U6 at (+2, -1)

**Note:** LTC4412 ideal diode removed - using D2 (SS14 Schottky) for power OR-ing.

---

## Step 3: Place Crystals & Oscillators (Near Their ICs)

### **Y1: NX2016SA-32MHZ (2.0x1.6mm) - 32MHz Crystal for nRF52840**
- **Location:** <3mm from U1, near XC1/XC2 pins (typically bottom-right of U1)
- **Position:** X=-9mm, Y=-13mm
- **Orientation:** Long axis parallel to U1 edge
- **Action:**
  1. Place Y1 at (-9, -13)
  2. Keep traces to U1 pins <3mm
  3. No vias between Y1 and U1

### **Y2: ABS07-32.768KHZ (3.2x1.5mm) - 32.768kHz Crystal for nRF52840**
- **Location:** <3mm from U1, near XL1/XL2 pins (typically top-right of U1)
- **Position:** X=-9mm, Y=-19mm
- **Orientation:** Long axis parallel to U1 edge
- **Action:**
  1. Place Y2 at (-9, -19)
  2. Keep traces to U1 pins <3mm
  3. No vias between Y2 and U1

### **Y3: X1G0042110003 (2.5x2.0mm) - 32MHz TCXO for SX1262**
- **Location:** <5mm from U2, near XTA pin (pin 14, typically right side)
- **Position:** X=-8mm, Y=+1mm
- **Orientation:** Output pin facing U2
- **Action:**
  1. Place Y3 at (-8, +1)
  2. Output connects to U2 pin 14 (XTA)
  3. VCC powered by U2 pin 13 (DIO3) - 1.8V internal supply

---

## Step 4: Place Connectors at Board Edges

### **J1: USB4105-GF-A (USB-C connector)**
- **Location:** ZONE 3, top edge, centered
- **Position:** X=+12mm, Y=-31mm (flush with top edge)
- **Orientation:** Receptacle opening facing outward (toward top edge)
- **Action:** Place J1 at (+12, -31) - edge-mounted

### **J2: B2B-PH-K-S (JST battery connector, 2-pin)**
- **Location:** ZONE 3, right edge
- **Position:** X=+23mm, Y=-16mm (flush with right edge)
- **Orientation:** Opening facing outward (toward right edge)
- **Action:** Place J2 at (+23, -16) - edge-mounted

### **J3: U.FL-R-SMT-1(10) (RF connector for LoRa antenna)**
- **Location:** ZONE 4/5 boundary, right edge
- **Position:** X=+23mm, Y=+4mm (flush with right edge)
- **Orientation:** Center pin connects to RF trace from U2
- **Action:**
  1. Place J3 at (+23, +4) - edge-mounted
  2. Ensure clear 50Ω RF path from U2 to J3

### **J4: 20021121-00006C4LF (SWD programming header, 2x3, 1.27mm pitch)**
- **Location:** ZONE 6, left edge
- **Position:** X=-23mm, Y=+17mm (flush with left edge)
- **Orientation:** Pin 1 (VCC) at top-left
- **Pinout:**
  ```
  1-VCC  2-SWDIO
  3-GND  4-SWDCLK
  5-GND  6-RESET
  ```
- **Action:** Place J4 at (-23, +17) - edge-mounted

### **J5: 640456-8 (Expansion header, 1x8, 2.54mm pitch)**
- **Location:** ZONE 6, bottom edge
- **Position:** X=-13mm, Y=+31mm (flush with bottom edge)
- **Orientation:** Pin 1 at left
- **Action:** Place J5 at (-13, +31) - edge-mounted

### **J6: 2.54-2P-LT (LRA motor connector, 2-pin, 2.54mm pitch)**
- **Location:** ZONE 6, near U6 (haptic driver)
- **Position:** X=-8mm, Y=+21mm
- **Orientation:** Pin 1 (LRA+) at left
- **Action:** Place J6 at (-8, +21) - keep <10mm from U6

---

## Step 5: Place Inductors (Critical for DC-DC & RF)

### **L_DCDC: 10uH inductor for nRF52840 DC-DC (0805 footprint)**
- **Location:** Near U1 DCC pin (typically left side of U1)
- **Position:** X=-17mm, Y=-16mm
- **Orientation:** Long axis perpendicular to U1
- **Action:**
  1. Place L_DCDC at (-17, -16)
  2. Keep trace to DCC pin <5mm

### **L_SX: 47nH inductor for SX1262 DC-DC (0402 footprint)**
- **Location:** Near U2 VBAT_IO pins
- **Position:** X=-17mm, Y=+1mm
- **Orientation:** Any
- **Action:** Place L_SX at (-17, +1)

### **L1: 4.7nH inductor for antenna matching (0402 MAPI-4020)**
- **Location:** Between U2 (RFI_P/RFI_N) and J3 (U.FL) in RF path
- **Position:** X=-5mm, Y=+4mm
- **Action:**
  1. Place L1 at (-5, +4) in-line with RF trace
  2. Part of matching network with C17

---

## Step 6: Place Diodes (Protection & Switching)

### **D1: USBLC6-2P6 (USB ESD protection, SOT-666)**
- **Location:** <3mm from J1 (USB connector)
- **Position:** X=+9mm, Y=-28mm
- **Orientation:** Pin 1 at top-left
- **Action:**
  1. Place D1 at (+9, -28) immediately after J1
  2. D+/D- traces from J1 must pass through D1 before going to U1

### **D2: SS14 (Schottky diode, SMA)**
- **Location:** Near U5 (ideal diode controller) or in power path
- **Position:** X=+1mm, Y=-24mm
- **Orientation:** Cathode band marking toward higher voltage side
- **Action:** Place D2 at (+1, -24)

### **D3: 1N4148W-E3-18 (Flyback diode for buzzer, SOD-123)**
- **Location:** Parallel to LS1 (buzzer), near Q1 (transistor)
- **Position:** X=-15mm, Y=+24mm
- **Orientation:** Cathode toward buzzer positive terminal
- **Action:** Place D3 at (-15, +24)

---

## Step 7: Place LEDs & User Interface

### **LED1: Green LED (0603 or similar)**
- **Location:** ZONE 6, visible area
- **Position:** X=-5mm, Y=+19mm
- **Orientation:** Cathode toward U1 (active-LOW configuration)
- **Action:** Place LED1 at (-5, +19)

### **LED2: Red LED (0603 or similar)**
- **Location:** Near LED1
- **Position:** X=-1mm, Y=+19mm
- **Orientation:** Cathode toward U1 (active-LOW configuration)
- **Action:** Place LED2 at (-1, +19)

### **SW1: B3FS-1050P (Tactile button)**
- **Location:** ZONE 6, accessible area
- **Position:** X=+2mm, Y=+21mm
- **Orientation:** Any (symmetrical footprint)
- **Action:** Place SW1 at (+2, +21)

### **LS1: MLT-5020 (Buzzer, 5mm diameter)**
- **Location:** ZONE 6, near edge for sound projection
- **Position:** X=-18mm, Y=+24mm
- **Orientation:** Positive terminal toward Q1 collector
- **Action:** Place LS1 at (-18, +24)

### **Q1: MMBT3904TT1G (NPN transistor, SC-75-3)**
- **Location:** Near LS1 (buzzer driver)
- **Position:** X=-15mm, Y=+21mm
- **Orientation:**
  - Collector → to LS1
  - Base → to U1 via R11
  - Emitter → to GND
- **Action:** Place Q1 at (-15, +21)

---

## Step 8: Place Test Points

### **TP1: HAPTIC_EN**
- **Position:** X=-11mm, Y=+17mm (near U6)
- **Action:** Place TP1 at (-11, +17)

### **TP2: SCL (I2C Clock)**
- **Position:** X=-1mm, Y=+1mm (along I2C bus trace)
- **Action:** Place TP2 at (-1, +1)

### **TP3: SDA (I2C Data)**
- **Position:** X=-1mm, Y=+3mm (along I2C bus trace)
- **Action:** Place TP3 at (-1, +3)

### **TP4: LRA+ (Motor drive positive)**
- **Position:** X=-10mm, Y=+21mm (near J6)
- **Action:** Place TP4 at (-10, +21)

### **TP5: LRA- (Motor drive negative)**
- **Position:** X=-6mm, Y=+21mm (near J6)
- **Action:** Place TP5 at (-6, +21)

### **TP6: ACCEL_INT1 (Accelerometer interrupt)**
- **Position:** X=+5mm, Y=-3mm (near U7)
- **Action:** Place TP6 at (+5, -3)

### **TP7: BUZZER (Buzzer control signal)**
- **Position:** X=-15mm, Y=+19mm (near Q1, LS1)
- **Action:** Place TP7 at (-15, +19)

---

## Step 9: Place Capacitors (By IC Proximity)

### **Around U1 (nRF52840):**

**C11, C12: 18pF 0402 (32MHz crystal load caps)**
- Place immediately adjacent to Y1
- C11: X=-8.5mm, Y=-14mm (one side of Y1)
- C12: X=-8.5mm, Y=-12mm (other side of Y1)
- Distance to Y1: <1mm

**C13, C14: 12.5pF 0402 (32.768kHz crystal load caps)**
- Place immediately adjacent to Y2
- C13: X=-8.5mm, Y=-20mm (one side of Y2)
- C14: X=-8.5mm, Y=-18mm (other side of Y2)
- Distance to Y2: <1mm

**C4: 10uF 0805 (VDDH bulk capacitor)**
- Position: X=-15mm, Y=-19mm (near U1 VDDH pin)
- Plus one 100nF 0402 in parallel

**C_DCC1, C_DCC2: 100nF 0402 (DC-DC bypass)**
- Near L_DCDC and U1 DCC pin
- C_DCC1: X=-17mm, Y=-18mm
- C_DCC2: X=-17mm, Y=-14mm

**C5, C6, C7, C8, C16, C18, C20, C21, C24, C25: 100nF 0402 (VDD/DEC bypass caps)**
- Distribute around U1 perimeter, <2mm from VDD/DEC pins
- Suggested positions (adjust to match actual pin locations):
  - C5: X=-15mm, Y=-15mm (DEC1)
  - C6: X=-11mm, Y=-15mm (DEC2)
  - C7: X=-15mm, Y=-17mm (DEC3)
  - C8: X=-11mm, Y=-17mm (DEC4)
  - C16: X=-15mm, Y=-13mm
  - C18: X=-11mm, Y=-13mm
  - C20: X=-13mm, Y=-19mm
  - C21: X=-13mm, Y=-13mm
  - C24: X=-17mm, Y=-15mm (DEC5)
  - C25: X=-17mm, Y=-17mm (DEC6)

**C26: 4.7uF 0805 (DECUSB, U1 pin AC5)**
- Position: X=-9mm, Y=-15mm (near USB pins)

### **Around U2 (SX1262):**

**C15, C19: 10uF 0805 (VDD_IN decoupling)**
- C15: X=-15mm, Y=-1mm (near U2 pin 1)
- C19: X=-11mm, Y=-1mm (near U2 pin 24)
- Distance to U2: <3mm

**C22: 4.7uF 0805 (VBAT_IO decoupling, U2 pin 11)**
- Position: X=-15mm, Y=+3mm (near U2)

**C23: 100nF 0402 (VREG decoupling, U2 pin 7)**
- Position: X=-13mm, Y=+3mm (near U2)

**C_VR_PA: 100nF 0402 (VR_PA decoupling, U2 pin 24)**
- Position: X=-11mm, Y=+3mm (near U2)

**C17: 2.2pF 0402 (Antenna matching capacitor)**
- Position: X=-3mm, Y=+4mm (in RF path with L1)
- Forms matching network: U2 → L1 → C17 → J3

### **Around U3 (AP2112K LDO):**

**C1: 10uF 0805 (LDO input)**
- Position: X=+3mm, Y=-21mm (left of U3)
- Distance to U3 pin 1: <3mm

**C2: 10uF 0805 (LDO output)**
- Position: X=+7mm, Y=-21mm (right of U3)
- Distance to U3 pin 5: <3mm

### **Around U4 (MCP73831 Charger):**

**C9: 4.7uF 1206 (Charger input)**
- Position: X=+11mm, Y=-21mm (left of U4)
- Distance to U4: <3mm

### **Around U5 (LTC4412 Ideal Diode):**

**C3: 10uF 0805 (Input/output decoupling)**
- Position: X=+5mm, Y=-24mm (near U5)
- Distance to U5: <3mm

### **Around U6 (DRV2605 Haptic Driver):**

**C_HAP1: 10uF 0805 (VDD bulk)**
- Position: X=-15mm, Y=+19mm (left of U6)
- Distance to U6: <2mm

**C_HAP2: 100nF 0402 (VDD bypass)**
- Position: X=-11mm, Y=+19mm (right of U6)
- Distance to U6: <2mm

### **Around U7 (LIS2DH12 Accelerometer):**

**C_ACC_VDD: 100nF 0402 (VDD bypass for U7)**
- Position: X=+2mm, Y=-3mm
- Distance to IC: <2mm

**C_ACC_VDDIO: 100nF 0402 (VDDIO bypass for U7)**
- Position: X=+2mm, Y=+1mm
- Distance to IC: <2mm

### **Other Capacitors:**

**C10: 4.7uF 1206**
- Position: X=+17mm, Y=-21mm (additional power decoupling)

**C18: 100nF 0402**
- Position: (assigned to U1 VDD bypass above)

---

## Step 10: Place Resistors

### **Power & Charging:**

**R1: 2kΩ 0603 (MCP73831 charge current programming)**
- Position: X=+13mm, Y=-19mm (near U4 PROG pin)
- Distance to U4: <3mm

**R6, R7: 5.1kΩ 0603 (USB CC pull-down resistors)**
- R6: X=+10mm, Y=-29mm (J1 CC1 pin)
- R7: X=+14mm, Y=-29mm (J1 CC2 pin)
- Connect CC1 and CC2 pins to GND

### **LED Current Limiting:**

**R2: 1kΩ 0603 (LED1 series resistor)**
- Position: X=-5mm, Y=+17mm (in series with LED1)

**R3: 1kΩ 0603 (LED2 series resistor)**
- Position: X=-1mm, Y=+17mm (in series with LED2)

### **Pull-ups & Pull-downs:**

**R4, R5, R8, R13, R16: 10kΩ 0603 (Pull-up resistors)**
- R4: X=+2mm, Y=+23mm (SW1 pull-up)
- R5: (spare or for second button)
- R8: X=+5mm, Y=-5mm (Accelerometer INT1 pull-up, optional)
- R13: (additional pull-up)
- R16: (additional pull-up)

**R14, R15: 4.7kΩ 0603 (I2C pull-ups)**
- R14: X=-3mm, Y=+1mm (SCL pull-up to 3.3V)
- R15: X=-3mm, Y=+3mm (SDA pull-up to 3.3V)
- Place near U1 (nRF52840) end of I2C bus

### **Buzzer Driver:**

**R11: 1kΩ 0603 (Q1 base resistor)**
- Position: X=-15mm, Y=+22mm (between U1 GPIO and Q1 base)

### **Other Resistors:**

**R9, R10: 0Ω 0603 (Jumpers or current sense)**
- R9: X=+9mm, Y=-23mm
- R10: X=+9mm, Y=-19mm
- Purpose: jumpers or current measurement points in power path

**R12: 1kΩ 0603 (DIO1 series resistor)**
- Position: Between U1 P1.15 and U2 DIO1

---

## Step 11: Final Checks & Via Placement

### **Thermal Vias:**
- [x] U1 (nRF52840): 9x vias in 3x3 grid, 0.3mm drill, 2mm spacing
- [x] U2 (SX1262): 4x vias in 2x2 grid, 0.3mm drill, 1.5mm spacing

### **RF Via Fence (around U2 and RF path):**
- Add 0.3mm vias every 3mm around perimeter of:
  - U2 (SX1262)
  - RF matching network (L1, C17)
  - RF trace from U2 to J3
- Vias connect top ground pour to bottom ground plane

### **Ground Stitching:**
- Add via stitching (0.3-0.4mm drill) every 5mm along ground pour boundaries
- Connect top and bottom ground planes

### **Crystal Ground Guards:**
- Add ground vias around Y1 and Y2 crystals
- 4-6 vias per crystal, forming a fence
- Distance: 1-2mm from crystal edge

---

## Step 12: Critical Distance Verification Checklist

Use this to verify component spacing after placement:

- [ ] **D1 to J1**: <3mm (USB ESD protection must be close to connector)
- [ ] **Y1 to U1**: <3mm (32MHz crystal to nRF52840)
- [ ] **Y2 to U1**: <3mm (32.768kHz crystal to nRF52840)
- [ ] **Y3 to U2**: <5mm (TCXO to SX1262)
- [ ] **C11, C12 to Y1**: <1mm (crystal load caps)
- [ ] **C13, C14 to Y2**: <1mm (crystal load caps)
- [ ] **L_DCDC to U1**: <5mm (DC-DC inductor)
- [ ] **All bypass caps to IC VDD pins**: <2mm
- [ ] **C1, C2 to U3**: <3mm (LDO input/output caps)
- [ ] **C9 to U4**: <3mm (charger input cap)
- [ ] **R1 to U4**: <3mm (charge programming resistor)
- [ ] **R6, R7 to J1**: <5mm (USB CC resistors)
- [ ] **L1, C17 in RF path**: aligned and <5mm apart
- [ ] **J6 to U6**: <10mm (LRA motor connector to haptic driver)

---

## Step 13: RF Trace Routing Requirements

After component placement, follow these RF routing rules:

### **BLE Antenna (from U1):**
- Trace width: 2.9mm (50Ω microstrip)
- Route from U1 ANT pin to BLE antenna zone (ZONE 1)
- Length: <15mm
- No vias in antenna trace
- Ground plane on bottom layer only

### **LoRa RF Path (from U2 to J3):**
- Trace width: 2.9mm (50Ω microstrip)
- Route: U2 (RFI_P/RFI_N, pins 22-23) → L1 → C17 → J3
- Total length: <20mm
- No vias in RF path
- Via fence on both sides (0.3mm vias, 3mm spacing)
- Ground plane on bottom layer only

### **USB Differential Pair (from J1 to U1):**
- Trace width: 0.4mm each trace
- Spacing: 0.2mm between D+ and D-
- Length match: within 0.5mm
- Route through D1 (ESD protection) first: J1 → D1 → U1
- Minimize vias (ideally zero)

---

## Step 14: Component Height Considerations

Verify clearances for enclosure fit:

**Tall Components (>3mm height):**
- J1 (USB-C): ~3.2mm height
- J2 (JST battery): ~5mm height
- J3 (U.FL): ~1.5mm height
- SW1 (button): ~3.5mm height
- LS1 (buzzer): ~3mm height

**Low-Profile Components (<2mm height):**
- All QFN ICs (U1, U2): <1mm
- All SOT-23 parts (U3, U4, U5): ~1.1mm
- All 0805 passives: ~1mm
- All 0603 passives: ~0.6mm
- All 0402 passives: ~0.5mm

---

## Assembly Notes

1. **Solder paste stencil**: Required for QFN packages (U1, U2, U7)
2. **Reflow profile**: Lead-free SAC305 solder, peak temp 245-250°C
3. **Assembly order**:
   - Bottom side first (if any bottom components)
   - Top side: smallest to largest (0402 → 0603 → 0805 → 1206 → ICs → connectors)
4. **Inspection**: X-ray inspection recommended for U1, U2, U7 (QFN/LGA packages)
5. **Programming**: Use J4 (SWD header) with J-Link, ST-Link, or similar programmer

---

## Reference: Component-to-IC Pin Connections Quick Reference

| Component | Connects To | IC Pin | Notes |
|-----------|-------------|--------|-------|
| Y1 | U1 | XC1/XC2 | 32MHz crystal |
| Y2 | U1 | XL1/XL2 | 32.768kHz crystal |
| Y3 | U2 | XTA (pin 14) | TCXO, powered by DIO3 |
| J1 (USB D+/D-) | U1 | D+/D- (pins 33-34) | Via D1 (ESD) |
| J3 (U.FL center) | U2 | RFI_P/RFI_N (pins 22-23) | Via L1, C17 matching |
| J4 pin 2 (SWDIO) | U1 | SWDIO (pin 26) | Programming |
| J4 pin 4 (SWDCLK) | U1 | SWDCLK (pin 25) | Programming |
| LED1 | U1 | P0.13 (pin 15) | Via R2 (1kΩ) |
| LED2 | U1 | P0.14 (pin 16) | Via R3 (1kΩ) |
| SW1 | U1 | P0.15 (pin 17) | Via R4 (10kΩ pull-up) |
| U5 (SCL) | U1 | P0.27 (pin 5) | I2C clock (haptic) |
| U5 (SDA) | U1 | P0.26 (pin 4) | I2C data (haptic) |
| U6 (SCL) | U1 | P0.27 (pin 5) | I2C clock (accel) |
| U6 (SDA) | U1 | P0.26 (pin 4) | I2C data (accel) |
| Q1 base | U1 | P0.17 (pin 19) | Buzzer control via R11 |

---

## Coordinate Summary Table

**Board Center: (0, 0) | X: -23 to +23mm | Y: -31 to +31mm**

| Ref | Component | X (mm) | Y (mm) | Zone | Notes |
|-----|-----------|--------|--------|------|-------|
| U1 | nRF52840 | -13 | -16 | 2 | Main MCU |
| U2 | SX1262 | -13 | +1 | 4 | LoRa radio |
| U3 | AP2112K | +5 | -21 | 3 | LDO |
| U4 | MCP73831 | +13 | -21 | 3 | Charger |
| U5 | DRV2605 | -13 | +19 | 6 | Haptic |
| U6 | LIS2DH12 | +2 | -1 | 5 | Accel |
| Y1 | 32MHz Xtal | -9 | -13 | 2 | Near U1 |
| Y2 | 32.768kHz Xtal | -9 | -19 | 2 | Near U1 |
| Y3 | TCXO | -8 | +1 | 4 | Near U2 |
| J1 | USB-C | +12 | -31 | 3 | Top edge |
| J2 | JST Battery | +23 | -16 | 3 | Right edge |
| J3 | U.FL | +23 | +4 | 4/5 | Right edge |
| J4 | SWD Header | -23 | +17 | 6 | Left edge |
| J5 | Expansion | -13 | +31 | 6 | Bottom edge |
| J6 | LRA Motor | -8 | +21 | 6 | Near U5 |
| LED1 | Green LED | -5 | +19 | 6 | Visible |
| LED2 | Red LED | -1 | +19 | 6 | Visible |
| SW1 | Button | +2 | +21 | 6 | Accessible |
| LS1 | Buzzer | -18 | +24 | 6 | Near edge |
| Q1 | NPN Transistor | -15 | +21 | 6 | Buzzer driver |
| L1 | 4.7nH | -5 | +4 | 4 | RF matching |
| D1 | USB ESD | +9 | -28 | 3 | Near J1 |

---

## Done!

Follow steps 1-14 in order for optimal component placement. After placement, proceed with routing following the critical trace requirements (RF, USB, I2C, power).
