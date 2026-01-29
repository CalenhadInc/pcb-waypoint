# Manual Schematic Component Checklist

## Quick Add Guide

In KiCAD Schematic Editor:
1. Press `A` to add symbol
2. Search for the symbol name (e.g., "C" for capacitor)
3. Place it on the schematic
4. Double-click to edit properties:
   - Set Reference (C1, R1, etc.)
   - Set Value (10uF, 4.7k, etc.)
   - Set Footprint (see list below)

---

## Components to Add (72 total)

### ICs (8 components)

| Ref | Symbol to Search | Value | Footprint |
|-----|------------------|-------|-----------|
| U1 | nRF52840 or Generic IC | nRF52840-QIAA-R | Package_DFN_QFN:QFN-73-1EP_7x7mm_P0.5mm |
| U2 | SX1262 or Generic IC | SX1262IMLTRT | Package_DFN_QFN:QFN-24-1EP_4x4mm_P0.5mm |
| U3 | AP2112K or LDO | AP2112K-3.3 | Package_TO_SOT_SMD:SOT-23-5 |
| U4 | MCP73831 | MCP73831 | Package_TO_SOT_SMD:SOT-23-5 |
| U5 | LTC4412 or Generic IC | LTC4412 | Package_TO_SOT_SMD:SOT-23-6 |
| U6 | DRV2605 or Generic IC | DRV2605 | Package_SON:WSON-8-1EP_2x2mm_P0.5mm |
| U7 | LIS2DH12 or Accelerometer | LIS2DH12 | Package_LGA:LGA-12_2x2mm_P0.5mm |
| U8 | LIS2DH12 or Accelerometer | LIS2DH12 | Package_LGA:LGA-12_2x2mm_P0.5mm |

### Capacitors (22 components)

**Large caps (0805):**
| Ref | Value | Footprint |
|-----|-------|-----------|
| C1, C2, C3, C4 | 10uF | Capacitor_SMD:C_0805_2012Metric |
| C9, C10 | 4.7uF | Capacitor_SMD:C_0603_1608Metric |
| C15, C19 | 10uF | Capacitor_SMD:C_0805_2012Metric |

**Small caps (0402):**
| Ref | Value | Footprint |
|-----|-------|-----------|
| C5, C6, C7, C8 | 100nF | Capacitor_SMD:C_0402_1005Metric |
| C11, C12 | 18pF | Capacitor_SMD:C_0402_1005Metric |
| C13, C14 | 12.5pF | Capacitor_SMD:C_0402_1005Metric |
| C16, C18 | 100nF | Capacitor_SMD:C_0402_1005Metric |
| C17 | 2.2pF | Capacitor_SMD:C_0402_1005Metric |
| C20, C21, C22 | 100nF | Capacitor_SMD:C_0402_1005Metric |

**Quick method:**
- Press `A`, type "C", add capacitor symbol
- Place 22 of them
- Edit each one to set ref (C1-C22) and value

### Resistors (17 components)

All 0402 package:

| Ref | Value | Footprint |
|-----|-------|-----------|
| R1 | 2k | Resistor_SMD:R_0402_1005Metric |
| R2, R3 | 1k | Resistor_SMD:R_0402_1005Metric |
| R4 | 10k | Resistor_SMD:R_0402_1005Metric |
| R5 | 0R | Resistor_SMD:R_0402_1005Metric |
| R6, R7 | 5.1k | Resistor_SMD:R_0603_1608Metric |
| R8 | 10k | Resistor_SMD:R_0402_1005Metric |
| R9, R10 | 0R | Resistor_SMD:R_0402_1005Metric |
| R11, R12 | 1k | Resistor_SMD:R_0402_1005Metric |
| R13 | 10k | Resistor_SMD:R_0402_1005Metric |
| R14, R15 | 4.7k | Resistor_SMD:R_0402_1005Metric |
| R16 | 10k | Resistor_SMD:R_0402_1005Metric |
| R17 | 1k | Resistor_SMD:R_0402_1005Metric |

**Quick method:**
- Add 17 resistor symbols (`A` → "R")
- Edit each for ref (R1-R17) and value

