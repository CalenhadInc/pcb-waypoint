# Waypoint v2 - PCB Design Specification

*Last Updated: February 2026*

## Overview

**Product:** Waypoint - Festival LoRa Mesh Communicator
**Purpose:** MagSafe-attached device for Meshtastic/MeshCore mesh networking
**Target:** 7-day festival use, ~30 day battery life

---

## Board Parameters

| Parameter | Value |
|-----------|-------|
| Dimensions | 46mm x 62mm |
| Layers | 2-layer FR4 |
| Thickness | 1.6mm |
| Copper | 1oz (35µm) |
| Finish | HASL or ENIG |
| Min trace/space | 0.15mm / 0.15mm (6mil) |

---

## Power Architecture

### Separate Rails Design

USB only charges battery. System always runs from battery.

```
USB 5V ──► MCP73831 (U4) ──► LiPo Battery (J2)
              │                    │
              C18                  C19
                                   │
                                   ▼
                         ┌─────────────────┐
            ┌──[100k]────┤ EN         VIN ├──┬── VBAT
            │            │                 │  │
       U1.B13 (P0.03)    │   AP2112K (U3) │  C15 (10µF)
       (Power Control)   │                 │  │
                         │            GND ├──┴── GND
                         │                 │
                         │           VOUT ├──┬── 3.3V Rail
                         └─────────────────┘  │
                                              C16 (10µF)
                                              │
                                             GND
```

**Key Points:**
- No Schottky diode (D2 removed) - eliminates safety hazard
- Battery never sees USB voltage (max 4.2V from charger)
- System runs from battery even when USB connected
- Optional GPIO control of LDO enable (P0.03) for deep sleep

### Power Components

| Ref | Part Number | Package | Function |
|-----|-------------|---------|----------|
| U3 | AP2112K-3.3TRG1 | SOT-23-5 | 3.3V LDO @ 600mA |
| U4 | MCP73831T-2ACI/OT | SOT-23-5 | LiPo charger @ 500mA |
| J2 | B2B-PH-K-S(LF)(SN) | JST-PH 2-pin | Battery connector |
| D1 | USBLC6-2P6 | SOT-666 | USB ESD protection |

### Power Passives

| Ref | Value | Package | Purpose |
|-----|-------|---------|---------|
| C15 | 10µF | 0805 | LDO input (VBAT) |
| C16 | 10µF | 0805 | LDO output (3.3V) |
| C18 | 100nF | 0402 | USB VBUS bypass |
| C19 | 10µF | 0805 | Charger/battery bulk |
| R1 | 2kΩ | 0402 | Charger PROG (sets 500mA) |

---

## U1: nRF52840 (MCU)

**Part:** nRF52840-QIAA-R (QFN-73, 7x7mm)

### Power Pins

| Pin | Name | Connection |
|-----|------|------------|
| B1, A22, AD14, AD23, W1 | VDD | 3.3V |
| Y2 | VDDH | 3.3V |
| B7, EP | VSS | GND |

### DC-DC Converter

| Pin | Name | Connection |
|-----|------|------------|
| B3 | DCC | L_DCDC1 to DCCH + C3 (10µF) |
| AB2 | DCCH | L_DCDC1 to DCC + C4 (10µF) |

**Inductor:** L_DCDC1 = 10µH (Murata LQM21PN100MGRD)

### Decoupling Capacitors

| Pin | Ref | Value |
|-----|-----|-------|
| C1 (DEC1) | C5 | 100nF |
| A18 (DEC2) | C6 | 100nF |
| D23 (DEC3) | C7 | 100nF |
| B5 (DEC4) | C8 | 100nF |
| N24 (DEC5) | C24 | 100nF |
| E24 (DEC6) | C25 | 100nF |
| AC5 (DECUSB) | C26 | 4.7µF |

### Crystal Oscillators

| Ref | Frequency | Pins | Load Caps |
|-----|-----------|------|-----------|
| Y1 | 32.000 MHz | B24 (XC1), A23 (XC2) | C11, C12: 18pF |
| Y2 | 32.768 kHz | D2 (XL1), F2 (XL2) | C13, C14: 12.5pF |

