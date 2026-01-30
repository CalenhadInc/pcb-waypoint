# U Chips Pin Assignments - Waypoint v2

This document contains all pin numbers and assignments for U1-U6 ICs.

**Note:** LTC4412 ideal diode controller removed - using simple SS14 Schottky diode (D2) instead.

---

## U1: nRF52840-QIAA-R (QFN-73, 7x7mm)

**Bluetooth/MCU - Nordic Semiconductor**

### Power Pins
| Pin | Name | Connection |
|-----|------|------------|
| B1 | VDD | 3.3V (power_in) |
| A22 | VDD | 3.3V |
| AD14 | VDD | 3.3V |
| AD23 | VDD | 3.3V |
| W1 | VDD | 3.3V |
| Y2 | VDDH | 3.3V (power_in) |
| B7 | VSS | GND (power_in) |
| EP | VSS | GND (thermal pad) |

### DC-DC Converter Pins
| Pin | Name | Connection |
|-----|------|------------|
| B3 | DCC | C3 (10uF) to GND |
| AB2 | DCCH | C4 (10uF) to GND |

### Decoupling Pins
| Pin | Name | Connection |
|-----|------|------------|
| C1 | DEC1 | C5 (100nF) to GND |
| A18 | DEC2 | C6 (100nF) to GND |
| D23 | DEC3 | C7 (100nF) to GND |
| B5 | DEC4 | C8 (100nF) to GND |
| N24 | DEC5 | C24 (100nF) to GND |
| E24 | DEC6 | C25 (100nF) to GND |
| AC5 | DECUSB | C26 (4.7µF) to GND |

### Crystal Pins
| Pin | Name | Connection |
|-----|------|------------|
| B24 | XC1 | Y1 (32MHz) + C11 (18pF) |
| A23 | XC2 | Y1 (32MHz) + C12 (18pF) |
| D2 | XL1/P0.00 | Y2 (32.768kHz) + C13 (12.5pF) |
| F2 | XL2/P0.01 | Y2 (32.768kHz) + C14 (12.5pF) |

### USB Pins
| Pin | Name | Connection |
|-----|------|------------|
| AD4 | D- | USB D- via D1 (USBLC6) |
| AD6 | D+ | USB D+ via D1 (USBLC6) |

### SPI to SX1262 (Port 1)
| Pin | Name | GPIO | Connection |
|-----|------|------|------------|
| A20 | NSS | P1.10 | U2 pin 19 (NSS) |
| B19 | SCK | P1.11 | U2 pin 18 (SCK) |
| B17 | MOSI | P1.12 | U2 pin 17 (MOSI) |
| A16 | MISO | P1.13 | U2 pin 16 (MISO) |
| B15 | BUSY | P1.14 | U2 pin 14 (BUSY) |
| A14 | DIO1 | P1.15 | R12 -> U2 pin 13 (DIO1) |
| R24 | RESET | P1.06 | U2 pin 15 (~RESET) |

### I2C Bus
| Pin | Name | GPIO | Connection |
|-----|------|------|------------|
| G1 | SDA | P0.26 | I2C SDA -> U5, U6 |
| H2 | SCL | P0.27 | I2C SCL -> U5, U6 |

### User Interface
| Pin | Name | GPIO | Connection |
|-----|------|------|------------|
| AD8 | LED1 | P0.13 | R2 -> LED1 |
| AC9 | LED2 | P0.14 | R3 -> LED2 |
| AD10 | BUTTON | P0.15 | SW1 + R4 pull-up |
| AC13 | RESET | P0.18 | R8 pull-up -> J4 |

### Haptic/Sensors
| Pin | Name | GPIO | Connection |
|-----|------|------|------------|
| J1 | HAPTIC_EN | P0.04 | U5 EN + TP1 + R16 |
| K2 | P0.05 | AIN3 | NC (available for PWM) |
| AD12 | BUZZER | P0.17 | Q1 base via R11 -> TP7 |

