# SX1261 / SX1262 Datasheet Summary

This document summarizes the key specifications for the Semtech SX1261 and SX1262 sub-GHz LoRa transceivers.

## Key Differentiators

| Feature | SX1261 | SX1262 |
|---|---|---|
| **Max RF Output Power** | +15 dBm | **+22 dBm** |
| **PA Supply** | Internal LDO or DC-DC | **Direct from VBAT** |
| **Typical TX Current** | 25.5 mA @ +14 dBm | 118 mA @ +22 dBm |

## General Features

*   **Modulation:** LoRa® and (G)FSK
*   **Frequency Range:** 150 - 960 MHz
*   **Package:** QFN 4x4 24-lead
*   **Low Power:**
    *   RX current: ~4.6 mA (LoRa, 125kHz)
    *   Sleep current (warm start): 600 nA
*   **SPI Interface:** Up to 16 MHz
*   **Voltage Range:** 1.8 V to 3.7 V

## Key Electrical Specifications

### LoRa® Modem

| Parameter | Value |
|---|---|
| **Spreading Factor (SF)** | 5 to 12 |
| **Bandwidth (BW)** | 7.8 kHz to 500 kHz |
| **Bit Rate** | 0.018 kbps to 62.5 kbps |
| **Receiver Sensitivity (Boosted)** | Down to -148 dBm (SF12, 10.4 kHz BW) |
| **Co-channel Rejection** | Up to 19 dB |

### FSK Modem

| Parameter | Value |
|---|---|
| **Bit Rate** | 0.6 kbps to 300 kbps |
| **Frequency Deviation** | 0.6 kHz to 200 kHz |
| **Receiver Sensitivity** | Down to -125 dBm (0.6kbps, 4kHz BW) |

## Power Amplifier Summary

| Parameter | SX1261 | SX1262 |
|---|---|---|
| **Max Power** | +14/15 dBm | +22 dBm |
| **IDDTX (indicative)** | 25.5 mA (@ +14 dBm) | 118 mA (@ +22 dBm) |
| **Output Power vs VBAT** | Flat from 1.8V to 3.7V | Dependent on VBAT. Requires >3.1V for +22dBm. |
| **Regulator for PA** | DC-DC buck or LDO | Direct from VBAT |

## Power Consumption

| Mode | Condition | Typical Current |
|---|---|---|
| **Sleep** | Cold Start | 160 nA |
| **Sleep** | Warm Start, Config Retained | 600 nA |
| **Standby RC** | RC13M, XOSC OFF | 0.6 mA |
| **Receive** | DC-DC, LoRa 125kHz | 4.6 mA |
| **Receive (Boosted)**| DC-DC, LoRa 125kHz | 5.3 mA |
| **Transmit (SX1262)** | +22 dBm, 868/915 MHz | 118 mA |
| **Transmit (SX1261)** | +14 dBm, 868/915 MHz | 25.5 mA |

## Pin Functions

| Pin | Name | Function |
|---|---|---|
| 1 | VDD_IN | Input voltage for PA regulator. |
| 3 | XTA | Crystal oscillator connection / TCXO input. |
| 6 | DIO3 | Can be used to power a TCXO. |
| 10 | VBAT | Main supply for the RFIC. |
| 12 | DIO2 | Can be used as RF Switch control (High for TX). |
| 13 | DIO1 | Generic IRQ line. |
| 14 | BUSY | Indicates chip is busy. |
| 15 | NRESET | Active-low reset. |
| 16-19 | MISO, MOSI, SCK, NSS | SPI Interface. |
| 21, 22 | RFI_P, RFI_N | Differential RF receiver inputs. |
| 23 | RFO | RF transmitter output. |

## Application Notes
*   A TCXO is recommended for designs with poor heat dissipation or where `LowDataRateOptimize` is not used.
*   DIO2 can be configured to automatically control an external RF switch.
*   DIO3 can be configured to provide a regulated, timed voltage supply for an external TCXO.
*   The chip contains an internal 256-byte data buffer for RX and TX payloads.
*   The device supports multiple operational modes including Sleep, Standby, Frequency Synthesis (FS), RX, and TX.
