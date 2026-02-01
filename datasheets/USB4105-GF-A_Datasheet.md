# USB4105-GF-A Datasheet Summary

This document summarizes the key specifications for the USB4105-GF-A, a USB Type-C receptacle.

## General Information

*   **Part Number:** USB4105-GF-A
*   **Manufacturer:** GCT (Global Connector Technology)
*   **Description:** USB Type-C Receptacle for USB 2.0, SMT Type, PCB Top Mount
*   **Durability:** 20,000 cycles

## Material

*   **Insulator:** LCP, UL 94V-0, Black
*   **Contact:** Copper Alloy
*   **Shell:** Stainless steel
*   **Mid Plate:** Stainless Steel

## Electrical Specifications

*   **Current Rating:**
    *   5.00A collectively for VBUS pins
    *   6.25A collectively for GND pins
    *   1.25A for A5/B5 (CC) pins
    *   0.25A for all other pins
*   **Voltage Rating:** 48V DC
*   **Power Rating:** 240W
*   **Contact Resistance:** 40mΩ max initial, 50mΩ max after test
*   **Dielectric Withstanding Voltage:** 100V AC
*   **Insulation Resistance:** 100MΩ min

## Mechanical & Environmental

*   **Operating Temperature:** -40°C to +85°C
*   **Mating Force:** 5 to 20 N
*   **Unmating Force:** 6 to 20 N after test

## Plating

*   **Contact Area:** Gold Flash (standard)
*   **Solder Tails:** Gold Flash
*   **Underplating:** 50µ" min Nickel
*   **Shell:** 30µ" min Nickel

## Pinout (Mating Sequence)

| Pin | Signal | Sequence |
|---|---|---|
| A1/B1/A12/B12 | GND | First |
| A4/B9/A9/B4 | VBUS | First |
| A5 | CC1 | Second |
| B5 | CC2 | Second |
| A6 | Dp1 | Second |
| A7 | Dn1 | Second |
| B7 | Dn2 | Second |
| B6 | Dp2 | Second |
| A8 | SBU1 | Second |
| B8 | SBU2 | Second |
| SHELL | GND | - |
