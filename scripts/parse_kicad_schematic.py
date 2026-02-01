#!/usr/bin/env python3
"""
KiCad Schematic Parser for Design Review Verification
Parses .kicad_sch files and generates BOM, netlist, and ERC reports.
"""

import re
import json
import csv
import sys
import subprocess
import shutil
from pathlib import Path
from dataclasses import dataclass, field
from typing import Optional
from collections import defaultdict


# Common KiCad CLI locations
KICAD_CLI_PATHS = [
    "/Applications/KiCad/KiCad.app/Contents/MacOS/kicad-cli",  # macOS
    "/usr/bin/kicad-cli",  # Linux
    "/usr/local/bin/kicad-cli",  # Linux alt
    "C:\\Program Files\\KiCad\\bin\\kicad-cli.exe",  # Windows
]


def find_kicad_cli() -> Optional[str]:
    """Find KiCad CLI executable."""
    # Check PATH first
    cli = shutil.which("kicad-cli")
    if cli:
        return cli

    # Check common locations
    for path in KICAD_CLI_PATHS:
        if Path(path).exists():
            return path

    return None


def generate_netlist_with_cli(
    schematic_path: str,
    output_path: str,
    format: str = "kicadsexpr"
) -> bool:
    """Generate netlist using KiCad CLI.

    Args:
        schematic_path: Path to .kicad_sch file
        output_path: Output netlist path
        format: One of kicadsexpr, kicadxml, cadstar, orcadpcb2, spice, spicemodel

    Returns:
        True if successful, False otherwise
    """
    cli = find_kicad_cli()
    if not cli:
        print("Warning: KiCad CLI not found, skipping netlist generation")
        return False

    try:
        result = subprocess.run(
            [cli, "sch", "export", "netlist",
             "--format", format,
             "--output", output_path,
             schematic_path],
            capture_output=True,
            text=True,
            timeout=60
        )

        if result.returncode != 0:
            print(f"KiCad CLI error: {result.stderr}")
            return False

        return True
    except subprocess.TimeoutExpired:
        print("KiCad CLI timed out")
        return False
    except Exception as e:
        print(f"KiCad CLI error: {e}")
        return False


def generate_bom_with_cli(
    schematic_path: str,
    output_path: str,
    format: str = "csv"
) -> bool:
    """Generate BOM using KiCad CLI.

    Args:
        schematic_path: Path to .kicad_sch file
        output_path: Output BOM path
        format: One of csv, json

    Returns:
        True if successful, False otherwise
    """
    cli = find_kicad_cli()
    if not cli:
        print("Warning: KiCad CLI not found, skipping BOM generation")
        return False

    try:
        result = subprocess.run(
            [cli, "sch", "export", "bom",
             "--output", output_path,
             schematic_path],
            capture_output=True,
            text=True,
            timeout=60
        )

        if result.returncode != 0:
            print(f"KiCad CLI BOM error: {result.stderr}")
            return False

        return True
    except Exception as e:
        print(f"KiCad CLI BOM error: {e}")
        return False


def run_erc_with_cli(
    schematic_path: str,
    output_path: str
) -> bool:
    """Run ERC using KiCad CLI.

    Args:
        schematic_path: Path to .kicad_sch file
        output_path: Output ERC report path

    Returns:
        True if successful, False otherwise
    """
    cli = find_kicad_cli()
    if not cli:
        print("Warning: KiCad CLI not found, skipping ERC")
        return False

    try:
        result = subprocess.run(
            [cli, "sch", "erc",
             "--output", output_path,
             schematic_path],
            capture_output=True,
            text=True,
            timeout=120
        )

        # ERC returns non-zero if there are errors, but still generates report
        return Path(output_path).exists()
    except Exception as e:
        print(f"KiCad CLI ERC error: {e}")
        return False


@dataclass
class Component:
    """Represents a schematic component/symbol."""
    reference: str
    value: str
    lib_id: str
    footprint: str
    description: str
    position: tuple[float, float]
    uuid: str
    pins: dict = field(default_factory=dict)
    in_bom: bool = True