### Battery Voltage Monitoring
| Pin | Name | GPIO | Connection |
|-----|------|------|------------|
| A12 | VBAT_SENSE | P0.02/AIN0 | R17/R18 voltage divider mid-point |

**Voltage Divider Circuit:**
```
VBAT ─── R17 (1MΩ) ─┬─ VBAT_SENSE ─── U1 pin A12 (AIN0/P0.02)
                    │
         R18 (1MΩ) ─┘
                    │
                   GND
```

**ADC Calculation:**
- Divider ratio: 1:1 (divides by 2)
- 4.2V battery → 2.1V at ADC
- 3.0V battery → 1.5V at ADC
- Current drain: 4.2V / 2MΩ = 2.1µA (negligible)

**Firmware thresholds:**
- Low battery warning: 3.4V (1.7V at ADC)
- Critical shutdown: 3.2V (1.6V at ADC)

### Debug/SWD
| Pin | Name | Connection |
|-----|------|------------|
| AC24 | SWDIO | R10 -> J4 pin 2 |
| AA24 | SWDCLK | R9 -> J4 pin 4 |

### Antenna
| Pin | Name | Connection |
|-----|------|------------|
| H23 | ANT | **TODO:** Add BLE antenna matching network if BLE used |

**Note:** If using BLE, add pi-match network + chip antenna or U.FL connector.

### Unconnected GPIO (Available)
| Pin | Name | GPIO |
|-----|------|------|
| B13 | AIN1 | P0.03 |
| B11 | AIN4 | P0.28 |
| A10 | AIN5 | P0.29 |
| B9 | AIN6 | P0.30 |
| A8 | AIN7 | P0.31 |

**Note:** A12 (P0.02/AIN0) is now used for battery voltage monitoring via VBAT_SENSE.

---

## U2: SX1262IMLTRT (QFN-24, 4x4mm)

**LoRa Radio - Semtech**

### Power Pins
| Pin | Name | Connection |
|-----|------|------------|
| 1 | VDD_IN | 3.3V + C9 (4.7uF) |
| 10 | VBAT | 3.3V + C10 (4.7uF) |
| 2 | GND | Ground (power_in) |
| 5 | GND | Ground |
| 8 | GND | Ground |
| 20 | GND | Ground |
| 25 | GND | Thermal pad |

### SPI Interface
| Pin | Name | Connection |
|-----|------|------------|
| 19 | NSS | U1 P1.10 + R13 (10k pull-up) |
| 18 | SCK | U1 P1.11 |
| 17 | MOSI | U1 P1.12 |
| 16 | MISO | U1 P1.13 |

### Control Pins
| Pin | Name | Connection |
|-----|------|------------|
| 14 | BUSY | U1 P1.14 |
| 13 | DIO1 | R12 -> U1 P1.15 |
| 12 | DIO2 | NC (no antenna switch needed) |
| 6 | DIO3 | Y3 pin 4 (V+) - TCXO power control |
| 15 | ~RESET | U1 P1.06 |

### Crystal/TCXO
| Pin | Name | Connection |
|-----|------|------------|
| 3 | XTA | Y3 pin 3 (OUT) - TCXO clock input |
| 4 | XTB | NC (not used with TCXO) |

**TCXO Wiring (Y3):**
```
U2 pin 6 (DIO3) ─── Y3 pin 4 (V+)
U2 pin 3 (XTA)  ─── Y3 pin 3 (OUT)
GND             ─── Y3 pin 2 (GND)
```

### RF Interface
| Pin | Name | Connection |
|-----|------|------------|
| 21 | RFI_P | R5 -> Matching network |
| 22 | RFI_N | C17 (2.2pF) -> GND |
| 23 | RFO | L1 (4.7nH) -> J3 antenna |

### Regulator
| Pin | Name | Connection |
|-----|------|------------|
| 7 | VREG | C23 (100nF) to GND |
| 9 | DCC_SW | L_SX1 (15nH) to VBAT_IO (pin 11) |
| 11 | VBAT_IO | L_SX1 + C22 (4.7µF) to GND |
| 24 | VR_PA | **TODO:** Add 100nF cap to GND |

