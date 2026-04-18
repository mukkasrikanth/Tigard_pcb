#!/usr/bin/env python3
"""
Tigard PCB Design — SKiDL Script
=================================
Recreates the full Tigard v1.1 schematic (tigard.sch) using the SKiDL library.
Generates a KiCad-compatible .net netlist file on the Desktop.

Tigard is a multi-protocol hardware debug tool built around the FTDI FT2232H,
supporting JTAG, SWD, SPI, I2C, and UART interfaces with configurable target
voltage levels (1.8V / 3.3V / 5V).

Sections:
  1. Power Supply (USB input, LDO regulators, decoupling)
  2. FT2232H USB-to-Serial/JTAG bridge
  3. EEPROM (93LC46B)
  4. Level-Translation Buffers (SN74LVC8T245)
  5. Mode Switch & Signal Routing
  6. Indicator LEDs & MOSFET driver
  7. Connectors (USB-C, JTAG, UART, SPI, CORTEX, I2C/Qwiic, LA)
  8. Mechanical (Mounting Holes, Logos, Test Point)

Copyright 2020 Franklin Harding — Licensed under CC-BY-SA 4.0
SKiDL translation 2026
"""

import os
from skidl import Part, Pin, Net, ERC, generate_netlist, SKIDL

# ──────────────────────────────────────────────────────────────────────────────
# Helper: Create parts with explicit pin definitions (no KiCad libs needed)
# ──────────────────────────────────────────────────────────────────────────────

def _part(part_name, ref, value, footprint, pins, ref_prefix="U"):
    """Create a Part with inline pin definitions using tool=SKIDL."""
    return Part(
        name=part_name,
        ref=ref,
        value=value,
        footprint=footprint,
        tool=SKIDL,
        ref_prefix=ref_prefix,
        pins=pins,
    )

def _2pin(part_name, ref, value, fp, ref_prefix="R"):
    """Create a generic 2-pin passive component."""
    return _part(part_name, ref, value, fp,
                 [Pin(num="1", name="1", func=Pin.types.PASSIVE),
                  Pin(num="2", name="2", func=Pin.types.PASSIVE)],
                 ref_prefix=ref_prefix)

def _cap(ref, value, fp="Capacitor_SMD:C_0402_1005Metric"):
    return _2pin("C_Small", ref, value, fp, ref_prefix="C")

def _res(ref, value, fp="Resistor_SMD:R_0402_1005Metric"):
    return _2pin("R_Small", ref, value, fp, ref_prefix="R")

def _res_std(ref, value, fp="Resistor_SMD:R_0402_1005Metric"):
    return _2pin("R", ref, value, fp, ref_prefix="R")

def _ferrite(ref, value="600R, 0.5A", fp="Inductor_SMD:L_0402_1005Metric"):
    return _2pin("Ferrite_Bead_Small", ref, value, fp, ref_prefix="FB")

def _led(ref, value, fp="LED_SMD:LED_0603_1608Metric"):
    return _part("LED", ref, value, fp,
                 [Pin(num="1", name="K", func=Pin.types.PASSIVE),
                  Pin(num="2", name="A", func=Pin.types.PASSIVE)],
                 ref_prefix="D")

def _led_small(ref, value, fp="LED_SMD:LED_0603_1608Metric"):
    return _part("LED_Small", ref, value, fp,
                 [Pin(num="1", name="K", func=Pin.types.PASSIVE),
                  Pin(num="2", name="A", func=Pin.types.PASSIVE)],
                 ref_prefix="D")

def _rpak4(ref, value, fp="tigard:R_Array_Convex_4x0402_RoundRect"):
    """4-element resistor array: pins 1-4 are one side, 5-8 are the other."""
    return _part("R_Pack04", ref, value, fp,
                 [Pin(num="1", name="R1.1", func=Pin.types.PASSIVE),
                  Pin(num="2", name="R2.1", func=Pin.types.PASSIVE),
                  Pin(num="3", name="R3.1", func=Pin.types.PASSIVE),
                  Pin(num="4", name="R4.1", func=Pin.types.PASSIVE),
                  Pin(num="5", name="R1.2", func=Pin.types.PASSIVE),
                  Pin(num="6", name="R2.2", func=Pin.types.PASSIVE),
                  Pin(num="7", name="R3.2", func=Pin.types.PASSIVE),
                  Pin(num="8", name="R4.2", func=Pin.types.PASSIVE)],
                 ref_prefix="RN")


# ══════════════════════════════════════════════════════════════════════════════
#  NETS — Named signals used throughout the design
# ══════════════════════════════════════════════════════════════════════════════

# Power rails
GND       = Net("GND")
VCC_5V    = Net("+5V")
VCC_3V3   = Net("+3V3")
VCC_1V8   = Net("+1V8")
VBUS      = Net("VBUS")
VTARGET   = Net("VTARGET")
VREF      = Net("VREF")
VREG      = Net("VREG")
VPHY      = Net("VPHY")
VPLL      = Net("VPLL")

# USB data
USB_DP    = Net("USB_DP")
USB_DN    = Net("USB_DN")

# FT2232H Channel A signals
AD0 = Net("AD0");  AD1 = Net("AD1");  AD2 = Net("AD2");  AD3 = Net("AD3")
AD4 = Net("AD4");  AD5 = Net("AD5");  AD6 = Net("AD6")

