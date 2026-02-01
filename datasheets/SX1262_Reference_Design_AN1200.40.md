# AN1200.40: SX1261/2 Reference Design Explanation Summary

This document provides a summary of the Semtech Application Note AN1200.40, which details the reference designs for the SX1261 and SX1262 transceivers.

## Reference Design Versions

The application note covers three main reference designs:

| PCB # | Part | Layers | Reference | Regions | Frequency Band (MHz) | Key Feature |
|---|---|---|---|---|---|---|
| **PCB_E406V03A** | SX1261 | 2 | XTAL | Europe, Asia, S. Korea | 863-923 | Low-power (+14 dBm), low-cost 2-layer design. |
| **PCB_E428V03A** | SX1262 | 4 | XTAL | USA, Canada, Australia | 902-928 | High-power (+22 dBm), 4-layer design for better thermal performance. |
| **PCB_E449V01A** | SX1262 | 4 | TCXO | Australia, India | 865-867 / 915-928 | High-power (+22 dBm) with TCXO for regions with long packet durations. |

## Key Design Differences

### 1. Layer Stackup: 2-Layer vs. 4-Layer
*   **2-Layer (E406V03A):** Low-cost FR-4. Top layer for all components and RF, bottom layer for ground and control. Sufficient for lower power (+14 dBm).
*   **4-Layer (E428V03A, E449V01A):** Required for higher power (+22 dBm) due to better thermal dissipation and RF performance.
    *   **Layer 1:** Components and critical RF routing.
    *   **Layer 2:** Solid ground plane for RF circuits.
    *   **Layer 3:** Control routing.
    *   **Layer 4:** Solid ground.

### 2. Frequency Reference: XTAL vs. TCXO
*   **XTAL (Crystal):** Used in E406V03A and E428V03A. A low-cost option suitable for packet durations less than 400ms. Requires careful thermal isolation (copper void on all layers) to prevent frequency drift, especially on 2-layer boards.
*   **TCXO (Temperature-Compensated Crystal Oscillator):** Used in E449V01A. Required for high-power applications with long packet durations (>400ms, up to 2.8s) where temperature stability is critical. Does not require thermal isolation cutouts.

### 3. Power Amplifier (PA) Configuration
*   The SX1261/2 can use an internal LDO or a more efficient DC-DC converter to power the PA regulator (VR_PA).
*   **E406V03A (SX1261):** VR_PA is powered from the internal VREG.
*   **E428V03A/E449V01A (SX1262):** VDD_IN (source for VR_PA) is powered directly from the main supply (VBAT) for higher power output. The DC-DC converter is used for the chip core only.

## Transmitter RF Path Design

The transmitter design involves three main stages:
1.  **Impedance Matching:** Matches the PA output (RFO pin) to an optimal impedance (Zopt) to maximize power transfer. Primarily uses a shunt capacitor (C5) and series inductor (L3).
2.  **2nd Harmonic Filter:** A parallel LC notch filter (L3, C4) designed to suppress the 2nd harmonic of the carrier frequency.
3.  **Higher-Order Harmonic Filter:** A 50-ohm Pi filter (C5, L4, C7) to attenuate higher-order harmonics.

An external RF switch (like Peregrine PE4259) is used to share the antenna between the transmit and receive paths.

## Receiver RF Path Design

*   The receiver uses a differential LNA for better common-mode rejection.
*   An LC network (C11, C12, L6) acts as a balun to convert the single-ended antenna signal to differential for the LNA inputs.
*   This network also performs impedance matching, transforming the 50Ω antenna impedance to the optimal source impedance for the LNA to achieve the lowest noise figure. For the SX1261 at 915 MHz, the optimal differential source impedance is noted as **74 + j134 Ω**.
