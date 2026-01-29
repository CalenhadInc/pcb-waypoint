# Complete Datasheet Collection for nRF52840 + SX1262 PCB Design

*Compiled: January 28, 2026*

This document contains all critical datasheets, application notes, and design resources needed to design an nRF52840 + SX1262 PCB from scratch.

---

## 📡 PRIMARY RADIO COMPONENTS

### nRF52840 (Nordic Semiconductor)
**Primary Resources:**
- **Product Specification v1.1** (619 pages)
  - https://infocenter.nordicsemi.com/pdf/nRF52840_PS_v1.1.pdf
  - Comprehensive datasheet with all electrical specs, pinouts, peripherals
  
- **Product Brief** (2 pages)
  - https://www.mouser.com/datasheet/2/297/nrf52840_soc_v3_0-2942478.pdf
  - Quick overview of key features and specifications

- **nRF52840 DK Hardware Files**
  - Available at: https://www.nordicsemi.com/Products/Development-hardware/nRF52840-DK/Download
  - Contains Altium reference schematic and PCB layout
  - Critical for understanding BLE antenna design, crystal layout, and power distribution

**Key Technical Specs:**
- ARM Cortex-M4F @ 64 MHz
- 1MB Flash, 256KB RAM
- USB 2.0 full-speed controller
- Supply voltage: 1.7V to 5.5V
- BLE 5.3, Thread, Zigbee, 802.15.4, ANT, 2.4GHz
- On-chip DC-DC converter and LDO
- 48 GPIO pins

---

### SX1262 (Semtech)
**Primary Resources:**
- **SX1261/2 Datasheet Rev 1.2** (111 pages)
  - https://cdn.sparkfun.com/assets/6/b/5/1/4/SX1262_datasheet.pdf
  - Complete electrical specifications, register map, SPI interface

- **AN1200.40: SX1261/2 Reference Design Explanation** (PDF)
  - https://cdn-reichelt.de/documents/datenblatt/A200/SX1262REFERENCE.pdf
  - Contains complete reference schematics for 868MHz and 915MHz
  - PCB layout examples (PCB_E428V03A, PCB_E449V01A)
  - Critical component values and placement guidelines

- **AN1200.37: Recommendations for Best Performance** (PDF)
  - https://cdn.sparkfun.com/assets/f/f/b/4/2/SX1262_AN-Recommendations_for_Best_Performance.pdf
  - Thermal management and crystal placement
  - Frequency drift mitigation techniques
  - PCB thermal isolation design

- **Official Product Page**
  - https://www.semtech.com/products/wireless-rf/lora-connect/sx1262
  - Latest documentation and errata

**Key Technical Specs:**
- Frequency range: 150-960 MHz
- Maximum output power: +22 dBm
- Receive sensitivity: -148 dBm @ SF12, 125 kHz
- Supply voltage: 1.8V to 3.7V
- Integrated DC-DC converter
- Supports LoRa and (G)FSK modulation
- QFN 4x4mm package

**Critical Design Notes from Application Notes:**
- TCXO recommended for +22dBm operation at extreme temperatures
- Requires thermal isolation around crystal oscillator
- DC-DC mode preferred for efficiency
- DIO2 controls antenna switch, DIO3 controls TCXO

---

## 🔌 POWER MANAGEMENT

### Battery Charging ICs

#### Option 1: TP4056 (Low-cost, simple)
- **Datasheet:**
  - https://dlnmh9ip6v2uc.cloudfront.net/datasheets/Prototyping/TP4056.pdf
  - 1A standalone linear Li-Ion charger
  - Fixed 4.2V charge voltage
  - Programmable charge current via RPROG resistor
  - Thermal regulation
  - Charge status indicators
  
- **Typical Use:** Simple single-cell LiPo charging
- **Pros:** Very cheap, simple, widely available
- **Cons:** Linear (inefficient), no USB PD support

