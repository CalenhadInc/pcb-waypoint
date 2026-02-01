# nRF52840 + SX1262 PCB Design Specification

## Board Parameters
- **Dimensions:** 46mm x 62mm
- **Layers:** 2-layer FR4
- **Thickness:** 1.6mm
- **Copper:** 1oz (35um)
- **Finish:** HASL or ENIG
- **Min trace/space:** 0.15mm / 0.15mm (6mil)

---

## Power Architecture

### Input: USB-C (5V) or LiPo Battery (3.7V nominal)

```
USB-C 5V ──────────┬──► 3.3V LDO (AP2112K)
                   │
VBAT ────[SS14]────┘
```

The Schottky diode prevents battery backfeed when USB is connected.

### Power Components

| Component | Part Number | Package | Function |
|-----------|-------------|---------|----------|
| LDO | AP2112K-3.3TRG1 | SOT-23-5 | 3.3V @ 600mA |
| Charger | MCP73831T-2ACI/OT | SOT-23-5 | 500mA charge current |
| Battery connector | JST-PH 2-pin | S2B-PH-K-S | Standard LiPo connector |
| USB-C | USB4105-GF-A | 16-pin SMD | USB 2.0 receptacle |
| ESD protection | USBLC6-2P6 | SOT-666 | USB ESD |
| Schottky Diode | SS14 | SMA | Battery backfeed protection |

### Power Passives

| Ref | Value | Package | Location |
|-----|-------|---------|----------|
| C18 | 100nF | 0402 | USB VBUS input |
| C15 | 10uF | 0805 | AP2112K input (VBAT side) |
| C16 | 10µF | 0402 | AP2112K output |
| C19 | 10uF | 0805 | MCP73831 output (VBAT) |
| R1 | 2k | 0402 | MCP73831 PROG (sets 500mA charge) |

---

## nRF52840 Section

### Part: nRF52840-QIAA-R7 (QFN-73, 7x7mm)

### Crystal Oscillators

| Function | Part | Frequency | Package | Load Cap |
|----------|------|-----------|---------|----------|
| HF Crystal | NX2016SA-32M-EXS00A-CS08760 | 32.000 MHz | 2.0x1.6mm | 8pF |
| LF Crystal | ABS07-32.768KHZ-7-T | 32.768 kHz | 3.2x1.5mm | 7pF |

### Crystal Load Capacitors
- **32MHz:** 2x 18pF (0402) - C_HF1, C_HF2
- **32.768kHz:** 2x 12.5pF (0402) - C_LF1, C_LF2

### Internal DC-DC Components

| Ref | Value | Package | Part Number |
|-----|-------|---------|-------------|
| L_DCDC | 10uH | 0805 | Murata LQM21PN100MGRD |
| C_DCC1 | 1uF | 0402 | Near DCC pin |
| C_DCC2 | 100nF | 0402 | Near DCC pin |

### Bypass Capacitors (all 0402)

| Pin | Value |
|-----|-------|
| VDD (each) | 100nF |
| VDDH | 4.7uF + 100nF |
| VBUS (USB) | 4.7uF |
| DECUSB | C26 (4.7uF) |
| DEC1-DEC4 | C5-C8 (100nF each) |
| DEC5 | C24 (100nF) |
| DEC6 | C25 (100nF) |

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
| BUTTON2 (Reset) | 18 | P0.18/RESET |

**Debug/Programming (SWD):**

| Signal | Pin | GPIO |
|--------|-----|------|
| SWDIO | 26 | SWDIO |
| SWDCLK | 25 | SWDCLK |
| RESET | 18 | P0.18 |

**Expansion Header / I2C / Haptics:**

| Signal | Pin | GPIO |
|--------|-----|------|
| SDA | 4 | P0.26 |
| SCL | 5 | P0.27 |
| HAPTIC_EN | 7 | P0.04 |
| TX | 6 | P0.06 |
| RX | 8 | P0.08 |

**Sensors:**

| Signal | Pin | GPIO |
|--------|-----|------|
| ACCEL_INT1 | 13 | P0.11 |
| BUZZER | 19 | P0.17 |
| VBAT_SENSE | 3 | P0.02 (AIN0) |

**Battery Voltage Sensing:**
- R17 (1MΩ) + R18 (1MΩ) voltage divider from VBAT
- C30 (100nF) filter capacitor
- Divider ratio: 1:1 (half of VBAT)
- At 4.2V battery: ~2.1V at ADC input

---

## SX1262 Section

### Part: SX1262IMLTRT (QFN-24, 4x4mm)

### Clock: 32MHz TCXO

| Part | Package | Stability | Voltage |
|------|---------|-----------|---------|
| YXC YSO110TR or TXC 7Q-32.000MBG-T | 2.0x1.6mm | +/-2.5ppm | 1.8V (from DIO3) |

*TCXO controlled by DIO3 - configure in software*

### DC-DC Inductor

| Ref | Value | Package | Part Number |
|-----|-------|---------|-------------|
| L_SX1 | 15nH | 0402 | Murata or equivalent |

### Antenna Matching Network (915 MHz)

