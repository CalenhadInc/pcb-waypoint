# Python KiCAD Automation - Options and Setup

This document outlines the different Python approaches for automating component placement in KiCAD, created for the Waypoint v2 PCB project.

## Overview

There are three main approaches to programmatically place components on KiCAD PCB files:

### 1. **KiCAD pcbnew API** (Official, Most Powerful)
- **Location**: `kicad-placer/place_components.py`
- **Pros**: Official API, full feature access, most reliable
- **Cons**: Requires KiCAD installation, platform-specific setup
- **Use When**: You need complex operations (via creation, copper pours, DRC)

### 2. **S-Expression Parser** (Portable, No KiCAD Required)
- **Location**: `kicad-placer/place_components_sexp.py`
- **Pros**: No KiCAD required, pure Python, portable
- **Cons**: Manual parsing, limited validation, can break file format
- **Use When**: Simple placement tasks, scripting environments, CI/CD

### 3. **Third-Party Libraries** (Not Implemented)
- Libraries like `pykicad`, `kicad-python`
- Less maintained, may not support latest KiCAD versions
- Not recommended for production use

## Quick Start

### Recommended: S-Expression Parser (No Setup Required)

```bash
cd kicad-placer
uv run python place_components_sexp.py ../designs/Untitled/Untitled.kicad_pcb output.kicad_pcb
```

This works immediately without any KiCAD-specific setup.

### Alternative: pcbnew API (More Robust)

```bash
cd kicad-placer

# Test if pcbnew works
./run_with_kicad_python.sh test_pcbnew.py

# Run the placer
./run_with_kicad_python.sh place_components.py ../designs/Untitled/Untitled.kicad_pcb output.kicad_pcb
```

## Project Structure

```
pcb-waypoint/
├── kicad-placer/                          # Python automation tools
│   ├── place_components.py                # Main script (pcbnew API)
│   ├── place_components_sexp.py           # Alternative (S-expression parser)
│   ├── test_pcbnew.py                     # Test pcbnew setup
│   ├── run_with_kicad_python.sh           # Wrapper to find KiCAD Python
│   ├── README.md                          # Overview and setup
│   ├── USAGE.md                           # Detailed usage guide
│   └── pyproject.toml                     # uv project config
├── docs/
│   ├── placement-instructions-by-refdes.md # Source of coordinate data
│   └── component-placement-guide.md        # Placement strategy
└── designs/
    └── Untitled/
        └── Untitled.kicad_pcb             # Input PCB file
```

## Features

Both scripts support:

✅ **80+ Component Placements**
- Main ICs (U1-U8): nRF52840, SX1262, LDO, charger, haptic driver, accelerometers
- Crystals & oscillators (Y1-Y3)
- Connectors (J1-J6): USB-C, battery, RF, SWD, expansion, motor
- Passives: Capacitors (C1-C22), Resistors (R1-R17), Inductors (L1, L_DCDC, L_SX)
- User interface: LEDs, buttons, buzzer
- Protection: Diodes (D1-D3)
- Test points (TP1-TP7)

✅ **Coordinate System**
- Center-origin (0,0 at board center)
- Board: 46mm x 62mm
- X range: -23mm to +23mm
- Y range: -31mm to +31mm

✅ **Thermal Via Placement** (pcbnew only)
- U1 (nRF52840): 9 vias in 3x3 grid
- U2 (SX1262): 4 vias in 2x2 grid

## Setup Instructions

### Using pcbnew API

#### macOS

1. **Install KiCAD**
   ```bash
   # Download from https://www.kicad.org/download/
   # Or via Homebrew
   brew install --cask kicad
   ```

2. **Test Setup**
   ```bash
   cd kicad-placer
   ./run_with_kicad_python.sh test_pcbnew.py
   ```

   Expected output:
   ```
   ✓ Found KiCAD Python at: /Applications/KiCad/.../site-packages
   ✓ Using KiCAD Python: /Applications/KiCad/.../python3

   Testing pcbnew import...
   ✓ pcbnew imported successfully
     Version: 7.0.10
     Location: /Applications/KiCad/.../pcbnew.py
   ```

3. **Run the Placer**
   ```bash
   ./run_with_kicad_python.sh place_components.py input.kicad_pcb output.kicad_pcb
   ```

#### Linux

1. **Install KiCAD**
   ```bash
   sudo apt install kicad python3-pcbnew
   # or
   sudo dnf install kicad python3-pcbnew
   ```

2. **Test Import**
   ```bash
   python3 -c "import pcbnew; print(pcbnew.Version())"
   ```

3. **Run the Placer**
   ```bash
   cd kicad-placer
   uv run python place_components.py input.kicad_pcb output.kicad_pcb
   ```

#### Windows

1. **Install KiCAD** from https://www.kicad.org/download/

2. **Add to PATH**
   ```powershell
   $env:PYTHONPATH = "C:\Program Files\KiCad\7.0\lib\python3\site-packages"
   ```

3. **Run with KiCAD's Python**
   ```powershell
   & "C:\Program Files\KiCad\7.0\bin\python.exe" place_components.py input.kicad_pcb output.kicad_pcb
   ```

### Using S-Expression Parser (All Platforms)

No setup required! Just run:

```bash
cd kicad-placer
uv run python place_components_sexp.py input.kicad_pcb output.kicad_pcb
```

## Usage Examples

### Basic Placement