# FT2232H Channel B signals
BD0 = Net("BD0");  BD1 = Net("BD1");  BD2 = Net("BD2");  BD3 = Net("BD3")
BD4 = Net("BD4");  BD5 = Net("BD5");  BD6 = Net("BD6");  BD7 = Net("BD7")

# Status LEDs from FT2232H
RXLED = Net("RXLED");  TXLED = Net("TXLED")

# EEPROM
EECS = Net("EECS");  EECLK = Net("EECLK");  EEDATA = Net("EEDATA")

# JTAG
TCK = Net("TCK");  TDI = Net("TDI");  TDO = Net("TDO");  TMS = Net("TMS")
nTRST = Net("~TRST");  nSRST = Net("~SRST")

# SPI
CLK  = Net("CLK");  COPI = Net("COPI");  CIPO = Net("CIPO");  CS = Net("CS")

# SWD
SWDIO       = Net("SWDIO")
CORTEX_PIN2 = Net("CORTEX_PIN2")

# UART
UART_TX   = Net("UART_TX");   UART_RX   = Net("UART_RX")
nUART_RTS = Net("~UART_RTS"); nUART_CTS = Net("~UART_CTS")
nUART_DTR = Net("~UART_DTR"); nUART_DSR = Net("~UART_DSR")
nUART_DCD = Net("~UART_DCD")

# Buffer control
nENABLE = Net("~ENABLE")
DO = Net("DO");  DI = Net("DI")

# Breakout pins (post-buffer)
xPB0 = Net("xPB0"); xPB1 = Net("xPB1"); xPB2 = Net("xPB2"); xPB3 = Net("xPB3")
xPB4 = Net("xPB4"); xPB5 = Net("xPB5"); xPB6 = Net("xPB6"); xPB7 = Net("xPB7")

# iCE40
ICE_CDONE = Net("ICE_CDONE")

# Internal connection nodes
D2_K_NET = Net("D2_K")
USB_SHLD = Net("USB_SHIELD")


# ══════════════════════════════════════════════════════════════════════════════
#  SECTION 1 — USB-C CONNECTOR (J1)
# ══════════════════════════════════════════════════════════════════════════════

J1 = _part("USB_C_Receptacle_USB2.0", "J1", "USB_C_Receptacle_USB2.0",
    "tigard:USB_C_Receptacle_HRO_TYPE-C-31-M-12",
    [Pin(num="A1",  name="GND",    func=Pin.types.PASSIVE),
     Pin(num="A4",  name="VBUS",   func=Pin.types.PASSIVE),
     Pin(num="A5",  name="CC1",    func=Pin.types.PASSIVE),
     Pin(num="A6",  name="Dp1",    func=Pin.types.PASSIVE),
     Pin(num="A7",  name="Dn1",    func=Pin.types.PASSIVE),
     Pin(num="A8",  name="SBU1",   func=Pin.types.PASSIVE),
     Pin(num="A9",  name="VBUS2",  func=Pin.types.PASSIVE),
     Pin(num="A12", name="GND2",   func=Pin.types.PASSIVE),
     Pin(num="B1",  name="GND3",   func=Pin.types.PASSIVE),
     Pin(num="B4",  name="VBUS3",  func=Pin.types.PASSIVE),
     Pin(num="B5",  name="CC2",    func=Pin.types.PASSIVE),
     Pin(num="B6",  name="Dp2",    func=Pin.types.PASSIVE),
     Pin(num="B7",  name="Dn2",    func=Pin.types.PASSIVE),
     Pin(num="B8",  name="SBU2",   func=Pin.types.PASSIVE),
     Pin(num="B9",  name="VBUS4",  func=Pin.types.PASSIVE),
     Pin(num="B12", name="GND4",   func=Pin.types.PASSIVE),
     Pin(num="S1",  name="SHIELD", func=Pin.types.PASSIVE)],
    ref_prefix="J")

# CC pull-downs (5.1kΩ) for USB-C
R1 = _res("R1", "5k1");  J1["CC1"] += R1[1];  R1[2] += GND
R2 = _res("R2", "5k1");  J1["CC2"] += R2[1];  R2[2] += GND

# VBUS → +5V via ferrite bead
J1["VBUS"] += VBUS;  J1["GND"] += GND;  J1["SHIELD"] += USB_SHLD

FB3 = _ferrite("FB3");  VBUS += FB3[1];  FB3[2] += VCC_5V

# VBUS decoupling
C26 = _cap("C26", "100n");  C26[1] += VCC_5V;  C26[2] += GND

# ESD: R3 + C25 on shield
R3  = _res("R3", "1M");    R3[1]  += USB_SHLD;  R3[2]  += GND
C25 = _cap("C25", "NF");   C25[1] += USB_SHLD;  C25[2] += GND

# USB data
J1["Dp1"] += USB_DP;  J1["Dn1"] += USB_DN


# ══════════════════════════════════════════════════════════════════════════════
#  SECTION 2 — LDO REGULATORS
# ══════════════════════════════════════════════════════════════════════════════

def _sot23_5_vreg(ref, value, fp="tigard:SOT-23-5_RoundRect"):
    return _part(value, ref, value, fp,
        [Pin(num="1", name="VIN",  func=Pin.types.PWRIN),
         Pin(num="2", name="GND",  func=Pin.types.PASSIVE),
         Pin(num="3", name="EN",   func=Pin.types.INPUT),
         Pin(num="4", name="NC",   func=Pin.types.NOCONNECT),
         Pin(num="5", name="VOUT", func=Pin.types.PWROUT)],
        ref_prefix="U")