**Note:** L_SX1 = 15nH per schematic. Verify against Semtech AN1200.40 reference design.

---

## U3: AP2112K-3.3TRG1 (SOT-23-5)

**3.3V LDO Regulator - Diodes Inc**

| Pin | Name | Connection |
|-----|------|------------|
| 1 | VIN | VBUS/VBAT via D2 + C15 (10uF) |
| 2 | GND | Ground |
| 3 | EN | VIN (tied high) |
| 4 | NC | Not connected |
| 5 | VOUT | 3.3V rail + C16 (10µF) |

---

## U4: MCP73831-2-OT (SOT-23-5)

**LiPo Battery Charger - Microchip**

| Pin | Name | Connection |
|-----|------|------------|
| 1 | STAT | Status output (tri-state) |
| 2 | VSS | GND + C19 |
| 3 | VBAT | Battery + via J2 + C19 |
| 4 | VDD | VBUS + C18 |
| 5 | PROG | R1 (2k) to GND (sets 500mA) |

---

## U5: DRV2605LDGS (WSON-10, 3x3mm)

**Haptic Driver - Texas Instruments**

| Pin | Name | Connection |
|-----|------|------------|
| 1 | REG | Internal regulator output + C27 (1µF) to GND |
| 2 | SCL | I2C Clock -> U1 P0.27 |
| 3 | SDA | I2C Data -> U1 P0.26 |
| 4 | IN/TRIG | PWM input (NC - not used) |
| 5 | EN | Enable -> U1 P0.04 + R16 pull-up + TP1 |
| 6 | NC | No Connect (leave unconnected) |
| 7 | OUT+ | LRA motor + -> J6 pin 1 + TP4 |
| 8 | GND | Ground |
| 9 | OUT- | LRA motor - -> J6 pin 2 + TP5 |
| 10 | VDD | 3.3V + C20 (100nF) |
| EP | Thermal | GND (solder to ground plane) |

---

## U6: LIS2DH12TR (LGA-12, 2x2mm)

**Accelerometer - STMicroelectronics**

| Pin | Name | Connection |
|-----|------|------------|
| 1 | SCL/SPC | I2C Clock -> U1 P0.27 |
| 2 | SDA/SDI | I2C Data -> U1 P0.26 |
| 3 | SA0 | I2C address select (GND = 0x18) |
| 4 | CS | I2C mode enable (tie to VDD) |
| 5 | INT2 | Interrupt 2 (NC) |
| 6 | INT1 | Interrupt 1 -> TP6 |
| 7 | Vdd_IO | 3.3V + C21 (100nF) + C29 (10µF) |
| 8 | Vdd | 3.3V + C21 (100nF) + C29 (10µF) |
| 9 | GND | Ground (power_in) |
| 10 | GND | Ground |
| 11 | GND | Ground |
| 12 | GND | Ground |
| 13 | GND | Ground |
| 14 | GND | Ground |

---

## Quick Reference: Critical Connections

### I2C Bus (All on same net)
```
U1 P0.26 (G1)  ──┬── U5 pin 3 (SDA)
                 ├── U6 pin 2 (SDA)
                 ├── R15 (4.7k) ── 3.3V
                 └── TP3

U1 P0.27 (H2)  ──┬── U5 pin 2 (SCL)
                 ├── U6 pin 1 (SCL)
                 ├── R14 (4.7k) ── 3.3V
                 └── TP2
```

### SPI Bus (U1 to U2)
```
U1 P1.10 (A20) ── R13 pull-up ── U2 pin 19 (NSS)
U1 P1.11 (B19) ────────────────── U2 pin 18 (SCK)
U1 P1.12 (B17) ────────────────── U2 pin 17 (MOSI)
U1 P1.13 (A16) ────────────────── U2 pin 16 (MISO)
U1 P1.14 (B15) ────────────────── U2 pin 14 (BUSY)
U1 P1.15 (A14) ──── R12 ───────── U2 pin 13 (DIO1)
U1 P1.06 (R24) ────────────────── U2 pin 15 (~RESET)
```

