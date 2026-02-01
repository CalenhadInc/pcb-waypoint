# AO3400 N-Channel MOSFET Datasheet Summary

This document summarizes the key specifications for the Alpha & Omega Semiconductor AO3400, an N-Channel Trench MOSFET.

## General Information

*   **Part Number:** AO3400
*   **Manufacturer:** Alpha & Omega Semiconductor (AOS)
*   **Type:** N-Channel MOSFET
*   **Package:** SOT-23
*   **Description:** Advanced trench MOSFET suitable for load switch or PWM applications.

## Absolute Maximum Ratings (at Tₐ = 25°C)

| Parameter | Symbol | Value | Unit |
|---|---|---|---|
| Drain-Source Voltage | VDS | 30 | V |
| Gate-Source Voltage | VGS | ±12 | V |
| **Continuous Drain Current (ID)** | | | |
| @ TA = 25°C | ID | 5.8 | A |
| @ TA = 70°C | ID | 4.9 | A |
| Pulsed Drain Current | IDM | 30 | A |
| **Power Dissipation (PD)** | | | |
| @ TA = 25°C | PD | 1.4 | W |
| @ TA = 70°C | PD | 0.9 | W |
| Junction and Storage Temperature | TJ, TSTG | -55 to 150 | °C |

## Key Electrical Characteristics (at Tₐ = 25°C)

| Parameter | Symbol | Condition | Typ | Max | Unit |
|---|---|---|---|---|---|
| **Static Drain-Source On-Resistance** | **RDS(ON)** | | | | |
| | | VGS = 10V, ID = 5.8A | 18 | **28** | mΩ |
| | | VGS = 4.5V, ID = 5A | 19 | **33** | mΩ |
| | | VGS = 2.5V, ID = 4A | 24 | **52** | mΩ |
| **Gate Threshold Voltage** | VGS(th) | VDS = VGS, ID = 250µA | 0.85 | 1.45 | V |
| **Diode Forward Voltage** | VSD | IS = 1A, VGS = 0V | 0.7 | 1 | V |
| Total Gate Charge | Qg | VGS = 4.5V, VDS = 15V, ID = 5.8A | 6 | 7 | nC |

## Thermal Characteristics

| Parameter | Symbol | Typ | Max | Unit |
|---|---|---|---|---|
| Max Junction-to-Ambient (t ≤ 10s) | RthJA | 70 | 90 | °C/W |
| Max Junction-to-Ambient (Steady-State) | RthJA | 100 | 125 | °C/W |
| Max Junction-to-Lead (Steady-State) | RthJL | 63 | 80 | °C/W |

This device is a "Green Product".