@dataclass
class Wire:
    """Represents a wire connection."""
    start: tuple[float, float]
    end: tuple[float, float]
    uuid: str


@dataclass
class Label:
    """Represents a net label."""
    name: str
    position: tuple[float, float]
    uuid: str


@dataclass
class PowerSymbol:
    """Represents a power symbol (VDD, GND, etc.)."""
    reference: str
    value: str
    position: tuple[float, float]
    uuid: str


class KiCadSchematicParser:
    """Parser for KiCad 6+ schematic files (.kicad_sch)."""

    def __init__(self, filepath: str):
        self.filepath = Path(filepath)
        self.content = ""
        self.components: list[Component] = []
        self.wires: list[Wire] = []
        self.labels: list[Label] = []
        self.power_symbols: list[PowerSymbol] = []
        self.title = ""
        self.date = ""
        self.revision = ""

    def parse(self):
        """Parse the schematic file."""
        with open(self.filepath, 'r') as f:
            self.content = f.read()

        self._parse_title_block()
        self._parse_symbols()
        self._parse_wires()
        self._parse_labels()

    def _parse_title_block(self):
        """Extract title block information."""
        title_match = re.search(r'\(title "([^"]+)"\)', self.content)
        date_match = re.search(r'\(date "([^"]+)"\)', self.content)
        rev_match = re.search(r'\(rev "([^"]+)"\)', self.content)

        self.title = title_match.group(1) if title_match else ""
        self.date = date_match.group(1) if date_match else ""
        self.revision = rev_match.group(1) if rev_match else ""

    def _parse_symbols(self):
        """Extract all symbol instances (components)."""
        # Find all top-level symbols (not inside lib_symbols)
        # We look for (symbol patterns that have lib_id and are component instances

        # First, find where lib_symbols ends
        lib_symbols_end = self.content.find('(embedded_fonts')
        if lib_symbols_end == -1:
            lib_symbols_end = 0

        # Get the instance section (after lib_symbols)
        instance_section = self.content[lib_symbols_end:]

        # Pattern to match symbol blocks
        symbol_pattern = re.compile(
            r'\(symbol\s*\n?\s*\(lib_id\s+"([^"]+)"\)\s*\n?\s*\(at\s+([\d.-]+)\s+([\d.-]+)',
            re.MULTILINE
        )

        # Find all symbol starts
        for match in symbol_pattern.finditer(instance_section):
            lib_id = match.group(1)
            x = float(match.group(2))
            y = float(match.group(3))

            # Get the full symbol block
            start_pos = match.start()

            # Find properties within this symbol block
            # We need to extract until the next top-level (symbol or end
            block_start = instance_section.find('(symbol', start_pos)
            if block_start == -1:
                continue

            # Count parentheses to find the end
            depth = 0
            block_end = block_start
            for i, char in enumerate(instance_section[block_start:], block_start):
                if char == '(':
                    depth += 1
                elif char == ')':
                    depth -= 1
                    if depth == 0:
                        block_end = i + 1
                        break

            block = instance_section[block_start:block_end]

            # Extract properties
            ref_match = re.search(r'\(property\s+"Reference"\s+"([^"]+)"', block)
            val_match = re.search(r'\(property\s+"Value"\s+"([^"]+)"', block)
            fp_match = re.search(r'\(property\s+"Footprint"\s+"([^"]+)"', block)
            desc_match = re.search(r'\(property\s+"Description"\s+"([^"]+)"', block)
            uuid_match = re.search(r'\(uuid\s+"([^"]+)"\)', block)
            in_bom_match = re.search(r'\(in_bom\s+(yes|no)\)', block)

            reference = ref_match.group(1) if ref_match else ""
            value = val_match.group(1) if val_match else ""
            footprint = fp_match.group(1) if fp_match else ""
            description = desc_match.group(1) if desc_match else ""
            uuid = uuid_match.group(1) if uuid_match else ""
            in_bom = in_bom_match.group(1) == "yes" if in_bom_match else True

            # Skip power symbols for main component list
            if lib_id.startswith("power:"):
                self.power_symbols.append(PowerSymbol(
                    reference=reference,
                    value=value,
                    position=(x, y),
                    uuid=uuid
                ))
            elif reference and not reference.startswith("#"):
                # Extract pin UUIDs
                pins = {}
                for pin_match in re.finditer(r'\(pin\s+"(\d+)"\s*\n?\s*\(uuid\s+"([^"]+)"\)', block):
                    pins[pin_match.group(1)] = pin_match.group(2)

                self.components.append(Component(
                    reference=reference,
                    value=value,
                    lib_id=lib_id,
                    footprint=footprint,
                    description=description,
                    position=(x, y),
                    uuid=uuid,
                    pins=pins,
                    in_bom=in_bom
                ))

    def _parse_wires(self):
        """Extract all wire connections."""
        wire_pattern = re.compile(
            r'\(wire\s*\n?\s*\(pts\s*\n?\s*\(xy\s+([\d.-]+)\s+([\d.-]+)\)\s*\(xy\s+([\d.-]+)\s+([\d.-]+)\)'
            r'.*?\(uuid\s+"([^"]+)"\)',
            re.DOTALL
        )

        for match in wire_pattern.finditer(self.content):
            self.wires.append(Wire(
                start=(float(match.group(1)), float(match.group(2))),
                end=(float(match.group(3)), float(match.group(4))),
                uuid=match.group(5)
            ))

    def _parse_labels(self):
        """Extract all net labels."""
        label_pattern = re.compile(
            r'\(label\s+"([^"]+)"\s*\n?\s*\(at\s+([\d.-]+)\s+([\d.-]+)',
            re.MULTILINE
        )

        for match in label_pattern.finditer(self.content):
            # Find the uuid for this label
            label_start = match.start()
            label_section = self.content[label_start:label_start+500]
            uuid_match = re.search(r'\(uuid\s+"([^"]+)"\)', label_section)
            uuid = uuid_match.group(1) if uuid_match else ""

            self.labels.append(Label(
                name=match.group(1),
                position=(float(match.group(2)), float(match.group(3))),
                uuid=uuid
            ))

    def generate_bom(self, output_path: Optional[str] = None) -> str:
        """Generate Bill of Materials."""
        # Sort by reference designator (natural sort)
        def sort_key(c):
            match = re.match(r'([A-Za-z_]+)(\d*)', c.reference)
            if match:
                prefix = match.group(1)
                num = int(match.group(2)) if match.group(2) else 0
                return (prefix, num)
            return (c.reference, 0)

        sorted_components = sorted(
            [c for c in self.components if c.in_bom],
            key=sort_key
        )

        # Generate CSV content
        lines = ["Reference,Value,Footprint,Library,Description"]
        for c in sorted_components:
            # Escape CSV fields
            desc = c.description.replace('"', '""')
            lines.append(f'"{c.reference}","{c.value}","{c.footprint}","{c.lib_id}","{desc}"')

        content = "\n".join(lines)

        if output_path:
            with open(output_path, 'w') as f:
                f.write(content)

        return content

    def generate_netlist_summary(self, output_path: Optional[str] = None) -> str:
        """Generate a simplified netlist summary showing labeled nets and connections."""
        # Group labels by net name
        nets = defaultdict(list)
        for label in self.labels:
            nets[label.name].append(label.position)

        # Group power symbols
        power_nets = defaultdict(list)
        for ps in self.power_symbols:
            power_nets[ps.value].append(ps.position)

        lines = [
            "# Netlist Summary",
            f"# Generated from: {self.filepath.name}",
            f"# Title: {self.title}",
            f"# Date: {self.date}",
            f"# Revision: {self.revision}",
            "",
            "## Signal Nets",
            ""
        ]

        for net_name, positions in sorted(nets.items()):
            lines.append(f"{net_name}: {len(positions)} connection(s)")
            for pos in positions:
                lines.append(f"  - at ({pos[0]:.2f}, {pos[1]:.2f})")

        lines.extend(["", "## Power Nets", ""])
        for net_name, positions in sorted(power_nets.items()):
            lines.append(f"{net_name}: {len(positions)} connection(s)")

        lines.extend(["", "## Component Pin Summary", ""])
        for c in sorted(self.components, key=lambda x: x.reference):
            lines.append(f"{c.reference} ({c.value}): {len(c.pins)} pins at ({c.position[0]:.2f}, {c.position[1]:.2f})")

        content = "\n".join(lines)

        if output_path:
            with open(output_path, 'w') as f:
                f.write(content)

        return content

    def generate_design_review_report(self, output_path: Optional[str] = None) -> str:
        """Generate a report specifically checking design review items."""

        issues = []
        passed = []

        # Build component lookup
        comp_by_ref = {c.reference: c for c in self.components}

        # Issue 1: Q1 should be MOSFET (2N7002 or similar)
        q1 = comp_by_ref.get("Q1")
        if q1:
            if "MOSFET" in q1.description.upper() or "2N7002" in q1.lib_id or "2N7002" in q1.value:
                passed.append("Issue 1: Q1 is MOSFET ✓")
                passed.append(f"  - Part: {q1.value}")
                passed.append(f"  - Library: {q1.lib_id}")
            elif "BJT" in q1.description.upper() or "MMBT3904" in q1.value:
                issues.append("Issue 1: Q1 is still BJT, needs MOSFET ✗")
                issues.append(f"  - Current: {q1.value}")
            else:
                passed.append(f"Issue 1: Q1 type unclear, please verify: {q1.value}")
        else:
            issues.append("Issue 1: Q1 not found in schematic ✗")

        # Issue 2: MOSFET gate pull-down resistor (R_GATE)
        r_gate = comp_by_ref.get("R_GATE")
        if r_gate:
            passed.append("Issue 2: R_GATE (gate pull-down) exists ✓")
            passed.append(f"  - Value: {r_gate.value}")
        else:
            issues.append("Issue 2: R_GATE (gate pull-down resistor) missing ✗")

        # Issue 3: C15 - check if exists and location
        c15 = comp_by_ref.get("C15")
        if c15:
            passed.append(f"Issue 3: C15 exists at ({c15.position[0]:.1f}, {c15.position[1]:.1f})")
            passed.append(f"  - Value: {c15.value}")
            passed.append("  - Verify: Should be at LDO VBAT input or removed")
        else:
            passed.append("Issue 3: C15 removed (or relocated) ✓")

        # Issue 4: Accelerometer INT pull-up (R_ACC1 or R_ACC_PU)
        r_acc = comp_by_ref.get("R_ACC1") or comp_by_ref.get("R_ACC_PU")
        if r_acc:
            passed.append("Issue 4: Accelerometer INT pull-up exists ✓")
            passed.append(f"  - Reference: {r_acc.reference}")
            passed.append(f"  - Value: {r_acc.value}")
        else:
            issues.append("Issue 4: Accelerometer INT pull-up missing ✗")
            issues.append("  - Need R_ACC1 or R_ACC_PU (10kΩ) on INT1 line")

        # Issue 5: SW1 debouncing - just note existence
        sw1 = comp_by_ref.get("SW1")
        if sw1:
            passed.append(f"Issue 5: SW1 exists - verify debounce capacitor manually")
        else:
            issues.append("Issue 5: SW1 not found ✗")

        # Issue 6: Accelerometer power - check U4/U5 exists (LIS2DH12)
        accel = None
        for ref, comp in comp_by_ref.items():
            if "LIS2DH" in comp.lib_id or "LIS2DH" in comp.value:
                accel = comp
                break
        if accel:
            passed.append(f"Issue 6: Accelerometer found ({accel.reference}: {accel.value})")
            passed.append("  - Verify VDD and VDD_IO connections manually")
        else:
            issues.append("Issue 6: Accelerometer (LIS2DH12) not found ✗")

        # Issue 7: U3 (LDO) - check exists
        u3 = comp_by_ref.get("U3")
        if u3:
            if "AP2112" in u3.lib_id or "AP2112" in u3.value:
                passed.append("Issue 7: U3 (AP2112K LDO) exists ✓")
                passed.append(f"  - Value: {u3.value}")
                passed.append("  - Verify VIN/VOUT/EN connections manually")
            else:
                passed.append(f"Issue 7: U3 exists but unexpected type: {u3.value}")
        else:
            issues.append("Issue 7: U3 (LDO) missing ✗")

        # Issue 8: Battery connector J2
        j2 = comp_by_ref.get("J2")
        if j2:
            passed.append(f"Issue 8: J2 (battery connector) exists ✓")
            passed.append(f"  - Type: {j2.value}")
            passed.append(f"  - Position: ({j2.position[0]:.1f}, {j2.position[1]:.1f})")
        else:
            issues.append("Issue 8: J2 (battery connector) missing ✗")

        # Issue 9: D2 (Schottky) should be REMOVED
        d2 = comp_by_ref.get("D2")
        if d2:
            issues.append("Issue 9: D2 (Schottky diode) still present - REMOVE ✗")
            issues.append(f"  - Current: {d2.value}")
            issues.append("  - This allows dangerous voltage to battery!")
        else:
            passed.append("Issue 9: D2 removed ✓")

        # Issue 10: J2 placement - covered above

        # Build report
        lines = [
            "# Design Review Verification Report",
            f"# Schematic: {self.filepath.name}",
            f"# Title: {self.title}",
            f"# Date: {self.date}",
            f"# Revision: {self.revision}",
            "",
            "=" * 60,
            ""
        ]

        if issues:
            lines.append(f"## ISSUES FOUND ({len(issues)} items)")
            lines.append("")
            lines.extend(issues)
            lines.append("")

        lines.append(f"## PASSED/VERIFIED ({len(passed)} items)")
        lines.append("")
        lines.extend(passed)
        lines.append("")

        # Component summary
        lines.extend([
            "=" * 60,
            "",
            "## Full Component Summary",
            "",
            f"Total components: {len(self.components)}",
            f"Total labeled nets: {len(set(l.name for l in self.labels))}",
            f"Total power symbols: {len(self.power_symbols)}",
            f"Total wires: {len(self.wires)}",
            ""
        ])

        # Key components table
        key_refs = ["Q1", "R_GATE", "R_ACC1", "D2", "U3", "J2", "SW1", "C15"]
        lines.append("### Key Components Status")
        lines.append("")
        lines.append("| Reference | Value | Library | Status |")
        lines.append("|-----------|-------|---------|--------|")

        for ref in key_refs:
            comp = comp_by_ref.get(ref)
            if comp:
                status = "Present"
                if ref == "D2":
                    status = "⚠️ REMOVE"
                lines.append(f"| {ref} | {comp.value} | {comp.lib_id.split(':')[-1]} | {status} |")
            else:
                status = "Missing" if ref != "D2" else "✓ Removed"
                lines.append(f"| {ref} | - | - | {status} |")

        content = "\n".join(lines)

        if output_path:
            with open(output_path, 'w') as f:
                f.write(content)

        return content

    def generate_json_export(self, output_path: Optional[str] = None) -> str:
        """Export full schematic data as JSON for programmatic access."""
        data = {
            "metadata": {
                "file": str(self.filepath),
                "title": self.title,
                "date": self.date,
                "revision": self.revision
            },
            "components": [
                {
                    "reference": c.reference,
                    "value": c.value,
                    "lib_id": c.lib_id,
                    "footprint": c.footprint,
                    "description": c.description,
                    "position": {"x": c.position[0], "y": c.position[1]},
                    "pins": c.pins,
                    "in_bom": c.in_bom
                }
                for c in self.components
            ],
            "nets": {
                name: [{"x": p[0], "y": p[1]} for p in positions]
                for name, positions in self._group_labels().items()
            },
            "power_symbols": [
                {
                    "value": ps.value,
                    "position": {"x": ps.position[0], "y": ps.position[1]}
                }
                for ps in self.power_symbols
            ],
            "statistics": {
                "component_count": len(self.components),
                "wire_count": len(self.wires),
                "label_count": len(self.labels),
                "unique_nets": len(set(l.name for l in self.labels)),
                "power_symbol_count": len(self.power_symbols)
            }
        }

        content = json.dumps(data, indent=2)

        if output_path:
            with open(output_path, 'w') as f:
                f.write(content)

        return content

    def _group_labels(self):
        """Group labels by net name."""
        nets = defaultdict(list)
        for label in self.labels:
            nets[label.name].append(label.position)
        return dict(nets)