### Crystals/Oscillators (3 components)

| Ref | Symbol | Value | Footprint |
|-----|--------|-------|-----------|
| Y1 | Crystal_GND24 | 32MHz | Crystal:Crystal_SMD_2016-4Pin_2.0x1.6mm |
| Y2 | Crystal | 32.768kHz | Crystal:Crystal_SMD_3215-2Pin_3.2x1.5mm |
| Y3 | Oscillator | TCXO | Oscillator:Oscillator_SMD_EuroQuartz_XO32-4Pin_3.2x2.5mm |

### Connectors (6 components)

| Ref | Symbol | Value | Footprint |
|-----|--------|-------|-----------|
| J1 | USB_C_Receptacle_USB2.0 | USB-C | Connector_USB:USB_C_Receptacle_GCT_USB4105-GF-A |
| J2 | Conn_01x02 | Battery | Connector_JST:JST_PH_B2B-PH-K_1x02_P2.00mm_Vertical |
| J3 | Conn_Coaxial | U.FL | Connector_Coaxial:U.FL_Hirose_U.FL-R-SMT-1_Vertical |
| J4 | Conn_02x03 | SWD | Connector_PinHeader_1.27mm:PinHeader_2x03_P1.27mm_Vertical_SMD |
| J5 | Conn_01x08 | Expansion | Connector_PinHeader_2.54mm:PinHeader_1x08_P2.54mm_Vertical |
| J6 | Conn_01x02 | LRA | Connector_PinHeader_2.54mm:PinHeader_1x02_P2.54mm_Vertical |

### Diodes (3 components)

| Ref | Symbol | Value | Footprint |
|-----|--------|-------|-----------|
| D1 | USBLC6-2P6 | USB ESD | Package_TO_SOT_SMD:SOT-666 |
| D2 | D_Schottky | SS14 | Diode_SMD:D_SMA |
| D3 | D | 1N4148W | Diode_SMD:D_SOD-123 |

### Other Components (11 components)

| Ref | Symbol | Value | Footprint |
|-----|--------|-------|-----------|
| LED1 | LED | Green | LED_SMD:LED_0805_2012Metric |
| LED2 | LED | Red | LED_SMD:LED_0805_2012Metric |
| SW1 | SW_Push | Button | Button_Switch_SMD:SW_SPST_B3U-1000P |
| LS1 | Buzzer | MLT-5020 | Buzzer_Beeper:Buzzer_CUI_CPT-9019S-SMT |
| Q1 | Q_NPN_BCE | MMBT3904 | Package_TO_SOT_SMD:SOT-23 |
| L1 | L | 4.7nH | Inductor_SMD:L_0402_1005Metric |
| TP1-TP7 | TestPoint | TP | TestPoint:TestPoint_Pad_D1.0mm |

---

## Time-Saving Tips

### Batch Adding
1. Add all capacitors first (22x), then edit refs/values
2. Add all resistors next (17x)
3. Then ICs, connectors, etc.

### Copy-Paste Method
1. Add one capacitor with footprint assigned
2. Copy it (`Ctrl+C`)
3. Paste 21 more times (`Ctrl+V`)
4. Edit each reference (C1, C2, C3...) and value

### Assign Footprints Later
1. Add all symbols first with just references
2. Then use `Tools → Assign Footprints` to do them all at once

---

## After Adding All Components

1. **Annotate:** `Tools → Annotate Schematic` (assigns sequential numbers)
2. **Check:** Verify you have all 72 components
3. **Update PCB:** `Tools → Update PCB from Schematic (F8)`
4. **Run Placement Script:**
   ```bash
   cd kicad-placer
   python3 place_components_sexp.py \
       ../waypoint-kicad/waypoint-kicad.kicad_pcb \
       ../waypoint-kicad/waypoint-kicad-placed.kicad_pcb
   ```

---

## Estimated Time

- **Manual schematic:** 30-45 minutes (much faster than full layout!)
- **Automated placement:** 5 seconds
- **Total:** ~45 minutes vs 7+ hours manual

**You're saving 6+ hours!** 🎉