### SPI to SX1262

| Pin | GPIO | Signal | Connection |
|-----|------|--------|------------|
| A20 | P1.10 | NSS | U2 pin 19 + R13 (10k pull-up) |
| B19 | P1.11 | SCK | U2 pin 18 |
| B17 | P1.12 | MOSI | U2 pin 17 |
| A16 | P1.13 | MISO | U2 pin 16 |
| B15 | P1.14 | BUSY | U2 pin 14 |
| A14 | P1.15 | DIO1 | U2 pin 13 via R12 |
| R24 | P1.06 | RESET | U2 pin 15 |

### I2C Bus (Shared)

| Pin | GPIO | Signal | Devices |
|-----|------|--------|---------|
| G1 | P0.26 | SDA | U5 (DRV2605), U6 (LIS2DH12) |
| H2 | P0.27 | SCL | U5 (DRV2605), U6 (LIS2DH12) |

Pull-ups: R14, R15 = 4.7kΩ to 3.3V

### User Interface

| Pin | GPIO | Signal | Connection |
|-----|------|--------|------------|
| AD8 | P0.13 | LED1 | R2 (1k) → LED1 (Green) |
| AC9 | P0.14 | LED2 | R3 (1k) → LED2 (Red) |
| AD10 | P0.15 | BUTTON | SW1 + R4 (10k pull-up) |
| AC13 | P0.18 | RESET | R8 (10k pull-up) → J4 |
| AD12 | P0.17 | BUZZER | R11 (1k) → Q1 base |

### Sensors & Control

| Pin | GPIO | Signal | Connection |
|-----|------|--------|------------|
| J1 | P0.04 | HAPTIC_EN | U5 EN + R16 (10k pull-up) |
| A12 | P0.02 (AIN0) | VBAT_SENSE | R17/R18 voltage divider |
| B13 | P0.03 | LDO_EN | U3 EN (optional power control) |

### USB

| Pin | Signal | Connection |
|-----|--------|------------|
| AD4 | D- | J1 USB D- via D1 |
| AD6 | D+ | J1 USB D+ via D1 |

### Debug (SWD)

| Pin | Signal | Connection |
|-----|--------|------------|
| AC24 | SWDIO | J4 pin 2 via R10 |
| AA24 | SWDCLK | J4 pin 4 via R9 |

### Antenna

| Pin | Signal | Connection |
|-----|--------|------------|
| H23 | ANT | L2 (2.7nH) → ANT1 chip antenna |

Matching: C28 = 1.0pF shunt to GND

---

## U2: SX1262 (LoRa Radio)

**Part:** SX1262IMLTRT (QFN-24, 4x4mm)

### Power Pins

| Pin | Name | Connection |
|-----|------|------------|
| 1, 24 | VDD_IN | 3.3V + C9 (4.7µF) |
| 10 | VBAT | 3.3V + C10 (4.7µF) |
| 2, 5, 8, 20, 25 | GND | Ground |

### SPI Interface

| Pin | Name | Connection |
|-----|------|------------|
| 19 | NSS | U1 P1.10 |
| 18 | SCK | U1 P1.11 |
| 17 | MOSI | U1 P1.12 |
| 16 | MISO | U1 P1.13 |
| 14 | BUSY | U1 P1.14 |
| 13 | DIO1 | U1 P1.15 via R12 |
| 15 | ~RESET | U1 P1.06 |

### TCXO

| Pin | Name | Connection |
|-----|------|------------|
| 6 | DIO3 | Y3 pin 4 (TCXO power) |
| 3 | XTA | Y3 pin 3 (TCXO output) |
| 4 | XTB | NC |

**TCXO:** Y3 = 32MHz, ±2.5ppm (YXC YSO110TR or TXC 7Q-32.000MBG-T)

### DC-DC & Regulator