def main():
    """Main entry point."""
    if len(sys.argv) < 2:
        print("Usage: python parse_kicad_schematic.py <schematic.kicad_sch> [output_dir]")
        sys.exit(1)

    schematic_path = sys.argv[1]
    output_dir = Path(sys.argv[2]) if len(sys.argv) > 2 else Path(".")
    output_dir.mkdir(parents=True, exist_ok=True)

    # Check for KiCad CLI
    cli = find_kicad_cli()
    if cli:
        print(f"Found KiCad CLI: {cli}")
    else:
        print("KiCad CLI not found - will use Python parser only")

    print(f"\nParsing: {schematic_path}")

    parser = KiCadSchematicParser(schematic_path)
    parser.parse()

    print(f"Found {len(parser.components)} components")
    print(f"Found {len(parser.wires)} wires")
    print(f"Found {len(parser.labels)} labels")
    print(f"Found {len(parser.power_symbols)} power symbols")

    # Generate outputs
    base_name = Path(schematic_path).stem

    # Python-generated outputs (always available)
    bom_path = output_dir / f"{base_name}_bom.csv"
    parser.generate_bom(str(bom_path))
    print(f"Generated: {bom_path}")

    netlist_summary_path = output_dir / f"{base_name}_netlist_summary.txt"
    parser.generate_netlist_summary(str(netlist_summary_path))
    print(f"Generated: {netlist_summary_path}")

    review_path = output_dir / f"{base_name}_design_review.txt"
    parser.generate_design_review_report(str(review_path))
    print(f"Generated: {review_path}")

    json_path = output_dir / f"{base_name}_export.json"
    parser.generate_json_export(str(json_path))
    print(f"Generated: {json_path}")

    # KiCad CLI outputs (authoritative, if available)
    if cli:
        print("\n--- KiCad CLI Exports (Authoritative) ---")

        # Netlist (S-expression format)
        netlist_path = output_dir / f"{base_name}.net"
        if generate_netlist_with_cli(schematic_path, str(netlist_path), "kicadsexpr"):
            print(f"Generated: {netlist_path}")

        # Netlist (XML format)
        netlist_xml_path = output_dir / f"{base_name}_netlist.xml"
        if generate_netlist_with_cli(schematic_path, str(netlist_xml_path), "kicadxml"):
            print(f"Generated: {netlist_xml_path}")

        # BOM
        bom_cli_path = output_dir / f"{base_name}_bom_kicad.csv"
        if generate_bom_with_cli(schematic_path, str(bom_cli_path)):
            print(f"Generated: {bom_cli_path}")

        # ERC Report
        erc_path = output_dir / f"{base_name}_erc.rpt"
        if run_erc_with_cli(schematic_path, str(erc_path)):
            print(f"Generated: {erc_path}")

    # Print design review summary to console
    print("\n" + "=" * 60)
    print(parser.generate_design_review_report())


if __name__ == "__main__":
    main()