#### Option 2: MCP73831/2 (Microchip - Professional)
- **Datasheet:**
  - https://ww1.microchip.com/downloads/en/DeviceDoc/MCP73831-Family-Data-Sheet-DS20001984H.pdf
  - Miniature charge management controller
  - Programmable charge current up to 500mA
  - 4.2V charge voltage regulation ±0.05V
  - Automatic charge termination
  - SOT-23-5 package
  
- **Typical Use:** Space-constrained designs, USB charging
- **Pros:** Tiny package, accurate, low quiescent current
- **Cons:** Lower current capability than TP4056

### Battery Protection
- **DW01A Battery Protection IC**
  - Usually paired with TP4056 modules
  - Overcharge, overdischarge, overcurrent protection
  - Commonly found on complete charging modules

---

## 🕐 FREQUENCY REFERENCES

### Crystal Oscillators

#### For nRF52840:
**32 MHz High-Frequency Crystal (Required)**
- Recommended: NDK NX2016SA series
- Load capacitance: typically 8pF or 12pF
- ESR: <50Ω maximum
- Frequency tolerance: ±20 ppm
- Package: 2016 (2.0 x 1.6mm)

**32.768 kHz Low-Frequency Crystal (Optional for RTC)**
- Package: Various SMD sizes available
- Load capacitance: 7pF or 12.5pF typical

#### For SX1262:
**32 MHz TCXO (Recommended for +22dBm operation)**
- **NDK NT2016SA Series**
  - https://www.ndk.com/images/products/catalog/tcxo_e.pdf
  - 32MHz TCXO with ±1.5ppm or ±2.5ppm stability
  - Package: 2.0 x 1.6mm
  - Supply voltage: 1.8V to 3.3V
  - Clipped sine wave output
  
- **Abracon AST3TQ Series**
  - https://abracon.com/Oscillators/AST3TQ.pdf
  - Ultra-miniature TCXO
  - ±280ppb to ±2.8ppm stability options
  - LVCMOS output
  - Various frequencies available

**When to use TCXO vs Crystal:**
- Crystal: For LoRaWAN with standard packet sizes at moderate temperatures
- TCXO: Required for +22dBm continuous operation, extreme temperatures (-40°C to +70°C), or proprietary protocols with long packets

---

## 📶 RF & ANTENNA DESIGN

### Antenna Matching Components
**From SX1262 Reference Design:**
- Matching network uses 0402 size components
- Typical values (915MHz):
  - Series inductor: 5.6nH to 8.2nH
  - Shunt capacitor: 2.7pF to 3.9pF
  - Values depend on antenna impedance
- 50Ω transmission line width for FR4:
  - 2-layer 1.6mm board: ~1.2mm trace width
  - 4-layer board: narrower traces possible

### Antenna Options
**Commercial Antennas:**
- IPEX/U.FL connector standard
- PCB antennas for 868/915MHz
- External whip antennas: 3-6dBi typical gain

**PCB Antenna Design References:**
- Texas Instruments DN023 (Inverted-F antenna design)
- Consider ground plane requirements
- Keep antenna area clear of ground copper
- Typically 20-30mm length for 915MHz

### RF Switch (if using separate RX/TX paths)
- Required if using external LNA or PA
- Typical parts: Skyworks SKY13330 or equivalent
- Control via SX1262 DIO2 pin

---

## 🔧 SUPPORTING COMPONENTS

### Voltage Regulators
**For 3.3V System Supply:**
- LDO options: AP2112K-3.3, MCP1700-3302E, XC6206P332MR
- Buck converter: TPS62172 (if efficiency critical)

**For nRF52840 (Can use internal DC-DC):**
- L1 inductor: 10µH to 22µH, DCR <1Ω
- Typical: Murata LQM2HPN series

**For SX1262 DC-DC mode:**
- L1 inductor: 33nH typical (see datasheet Section 5.1.5)
- High current capability required

### Bypass Capacitors
- 0.1µF close to each IC power pin (0402 size)
- 1µF or 10µF bulk capacitors (0805 or larger)
- Low ESR ceramic (X5R or X7R)

### ESD Protection
- For USB: TPD2E001 or USBLC6-2SC6
- For antenna: Optional, LC filter can provide some protection

---

