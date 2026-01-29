# Component Placement Guide - Waypoint v2 PCB

Based on BOM: `eddywd-waypoint-v2-BOM-V2026-01-29T090142167Z`

Board: 46mm x 62mm, 2-layer FR4

---

## Component Mapping by Section

### **Power Management Section (Top-Center/Right)**

**Primary Components:**
- **U3**: AP2112K-3.3TRG1 (SOT-23-5) - 3.3V LDO regulator
- **U4**: MCP73831T-2ACI/OT (SOT-23-5) - LiPo battery charger
- **U5**: LTC4412MPS6 (SOT-23-6) - Ideal diode controller for power path management
- **D1**: USBLC6-2P6 (SOT-666) - USB ESD protection
- **D2**: SS14 (SMA) - Schottky diode
- **J1**: USB4105-GF-A - USB-C connector
- **J2**: B2B-PH-K-S - JST battery connector (2-pin)

**Placement Strategy:**
```
[J1: USB-C]────[D1: ESD]
      │
      ├──[U5: LTC4412]──[C3: 10uF]
      │
      ├──[U3: AP2112K]──[C1: 10uF IN]──[C2: 10uF OUT]
      │
      └──[U4: MCP73831]──[C9: 4.7uF]──[R1: 2k PROG]
                               │
                         [J2: JST Battery]
```

**Critical Placement:**
1. **D1 (ESD)** must be <3mm from USB connector J1
2. **C1, C2, C3, C9** (bulk caps) within 5mm of their respective ICs
3. Place U5 (ideal diode) between USB input and the rest of the power tree
4. Keep J2 (battery connector) accessible at board edge

**Power Passives:**
- C1, C2, C3: 10uF 0805 (input/output decoupling)
- C9, C10: 4.7uF 1206 (charger decoupling)
- R1: 2kΩ 0603 (charge current programming)

---

### **nRF52840 Section (Upper-Left Quadrant)**

**Primary Component:**
- **U1**: NRF52840-QIAA-R (QFN-73, 7x7mm)

**Immediate Adjacent Components (<5mm from U1):**

**Crystals:**
- **Y1**: NX2016SA-32MHZ (2.0x1.6mm, 32MHz) - place on XC1/XC2 side
  - C11, C12: 18pF 0402 (load capacitors)
- **Y2**: ABS07-32.768KHZ (3.2x1.5mm, 32.768kHz) - place on XL1/XL2 side
  - C13, C14: 12.5pF 0402 (load capacitors)

**DC-DC Components:**
- L_DCDC: (inductor for internal DC-DC) - place near DCC pin
  - C_DCC1: 100nF 0402
  - C_DCC2: 100nF 0402

**Bypass Capacitors (from C5-C8, C16, C18, C20-C22):**
- Distribute 100nF 0402 caps around U1 perimeter
- One cap per VDD pin, placed <2mm from pin
- Use C4 (10uF 0805) + C_bypass (100nF) for VDDH

**Critical Rules:**
1. **Y1 and Y2 crystals** must be <3mm from their respective pins
2. **No vias** under crystals or between crystal pads
3. **Ground pour** under crystals on bottom layer (via stitching around them)
4. **Thermal vias**: 9x 0.3mm vias in 3x3 grid under U1 center pad

**Keep-Out Zone:**
- Reserve 15mm x 5mm area at top-left corner for BLE PCB antenna
- No components or ground pour in antenna area

---

### **SX1262 LoRa Section (Middle-Left)**

**Primary Component:**
- **U2**: SX1262IMLTRT (QFN-24, 4x4mm with 2.6x2.6mm EP)

**Immediate Adjacent Components (<5mm from U2):**

**TCXO:**
- **Y3**: X1G0042110003 (2.5x2.0mm, 32MHz TCXO)
  - Connect to XTA pin (pin 14)
  - Powered by DIO3 (1.8V internal supply from SX1262)

**DC-DC Inductor:**
- L_SX: (47nH inductor for internal DC-DC) - place near VBAT_IO pins

**Bypass Capacitors:**
- C15, C19: 10uF 0805 (VDD_IN decoupling, pins 1 & 24)
- C_VBAT: 100nF 0402 (VBAT pin 20)
- C_VREG: 4.7uF 1206 (VREG pin 18)
- C_VR_PA: 100nF 0402 (VR_PA pin 19)

**Antenna Matching Network:**
- **L1**: 4.7nH 0402 inductor (MAPI-4020 footprint)
- **C17**: 2.2pF 0402 capacitor
- **J3**: U.FL-R-SMT-1(10) connector