# U1: AP7365-18 (5V → 1.8V)
U1 = _sot23_5_vreg("U1", "AP7365-18")
U1["VIN"] += VCC_5V;  U1["EN"] += VCC_5V;  U1["VOUT"] += VCC_1V8;  U1["GND"] += GND
C1 = _cap("C1", "2u2");  C1[1] += VCC_5V;   C1[2] += GND
C2 = _cap("C2", "2u2");  C2[1] += VCC_1V8;  C2[2] += GND

# U2: AP7365-33 (5V → 3.3V)
U2 = _sot23_5_vreg("U2", "AP7365-33")
U2["VIN"] += VCC_5V;  U2["EN"] += VCC_5V;  U2["VOUT"] += VCC_3V3;  U2["GND"] += GND
C3 = _cap("C3", "2u2");  C3[1] += VCC_5V;   C3[2] += GND
C4 = _cap("C4", "2u2");  C4[1] += VCC_3V3;  C4[2] += GND


# ══════════════════════════════════════════════════════════════════════════════
#  SECTION 3 — TARGET VOLTAGE SWITCH (SW1: DP4T)
# ══════════════════════════════════════════════════════════════════════════════

SW1 = _part("SW_DP4T", "SW1", "TARGET", "tigard:SW_ALPS_SSSS224100_DP4T",
    [Pin(num="1",  name="A",   func=Pin.types.PASSIVE),
     Pin(num="2",  name="B",   func=Pin.types.PASSIVE),
     Pin(num="3",  name="C",   func=Pin.types.PASSIVE),
     Pin(num="4",  name="COM", func=Pin.types.PASSIVE),
     Pin(num="5",  name="D",   func=Pin.types.PASSIVE)],
    ref_prefix="SW")

SW1["A"] += VCC_5V;  SW1["B"] += VCC_3V3;  SW1["C"] += VCC_1V8
SW1["COM"] += VTARGET

# ISO solder jumper — VTARGET to VREF
JP1 = _2pin("Jumper_NC_Small", "JP1", "ISO",
            "Jumper:SolderJumper-2_P1.3mm_Bridged_RoundedPad1.0x1.5mm", ref_prefix="JP")
JP1[1] += VTARGET;  JP1[2] += VREF


# ══════════════════════════════════════════════════════════════════════════════
#  SECTION 4 — POWER INDICATOR LEDs
# ══════════════════════════════════════════════════════════════════════════════

# D1 (YELLOW PWR LED) + R4
D1 = _led("D1", "YELLOW")
R4 = _res_std("R4", "330")
VCC_3V3 += R4[1];  R4[2] += D1["A"];  D1["K"] += GND

# D2 (BLUE VREF LED) + R5, controlled by Q1 NMOS
D2 = _led("D2", "BLUE")
R5 = _res_std("R5", "330")
VCC_3V3 += R5[1];  R5[2] += D2["A"];  D2["K"] += D2_K_NET

Q1 = _part("Q_NMOS_GSD", "Q1", "BSH103", "tigard:SOT-23_RoundRect",
    [Pin(num="1", name="G", func=Pin.types.INPUT),
     Pin(num="2", name="S", func=Pin.types.PASSIVE),
     Pin(num="3", name="D", func=Pin.types.PASSIVE)],
    ref_prefix="Q")
Q1["G"] += VREF;  Q1["S"] += GND;  Q1["D"] += D2_K_NET

R24 = _res("R24", "10k");  R24[1] += VREF;  R24[2] += GND


# ══════════════════════════════════════════════════════════════════════════════
#  SECTION 5 — FT2232HQ (U3)
# ══════════════════════════════════════════════════════════════════════════════

