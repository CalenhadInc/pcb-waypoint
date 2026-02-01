# MCP73831 / MCP73832 Datasheet Summary

This document summarizes the key specifications for the Microchip MCP73831 and MCP73832, which are miniature, fully integrated Li-Ion/Li-Polymer charge management controllers.

## Key Features

*   **Controller Type:** Linear Charge Management
*   **Charge Algorithm:** Constant-Current / Constant-Voltage
*   **Programmable Charge Current:** 15 mA to 500 mA (set by a single external resistor)
*   **Preset Voltage Regulation:** High-accuracy (±0.75%)
*   **Voltage Options:** 4.20V, 4.35V, 4.40V, 4.50V
*   **Packages:**
    *   5-Lead SOT-23
    *   8-Lead 2x3 mm DFN
*   **Status Output:**
    *   **MCP73831:** Tri-state logic (High, Low, High-Z)
    *   **MCP73832:** Open-drain (Low, High-Z)
*   **Safety Features:**
    *   Thermal Regulation
    *   Reverse Discharge Protection
    *   Undervoltage Lockout (UVLO)

## Functional Stages

1.  **Preconditioning (Trickle Charge):** If the battery voltage is below a set threshold (`VPTH`), the charger supplies a selectable percentage (10%, 20%, 40%) of the full charge current. Can be disabled.
2.  **Fast Charge (Constant Current):** The charger supplies a constant current set by the `RPROG` resistor. The current is calculated as `IREG = 1000V / RPROG`.
3.  **Constant Voltage:** When the battery reaches the regulation voltage (`VREG`), the charger maintains a constant voltage, and the charge current begins to taper off.
4.  **Charge Termination:** The charge cycle ends when the current falls to a selectable percentage (5%, 7.5%, 10%, 20%) of the fast charge current.
5.  **Automatic Recharge:** If the battery voltage falls below the recharge threshold (`VRTH`, typically ~94% of `VREG`), a new charge cycle begins.

## Electrical Characteristics

| Parameter | Symbol | Value | Unit |
|---|---|---|---|
| **Input Supply Voltage** | VDD | 3.75 to 6.0 | V |
| **Regulated Output Voltage** | VREG | 4.20 (±0.75%) | V |
| **Fast Charge Current** | IREG | 15 to 500 | mA |
| **Supply Current (Charging)** | ISS | 510 (typ) | µA |
| **Supply Current (Shutdown)**| - | < 2 | µA |
| **Pass Transistor On-Resistance** | RDSON | 350 (typ) | mΩ |

## Pin Descriptions (SOT-23)

| Pin | Symbol | Function |
|---|---|---|
| 1 | STAT | Charge Status Output |
| 2 | VSS | 0V Reference (Ground) |
| 3 | VBAT | Battery Charge Control Output (to battery positive) |
| 4 | VDD | Input Supply |
| 5 | PROG | Current Regulation Set (connect resistor to VSS) |

## Applications

*   Lithium-Ion/Lithium-Polymer Battery Chargers
*   Portable devices (PDAs, cell phones, MP3 players)
*   USB-based chargers
*   Bluetooth headsets