## 📐 REFERENCE DESIGNS TO STUDY

### Complete Open-Source Design
1. **BigCorvus LoRa-BLE-Relay-v2** (Most complete)
   - Repository: https://github.com/BigCorvus/LoRa-BLE-Relay-v2
   - Eagle format (.sch, .brd)
   - Gerbers and BOM included
   - 110x50mm board with GPS, SD card, sensors

### Commercial Reference Schematics
2. **RAK4630/RAK4631 Module**
   - Datasheet: https://docs.rakwireless.com/product-categories/wisblock/rak4631/datasheet/
   - Best GPIO mapping reference
   - Shows proper SPI connections

3. **LILYGO T-Echo**
   - Repository: https://github.com/Xinyuan-LilyGO/T-Echo
   - PDF schematics in /schematic folder
   - Includes GPS, e-Paper display, NFC

4. **Seeed Wio-SX1262 Module**
   - Schematic: https://files.seeedstudio.com/products/SenseCAP/Wio_SX1262/Wio-SX1262%20for%20XIAO%20V1.0_SCH.pdf
   - Minimal SX1262 implementation reference

### Manufacturer Reference Designs
5. **Nordic nRF52840 DK**
   - Download: https://www.nordicsemi.com/Products/Development-hardware/nRF52840-DK/Download
   - Altium design files
   - Arduino-compatible headers

6. **Semtech SX1262 Reference Designs**
   - PCB_E428V03A (915MHz)
   - PCB_E449V01A (868MHz with TCXO)
   - Request from Semtech or check AN1200.40 PDF

---

## 🎯 CRITICAL GPIO MAPPING (from RAK4630)

### SX1262 SPI Interface Connections
| SX1262 Pin | nRF52840 GPIO | Function |
|------------|---------------|----------|
| NSS        | P1.10         | SPI Chip Select |
| SCK        | P1.11         | SPI Clock |
| MOSI       | P1.12         | SPI Data Out |
| MISO       | P1.13         | SPI Data In |
| BUSY       | P1.14         | Status Signal |
| DIO1       | P1.15         | Interrupt |
| NRESET     | P1.06         | Reset |

**Additional SX1262 Control:**
- DIO2: Antenna switch control (configure via register)
- DIO3: TCXO power enable (configure via register)

---

## 📚 ADDITIONAL APPLICATION NOTES

### Nordic Application Notes
- nRF52840 Hardware Design Guide
- Bluetooth Antenna Design Guide
- DC-DC Inductor Selection Guide

### Semtech Application Notes
- AN1200.91: Miniaturized Design Using Johanson IPD
- AN1200.22: LoRa Modem Design Guide
- AN1200.13: LoRa Modulation Basics

---

## 🛠️ DESIGN CHECKLIST

### Power Supply
- [ ] 3.3V LDO or buck converter selected
- [ ] Battery charging IC chosen (TP4056 or MCP73831)
- [ ] Battery protection circuit included
- [ ] Bypass capacitors on all IC power pins
- [ ] nRF52840 DC-DC inductor sized (if using internal DC-DC)
- [ ] SX1262 DC-DC inductor selected (if using DC-DC mode)

### RF Design
- [ ] Antenna type selected (PCB, IPEX connector, or both)
- [ ] 50Ω transmission lines calculated for PCB stackup
- [ ] Antenna matching network designed
- [ ] Crystal vs TCXO decision made for SX1262
- [ ] Thermal isolation planned around SX1262 crystal (if using crystal)
- [ ] ESD protection considered for antenna port

### MCU Design
- [ ] 32MHz crystal selected for nRF52840
- [ ] Optional 32.768kHz crystal for RTC
- [ ] USB data lines routed with 90Ω differential impedance
- [ ] Programming header included (SWD: SWDIO, SWCLK, GND, VDD)
- [ ] Reset button included
- [ ] User LEDs included

### Component Selection
- [ ] All 0402 or 0603 sized passives (easier assembly)
- [ ] QFN packages have thermal vias under pad
- [ ] Check LCSC/JLCPCB availability if using assembly service

