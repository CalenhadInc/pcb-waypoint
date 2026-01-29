# Waypoint Enclosure Layout

## Device Overview

**Product:** Waypoint - Festival LoRa Mesh Communicator
**Use Case:** MagSafe-attached device for Meshtastic/MeshCore mesh networking
**Target:** 7-day festival use, ~30 day battery life

---

## Enclosure Dimensions

| Dimension | Size |
|-----------|------|
| Total enclosure | 64.2mm x 97.2mm |
| Thickness | ~16mm (estimated) |
| PCB | 46mm x 42mm |
| Battery | ~50mm x 34mm x 8mm |
| Weight | TBD |

---

## Layout Overview

Device attaches to TOP of iPhone back via MagSafe.

```
                       64.2mm
    ←────────────────────────────────────────→

    ┌────────────────────────────────────────┐  ─┬─
    │         ○○○○○○○○○○○○○○○○               │   │
    │       ○                 ○    ░░░░░░░░░░│   │
    │      ○    MAGSAFE        ○   ░░░░░░░░░░│   │
    │     ○      RING           ○  ░ANTENNA░░│   │
    │      ○    (top of         ○  ░░░░░░░░░░│   │
    │       ○    device)       ○   ░░░░░░░░░░│   │
    │         ○○○○○○○○○○○○○○○○     ░░LoRa░░░░│   │
    │  ┌────────────────────────┐  ░░915MHz░░│   │  97.2mm
    │  │ ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ │  ░░░░░░░░░░│   │
    │  │ ▓▓▓▓ BATTERY ▓▓▓▓▓▓▓▓ │  ░░░░░░░░░░│   │
    │  │ ▓▓▓▓ 2000mAh ▓▓▓▓▓▓▓▓ │  ░░░░░░░░░░│   │
    │  │ ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ │  ░░░░░░░░░░│   │
    │  └────────────────────────┘  ░░░░░░░░░░│   │
    │  ┌────────────────────────┐             │   │
    │○ │                        │             │   │
    │○ │         PCB            │             │   │
    │  │       46 x 42mm        │             │   │
    │  │                        │             │   │
    │  └────────────────────────┘             │   │
    │  [NFC]              [USB-C]             │   │
    └────────────────────────────────────────┘  ─┴─

     LEFT                               BOTTOM
    (Buttons)                    (USB-C + NFC)
```

---

## Zone Breakdown

### TOP HALF (MagSafe + Battery + Antenna)

| Zone | Contents | Size |
|------|----------|------|
| MagSafe ring | Magnetic alignment ring | ~56mm diameter |
| Battery area | 2000mAh LiPo | 50mm x 34mm x 8mm |
| Antenna strip | LoRa 915MHz wire/flex | 8-10mm x ~80mm |

### BOTTOM HALF (PCB + Ports)

| Zone | Contents | Size |
|------|----------|------|
| PCB | Main electronics | 46mm x 42mm |
| USB-C | Charging port | 12mm x 5mm cutout |
| NFC | Friend tap zone | 25mm diameter tag |
| Buttons | User + Reset | 2x 4mm holes |

---

## Component Placement

| Component | Location | Position (from bottom-left) |
|-----------|----------|----------------------------|
| MagSafe ring | Top center, back | (32mm, 80mm) center |
| Battery | Top half, under MagSafe | (8mm, 50mm) to (58mm, 85mm) |
| Antenna | Right side strip | (56mm, 10mm) to (64mm, 90mm) |
| PCB | Bottom half | (8mm, 8mm) to (54mm, 50mm) |
| USB-C | Bottom edge, center-left | (20mm, 0mm) |
| NFC | Bottom-right corner, back | (50mm, 5mm) |
| Buttons | Left side | (0mm, 25mm) and (0mm, 35mm) |
| LEDs | Front face | (25mm, 20mm) |

---

## Cross-Section Views

### Side View (Left Side)

```
    TOP                                    BOTTOM
     │                                        │
     ▼                                        ▼
    ┌──────────────────────────────────────────┐
    │░░░░░░░░░░░░ CASE TOP ░░░░░░░░░░░░░░░░░░░│ 1mm
    ├──────────────────────────────────────────┤
    │   MagSafe   │        PCB components      │ 2mm
    ├─────────────┤════════════════════════════│ 1.6mm
    │             │                            │
    │   Battery   │           PCB              │ 8mm
    │             │                            │
    ├─────────────┴────────────────────────────┤
    │░░░░░░░░░░░░░ CASE BACK ░░░░░░░░░░░░░░░░░│ 1mm
    └──────────────────────────────────────────┘

    Total thickness: ~14-16mm
```

### Top View (Component Layers)

```
    Layer 1 (Top):     Case shell + button holes
    Layer 2:           PCB (bottom half) + Battery (top half)
    Layer 3:           MagSafe ring + Antenna channel
    Layer 4 (Bottom):  Case back + NFC window
```

---

## Phone Attachment

```
    PHONE BACK (with Waypoint attached)

    ┌─────────────────────────────────┐
    │                                 │
    │   ┌─────────────────────────┐   │
    │   │      WAYPOINT           │   │ ← Device here
    │   │                         │   │
    │   │   MagSafe aligns with   │   │
    │   │   phone's MagSafe       │   │
    │   │                         │   │
    │   └─────────────────────────┘   │
    │         ↑                       │
    │     Alignment point             │
    │         ○                       │
    │        ○ ○                      │
    │       ○   ○   (phone's          │
    │        ○ ○     MagSafe ring)    │
    │         ○                       │
    │                                 │
    │   [Camera]                      │
    │                                 │
    └─────────────────────────────────┘
```

