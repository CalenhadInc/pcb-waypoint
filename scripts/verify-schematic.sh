#!/bin/bash
# Verify KiCad schematic and generate exports
# Usage: ./scripts/verify-schematic.sh [schematic.kicad_sch] [output_dir]

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"

# Defaults
SCHEMATIC="${1:-$PROJECT_DIR/waypoint-kicad/waypoint-kicad.kicad_sch}"
OUTPUT_DIR="${2:-$PROJECT_DIR/exports}"

echo "=== KiCad Schematic Verification ==="
echo "Schematic: $SCHEMATIC"
echo "Output:    $OUTPUT_DIR"
echo ""

# Run the Python parser
python3 "$SCRIPT_DIR/parse_kicad_schematic.py" "$SCHEMATIC" "$OUTPUT_DIR"

echo ""
echo "=== Generated Files ==="
ls -lh "$OUTPUT_DIR"

echo ""
echo "=== Quick Commands ==="
echo "View ERC:      cat $OUTPUT_DIR/*_erc.rpt"
echo "View BOM:      column -t -s, $OUTPUT_DIR/*_bom_kicad.csv | head -20"
echo "View Nets:     head -100 $OUTPUT_DIR/*.net"