### PCB Layout
- [ ] 4-layer stackup recommended (better RF performance)
- [ ] Solid ground plane on layer 2
- [ ] Power plane on layer 3 (or split ground)
- [ ] RF traces on top layer, minimal vias
- [ ] Keep digital switching away from RF section
- [ ] Thermal relief for SX1262 (if needed per AN1200.37)

---

## 💡 DESIGN RECOMMENDATIONS

### For First Prototype:
1. **Start with modules if possible:**
   - XIAO nRF52840 ($7) + Wio-SX1262 ($8) = validated hardware
   - Design custom carrier board in KiCad
   - Reduces RF complexity risk

2. **If designing from scratch:**
   - Use 4-layer PCB (cost difference minimal, much better performance)
   - Follow Semtech PCB_E428V03A layout closely for SX1262 section
   - Follow Nordic nRF52840-DK layout for MCU section
   - Use TCXO for SX1262 to avoid crystal thermal issues
   - Include test points on all SPI signals
   - Add U.FL connector for external antenna testing

3. **Component Sourcing:**
   - nRF52840-QIAA-R7 (7x7mm QFN) widely available
   - SX1262IMLTRT (QFN24) - check stock at Mouser/Digikey
   - Consider SX1268 as alternative (same pinout, China bands)

4. **Firmware Resources:**
   - Nordic nRF Connect SDK (Zephyr-based)
   - Arduino nRF52 core (easiest to start)
   - Meshtastic firmware (if building mesh device)

---

## 📦 PACKAGE INFORMATION

### IC Package Sizes
- **nRF52840-QIAA:** 7x7mm QFN-73 (aQFN73)
  - 0.5mm pitch
  - Center thermal/ground pad
  - Land pattern in datasheet Section 15

- **SX1262:** 4x4mm QFN-24
  - 0.5mm pitch  
  - Center thermal/ground pad
  - Land pattern in datasheet Section 15.3

### Recommended via sizes:
- Power/ground vias: 0.3mm drill, 0.6mm pad
- Thermal vias under QFN: 0.2mm drill, 0.45mm pad
- Signal vias: 0.25mm drill, 0.5mm pad

---

## 🔗 QUICK LINKS SUMMARY

**Primary Datasheets:**
- nRF52840: https://infocenter.nordicsemi.com/pdf/nRF52840_PS_v1.1.pdf
- SX1262: https://cdn.sparkfun.com/assets/6/b/5/1/4/SX1262_datasheet.pdf

**Application Notes:**
- SX1262 Reference Design: https://cdn-reichelt.de/documents/datenblatt/A200/SX1262REFERENCE.pdf  
- SX1262 Best Performance: https://cdn.sparkfun.com/assets/f/f/b/4/2/SX1262_AN-Recommendations_for_Best_Performance.pdf

**Reference Designs:**
- BigCorvus (most complete): https://github.com/BigCorvus/LoRa-BLE-Relay-v2
- RAK4630 Datasheet: https://docs.rakwireless.com/product-categories/wisblock/rak4631/datasheet/

**Component Datasheets:**
- TP4056: https://dlnmh9ip6v2uc.cloudfront.net/datasheets/Prototyping/TP4056.pdf
- MCP73831: https://ww1.microchip.com/downloads/en/DeviceDoc/MCP73831-Family-Data-Sheet-DS20001984H.pdf
- NDK TCXO: https://www.ndk.com/images/products/catalog/tcxo_e.pdf

---

## 📝 NOTES

1. **Always start with reference designs** - Don't design RF sections from scratch unless you have RF experience and test equipment (VNA, spectrum analyzer)

2. **Test points are your friend** - Add them for all critical signals, especially SPI

3. **Order extra PCBs** - First spin rarely works perfectly, especially with RF

4. **Consider FCC/CE certification** - If this is a product, use pre-certified modules (RAK4630) or budget for testing

5. **Meshtastic compatibility** - If targeting Meshtastic, check their hardware documentation for specific GPIO requirements

---

*This datasheet collection is current as of January 2026. Always verify with manufacturer websites for latest revisions and errata.*