---

## Antenna Design

### LoRa 915MHz Antenna

| Spec | Value |
|------|-------|
| Type | Wire or flex PCB |
| Frequency | 915 MHz |
| Length | ~82mm (λ/4) |
| Width zone | 8-10mm |
| Location | Right side of enclosure |
| Feed point | U.FL on PCB right edge |

```
    Antenna runs full height of device:

    ┌─────────┐
    │         │ TOP
    │  ░░░░░░ │
    │  ░    ░ │
    │  ░ A  ░ │
    │  ░ N  ░ │
    │  ░ T  ░ │  ~80mm length
    │  ░ E  ░ │
    │  ░ N  ░ │
    │  ░ N  ░ │
    │  ░ A  ░ │
    │  ░    ░ │
    │  ░●───░─│── Feed from U.FL
    │  ░░░░░░ │
    └─────────┘ BOTTOM
```

### BLE 2.4GHz Antenna

| Spec | Value |
|------|-------|
| Type | PCB trace (on main PCB) |
| Frequency | 2.4 GHz |
| Size | ~15mm x 5mm |
| Location | Bottom-left corner of PCB |

---

## NFC Placement

**Goal:** Friends can tap, owner doesn't accidentally trigger.

| Spec | Value |
|------|-------|
| Location | Bottom-right corner, back side |
| Tag size | ~25mm diameter or 30x15mm |
| Case window | Thin plastic (~0.5mm) for RF |
| Distance from USB-C | ~25mm (no interference) |

```
    Back view (NFC location):

    ┌────────────────────────────────┐
    │                                │
    │      ○○○○○○○○○                 │
    │     ○ MAGSAFE ○                │
    │     ○   RING  ○                │
    │      ○○○○○○○○○                 │
    │                                │
    │                                │
    │                                │
    │                         ┌────┐ │
    │                         │NFC │ │ ← Bottom-right corner
    │                         └────┘ │
    └────────────────────────────────┘
```

When owner holds device, their hand covers middle - NFC is in corner, away from grip.

---

## Button Placement

Buttons on LEFT side, matching iPhone button positions.

| Button | Function | Position (from bottom) |
|--------|----------|------------------------|
| SW1 | User button | ~35mm |
| SW2 | Reset button | ~25mm |

```
    Left side view:

    ┌──────────────┐ TOP
    │   MagSafe    │
    │              │
    │   Battery    │
    │              │
    ├──────────────┤
    │              │
    ○  SW1 (User)  │ ← ~35mm from bottom
    ○  SW2 (Reset) │ ← ~25mm from bottom
    │              │
    │     PCB      │
    │              │
    └──────────────┘ BOTTOM
```

---

## USB-C Port

| Spec | Value |
|------|-------|
| Location | Bottom edge, center-left |
| Cutout size | 12mm x 5mm |
| Position | ~20mm from left edge |
| Orientation | Port faces down (away from phone) |

```
    Bottom edge:

    ←────────────── 64.2mm ───────────────→

    ┌────────────────────────────────────────┐
    │                PCB                     │
    ├────┬─────────────────────────────┬─────┤
    │    │         ════════            │     │
    │    │          USB-C              │ NFC │
    └────┴─────────────────────────────┴─────┘

       ~20mm        center            corner
```

---

## Case Cutouts Summary

| Feature | Location | Size | Notes |
|---------|----------|------|-------|
| USB-C port | Bottom, center-left | 12mm x 5mm | Rounded corners |
| Button 1 (SW1) | Left side, upper | 4mm diameter | Tactile click |
| Button 2 (SW2) | Left side, lower | 4mm diameter | Tactile click |
| LED window | Front, lower area | 6mm x 3mm | Translucent plastic |
| NFC window | Back, bottom-right | 30mm x 20mm | Thin plastic |
| Antenna channel | Right side, internal | 10mm x 80mm | No metal nearby |

---

## Manufacturing Notes

### 3D Printed Case

| Spec | Value |
|------|-------|
| Material | PLA or PETG |
| Wall thickness | 1.5-2mm |
| Infill | 20-30% |
| Layer height | 0.2mm |
| Color | TBD (red in prototype) |

### Assembly Order

1. Install MagSafe ring in top of case back
2. Place battery in top half
3. Route antenna wire through right channel
4. Connect battery to PCB
5. Place PCB in bottom half
6. Connect U.FL to antenna
7. Attach NFC tag to case back
8. Close case, secure with screws or clips

---

## Compatibility

### iPhone Models (MagSafe)

| Model | Compatible |
|-------|------------|
| iPhone 12/13/14/15 | Yes (MagSafe) |
| iPhone 12/13/14/15 Mini | Yes (may overhang slightly) |
| iPhone 12/13/14/15 Pro | Yes |
| iPhone 12/13/14/15 Pro Max | Yes |
| Older iPhones | With MagSafe case |
| Android | With MagSafe adapter |

### MagSafe Alignment

Device designed to sit at TOP of phone back:
- MagSafe ring at top of device
- Aligns with phone's MagSafe ring (centered on phone)
- Does not cover camera
- USB-C accessible at bottom