U3 = _part("FT2232HQ", "U3", "FT2232HQ",
    "Package_DFN_QFN:QFN-64-1EP_9x9mm_P0.5mm_EP4.35x4.35mm_ThermalVias",
    [
        # Power
        Pin(num="1",  name="GND1",    func=Pin.types.PASSIVE),
        Pin(num="3",  name="VCCIO1",  func=Pin.types.PWRIN),
        Pin(num="5",  name="GND2",    func=Pin.types.PASSIVE),
        Pin(num="8",  name="VCCIO2",  func=Pin.types.PWRIN),
        Pin(num="10", name="VREGIN",  func=Pin.types.PWRIN),
        Pin(num="11", name="VREGOUT", func=Pin.types.PWROUT),
        Pin(num="12", name="GND3",    func=Pin.types.PASSIVE),
        Pin(num="17", name="GND4",    func=Pin.types.PASSIVE),
        Pin(num="37", name="VCCIO3",  func=Pin.types.PWRIN),
        Pin(num="39", name="GND5",    func=Pin.types.PASSIVE),
        Pin(num="42", name="VCCIO4",  func=Pin.types.PWRIN),
        Pin(num="47", name="GND6",    func=Pin.types.PASSIVE),
        Pin(num="48", name="VCCA",    func=Pin.types.PWRIN),
        Pin(num="49", name="VCCD",    func=Pin.types.PWRIN),
        Pin(num="50", name="GND7",    func=Pin.types.PASSIVE),
        Pin(num="51", name="VCCCORE", func=Pin.types.PWRIN),
        Pin(num="56", name="AGND",    func=Pin.types.PASSIVE),
        Pin(num="57", name="VPLL",    func=Pin.types.PWRIN),
        Pin(num="60", name="AGND2",   func=Pin.types.PASSIVE),
        Pin(num="61", name="VPHY",    func=Pin.types.PWRIN),
        Pin(num="65", name="GND_EP",  func=Pin.types.PASSIVE),
        # USB
        Pin(num="7",  name="DM",      func=Pin.types.BIDIR),
        Pin(num="6",  name="DP",      func=Pin.types.BIDIR),
        # Config
        Pin(num="9",  name="RESET",   func=Pin.types.INPUT),
        Pin(num="4",  name="REF",     func=Pin.types.PASSIVE),
        Pin(num="13", name="TEST",    func=Pin.types.INPUT),
        # EEPROM
        Pin(num="14", name="EECS",    func=Pin.types.OUTPUT),
        Pin(num="15", name="EECLK",   func=Pin.types.OUTPUT),
        Pin(num="16", name="EEDATA",  func=Pin.types.BIDIR),
        # Crystal
        Pin(num="58", name="OSCI",    func=Pin.types.INPUT),
        Pin(num="59", name="OSCO",    func=Pin.types.OUTPUT),
        # Channel A (MPSSE)
        Pin(num="18", name="ADBUS0",  func=Pin.types.BIDIR),
        Pin(num="19", name="ADBUS1",  func=Pin.types.BIDIR),
        Pin(num="20", name="ADBUS2",  func=Pin.types.BIDIR),
        Pin(num="21", name="ADBUS3",  func=Pin.types.BIDIR),
        Pin(num="22", name="ADBUS4",  func=Pin.types.BIDIR),
        Pin(num="23", name="ADBUS5",  func=Pin.types.BIDIR),
        Pin(num="24", name="ADBUS6",  func=Pin.types.BIDIR),
        Pin(num="25", name="ADBUS7",  func=Pin.types.BIDIR),
        Pin(num="26", name="ACBUS0",  func=Pin.types.BIDIR),
        Pin(num="27", name="ACBUS1",  func=Pin.types.BIDIR),
        Pin(num="28", name="ACBUS2",  func=Pin.types.BIDIR),
        Pin(num="29", name="ACBUS3",  func=Pin.types.BIDIR),
        Pin(num="30", name="ACBUS4",  func=Pin.types.BIDIR),
        Pin(num="31", name="ACBUS5",  func=Pin.types.BIDIR),
        Pin(num="32", name="ACBUS6",  func=Pin.types.BIDIR),
        Pin(num="33", name="ACBUS7",  func=Pin.types.BIDIR),
        Pin(num="2",  name="ACBUS8",  func=Pin.types.BIDIR),
        Pin(num="64", name="ACBUS9",  func=Pin.types.BIDIR),
        # Channel B (UART)
        Pin(num="38", name="BDBUS0",  func=Pin.types.BIDIR),
        Pin(num="40", name="BDBUS1",  func=Pin.types.BIDIR),
        Pin(num="41", name="BDBUS2",  func=Pin.types.BIDIR),
        Pin(num="43", name="BDBUS3",  func=Pin.types.BIDIR),
        Pin(num="44", name="BDBUS4",  func=Pin.types.BIDIR),
        Pin(num="45", name="BDBUS5",  func=Pin.types.BIDIR),
        Pin(num="46", name="BDBUS6",  func=Pin.types.BIDIR),
        Pin(num="53", name="BDBUS7",  func=Pin.types.BIDIR),
        Pin(num="34", name="BCBUS0",  func=Pin.types.BIDIR),
        Pin(num="35", name="BCBUS1",  func=Pin.types.BIDIR),
        Pin(num="36", name="BCBUS2",  func=Pin.types.BIDIR),
        Pin(num="52", name="BCBUS3",  func=Pin.types.BIDIR),
        Pin(num="54", name="BCBUS4",  func=Pin.types.BIDIR),
        Pin(num="55", name="BCBUS5",  func=Pin.types.BIDIR),
        Pin(num="62", name="BCBUS6",  func=Pin.types.BIDIR),
        Pin(num="63", name="BCBUS7",  func=Pin.types.BIDIR),
    ], ref_prefix="U")

# ── Power pins ──
for gnd_pin in ["GND1","GND2","GND3","GND4","GND5","GND6","GND7","AGND","AGND2","GND_EP"]:
    U3[gnd_pin] += GND

U3["VCCIO1"] += VCC_3V3; U3["VCCIO2"] += VCC_3V3
U3["VCCIO3"] += VCC_3V3; U3["VCCIO4"] += VCC_3V3
U3["VCCA"]   += VCC_3V3; U3["VCCD"]   += VCC_3V3
U3["VCCCORE"] += VCC_1V8
U3["VREGIN"] += VREG;  U3["VREGOUT"] += VREG
U3["VPLL"]   += VPLL;  U3["VPHY"]    += VPHY
U3["TEST"]   += GND

# Ferrite beads for analog supplies
FB1 = _ferrite("FB1"); VCC_3V3 += FB1[1]; FB1[2] += VPHY
FB2 = _ferrite("FB2"); VCC_3V3 += FB2[1]; FB2[2] += VPLL

