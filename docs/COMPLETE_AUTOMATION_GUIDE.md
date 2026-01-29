# Complete PCB Automation Guide - Waypoint v2

## 🎯 What We've Built

A **hybrid automation solution** that saves ~4 hours on PCB creation:

1. **Manual Schematic** (2-3 hours) - Full control, visual verification
2. **Automated Placement** (5 minutes) - Python script places 80+ components
3. **Manual Routing** (3-4 hours) - Critical traces need expertise

**Total time**: ~7 hours (vs 11 hours fully manual) = **36% faster!**

## 📁 Project Structure

```
pcb-waypoint/
├── kicad-placer/                          # Python automation tools
│   ├── place_components.py                # Placement (pcbnew API)
│   ├── place_components_sexp.py          # Placement (S-expression) ⭐ RECOMMENDED
│   ├── generate_schematic.py              # SKiDL (requires KiCAD libs)
│   ├── generate_schematic_simple.py       # SKiDL (simplified)
│   ├── test_pcbnew.py                     # Test pcbnew setup
│   ├── run_with_kicad_python.sh           # Wrapper script
│   ├── setup_kicad_paths.sh               # KiCAD lib finder
│   ├── README.md                          # Overview
│   ├── USAGE.md                           # Detailed guide
│   ├── SKIDL_WORKFLOW.md                  # SKiDL explanation
│   └── pyproject.toml                     # uv config
├── docs/
│   ├── design-specification.md            # Source of truth
│   ├── placement-instructions-by-refdes.md # Coordinate data
│   └── component-placement-guide.md        # Placement strategy
├── MANUAL_KICAD_RECREATION_GUIDE.md       # Step-by-step schematic guide
├── PYTHON_KICAD_AUTOMATION.md             # Options overview
└── COMPLETE_AUTOMATION_GUIDE.md           # This file
```

## 🚀 Quick Start (Recommended Path)

### Option 1: Just Automated Placement (Simplest)

Already have a KiCAD PCB file? Just want to place components?

```bash
cd kicad-placer
uv run python place_components_sexp.py input.kicad_pcb output.kicad_pcb
```

**That's it!** No KiCAD installation required, no setup, works immediately.

### Option 2: Complete Workflow (Full Board Creation)

Starting from scratch? Follow this sequence:

#### Step 1: Create Schematic (Manual - 2-3 hours)

```
1. Open KiCAD Schematic Editor
2. File → New Project → "waypoint-v2"
3. Follow MANUAL_KICAD_RECREATION_GUIDE.md
4. Add all components from design-specification.md
5. Wire connections per spec
6. Tools → Assign Footprints
7. File → Export → Netlist
```

#### Step 2: Create PCB and Update from Schematic (5 minutes)

```
1. Open KiCAD PCB Editor
2. File → New → Board
3. Tools → Update PCB from Schematic (F8)
4. All components appear in a pile at origin
5. Save as "waypoint-v2-unplaced.kicad_pcb"
```

#### Step 3: Automated Placement (5 minutes) ⭐

```bash
cd kicad-placer
uv run python place_components_sexp.py \
    ../designs/waypoint-v2-unplaced.kicad_pcb \
    ../designs/waypoint-v2-placed.kicad_pcb
```

Output:
```
✓ Placed U1       at ( -13.0,  -16.0) mm  # nRF52840
✓ Placed U2       at ( -13.0,    1.0) mm  # SX1262
✓ Placed U3       at (   5.0,  -21.0) mm  # LDO
...
✓ Placed 80 components
✅ Board saved successfully!
```

#### Step 4: Route Traces (Manual - 3-4 hours)

```
1. Open waypoint-v2-placed.kicad_pcb in KiCAD
2. Route critical traces:
   - RF: 2.9mm width, no vias, <20mm
   - USB: 0.4mm width, 0.2mm spacing, 90Ω
   - Crystals: <3mm, no vias
3. Add copper pours (top: signals, bottom: ground)
4. Add via stitching (RF: 3mm, ground: 5mm)
5. Run DRC and fix violations
6. Generate Gerbers
```

## 📊 What Gets Automated

