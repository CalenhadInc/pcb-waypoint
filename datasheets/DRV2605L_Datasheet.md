# DRV2605L Haptic Driver Datasheet Summary

This document summarizes the key specifications for the Texas Instruments DRV2605L, a haptic driver for both Linear Resonance Actuators (LRA) and Eccentric Rotating Mass (ERM) motors.

## Key Features

*   **Actuator Support:** Flexible driver for both LRA and ERM actuators.
*   **Control Interface:** I²C and PWM input.
*   **Playback Engine:**
    *   **ROM Library:** Integrated Immersion TouchSense® 2200 with over 100 licensed haptic effects.
        *   6 ERM libraries, 1 LRA library.
    *   **Real-Time Playback (RTP):** Allows direct waveform control from a host processor via I²C.
    *   **Audio-to-Vibe:** Converts an audio input signal into haptic feedback.
*   **Smart-Loop Architecture:**
    *   **Closed-Loop Control:** Provides consistent and reliable actuator performance.
    *   **Automatic Overdrive and Braking:** Reduces start-up and brake time.
    *   **Auto-Resonance for LRA:** Automatically tracks and drives the LRA at its resonant frequency.
    *   **Automatic Level Calibration:** Compensates for variations in actuator BEMF and internal resistance.
*   **Voltage Range:** 2.0 V to 5.2 V.
*   **Output Drive:** Efficient differential switching output.
*   **Packages:** 9-pin DSBGA (1.5mm x 1.5mm), 10-pin VSSOP.

## Functional Overview

The DRV2605L simplifies haptic system design by integrating a powerful playback engine and a closed-loop control system.

*   **For ERMs:** It provides automatic overdrive and braking, which overcomes motor inertia for crisp start/stop performance. This is achieved without complex waveform design by the host.
*   **For LRAs:** Its auto-resonance engine tracks the LRA's resonant frequency in real-time, which is critical as the frequency can shift due to temperature, age, and mechanical mounting. This ensures optimal power delivery and vibration strength.

The device can be controlled in several modes:
*   **Internal Trigger:** Playback of ROM waveforms initiated by an I²C command (setting the `GO` bit).
*   **External Trigger:** Playback initiated by a hardware trigger on the `IN/TRIG` pin.
*   **PWM Input:** Actuator strength is controlled by the duty cycle of a PWM signal.
*   **Analog Input:** Actuator strength is controlled by an analog voltage.
*   **RTP:** Continuous waveform streaming over I²C.

## Key Electrical Specifications

| Parameter | Value | Unit |
|---|---|---|
| **Supply Voltage (VDD)** | 2 to 5.2 | V |
| **Shutdown Current (EN=0)** | 4 (typ), 7 (max) | µA |
| **Quiescent Current (Standby)** | 0.5 (typ) | mA |
| **I²C Slave Address** | 0x5A | (7-bit) |
| **PWM Input Frequency** | 10 to 250 | kHz |
| **LRA Frequency Range** | 125 to 300 | Hz |

## Pin Functions (DSBGA)

| Pin | Name | Function |
|---|---|---|
| A1 | EN | Device Enable |
| A2 | REG | 1.8V Regulator Output |
| A3, C3 | OUT+, OUT- | Differential motor drive output |
| B1 | IN/TRIG | Multi-mode input (PWM, Analog, Trigger) |
| B2, C1 | SDA, SCL | I²C Data and Clock |
| B3 | GND | Supply Ground |
| C2 | VDD | Power Supply Input |