*Values from Semtech AN1200.40 reference design:*

| Ref | Value | Package | Notes |
|-----|-------|---------|-------|
| C_MATCH1 | 2.2pF | 0402 | Series/shunt per reference |
| L_MATCH1 | 4.7nH | 0402 | Matching inductor |

### Bypass Capacitors

| Pin | Value | Package |
|-----|-------|---------|
| VDD_IN | 10uF + 100nF | 0805 + 0402 |
| VBAT | 100nF | 0402 |
| VREG | 4.7uF | 0603 |
| VR_PA | 100nF | 0402 |

### SX1262 Pin Connections

| Pin | Name | Connection |
|-----|------|------------|
| 1 | VDD_IN | 3.3V |
| 2 | GND | Ground |
| 3 | DIO2 | NC (antenna switch via register) |
| 4 | DIO1 | nRF52840 P1.15 |
| 5 | BUSY | nRF52840 P1.14 |
| 6 | NRESET | nRF52840 P1.06 |
| 7 | MISO | nRF52840 P1.13 |
| 8 | MOSI | nRF52840 P1.12 |
| 9 | SCK | nRF52840 P1.11 |
| 10 | NSS | nRF52840 P1.10 |
| 11-12 | GND | Ground |
| 13 | DIO3 | TCXO VCC (internal) |
| 14 | XTA | TCXO output |
| 15 | XTB | NC (not used with TCXO) |
| 16-17 | GND | Ground |
| 18 | VREG | 4.7uF to GND |
| 19 | VR_PA | 100nF to GND |
| 20 | VBAT | 3.3V (via 100nF) |
| 21 | GND | Ground |
| 22 | RFI_N | Matching network |
| 23 | RFI_P | Matching network |
| 24 | VDD_IN | 3.3V |
| PAD | GND | Ground (thermal vias) |

---

## Haptic Feedback Section

### Driver: DRV2605LDGS (I2C LRA/ERM driver with effects library)

| Spec | Value |
|------|-------|
| Part | DRV2605LDGS |
| Package | VSSOP-10 (3x3mm) |
| Interface | I2C (shared bus with accelerometer) |
| Supply | 2.0V - 5.2V (use 3.3V) |
| Output | Up to 300mA peak |
| Features | 123 built-in effects, auto-resonance, closed-loop |

### LRA Motor

| Part | Size | Resonant Freq |
|------|------|---------------|
| Jinlong G0832012D | 8x3.2mm | 235 Hz |

### Haptic Connections

| Signal | nRF52840 Pin | DRV2605L Pin |
|--------|--------------|--------------|
| SDA | P0.26 | SDA (pin 3) |
| SCL | P0.27 | SCL (pin 2) |
| EN | P0.04 | EN (pin 5) |

### Haptic Passives

| Ref | Value | Package | Purpose |
|-----|-------|---------|---------|
| C27 | 1µF | 0402 | REG pin decoupling |
| R16 | 10k | 0402 | EN pull-up |

---

## Accelerometer Section

### Part: LIS2DH12TR (3-axis accelerometer)

| Spec | Value |
|------|-------|
| Part | LIS2DH12TR |
| Package | LGA-12 (2x2mm) |
| Interface | I2C (shares bus with expansion header) |
| Supply | 1.71V - 3.6V (use 3.3V) |
| I2C Address | 0x18 or 0x19 (selectable via SA0 pin) |
| Features | Tap detection, motion wake, free-fall detection |

### Accelerometer Connections

| LIS2DH12 Pin | Connection | Notes |
|--------------|------------|-------|
| VDD | 3.3V | Power supply |
| VDDIO | 3.3V | I/O supply |
| GND | Ground | Ground |
| SCL | P0.27 (nRF52840) | I2C clock (shared bus) |
| SDA | P0.26 (nRF52840) | I2C data (shared bus) |
| INT1 | P0.11 (nRF52840) | Interrupt 1 (tap, motion) |
| INT2 | NC | Not connected |
| SA0 | GND | I2C address = 0x18 |
| CS | VDD | I2C mode (disable SPI) |

### Accelerometer Passives

| Ref | Value | Package | Purpose |
|-----|-------|---------|---------|
| C_ACC1 | 100nF | 0402 | VDD bypass |
| C_ACC2 | 100nF | 0402 | VDDIO bypass |
| R_ACC1 | 10k | 0402 | INT1 pull-up (optional) |

### Use Cases
- **Motion wake:** Sleep when stationary, wake on movement
- **Tap gestures:** Double-tap to send quick message
- **Drop detection:** Alert if device falls
- **Man down:** No movement alert after timeout

---

## Buzzer Section

### Part: Passive Buzzer (MLT-5030)

| Spec | Value |
|------|-------|
| Part | MLT-5030 or equivalent |
| Type | Passive buzzer (magnetic) |
| Package | 5mm diameter |
| Voltage | 3-5V |
| Frequency | 2-4 kHz (driven by PWM) |
| Current | ~30mA |

### Buzzer Driver Circuit

**NPN transistor switch:**