### Power Distribution
```
VBUS (USB) ──┬── U4 pin 4 (VDD) ─── Charger
             │
             D2 (SS14 Schottky)
             │
VBAT ────────┼── U3 pin 1 (VIN) ─── LDO
             │
             └── R17 ─┬─ VBAT_SENSE ─── U1 AIN0 (battery monitoring)
                      │
                  R18 ─┘
                      │
                     GND

U3 pin 5 (VOUT) ──── 3.3V rail
```

**Note:** D2 Schottky provides simple OR-ing of VBUS and VBAT.
~0.3V drop on battery path. See "Schematic Review Fixes" for power path improvement.

**Battery Monitoring:** R17+R18 (1MΩ each) form a voltage divider for ADC reading on P0.02.

### 3.3V Connections (all from U3 pin 5 VOUT)

**U1 (nRF52840) - 6 pins:**
| Pin | Name |
|-----|------|
| B1 | VDD |
| A22 | VDD |
| AD14 | VDD |
| AD23 | VDD |
| W1 | VDD |
| Y2 | VDDH |

**U2 (SX1262) - 2 pins:**
| Pin | Name |
|-----|------|
| 1 | VDD_IN |
| 10 | VBAT |

**U5 (DRV2605) - 1 pin:**
| Pin | Name |
|-----|------|
| 10 | VDD |

**U6 (LIS2DH12) - 3 pins:**
| Pin | Name |
|-----|------|
| 4 | CS (tie high for I2C mode) |
| 7 | Vdd_IO |
| 8 | Vdd |

**Pull-up Resistors to 3.3V:**
| Resistor | Purpose |
|----------|---------|
| R4 | Button (SW1) pull-up |
| R13 | SPI NSS pull-up |
| R14 | I2C SCL pull-up |
| R15 | I2C SDA pull-up |
| R16 | Haptic EN pull-up |

---

## Schematic Review Fixes

| Ref | Issue | Severity | Fix |
|-----|-------|----------|-----|
| VR_PA | Missing decoupling cap on U2 pin 24 | HIGH | Add 100nF cap to GND |
| L_SX1 | Verify value - schematic shows 15nH | VERIFY | Check against Semtech reference design |
| D2 | Schottky on both USB+VBAT causes headroom issues | MEDIUM | Consider moving D2 to USB path only (see below) |
| C16 | Was 100nF | DONE | Changed to **10µF** ✓ |
| C27 | Was missing | DONE | Added 1µF to DRV2605 REG (pin 1) ✓ |
| R17/R18 | Battery voltage divider | DONE | Correctly wired ✓ |

### Battery Voltage Divider (Verified Correct)

```
VBAT ─── R17 (1MΩ) ─┬─ VBAT_SENSE ─── U1 AIN0 (P0.02)
                    │
         R18 (1MΩ) ─┤
                    │
         C30 (100nF)┘
                    │
                   GND
```

### Power Path Improvement (Optional)

To improve battery headroom, move D2 Schottky to USB path only:

**Current:**
```
VBUS ──┬── D2 ──┬── U3 VIN
       │        │
VBAT ──┴────────┘
```

**Improved:**
```
VBUS ─── D2 ──┬── U3 VIN
              │
VBAT ─────────┘  (direct, no diode drop)
```

This allows operation down to 3.25V battery (vs 3.85V currently).

---

## Suggested Parts

| Ref | Part Number | Value | Package | Notes |
|-----|-------------|-------|---------|-------|
| L_SX1 | Murata LQW15AN15NJ00 | 15nH | 0402 | Per schematic |
| C_VRPA | Standard MLCC | 100nF | 0402 | Add for U2 VR_PA (pin 24) |
| R17, R18 | Standard | 1MΩ | 0402 | 1% tolerance for accuracy |
| C30 | Standard MLCC | 100nF | 0402 | VBAT_SENSE filter cap |

---

*Generated: 2026-01-30*
*Updated: 2026-01-30 - Added battery monitoring, verified R17/R18/C30 correct, updated L_SX1 to 15nH*