# Decoupling
C6  = _cap("C6",  "2u2");   C6[1]  += VPHY; C6[2]  += GND
C5  = _cap("C5",  "100n");  C5[1]  += VPLL; C5[2]  += GND
C7  = _cap("C7",  "2u2");   C7[1]  += VPLL; C7[2]  += GND
C8  = _cap("C8",  "100n");  C8[1]  += VPHY; C8[2]  += GND
C9  = _cap("C9",  "2u2");   C9[1]  += VREG; C9[2]  += GND
C10 = _cap("C10", "2u2");   C10[1] += VREG; C10[2] += GND
C11 = _cap("C11", "100n");  C11[1] += VREG; C11[2] += GND
C12 = _cap("C12", "100n");  C12[1] += VREG; C12[2] += GND
C13 = _cap("C13", "100n");  C13[1] += VREG; C13[2] += GND
C14 = _cap("C14", "100n");  C14[1] += VCC_3V3; C14[2] += GND
C15 = _cap("C15", "100n");  C15[1] += VCC_3V3; C15[2] += GND
C16 = _cap("C16", "100n");  C16[1] += VCC_3V3; C16[2] += GND
C17 = _cap("C17", "100n");  C17[1] += VCC_3V3; C17[2] += GND

# USB data
U3["DM"] += USB_DN;  U3["DP"] += USB_DP

# Reference resistor
R6 = _res("R6", "12k, 1%"); U3["REF"] += R6[1]; R6[2] += GND

# Reset pull-up
R7 = _res("R7", "10k"); VCC_3V3 += R7[1]; R7[2] += U3["RESET"]

# 12 MHz Crystal
Y1 = _part("Crystal_GND24", "Y1", "12MHz",
    "tigard:Crystal_SMD_3225-4Pin_3.2x2.5mm_RoundRect",
    [Pin(num="1", name="1", func=Pin.types.PASSIVE),
     Pin(num="2", name="2", func=Pin.types.PASSIVE),
     Pin(num="3", name="3", func=Pin.types.PASSIVE),
     Pin(num="4", name="4", func=Pin.types.PASSIVE)],
    ref_prefix="Y")
Y1["1"] += U3["OSCI"];  Y1["3"] += U3["OSCO"]
Y1["2"] += GND;         Y1["4"] += GND

# Load caps
C23 = _cap("C23", "30pF"); C23[1] += U3["OSCI"]; C23[2] += GND
C24 = _cap("C24", "30pF"); C24[1] += U3["OSCO"]; C24[2] += GND

# EEPROM bus
U3["EECS"] += EECS;  U3["EECLK"] += EECLK;  U3["EEDATA"] += EEDATA

# Channel A
U3["ADBUS0"] += AD0;  U3["ADBUS1"] += AD1;  U3["ADBUS2"] += AD2
U3["ADBUS3"] += AD3;  U3["ADBUS4"] += AD4;  U3["ADBUS5"] += AD5
U3["ADBUS6"] += AD6
U3["ACBUS0"] += RXLED; U3["ACBUS1"] += TXLED

# Channel B
U3["BDBUS0"] += BD0;  U3["BDBUS1"] += BD1;  U3["BDBUS2"] += BD2
U3["BDBUS3"] += BD3;  U3["BDBUS4"] += BD4;  U3["BDBUS5"] += BD5
U3["BDBUS6"] += BD6;  U3["BDBUS7"] += BD7
U3["BCBUS0"] += nENABLE

# RXLED/TXLED LEDs
D3 = _led_small("D3", "GREEN")
D4 = _led_small("D4", "YELLOW")
R8 = _res("R8", "330"); VCC_3V3 += R8[1]; R8[2] += D3["A"]; D3["K"] += RXLED
R9 = _res("R9", "330"); VCC_3V3 += R9[1]; R9[2] += D4["A"]; D4["K"] += TXLED

# Enable LED
D5  = _led_small("D5", "GREEN")
R10 = _res("R10", "10k"); VCC_3V3 += R10[1]; R10[2] += nENABLE
R11 = _res("R11", "330"); VCC_3V3 += R11[1]; R11[2] += D5["A"]; D5["K"] += nENABLE

# I2C pull-up
R22 = _res("R22", "2k2"); R22[1] += BD6; R22[2] += BD7


# ══════════════════════════════════════════════════════════════════════════════
#  SECTION 6 — EEPROM (U4: 93LC46B)
# ══════════════════════════════════════════════════════════════════════════════

U4 = _part("93LCxxBxxOT", "U4", "93LC46BT-I/OT", "tigard:SOT-23-6_RoundRect",
    [Pin(num="1", name="CS",  func=Pin.types.INPUT),
     Pin(num="2", name="CLK", func=Pin.types.INPUT),
     Pin(num="3", name="DI",  func=Pin.types.INPUT),
     Pin(num="4", name="DO",  func=Pin.types.OUTPUT),
     Pin(num="5", name="VSS", func=Pin.types.PASSIVE),
     Pin(num="6", name="VCC", func=Pin.types.PWRIN)],
    ref_prefix="U")

U4["CS"] += EECS;   U4["CLK"] += EECLK
U4["DI"] += EEDATA; U4["DO"]  += EEDATA
U4["VCC"] += VCC_3V3; U4["VSS"] += GND

C18 = _cap("C18", "100n"); C18[1] += VCC_3V3; C18[2] += GND

# Pull-ups
R12 = _res("R12", "10k"); VCC_3V3 += R12[1]; R12[2] += EECS
R13 = _res("R13", "10k"); VCC_3V3 += R13[1]; R13[2] += EECLK
R14 = _res("R14", "10k"); VCC_3V3 += R14[1]; R14[2] += EEDATA
R15 = _res("R15", "2.2k"); R15[1] += EEDATA; R15[2] += EEDATA