| Part | Part Number | Package | Function |
|------|-------------|---------|----------|
| Q1 | 2N3904 or MMBT3904 | SOT-23 | NPN switch |
| R_BUZZ | 1k | 0402 | Base resistor |
| D_BUZZ | 1N4148W | SOD-123 | Flyback diode |

### Buzzer Connections

```
P0.17 (nRF52840) ──[1k]──┬── Q1 Base
                          │
                     Q1 Collector ── Buzzer (+) ── 3.3V
                          │                    │
                          │                 [Diode]
                          │                    │
                     Q1 Emitter ──────────── GND
```

| Signal | Connection |
|--------|------------|
| BUZZER | P0.17 (nRF52840) via 1k resistor to transistor base |
| Buzzer + | 3.3V via transistor collector |
| Buzzer - | Ground |

### Use Cases
- **Audible alerts:** Louder than haptic for noisy environments
- **Find device:** Beep pattern to locate lost device
- **Alarms:** Critical notifications

---

## Antennas

### 915 MHz LoRa Antenna

**Type:** U.FL connector + PCB trace option

| Part | Part Number |
|------|-------------|
| U.FL connector | U.FL-R-SMT-1(10) |

*PCB antenna placeholder: 30mm inverted-F trace near board edge*

### 2.4 GHz BLE Antenna

**Type:** Chip antenna with matching network

| Ref | Part | Value | Purpose |
|-----|------|-------|---------|
| ANT1 | Chip Antenna | 2.4GHz | 1206 ceramic chip antenna |
| L2 | Inductor | 2.7nH | Antenna matching |
| C28 | Capacitor | 1.0pF | Antenna matching |

- Connected to nRF52840 ANT pin (H23) via L2
- Location: Opposite corner from LoRa antenna

---

## User Interface

### LEDs

| Ref | Color | Part Number | Resistor |
|-----|-------|-------------|----------|
| LED1 | Green | 150060VS75000 (Wurth) | 1k (0402) |
| LED2 | Red | 150060RS75000 (Wurth) | 1k (0402) |

*Active LOW configuration (cathode to GPIO)*

### Buttons

| Ref | Function | Part Number |
|-----|----------|-------------|
| SW1 | User button | B3FS-1050P |

*R4 (10k) pull-up to 3.3V, active-low*

**Note:** Hardware reset via SWD header (J4 pin 6) and R8 (10k) pull-up on nRESET line.

### Buzzer

See **Buzzer Section** for full circuit details.

| Ref | Part | Package |
|-----|------|---------|
| BZ1 | MLT-5030 passive buzzer | 5mm round |
| Q1 | MMBT3904 NPN transistor | SOT-23 |
| R_BUZZ | 1k resistor | 0402 |
| D_BUZZ | 1N4148W diode | SOD-123 |

---

## Connectors

### Programming Header (2x3, 1.27mm pitch)

Standard ARM SWD pinout:

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
5: HAPTIC_EN (P0.04)
6: LRA+
7: LRA-
8: GPIO (P0.05)
```

**Part:** TE Connectivity 640456-8

### LRA Motor Connector (2-pin, 2.54mm)

**Part:** 2.54-2P-LT (LCSC C722697)

---

## 2-Layer Layout Guidelines

### Layer Stack
- **Top:** Components, signals, RF traces
- **Bottom:** Ground pour (maximize), routing

### Critical Routing Rules

1. **RF Traces (50 ohm microstrip on 1.6mm FR4):**
   - Width: 2.9mm (with ground pour on bottom)
   - Keep as short as possible
   - No vias in RF path
   - No traces under antenna areas

2. **USB Differential Pair (90 ohm):**
   - Width: 0.4mm each trace
   - Spacing: 0.2mm between traces
   - Length match within 0.5mm

3. **Ground Stitching:**
   - Via fence around RF sections
   - Vias every 3mm along ground pour edges

4. **Thermal Vias:**
   - 9x vias under nRF52840 (3x3 grid, 0.3mm drill)
   - 4x vias under SX1262 (2x2 grid, 0.3mm drill)

5. **Component Placement Zones:**

```
+------------------------------------------------+
|  [BLE ANT]              [USB-C]                | <- 46mm
|                                                |
|  [nRF52840]      [Power]    [Charger]          |
|  [32M][32K]      [LIS2DH12]                    |
|                                                |
|  [SX1262]        [Matching]  [U.FL]            |
|  [TCXO]                                        |
|                                                |
|  [SWD]  [DRV2605L] [LEDs]   [JST BAT]          |
|         [Button]  [Buzzer]  [LoRa PCB ANT]     |
|                                        [LRA]   |
+------------------------------------------------+
                    ^ 62mm
```

---

## Test Points

| Ref | Net | Purpose |
|-----|-----|---------|
| TP1 | HAPTIC_EN | Debug P0.04 |
| TP2 | SCL | Debug I2C clock (shared by accel) |
| TP3 | SDA | Debug I2C data (shared by accel) |
| TP4 | LRA+ | Motor drive + |
| TP5 | LRA- | Motor drive - |
| TP6 | ACCEL_INT1 | Accelerometer interrupt |
| TP7 | BUZZER | Buzzer control signal |