**Placement Strategy:**
```
[U2: SX1262]
    │
    ├─[Y3: TCXO]────(to XTA pin 14)
    │
    ├─[RFI_P/RFI_N]──[L1: 4.7nH]──[C17: 2.2pF]──[J3: U.FL]
    │
    └─[Bypass caps around perimeter]
```

**Critical Rules:**
1. **RF path** from RFI_P/RFI_N (pins 22-23) to J3 must be:
   - 50-ohm microstrip (2.9mm width on 1.6mm FR4)
   - As short as possible (<20mm)
   - No vias in RF trace
   - Solid ground plane underneath
2. **Via fence** around entire SX1262 section (0.3mm vias every 3mm)
3. **Thermal vias**: 4x 0.3mm vias in 2x2 grid under U2 center pad
4. Keep J3 (U.FL) accessible at board edge
5. **Alternative**: If using PCB antenna, place 30mm inverted-F trace near bottom-right edge

---

### **Haptic Feedback Section (Bottom-Center)**

**Primary Component:**
- **U6**: DRV2605LDGSR (haptic driver with I2C control)

**Supporting Components:**
- C_HAP1: 10uF 0805 (VDD bypass)
- C_HAP2: 100nF 0402 (VDD bypass)
- **J6**: 2.54-2P-LT (LRA motor connector, 2-pin 2.54mm)

**I2C Connections:**
- SCL: to nRF52840 P0.27 (shared with accelerometer)
- SDA: to nRF52840 P0.26 (shared with accelerometer)

**Placement Strategy:**
```
[U6: DRV2605]──[C_HAP1: 10uF]──[C_HAP2: 100nF]
       │
       ├──[OUT+]─────[J6: LRA Motor]
       ├──[OUT-]─────[J6: LRA Motor]
       │
       └──[SCL/SDA]──(to U1 and U7/U8)
```

**Critical Rules:**
1. Place near bottom edge for easy access to motor
2. Keep motor traces short (<10mm) and away from RF sections
3. J6 should be at board edge or easily accessible
4. Add 100nF bypass cap right at VDD pin

**Note:** DRV2605 uses I2C control (more flexible than the original DRV2603 EN/PWM design)

---

### **Accelerometer Section (Upper-Center)**

**Primary Components:**
- **U7, U8**: LIS2DH12TR (LGA-12, 2x2mm, 3-axis accelerometer)

**Note:** BOM lists two LIS2DH12TR chips. Verify if:
- Both are accelerometers (redundancy or different mounting orientations?)
- One might be a different sensor with same footprint

**Supporting Components:**
- C_ACC_VDD: 100nF 0402 (VDD bypass for each IC)
- C_ACC_VDDIO: 100nF 0402 (VDDIO bypass for each IC)
- R_ACC_INT: 10kΩ 0402 (INT1 pull-up, optional)

**I2C Connections:**
- SCL: to nRF52840 P0.27 (shared bus with DRV2605)
- SDA: to nRF52840 P0.26 (shared bus with DRV2605)

**Placement Strategy:**
- Place near U1 (nRF52840) to minimize I2C trace lengths
- Orient for optimal motion sensing (typically perpendicular to board)
- SA0 pin to GND for I2C address 0x18 (or VDD for 0x19 if using two sensors)

**Critical Rules:**
1. Bypass caps <2mm from VDD/VDDIO pins
2. Keep away from high-vibration sources (buzzer, motor)
3. Consider mechanical coupling to enclosure for accurate motion sensing

---

### **User Interface Section (Bottom Edge)**

**LEDs:**
- **LED1**: Green LED with R2 (1kΩ 0603 series resistor)
- **LED2**: Red LED with R3 (1kΩ 0603 series resistor)
- Active-LOW configuration (cathode to GPIO)

**Buttons:**
- **SW1**: B3FS-1050P (user button)
  - Pull-up: R4, R5, R8, R13, or R16 (10kΩ 0603)
  - Debounce: 100nF 0402 cap

**Buzzer Circuit:**
- **LS1**: MLT-5020 (5mm passive buzzer)
- **Q1**: MMBT3904TT1G (NPN transistor, SC-75-3)
- **R17**: 1kΩ 0603 (base resistor)
- **D3**: 1N4148W-E3-18 (SOD-123 flyback diode)

**Placement:**
```
[LED1]──[R2]──(to P0.13)
[LED2]──[R3]──(to P0.14)

[SW1]──[R_PULLUP]──(to GPIO + 3.3V)
   │
   [100nF debounce]──GND

      3.3V
        │
    [LS1 Buzzer]
        │
     [D3 Diode]
        │
    Q1 Collector
        │
   Q1 Base──[R17]──(P0.17)
        │
    Q1 Emitter──GND
```