### Placement Script Handles:

✅ **80+ Components**:
- U1-U8: ICs (nRF52840, SX1262, LDO, charger, sensors)
- Y1-Y3: Crystals and oscillators
- J1-J6: Connectors (USB, battery, RF, SWD, headers)
- C1-C34: Capacitors (bypass, bulk, load)
- R1-R17: Resistors (pull-up, LED, programming)
- L1-L3: Inductors (DC-DC, matching)
- D1-D3: Diodes (ESD, Schottky, flyback)
- LED1-LED2, SW1, LS1, Q1, TP1-TP7

✅ **Precise Positioning**:
- Crystals within 3mm of their ICs
- Bypass caps within 2mm of power pins
- RF matching network correctly aligned
- Connectors at board edges
- All per design specification

✅ **Coordinate System Conversion**:
- Input: Center-origin (0,0 at board center)
- Output: KiCAD's top-left origin
- Automatic conversion - you don't need to think about it

### What You Still Do Manually:

❌ **Schematic Creation** (2-3 hours)
- Requires domain knowledge
- Visual verification important
- Easy in KiCAD GUI

❌ **Routing** (3-4 hours)
- Critical RF traces need expertise
- Design rules specific to board
- Optimization opportunities

❌ **Verification** (30 min)
- DRC checks
- Visual inspection
- Final tweaks

## 🔧 Tools Comparison

### 1. S-Expression Parser (⭐ Recommended)

**File**: `place_components_sexp.py`

**Pros**:
- ✅ No KiCAD installation needed
- ✅ Pure Python, works anywhere
- ✅ Fast and simple
- ✅ Works immediately

**Cons**:
- ⚠️ Manual via creation
- ⚠️ Limited validation

**When to use**: Just want to place components quickly

### 2. pcbnew API (Most Robust)

**File**: `place_components.py`

**Pros**:
- ✅ Official KiCAD API
- ✅ Full feature access
- ✅ Thermal via creation
- ✅ Native validation

**Cons**:
- ⚠️ Requires KiCAD installation
- ⚠️ Platform-specific setup

**When to use**: Need advanced features like via creation

### 3. SKiDL Schematic Generator (Experimental)

**File**: `generate_schematic.py`

**Pros**:
- ✅ Programmatic schematic creation
- ✅ Reproducible builds
- ✅ Version control friendly

**Cons**:
- ⚠️ Requires KiCAD libraries
- ⚠️ Complex setup
- ⚠️ Steep learning curve

**When to use**: Want to explore programmatic schematic design

## 📖 Documentation Guide

### For Your Current Task, Read These (in order):

1. **MANUAL_KICAD_RECREATION_GUIDE.md** - How to create the schematic
2. **kicad-placer/USAGE.md** - How to use the placement script
3. **design-specification.md** - Routing rules and design details

### For Understanding Options:

- **PYTHON_KICAD_AUTOMATION.md** - Overview of all approaches
- **kicad-placer/README.md** - Placement tool overview
- **kicad-placer/SKIDL_WORKFLOW.md** - SKiDL explanation

### For Reference:

- **placement-instructions-by-refdes.md** - Coordinate data
- **component-placement-guide.md** - Placement strategy

## ⏱️ Time Breakdown

### Manual Workflow (Total: ~11 hours)

```
Schematic:       3 hours
Placement:       4 hours  ← This is what we automate!
Routing:         4 hours
────────────────────────
Total:          11 hours
```

### Hybrid Workflow (Total: ~7 hours) ⭐

```
Schematic:       3 hours
Placement:       5 minutes  ← Automated! 🎉
Routing:         4 hours
────────────────────────
Total:          ~7 hours
Savings:         4 hours  (36% faster)
```

### Where the Time Goes:

| Task | Manual | Hybrid | Notes |
|------|--------|--------|-------|
| Learning KiCAD | 2 hours | 2 hours | One-time cost |
| Creating schematic | 3 hours | 3 hours | Domain knowledge required |
| Assigning footprints | 30 min | 30 min | Easy in GUI |
| **Placing components** | **4 hours** | **5 min** | ⭐ Automated! |
| Routing traces | 4 hours | 4 hours | Expertise needed |
| DRC and fixes | 30 min | 30 min | Verification |
| Generate Gerbers | 10 min | 10 min | Automated |

