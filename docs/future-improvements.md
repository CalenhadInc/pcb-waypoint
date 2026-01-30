# Future Improvements - Waypoint

Simple enhancements for future revisions.

---

## Cost Optimizations

### DRV2605 → DRV2603 ($0.60 savings)
- **Trade-off**: Lose 123 built-in effects, need firmware PWM
- **When**: High volume (100k+) or simple vibration only
- **Verdict**: Keep DRV2605 for now - effects library worth $0.60

---

## Potential Additions

### NFC Tag
- **Part**: NTAG216
- **Purpose**: Tap-to-pair, friend exchange
- **Interface**: I2C or passive
- **Cost**: ~$0.40

### Fuel Gauge
- **Part**: MAX17048
- **Purpose**: Accurate battery % (vs voltage guessing)
- **Interface**: I2C
- **Cost**: ~$1.20

### Barometric Pressure
- **Part**: BMP390
- **Purpose**: Altitude, weather
- **Interface**: I2C (shared bus)
- **Cost**: ~$1.50

---

## Software Improvements (No HW Change)

Works on current v2 hardware:

- OTA firmware updates via BLE
- Mesh networking (Meshtastic/MeshCore)
- Haptic patterns using DRV2605 effects
- Motion gestures (shake to send)
- Encrypted messaging (AES-128)

---

*Last updated: 2026-01-30*