```bash
# S-expression parser (recommended to start)
uv run python place_components_sexp.py ../designs/Untitled/Untitled.kicad_pcb output.kicad_pcb

# pcbnew API (more robust)
./run_with_kicad_python.sh place_components.py ../designs/Untitled/Untitled.kicad_pcb output.kicad_pcb
```

### Verify Setup

```bash
# Test if pcbnew can be imported
./run_with_kicad_python.sh test_pcbnew.py

# Or manually
python3 -c "import pcbnew; print(pcbnew.Version())"
```

### Extract Positions from Existing Board

```python
#!/usr/bin/env python3
import pcbnew

board = pcbnew.LoadBoard("existing_board.kicad_pcb")

for fp in board.GetFootprints():
    pos = fp.GetPosition()
    x = pcbnew.ToMM(pos.x)
    y = pcbnew.ToMM(pos.y)
    rot = fp.GetOrientationDegrees()
    ref = fp.GetReference()

    print(f'"{ref}": ({x:.1f}, {y:.1f}, 0, "Notes"),  # {rot}°')
```

## Customization

### Modify Placement Data

Edit `place_components.py`:

```python
PLACEMENT_DATA = {
    "U1": (x_mm, y_mm, zone, "Description"),
    "R5": (x_mm, y_mm, zone, "Description"),
    # Add your components here
}
```

### Change Board Dimensions

```python
# In place_component() function
board_width_mm = 100   # Your board width
board_height_mm = 80   # Your board height
```

### Add Component Rotations

```python
place_component(board, "U1", x, y, rotation=90)  # Rotate 90°
```

## Workflow Integration

### 1. Manual Recreation (Current)
```
Schematic → Assign Footprints → Update PCB → Python Placer → Manual Routing
```

### 2. Automation with Python
```
Schematic → Netlist → Python Script → Placed PCB → Route & DRC
```

### 3. Full Automation (Future)
```
Design Spec → Generate Schematic → Auto-place → Auto-route → Generate Gerbers
```

## Next Steps After Placement

1. **Open in KiCAD**: Verify all components are placed correctly
2. **Add Via Fences**: Around RF sections (U2, matching network)
3. **Route Critical Traces**:
   - RF: 2.9mm width, 50Ω, no vias
   - USB: 0.4mm width, 0.2mm spacing, 90Ω
   - Crystals: <3mm to IC, no vias
4. **Ground Stitching**: Vias every 5mm
5. **Run DRC**: Check for violations
6. **Generate Gerbers**: For fabrication

## Troubleshooting

### pcbnew Import Error

```bash
# Option 1: Use S-expression parser instead
uv run python place_components_sexp.py input.kicad_pcb output.kicad_pcb

# Option 2: Use wrapper script
./run_with_kicad_python.sh place_components.py input.kicad_pcb output.kicad_pcb

# Option 3: Set PYTHONPATH manually
export PYTHONPATH="/Applications/KiCad/KiCad.app/Contents/Frameworks/Python.framework/Versions/Current/lib/python3.11/site-packages:$PYTHONPATH"
python3 place_components.py input.kicad_pcb output.kicad_pcb

# Option 4: Use KiCAD's Python directly
/Applications/KiCad/KiCad.app/Contents/Frameworks/Python.framework/Versions/Current/bin/python3 place_components.py input.kicad_pcb output.kicad_pcb
```

### Components Not Found

Make sure:
1. All components exist in schematic
2. Footprints are assigned
3. PCB is updated from schematic (F8)
4. Reference designators match PLACEMENT_DATA

### Coordinates Don't Match

The script uses **center-origin** coordinates while KiCAD uses **top-left origin**.

The script automatically converts coordinates. If components are in wrong positions:
1. Check board dimensions in script
2. Verify coordinate system in placement data
3. Adjust offsets if needed

## Resources

### Documentation
- [KiCAD Python API](https://docs.kicad.org/doxygen-python/)
- [S-Expression Format](https://dev-docs.kicad.org/en/file-formats/sexpr-intro/)
- [Waypoint v2 Placement Guide](docs/placement-instructions-by-refdes.md)

### Tools
- [KiCAD](https://www.kicad.org/) - PCB design software
- [uv](https://github.com/astral-sh/uv) - Fast Python package manager
- [pcbnew](https://docs.kicad.org/doxygen-python/namespacepcbnew.html) - KiCAD Python API

### Example Projects
- This project: Waypoint v2 PCB (nRF52840 + SX1262 LoRa tracker)
- [KiBot](https://github.com/INTI-CMNB/KiBot) - KiCAD automation tool
- [KiCAD Action Plugins](https://github.com/topics/kicad-action-plugin) - Community plugins

## Comparison: pcbnew vs S-Expression

| Feature | pcbnew API | S-Expression Parser |
|---------|------------|---------------------|
| **Setup Complexity** | Medium | None |
| **Dependencies** | KiCAD installation | None (pure Python) |
| **Portability** | Platform-specific | Universal |
| **Speed** | Fast | Fast |
| **Reliability** | Very High | Medium-High |
| **Feature Access** | Complete | Limited |
| **Via Creation** | Native | Manual string building |
| **Validation** | Built-in | Manual |
| **File Format Support** | Always current | May break on format changes |

**Recommendation**: Start with S-expression parser for basic placement, switch to pcbnew API when you need advanced features.

---

**Status**: ✅ Ready to use

Both scripts are functional and include complete placement data for the Waypoint v2 PCB (80+ components).

**Created**: 2026-01-29
**Project**: Waypoint v2 PCB
**Tool**: uv + Python 3.9+