# ══════════════════════════════════════════════════════════════════════════════
#  SECTION 7 — OUTPUT BUFFER (U5: SN74LVC8T245)
# ══════════════════════════════════════════════════════════════════════════════

def _make_8t245(ref):
    return _part("SN74LVC8T245", ref, "SN74LVC8T245",
        "Package_SO:TSSOP-24_4.4x7.8mm_P0.65mm",
        [Pin(num="1",  name="VCCA", func=Pin.types.PWRIN),
         Pin(num="2",  name="A1",   func=Pin.types.BIDIR),
         Pin(num="3",  name="A2",   func=Pin.types.BIDIR),
         Pin(num="4",  name="A3",   func=Pin.types.BIDIR),
         Pin(num="5",  name="A4",   func=Pin.types.BIDIR),
         Pin(num="6",  name="A5",   func=Pin.types.BIDIR),
         Pin(num="7",  name="A6",   func=Pin.types.BIDIR),
         Pin(num="8",  name="A7",   func=Pin.types.BIDIR),
         Pin(num="9",  name="A8",   func=Pin.types.BIDIR),
         Pin(num="10", name="OE",   func=Pin.types.INPUT),
         Pin(num="11", name="DIR",  func=Pin.types.INPUT),
         Pin(num="12", name="GND1", func=Pin.types.PASSIVE),
         Pin(num="13", name="GND2", func=Pin.types.PASSIVE),
         Pin(num="14", name="GND3", func=Pin.types.PASSIVE),
         Pin(num="15", name="B8",   func=Pin.types.BIDIR),
         Pin(num="16", name="B7",   func=Pin.types.BIDIR),
         Pin(num="17", name="B6",   func=Pin.types.BIDIR),
         Pin(num="18", name="B5",   func=Pin.types.BIDIR),
         Pin(num="19", name="B4",   func=Pin.types.BIDIR),
         Pin(num="20", name="B3",   func=Pin.types.BIDIR),
         Pin(num="21", name="B2",   func=Pin.types.BIDIR),
         Pin(num="22", name="B1",   func=Pin.types.BIDIR),
         Pin(num="23", name="VCCB", func=Pin.types.PWRIN),
         Pin(num="24", name="DIR2", func=Pin.types.INPUT)],
        ref_prefix="U")

U5 = _make_8t245("U5")
U5["VCCA"] += VCC_3V3;  U5["VCCB"] += VREF
U5["GND1"] += GND;  U5["GND2"] += GND;  U5["GND3"] += GND
U5["DIR"]  += VCC_3V3;  U5["DIR2"] += VCC_3V3
U5["OE"]   += nENABLE

R18 = _res("R18", "10k"); VCC_3V3 += R18[1]; R18[2] += nENABLE

# A-side (3.3V domain)
U5["A1"] += BD0;  U5["A2"] += BD1;  U5["A3"] += BD3;  U5["A4"] += BD4
U5["A5"] += AD4;  U5["A6"] += AD2;  U5["A7"] += AD0;  U5["A8"] += BD5

# B-side (VREF domain)
U5["B1"] += CLK;       U5["B2"] += DO
U5["B3"] += CS;        U5["B4"] += nTRST
U5["B5"] += nSRST;     U5["B6"] += nUART_DTR
U5["B7"] += nUART_RTS; U5["B8"] += UART_TX

# A-side pull-ups
RN1 = _rpak4("RN1", "100k")
RN2 = _rpak4("RN2", "100k")
RN1["R1.1"] += VCC_3V3; RN1["R1.2"] += BD0
RN1["R2.1"] += VCC_3V3; RN1["R2.2"] += BD1
RN1["R3.1"] += VCC_3V3; RN1["R3.2"] += BD3
RN1["R4.1"] += VCC_3V3; RN1["R4.2"] += BD4
RN2["R1.1"] += VCC_3V3; RN2["R1.2"] += AD4
RN2["R2.1"] += VCC_3V3; RN2["R2.2"] += AD2
RN2["R3.1"] += VCC_3V3; RN2["R3.2"] += AD0
RN2["R4.1"] += VCC_3V3; RN2["R4.2"] += BD5

# B-side series resistors
RN3 = _rpak4("RN3", "100")
RN4 = _rpak4("RN4", "100")
RN3["R1.1"] += CLK;   RN3["R1.2"] += xPB0
RN3["R2.1"] += DO;    RN3["R2.2"] += xPB1
RN3["R3.1"] += CS;    RN3["R3.2"] += xPB3
RN3["R4.1"] += nTRST; RN3["R4.2"] += xPB4
RN4["R1.1"] += nSRST;     RN4["R1.2"] += xPB5
RN4["R2.1"] += nUART_DTR; RN4["R2.2"] += nUART_DTR
RN4["R3.1"] += nUART_RTS; RN4["R3.2"] += nUART_RTS
RN4["R4.1"] += UART_TX;   RN4["R4.2"] += xPB6

# Buffer decoupling
C19 = _cap("C19", "100n"); C19[1] += VCC_3V3; C19[2] += GND
C20 = _cap("C20", "100n"); C20[1] += VCC_3V3; C20[2] += GND
C21 = _cap("C21", "100n"); C21[1] += VREF;    C21[2] += GND
C22 = _cap("C22", "100n"); C22[1] += VREF;    C22[2] += GND

