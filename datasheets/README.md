# Component Datasheets

This directory contains datasheets for components used in the PCB Waypoint design.

## Downloaded Datasheets (Available in this directory)

| Component | Part Number | File | Size |
|-----------|-------------|------|------|
| LoRa Radio | SX1262IMLTRT | `SX1262_Datasheet.pdf` | 2.5 MB |
| SX1262 Reference Design | AN1200.40 | `SX1262_Reference_Design_AN1200.40.pdf` | 2.5 MB |
| Haptic Driver | DRV2605LDGSR | `DRV2605L_Datasheet.pdf` | 2.6 MB |
| Battery Charger | MCP73831T-2ACI/OT | `MCP73831_Datasheet.pdf` | 889 KB |
| N-Channel MOSFET | AO3400 | `AO3400_Datasheet.pdf` | 911 KB |
| N-Channel MOSFET | 2N7002 | `2N7002_Datasheet.pdf` | 304 KB |
| Signal Diode | 1N4148W | `1N4148W_Datasheet.pdf` | 320 KB |
| Schottky Diode | SS14 (reference) | `SS14_Datasheet.pdf` | 2.3 MB |
| USB-C Connector | USB4105-GF-A | `USB4105-GF-A_Datasheet.pdf` | 165 KB |
| USB ESD Protection | USBLC6-2P6 | `USBLC6-2P6_Datasheet.pdf` | 116 KB |

## Manual Download Required

The following datasheets require manual download due to website bot protection:

### Critical Components

| Component | Part Number | Download Link |
|-----------|-------------|---------------|
| Microcontroller | nRF52840-QIAA-R | [Nordic Product Specification (619 pages)](https://infocenter.nordicsemi.com/pdf/nRF52840_PS_v1.1.pdf) |
| Accelerometer | LIS2DH12TR | [ST Microelectronics](https://www.st.com/resource/en/datasheet/lis2dh12.pdf) |
| LDO Regulator | AP2112K-3.3TRG1 | [Diodes Incorporated](https://www.diodes.com/assets/Datasheets/AP2112.pdf) |
| Ideal Diode Controller | LTC4412MPS6 | [Analog Devices](https://www.analog.com/media/en/technical-documentation/data-sheets/4412fb.pdf) |

### Transistors & Discretes

| Component | Part Number | Download Link |
|-----------|-------------|---------------|
| NPN Transistor (current) | MMBT3904 | [ON Semiconductor](https://www.onsemi.com/pdf/datasheet/mmbt3904-d.pdf) |
| N-Channel MOSFET | BS170 | [ON Semiconductor](https://www.onsemi.com/pdf/datasheet/bs170-d.pdf) |

### Crystals & Oscillators

| Component | Part Number | Download Link |
|-----------|-------------|---------------|
| 32MHz Crystal | NX2016SA-32MHZ | [NDK](https://www.ndk.com/images/products/catalog/c_NX2016SA-STD-CRE-6_e.pdf) |
| 32.768kHz Crystal | ABS07-32.768KHZ-T | [Abracon](https://abracon.com/Resonators/ABS07.pdf) |
| TCXO | X1G0042110003 | [Epson](https://www5.epsondevice.com/en/products/crystal_oscillator/hg1.html) |

### Connectors

| Component | Part Number | Download Link |
|-----------|-------------|---------------|
| Battery Connector | B2B-PH-K-S(LF)(SN) | [JST](https://www.jst.com/products/crimp-style-connectors-wire-to-board-type/ph-connector/) |
| SWD Header | 20021121-00006C4LF | [Amphenol](https://www.amphenol-cs.com/product/2002112100006c4lf.html) |
| Expansion Header | 640456-8 | [TE Connectivity](https://www.te.com/usa-en/product-640456-8.html) |

### User Interface

| Component | Part Number | Download Link |
|-----------|-------------|---------------|
| Tactile Switch | B3FS-1050P | [Omron](https://omronfs.omron.com/en_US/ecb/products/pdf/en-b3fs.pdf) |
| Green LED | 150060VS75000 | [Wurth Elektronik](https://www.we-online.com/catalog/datasheet/150060VS75000.pdf) |
| Red LED | 150060RS75000 | [Wurth Elektronik](https://www.we-online.com/catalog/datasheet/150060RS75000.pdf) |
| Buzzer | MLT-5020/5030 | [Jiangsu Huaneng](https://datasheet.lcsc.com/lcsc/1811081431_Jiangsu-Huaneng-Elec-MLT-5020_C94598.pdf) |

### Motor & Haptics

| Component | Part Number | Download Link |
|-----------|-------------|---------------|
| LRA Motor | Jinlong G0832012D | [Jinlong Machinery](http://www.vibration-motor.com/coin-vibration-motors/linear-resonant-actuators) |

## Recommended Components for Design Changes

### MOSFET Replacement for Q1 (Buzzer Driver)

| Option | Part Number | Vds | Rds(on) | Package | Download |
|--------|-------------|-----|---------|---------|----------|
| Recommended | 2N7002 | 60V | 2-5Ω | SOT-23 | `2N7002_Datasheet.pdf` (included) |
| Low Rds(on) | AO3400 | 30V | 30mΩ | SOT-23 | `AO3400_Datasheet.pdf` (included) |
| Direct Replacement | BS170F | 60V | 1.2Ω | SOT-23 | [Fairchild/ON Semi](https://www.onsemi.com/pdf/datasheet/bs170-d.pdf) |
| Budget | DMN2056U | 20V | 100mΩ | SOT-23 | [Diodes Inc](https://www.diodes.com/assets/Datasheets/DMN2056U.pdf) |

## Application Notes

| Topic | Document | Link |
|-------|----------|------|
| SX1262 Best Performance | AN1200.37 | [Semtech](https://cdn.sparkfun.com/assets/f/f/b/4/2/SX1262_AN-Recommendations_for_Best_Performance.pdf) |
| SX1262 Reference Design | AN1200.40 | `SX1262_Reference_Design_AN1200.40.pdf` (included) |
| nRF52840 Hardware Design | nAN-12 | [Nordic DevZone](https://devzone.nordicsemi.com/nordic/nordic-blog/b/blog/posts/design-guide-for-nrf52840-based-designs) |
| Antenna Design | DN023 | [Texas Instruments](https://www.ti.com/lit/an/swra117d/swra117d.pdf) |

## How to Download Manually

1. Click the download link for the component
2. If redirected to a login page, look for "Download PDF" or "Datasheet" button
3. Save the file to this `datasheets/` directory
4. Use the naming convention: `PartNumber_Datasheet.pdf`

## Verification

After downloading, verify PDFs are valid:
```bash
file datasheets/*.pdf | grep "PDF document"
```

---

*Last updated: January 31, 2026*