**Critical Rules:**
1. Place LEDs where they'll be visible (near edge or with light pipes)
2. Buttons need mechanical access through enclosure
3. Buzzer should be near edge for better sound projection
4. Keep buzzer away from sensitive RF sections

---

### **Connectors Section**

**J4: SWD Programming Header (2x3, 1.27mm pitch)**
- Part: 20021121-00006C4LF
- Standard ARM Cortex-M SWD pinout:
  ```
  1: VCC (3.3V)    2: SWDIO
  3: GND           4: SWDCLK
  5: GND           6: RESET
  ```
- Place at accessible edge (not under other components)
- Keep traces to U1 (SWDIO/SWDCLK pins) short

**J5: Expansion Header (1x8, 2.54mm pitch)**
- Part: 640456-8
- Pinout:
  ```
  1: VCC (3.3V)
  2: GND
  3: SDA (P0.26)
  4: SCL (P0.27)
  5: HAPTIC_EN (P0.04)
  6: LRA+
  7: LRA-
  8: GPIO (P0.05)
  ```
- Place at board edge for easy access
- Provides breakout for I2C, haptic control, and GPIO

---

### **Test Points**

Place 1mm test pads at these locations:

| Ref | Net | Purpose | Nearby Component |
|-----|-----|---------|------------------|
| TP1 | HAPTIC_EN | Debug P0.04 | Near U1, U6 |
| TP2 | SCL | Debug I2C clock | Along I2C bus trace |
| TP3 | SDA | Debug I2C data | Along I2C bus trace |
| TP4 | LRA+ | Motor drive + | Near U6, J6 |
| TP5 | LRA- | Motor drive - | Near U6, J6 |
| TP6 | ACCEL_INT1 | Accelerometer interrupt | Near U7/U8 |
| TP7 | BUZZER | Buzzer control signal | Near Q1, LS1 |

Additional recommended test points:
- TP_VBUS: USB input voltage
- TP_VBAT: Battery voltage
- TP_3V3: 3.3V rail
- TP_GND: Ground reference

---

## Overall Layout Strategy

### **Recommended Component Zones:**

```
+------------------------------------------------+ 46mm
|  [BLE ANTENNA]      [J1:USB-C] [D1][U5]        |
|   KEEPOUT           [U3:LDO] [U4:CHG] [J2:BAT] |
|                                                |
|  [U1: nRF52840]     [U7/U8: Accel]             |
|  [Y1][Y2][L_DCDC]                              |
|  [Bypass caps]                                 |
|                                                |
|  [U2: SX1262]       [L1][C17][J3:U.FL]         |
|  [Y3:TCXO]                                     |
|  [Bypass caps]                                 |
|                                                |
|  [J4:SWD]  [U6:HAP] [LED1][LED2] [SW1]         |
|            [J6:LRA] [Q1][LS1:BZ]               |
|                                                |
|  [J5: Expansion]            [LoRa ANT KEEPOUT] |
+------------------------------------------------+
              ^ 62mm
```

---

## Critical Routing Guidelines

### **1. RF Traces (50Ω microstrip)**
- **Width**: 2.9mm on 1.6mm FR4 with bottom ground plane
- **BLE antenna trace** from U1 to antenna area: <15mm
- **LoRa RF path** from U2 (RFI_P/RFI_N) through matching to J3: <20mm
- **No vias** in RF paths
- **Via fence** (0.3mm vias, 3mm spacing) around RF sections

### **2. USB Differential Pair (90Ω)**
- **Width**: 0.4mm each trace
- **Spacing**: 0.2mm between D+ and D-
- **Length match**: within 0.5mm
- Route from J1 to U1 USB pins with no vias if possible

### **3. Crystal Traces**
- Keep as short as possible (<3mm)
- No vias between crystal and IC pins
- Guard with ground traces/vias
- No high-speed signals crossing crystal traces

### **4. I2C Bus (SCL, SDA)**
- Can be routed at normal trace widths (0.2-0.3mm)
- Add pull-up resistors at U1 (nRF52840) end
- Keep traces parallel where possible
- Max length <50mm for reliable communication

### **5. Power Distribution**
- 3.3V rail: 0.5mm minimum width for main distribution
- Ground pour: maximize copper area on both layers
- Connect ground pours with via stitching every 5mm