| Pin | Name | Connection |
|-----|------|------------|
| 7 | VREG | C23 (100nF) to GND |
| 9 | DCC_SW | L_SX1 (15nH) to VBAT_IO |
| 11 | VBAT_IO | L_SX1 + C22 (4.7µF) to GND |
| 24 | VR_PA | C_VRPA (100nF) to GND |

### RF Interface

| Pin | Name | Connection |
|-----|------|------------|
| 21 | RFI_P | Matching network |
| 22 | RFI_N | C17 (2.2pF) to GND |
| 23 | RFO | L1 (4.7nH) → J3 (U.FL) |

---

## U5: DRV2605L (Haptic Driver)

**Part:** DRV2605LDGS (WSON-10, 3x3mm)

| Pin | Name | Connection |
|-----|------|------------|
| 1 | REG | C27 (1µF) to GND |
| 2 | SCL | U1 P0.27 |
| 3 | SDA | U1 P0.26 |
| 4 | IN/TRIG | NC |
| 5 | EN | U1 P0.04 + R16 (10k pull-up) |
| 7 | OUT+ | J6 pin 1 (LRA+) |
| 8 | GND | Ground |
| 9 | OUT- | J6 pin 2 (LRA-) |
| 10 | VDD | 3.3V + C20 (100nF) |

**I2C Address:** 0x5A (fixed)

---

## U6: LIS2DH12 (Accelerometer)

**Part:** LIS2DH12TR (LGA-12, 2x2mm)

| Pin | Name | Connection |
|-----|------|------------|
| 1 | SCL | U1 P0.27 |
| 2 | SDA | U1 P0.26 |
| 3 | SA0 | GND (I2C address 0x18) |
| 4 | CS | 3.3V (I2C mode) |
| 5 | INT2 | NC |
| 6 | INT1 | R_ACC_PU (10k) to 3.3V + TP6 |
| 7 | Vdd_IO | 3.3V (tied to Vdd) + C21 (100nF) |
| 8 | Vdd | 3.3V + C29 (10µF) |
| 9-14 | GND | Ground |

**I2C Address:** 0x18 (SA0 = GND)

**Note:** INT1 is open-drain, requires external pull-up.

---

## Buzzer Circuit

**Transistor:** Q1 = 2N7002 (N-Channel MOSFET, SOT-23)

```
P0.17 (U1.AD12) ──[R11: 1k]──┬── Q1 Gate
                              │
                           [R_GATE: 10k]
                              │
                             GND

                         3.3V
                           │
                        [D2: 1N4148W] (flyback)
                           │
                       LS1 Buzzer
                           │
                      Q1 Drain
                           │
                      Q1 Source
                           │
                          GND
```

**Note:** D2 is now the flyback diode (was D3, renumbered after removing power Schottky).

---

## Battery Voltage Monitoring

```
VBAT ─── R17 (1MΩ) ─┬─ VBAT_SENSE ─── U1 pin A12 (P0.02/AIN0)
                    │
         R18 (1MΩ) ─┤
                    │
         C30 (100nF)┘
                    │
                   GND
```

**ADC Calculation:**
- Divider ratio: 1:1 (divides by 2)
- 4.2V battery → 2.1V at ADC
- 3.0V battery → 1.5V at ADC
- Current drain: 4.2V / 2MΩ = 2.1µA

---

## Connectors

### J1: USB-C (USB4105-GF-A)

- USB 2.0 data via D1 ESD protection
- VBUS to U4 (charger) only
- CC1/CC2: R6, R7 = 5.1kΩ to GND

### J2: Battery (B2B-PH-K-S)

- Pin 1: VBAT (to U3 VIN, U4 BAT, R17)
- Pin 2: GND

### J3: LoRa Antenna (U.FL-R-SMT-1)

- 50Ω coaxial to matching network

### J4: SWD Header (2x3, 1.27mm)

```
┌───┬───┐
│VCC│SWD│  1: VCC (3.3V)
├───┼───┤  2: SWDIO
│GND│CLK│  3: GND
├───┼───┤  4: SWDCLK
│GND│RST│  5: GND
└───┴───┘  6: RESET
```