## 🎓 Learning Path

### Beginner (First PCB)

1. Start with **manual schematic** (learn KiCAD basics)
2. Use **automated placement** (see it work!)
3. Manual routing with tutorial
4. Estimated: 12 hours first time, 7 hours next time

### Intermediate (Done a few PCBs)

1. Manual schematic (you know what you're doing)
2. Automated placement (saves time)
3. Manual routing (you're good at this)
4. Estimated: 7 hours

### Advanced (Want more automation)

1. Explore SKiDL for schematic generation
2. Automated placement (standard)
3. Consider auto-routing for non-critical nets
4. Estimated: 5-6 hours (with setup time)

## 🐛 Troubleshooting

### "Component not found" warnings

**Cause**: Component doesn't exist in PCB yet

**Solution**:
```
In KiCAD Schematic Editor:
Tools → Annotate Schematic (assign ref des)

In KiCAD PCB Editor:
Tools → Update PCB from Schematic (F8)
```

### "ImportError: No module named 'pcbnew'"

**Cause**: KiCAD Python not in PATH

**Solution** (choose one):
```bash
# Option 1: Use S-expression parser instead (no pcbnew needed)
uv run python place_components_sexp.py input.kicad_pcb output.kicad_pcb

# Option 2: Use wrapper script
./run_with_kicad_python.sh place_components.py input.kicad_pcb output.kicad_pcb

# Option 3: Set PYTHONPATH
export PYTHONPATH="/Applications/KiCad/.../site-packages:$PYTHONPATH"
```

### Components in wrong positions

**Cause**: Board dimensions don't match script

**Solution**:
```python
# Edit place_components.py:
board_width_mm = 46   # Change to your board width
board_height_mm = 62  # Change to your board height
```

### SKiDL can't find libraries

**Cause**: KICAD7_SYMBOL_DIR not set

**Solution**:
```bash
cd kicad-placer
chmod +x setup_kicad_paths.sh
source setup_kicad_paths.sh
```

## 🎯 Success Checklist

After running the placement script:

- [ ] Open placed PCB in KiCAD
- [ ] All components visible (not off-board)
- [ ] Connectors at board edges
- [ ] Crystals near their ICs (<5mm)
- [ ] Bypass caps near power pins (<3mm)
- [ ] No overlapping components
- [ ] Test points accessible
- [ ] Silkscreen readable

If all checked, proceed to routing!

## 🚀 Next Steps

### Ready to Start?

1. **Review your docs**: `design-specification.md` and `MANUAL_KICAD_RECREATION_GUIDE.md`
2. **Create schematic**: Follow the guide step-by-step
3. **Update PCB**: Import netlist
4. **Run placement**: `uv run python place_components_sexp.py ...`
5. **Route traces**: Follow critical routing rules
6. **DRC**: Fix any violations
7. **Gerbers**: Generate for fabrication

### Want to Learn More?

- **KiCAD Getting Started**: https://docs.kicad.org/
- **SKiDL Documentation**: https://devbisme.github.io/skidl/
- **pcbnew API**: https://docs.kicad.org/doxygen-python/
- **This project's docs**: All the .md files!

## 📝 Summary

**What works perfectly right now**:
✅ Component placement automation (S-expression parser)
✅ Component placement automation (pcbnew API)
✅ Complete coordinate data for Waypoint v2
✅ Comprehensive documentation

**What requires manual work**:
❌ Schematic creation (but we have a guide!)
❌ Routing (but we have design rules!)

**What's experimental**:
🔬 SKiDL schematic generation (works but complex setup)

**Recommended approach**:
🎯 Manual schematic + Automated placement + Manual routing = **Best results!**

**Time saved**:
⏱️ 4 hours per board (36% faster than fully manual)

---

**You're all set!** The automation is ready to use. Start with the schematic, let Python handle placement, and you'll have a professional PCB in ~7 hours. 🎉