R17 = _res("R17", "1M"); R17[1] += VREF; R17[2] += GND


# ══════════════════════════════════════════════════════════════════════════════
#  SECTION 8 — INPUT BUFFER (U6: SN74LVC8T245)
# ══════════════════════════════════════════════════════════════════════════════

U6 = _make_8t245("U6")
U6["VCCA"] += VCC_3V3;  U6["VCCB"] += VREF
U6["GND1"] += GND;  U6["GND2"] += GND;  U6["GND3"] += GND
U6["DIR"]  += GND;  U6["DIR2"] += GND   # B→A direction
U6["OE"]   += nENABLE

R19 = _res("R19", "10k"); VCC_3V3 += R19[1]; R19[2] += nENABLE

# Input series resistors
RN5 = _rpak4("RN5", "100")
RN6 = _rpak4("RN6", "100")
RN5["R1.1"] += AD1; RN5["R1.2"] += U6["A1"]
RN5["R2.1"] += AD3; RN5["R2.2"] += U6["A2"]
RN5["R3.1"] += AD5; RN5["R3.2"] += U6["A3"]
RN5["R4.1"] += AD6; RN5["R4.2"] += U6["A4"]
RN6["R1.1"] += BD2; RN6["R1.2"] += U6["A5"]
RN6["R2.1"] += BD6; RN6["R2.2"] += U6["A6"]

nc_a = Net("NC_A7"); nc_b = Net("NC_A8")
RN6["R3.1"] += nc_a;  RN6["R3.2"] += U6["A7"]
RN6["R4.1"] += nc_b;  RN6["R4.2"] += U6["A8"]

# B-side (target inputs)
U6["B1"] += UART_RX;    U6["B2"] += nUART_CTS
U6["B3"] += nUART_DSR;  U6["B4"] += nUART_DCD
U6["B5"] += DI;          U6["B6"] += xPB2
U6["B7"] += ICE_CDONE;  U6["B8"] += UART_RX

# Pull-ups on target side
RN7 = _rpak4("RN7", "100k")
RN8 = _rpak4("RN8", "100k")
RN7["R1.1"] += VREF; RN7["R1.2"] += UART_RX
RN7["R2.1"] += VREF; RN7["R2.2"] += nUART_CTS
RN7["R3.1"] += VREF; RN7["R3.2"] += nUART_DSR
RN7["R4.1"] += VREF; RN7["R4.2"] += nUART_DCD
RN8["R1.1"] += VREF; RN8["R1.2"] += DI
RN8["R2.1"] += VREF; RN8["R2.2"] += xPB2
RN8["R3.1"] += VREF; RN8["R3.2"] += ICE_CDONE
RN8["R4.1"] += VREF; RN8["R4.2"] += UART_RX


# ══════════════════════════════════════════════════════════════════════════════
#  SECTION 9 — MODE SWITCH (SW2: DPDT)
# ══════════════════════════════════════════════════════════════════════════════

SW2 = _part("SW_DPDT", "SW2", "MODE", "tigard:SW_CuK_JS202011CQN_DPDT_Straight",
    [Pin(num="1", name="A1",   func=Pin.types.PASSIVE),
     Pin(num="2", name="COM1", func=Pin.types.PASSIVE),
     Pin(num="3", name="B1",   func=Pin.types.PASSIVE),
     Pin(num="4", name="A2",   func=Pin.types.PASSIVE),
     Pin(num="5", name="COM2", func=Pin.types.PASSIVE),
     Pin(num="6", name="B2",   func=Pin.types.PASSIVE)],
    ref_prefix="SW")

SW2["COM1"] += CIPO;  SW2["A1"] += TDO;   SW2["B1"] += DI
SW2["COM2"] += CORTEX_PIN2; SW2["A2"] += TMS; SW2["B2"] += SWDIO

R16 = _res("R16", "330"); R16[1] += CS; R16[2] += CS

# HACK jumper
JP2 = _2pin("Jumper_NO_Small", "JP2", "HACK",
            "Jumper:SolderJumper-2_P1.3mm_Open_RoundedPad1.0x1.5mm", ref_prefix="JP")
JP2[1] += DO; JP2[2] += COPI


# ══════════════════════════════════════════════════════════════════════════════
#  SECTION 10 — CONNECTORS
# ══════════════════════════════════════════════════════════════════════════════

def _conn(ref, value, num_pins, fp, ref_prefix="J"):
    pins = [Pin(num=str(i+1), name=str(i+1), func=Pin.types.PASSIVE) for i in range(num_pins)]
    part_name = f"Conn_01x{num_pins:02d}" if "01x" in value or num_pins <= 9 else f"Conn_02x{num_pins//2:02d}"
    return _part(part_name, ref, value, fp, pins, ref_prefix=ref_prefix)

# J2: JTAG 1×9
J2 = _part("Conn_01x09", "J2", "JTAG", "tigard:PinHeader_1x09_P2.54mm_Vertical",
    [Pin(num=str(i), name=str(i), func=Pin.types.PASSIVE) for i in range(1,10)],
    ref_prefix="J")
J2["1"] += GND;    J2["2"] += TCK;   J2["3"] += TDI
J2["4"] += TDO;    J2["5"] += TMS;   J2["6"] += nTRST
J2["7"] += nSRST;  J2["8"] += ICE_CDONE;  J2["9"] += VTARGET