### J5: Expansion Header (1x8, 2.54mm)

1: VCC, 2: GND, 3: SDA, 4: SCL, 5: HAPTIC_EN, 6: LRA+, 7: LRA-, 8: GPIO

### J6: LRA Motor (1x2, 2.54mm)

- Pin 1: LRA+ (U5 OUT+)
- Pin 2: LRA- (U5 OUT-)

---

## Test Points

| Ref | Net | Purpose |
|-----|-----|---------|
| TP1 | HAPTIC_EN | P0.04 debug |
| TP2 | SCL | I2C clock |
| TP3 | SDA | I2C data |
| TP4 | LRA+ | Motor drive + |
| TP5 | LRA- | Motor drive - |
| TP6 | ACCEL_INT1 | Accelerometer interrupt |
| TP7 | BUZZER | P0.17 debug |

---

## Component Summary

### ICs (6)

| Ref | Part | Function |
|-----|------|----------|
| U1 | nRF52840-QIAA-R | BLE/MCU |
| U2 | SX1262IMLTRT | LoRa radio |
| U3 | AP2112K-3.3TRG1 | 3.3V LDO |
| U4 | MCP73831T-2ACI/OT | Battery charger |
| U5 | DRV2605LDGS | Haptic driver |
| U6 | LIS2DH12TR | Accelerometer |

### Passives

- **Capacitors:** C1-C30 (various values, 0402/0603/0805)
- **Resistors:** R1-R18, R_GATE, R_ACC_PU (various values, 0402)
- **Inductors:** L1 (4.7nH), L2 (2.7nH), L_DCDC1 (10µH), L_SX1 (15nH)

### Other

| Ref | Part | Function |
|-----|------|----------|
| Y1 | 32MHz crystal | nRF52840 HF |
| Y2 | 32.768kHz crystal | nRF52840 LF |
| Y3 | 32MHz TCXO | SX1262 reference |
| D1 | USBLC6-2P6 | USB ESD |
| D2 | 1N4148W | Buzzer flyback |
| Q1 | 2N7002 | Buzzer driver |
| ANT1 | Chip antenna | BLE 2.4GHz |
| LED1, LED2 | 0805 LED | Status indicators |
| SW1 | B3FS-1050P | User button |
| LS1 | MLT-5030 | Passive buzzer |

---

## Layout Guidelines

### RF Traces (50Ω microstrip)

- Width: 2.9mm on 1.6mm FR4
- Keep < 20mm length
- No vias in RF path
- Solid ground plane underneath

### USB Differential (90Ω)

- Width: 0.4mm each
- Spacing: 0.2mm
- Length match within 0.5mm

### Crystal Placement

- Y1, Y2 within 3mm of U1 pins
- No vias between crystal and IC
- Ground guard around crystals

### Thermal Vias

- U1 (nRF52840): 9x vias in 3x3 grid (0.3mm drill)
- U2 (SX1262): 4x vias in 2x2 grid (0.3mm drill)

### Ground Stitching

- Via fence around RF sections (3mm spacing)
- General ground stitching (5mm spacing)

---

## Revision History

| Version | Date | Changes |
|---------|------|---------|
| v5 | 2026-02-01 | Removed D2 (Schottky), separate rails power architecture |
| v4 | 2026-01-30 | Removed LTC4412, added DRV2605 haptic driver |
| v3 | 2026-01-29 | Added battery voltage monitoring |
| v2 | 2026-01-28 | Initial component selection |
| v1 | 2026-01-27 | Project start |

---

## Related Documents

- `decision-log.md` - Design decisions and trade-offs
- `enclosure-layout.md` - Mechanical design
- `future-improvements.md` - Roadmap
- `costing/bom-with-pricing.md` - Detailed BOM pricing
- `costing/supplier-comparison.md` - Sourcing strategy
- `automation/` - PCB automation scripts and guides
- `../datasheets/` - Component datasheets and references
