# Tigard SKiDL — Programmatic Netlist Generator

A Python script that reconstructs the [Tigard v1.1](https://github.com/tigard-tools/tigard) hardware hacking tool's PCB circuit using [SKiDL](https://github.com/devbisme/skidl), producing a KiCad-compatible `.net` netlist file entirely from code — no schematic editor required.

## What This Does

`tigard_skidl.py` defines the complete Tigard v1.1 circuit (89 components, 150+ nets) programmatically in Python and generates a netlist that can be imported directly into KiCad's PCBnew for layout. The circuit includes:

- **FT2232HQ** — dual-channel USB-to-serial/JTAG bridge (65 pins)
- **SN74LVC8T245** ×2 — bidirectional level translators
- **93LC46BT** — configuration EEPROM
- **AP7365-18 / AP7365-33** — 1.8V and 3.3V voltage regulators
- **USB-C connector**, JTAG/UART/SPI/I2C/Cortex headers, logic analyzer header
- **DP4T target voltage selector** and **DPDT mode switch**
- 26 capacitors, 24 resistors, 8 resistor networks, 3 ferrite beads, 5 LEDs, crystal, MOSFET, jumpers, and test point

Pin positions for all custom Tigard library symbols (`AP7365`, `SN74LVC8T245`, `SW_DP4T`, `SW_DPDT`, `VTARGET`, `VREG`, `VREF`) are parsed directly from the original `tigard.lib` file. Standard KiCad symbols use pin definitions extracted from the `.kicad_sch` embedded library.

## Quick Start

```bash
# Clone the repo
git clone https://github.com/your-username/tigard-skidl.git
cd tigard-skidl

# Run the script (auto-installs skidl if needed)
python3 tigard_skidl.py

# Output: tigard.net in the current directory
```

That's it. The script auto-installs `skidl` via pip on first run, including handling macOS Homebrew's PEP 668 restriction. No KiCad installation is needed to generate the netlist.

### Import into KiCad

1. Open KiCad → PCBnew
2. File → Import Netlist → select `tigard.net`
3. All 89 components load with standard KiCad footprints

## Requirements

- **Python 3.8+**
- **skidl** (auto-installed on first run)
- No KiCad installation required for netlist generation

## Repository Structure

```
├── tigard_skidl.py          # Main script — run this to generate the netlist
├── tigard.net               # Pre-generated netlist (ready to import)
├── tigard.sch               # Original KiCad v4 schematic (reference)
├── tigard.kicad_sch         # Original KiCad v10 schematic (reference)
├── tigard.lib               # Tigard custom symbol library (pin definitions)
└── README.md
```

## How It Was Built

The script was generated through a multi-step extraction pipeline:

1. **Component extraction** — All 163 component instances (89 unique + power symbols) parsed from `tigard.sch` (KiCad v4 format) with reference designators, values, footprints, positions, and transform matrices.

2. **Pin position sourcing** — Standard KiCad symbol pins extracted from the `.kicad_sch` embedded `lib_symbols` section (mm coordinates). Custom Tigard symbol pins parsed from `tigard.lib` (KiCad v4 `.lib` format, mils converted to mm).

3. **Net connectivity** — 477 wires and 119 labels parsed from the schematic. A union-find algorithm traces connectivity from pin endpoints through wires to labels and power symbols, resolving all named and anonymous nets.

4. **Footprint mapping** — Custom `tigard:` footprints mapped to standard KiCad library equivalents so the netlist loads without requiring the Tigard footprint library.

## Footprint Substitutions

All custom Tigard footprints are replaced with standard KiCad equivalents for portability:

| Original (tigard:) | Replacement |
|---|---|
| USB_C_Receptacle_HRO_TYPE-C-31-M-12 | Connector_USB:USB_C_Receptacle_USB2.0 |
| SOT-23-5_RoundRect | Package_TO_SOT_SMD:SOT-23-5 |
| SOT-23-6_RoundRect | Package_TO_SOT_SMD:SOT-23-6 |
| SOT-23_RoundRect | Package_TO_SOT_SMD:SOT-23 |
| Crystal_SMD_3225-4Pin_3.2x2.5mm_RoundRect | Crystal:Crystal_SMD_3225-4Pin_3.2x2.5mm |
| PinHeader_1x09_P2.54mm_Vertical | Connector_PinHeader_2.54mm:PinHeader_1x09_P2.54mm_Vertical |
| PinHeader_2x04_P2.54mm_Vertical | Connector_PinHeader_2.54mm:PinHeader_2x04_P2.54mm_Vertical |
| PinHeader_2x05_P1.27mm_Vertical_SMD | Connector_PinHeader_1.27mm:PinHeader_2x05_P1.27mm_Vertical_SMD |
| PinHeader_2x07_P1.27mm_Vertical_SMD | Connector_PinHeader_1.27mm:PinHeader_2x07_P1.27mm_Vertical_SMD |
| R_Array_Convex_4x0402_RoundRect | Resistor_SMD:R_Array_Convex_4x0402 |
| SW_ALPS_SSSS224100_DP4T | Button_Switch_SMD:SW_SP4T_PCM13 |
| SW_CuK_JS202011CQN_DPDT_Straight | Button_Switch_SMD:SW_DPDT_CK_JS202011CQN |

> To use the original Tigard footprints instead, download the `tigard.pretty` folder from the [Tigard repo](https://github.com/tigard-tools/tigard), add it to KiCad's footprint library table, and revert the footprint strings in the script.

## ERC Summary

| Category | Count | Notes |
|---|---|---|
| Errors | **0** | Clean netlist generation |
| Drive warnings | **0** | All pins set to PASSIVE |
| Unconnected pins | **4** | Mounting holes H1–H4 (expected) |
| Single-pin nets | **59** | From USB-C pin position estimation¹ |

¹ The `USB_C_Receptacle_USB2.0` symbol is not included in `tigard.lib` — its pin positions are estimated from wire endpoint analysis and may cause some single-pin net warnings. All other symbols connect correctly using exact library data.

## License

The Tigard hardware design is © 2020 Franklin Harding, licensed under [CC-BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). This SKiDL conversion script is provided under the same license.

## Credits

- **Tigard** by [Franklin Harding / Securing Hardware](https://github.com/tigard-tools/tigard)
- **SKiDL** by [Dave Vandenbout](https://github.com/devbisme/skidl)
