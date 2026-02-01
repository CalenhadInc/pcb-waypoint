# Agent Guidelines for pcb-waypoint

## Project Overview

Waypoint is a festival LoRa mesh communicator PCB design. The schematic is in KiCad format.

## Key Documents

- `docs/waypoint-v2-design.md` - **Source of truth** for component references, pin assignments, and design decisions
- `docs/design-review-changes.md` - Historical document from January 2026 review (many items now resolved)
- `waypoint-kicad/waypoint-kicad.kicad_sch` - Current schematic

## Scripts

### `scripts/verify-schematic.sh`

**Purpose:** Export schematic data for verification.

**Usage:**
```bash
./scripts/verify-schematic.sh                          # Uses defaults
./scripts/verify-schematic.sh path/to/schematic.kicad_sch output/dir
```

**When to use:**
- After making schematic changes to verify exports
- To generate authoritative netlist and BOM via KiCad CLI
- To run ERC (Electrical Rules Check)

**Outputs (in `exports/`):**
| File | Source | Description |
|------|--------|-------------|
| `*.net` | KiCad CLI | Authoritative netlist (S-expression) |
| `*_netlist.xml` | KiCad CLI | Authoritative netlist (XML) |
| `*_bom_kicad.csv` | KiCad CLI | Authoritative BOM |
| `*_erc.rpt` | KiCad CLI | ERC report with errors/warnings |
| `*_bom.csv` | Python | Component list |
| `*_export.json` | Python | Full machine-readable data |
| `*_summary.txt` | Python | Component summary by type |
| `*_netlist_summary.txt` | Python | Net label summary |

### `scripts/parse_kicad_schematic.py`

**Purpose:** Parse KiCad schematic and generate exports. Called by `verify-schematic.sh`.

**Important:** This script **exports what exists** - it makes no assertions about what components should or shouldn't be present. Design verification should be done by comparing exports against `docs/waypoint-v2-design.md`.

**Usage:**
```bash
python3 scripts/parse_kicad_schematic.py <schematic.kicad_sch> [output_dir]
```

## Component Naming

- `docs/waypoint-v2-design.md` - Current component designators (source of truth)
- `docs/decision-log.md` - Decision 15 documents component renaming history

## KiCad CLI

The scripts use KiCad CLI when available at:
- macOS: `/Applications/KiCad/KiCad.app/Contents/MacOS/kicad-cli`
- Linux: `/usr/bin/kicad-cli`

KiCad CLI generates authoritative exports that match what KiCad GUI would produce.