### **6. Thermal Management**
- **U1 (nRF52840)**: 9x 0.3mm thermal vias in 3x3 grid under center pad
- **U2 (SX1262)**: 4x 0.3mm thermal vias in 2x2 grid under center pad
- Connect to bottom ground plane for heat dissipation

---

## Passive Component Mapping

### **Capacitors:**

| Reference | Value | Package | Qty | Primary Use |
|-----------|-------|---------|-----|-------------|
| C1, C2, C3, C4, C15, C19 | 10uF | 0805 | 6 | Power supply bulk decoupling |
| C9, C10 | 4.7uF | 1206 | 2 | Charger input/output |
| C5, C6, C7, C8, C16, C18, C20, C21, C22 | 100nF | 0402 | 9+ | Bypass caps (VDD pins) |
| C11, C12 | 18pF | 0402 | 2 | 32MHz crystal load caps |
| C13, C14 | 12.5pF | 0402 | 2 | 32.768kHz crystal load caps |
| C17 | 2.2pF | 0402 | 1 | Antenna matching |

### **Resistors:**

| Reference | Value | Package | Qty | Use |
|-----------|-------|---------|-----|-----|
| R1 | 2kΩ | 0603 | 1 | MCP73831 charge current programming |
| R2, R3 | 1kΩ | 0603 | 2 | LED current limiting |
| R4, R5, R8, R13, R16 | 10kΩ | 0603 | 5 | Pull-ups (buttons, I2C, etc.) |
| R6, R7 | 5.1kΩ | 0603 | 2 | USB CC pull-down resistors |
| R9, R10 | 0Ω | 0603 | 2 | Jumpers / current sense |
| R11, R12, R17 | 1kΩ | 0603 | 3 | General purpose (buzzer base, etc.) |
| R14, R15 | 4.7kΩ | 0603 | 2 | I2C pull-ups |

---

## Design Rule Checklist

- [ ] All bypass caps within 2mm of their IC power pins
- [ ] Crystals Y1, Y2 within 3mm of nRF52840 pins
- [ ] TCXO Y3 within 5mm of SX1262 XTA pin
- [ ] RF traces are 2.9mm wide with solid ground plane underneath
- [ ] Via fence around RF sections (every 3mm)
- [ ] No vias in RF signal paths
- [ ] USB differential pair: 0.4mm width, 0.2mm spacing, length-matched
- [ ] USB ESD (D1) within 3mm of USB connector
- [ ] Thermal vias under U1 (9x) and U2 (4x)
- [ ] BLE antenna keepout: 15mm x 5mm at top-left
- [ ] LoRa antenna keepout at bottom-right (if using PCB antenna)
- [ ] All connectors (J1-J6) accessible at board edges
- [ ] SWD header (J4) not blocked by other components
- [ ] Test points labeled and accessible
- [ ] Ground stitching vias every 5mm along ground pour boundaries
- [ ] No acute angle traces (use 45° or curved corners)
- [ ] Silkscreen labels for all connectors and important components
- [ ] Polarity markings for LEDs, diodes, and polarized capacitors

---

## Notes & Special Considerations

1. **LTC4412 Ideal Diode Controller (U5):**
   - Replaces simple Schottky diode for better power path management
   - Provides automatic switchover between USB and battery
   - Lower voltage drop than traditional diode OR-ing

2. **DRV2605 vs DRV2603:**
   - DRV2605 has I2C control with built-in waveform library
   - More flexible than original DRV2603 (EN/PWM control)
   - Shares I2C bus with accelerometer(s) - check I2C address conflict
   - Default I2C address: 0x5A

3. **Dual Accelerometers (U7, U8):**
   - BOM lists two LIS2DH12TR chips
   - If both are accelerometers: use different I2C addresses (SA0 pin)
     - U7: SA0 → GND (address 0x18)
     - U8: SA0 → VDD (address 0x19)
   - Possible use cases: redundancy, different mounting orientations, or one may be a different sensor

4. **Crystal Load Capacitors:**
   - Y1 (32MHz): Uses 18pF caps (original spec called for 8pF)
   - Verify crystal spec matches PCB design
   - Load capacitance formula: CL = (C1 × C2)/(C1 + C2) + Cstray

5. **Antenna Options:**
   - J3 (U.FL) allows external antenna connection
   - Can also use PCB trace antenna (inverted-F)
   - Don't populate both - choose based on enclosure design

---

## Revision History

- **v2 (2026-01-29):** Updated based on actual BOM with LTC4412, DRV2605, dual LIS2DH12
- **v1 (2026-01-28):** Initial placement guide from design specification