# J3: UART 1×9
J3 = _part("Conn_01x09", "J3", "UART", "tigard:PinHeader_1x09_P2.54mm_Vertical",
    [Pin(num=str(i), name=str(i), func=Pin.types.PASSIVE) for i in range(1,10)],
    ref_prefix="J")
J3["1"] += VTARGET; J3["2"] += GND;       J3["3"] += UART_TX
J3["4"] += UART_RX; J3["5"] += nUART_RTS; J3["6"] += nUART_CTS
J3["7"] += nUART_DTR; J3["8"] += nUART_DSR; J3["9"] += nUART_DCD

# J4: SPI 2×4
J4 = _part("Conn_02x04_Odd_Even", "J4", "SPI", "tigard:PinHeader_2x04_P2.54mm_Vertical",
    [Pin(num=str(i), name=str(i), func=Pin.types.PASSIVE) for i in range(1,9)],
    ref_prefix="J")
R20 = _res("R20", "10k"); R21 = _res("R21", "10k")
J4["1"] += CS;    J4["2"] += VTARGET
J4["3"] += CIPO;  J4["4"] += CLK
J4["5"] += COPI;  J4["6"] += COPI
J4["7"] += GND;   J4["8"] += GND
R20[1] += VTARGET; R20[2] += CS
R21[1] += VTARGET; R21[2] += CIPO

# J5: CORTEX 2×5 1.27mm
J5 = _part("Conn_02x05_Odd_Even", "J5", "CORTEX",
    "tigard:PinHeader_2x05_P1.27mm_Vertical_SMD",
    [Pin(num=str(i), name=str(i), func=Pin.types.PASSIVE) for i in range(1,11)],
    ref_prefix="J")
J5["1"]  += VTARGET;  J5["2"]  += TCK
J5["3"]  += GND;      J5["4"]  += CORTEX_PIN2
J5["5"]  += GND;      J5["6"]  += TDI
J5["7"]  += GND;      J5["8"]  += TDO
J5["9"]  += GND;      J5["10"] += nSRST

# J6: Logic Analyzer 2×7
J6 = _part("Conn_02x07_Odd_Even", "J6", "LA",
    "tigard:PinHeader_2x07_P1.27mm_Vertical_SMD",
    [Pin(num=str(i), name=str(i), func=Pin.types.PASSIVE) for i in range(1,15)],
    ref_prefix="J")
J6["1"]  += xPB0;  J6["2"]  += xPB1;  J6["3"]  += xPB2;  J6["4"]  += xPB3
J6["5"]  += xPB4;  J6["6"]  += xPB5;  J6["7"]  += xPB6;  J6["8"]  += xPB7
J6["9"]  += GND;   J6["10"] += GND;   J6["11"] += GND;   J6["12"] += GND
J6["13"] += GND;   J6["14"] += GND

# J7: I2C / Qwiic (JST-SH 1×4 + mounting pin)
J7 = _part("Conn_01x04_MountingPin", "J7", "I2C",
    "Connector_JST:JST_SH_SM04B-SRSS-TB_1x04-1MP_P1.00mm_Horizontal",
    [Pin(num="1", name="1",  func=Pin.types.PASSIVE),
     Pin(num="2", name="2",  func=Pin.types.PASSIVE),
     Pin(num="3", name="3",  func=Pin.types.PASSIVE),
     Pin(num="4", name="4",  func=Pin.types.PASSIVE),
     Pin(num="5", name="MP", func=Pin.types.PASSIVE)],
    ref_prefix="J")
J7["1"] += GND;  J7["2"] += VTARGET;  J7["3"] += CLK;  J7["4"] += COPI
J7["MP"] += GND


# ══════════════════════════════════════════════════════════════════════════════
#  SECTION 11 — TEST POINT & MECHANICAL
# ══════════════════════════════════════════════════════════════════════════════

TP1 = _part("TestPoint", "TP1", "GND",
    "TestPoint:TestPoint_Keystone_5000-5004_Miniature",
    [Pin(num="1", name="1", func=Pin.types.PASSIVE)],
    ref_prefix="TP")
TP1["1"] += GND

# Mounting holes (no electrical connections)
for mh_ref in ["H1", "H2", "H3", "H4"]:
    _part("MountingHole", mh_ref, "MountingHole",
          "MountingHole:MountingHole_3.2mm_M3_ISO7380",
          [Pin(num="1", name="1", func=Pin.types.PASSIVE)],
          ref_prefix="H")

# Logos (graphical, no pins needed)
_part("Logo_Open_Hardware_Small", "LOGO1", "Logo_Open_Hardware_Small",
      "tigard:OSHW-Symbol_4.4x4mm_SilkScreen", [], ref_prefix="LOGO")
_part("Logo_SH", "LOGO2", "Logo_SH",
      "tigard:Securing_Hardware_Logo", [], ref_prefix="LOGO")


# ══════════════════════════════════════════════════════════════════════════════
#  GENERATE NETLIST
# ══════════════════════════════════════════════════════════════════════════════

output_path = os.path.expanduser("~/Desktop/tigard_skidl.net")

print("=" * 60)
print("  Tigard PCB — SKiDL Netlist Generator")
print("=" * 60)
print(f"\n  Output: {output_path}\n")

# Electrical Rules Check (informational)
ERC()

# Generate netlist
generate_netlist(file_=output_path)

print(f"\n✅  Netlist successfully exported to:")
print(f"    {output_path}")
print("\n  Open this .net file in KiCad Pcbnew to import the design.")
print("=" * 60)
