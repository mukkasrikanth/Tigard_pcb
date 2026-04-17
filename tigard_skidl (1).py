#!/usr/bin/env python3
"""
SKiDL script to build the Tigard v1.1 PCB circuit.
Generated from tigard.sch with tigard.lib pin definitions.

Tigard - Copyright 2020 Franklin Harding
Licensed under CC-BY-SA 4.0
"""

# Auto-install skidl if not already installed
import subprocess, sys

def install_skidl():
    print("skidl not found. Installing...")
    ret = subprocess.run([sys.executable, "-m", "pip", "install", "skidl"],
                         capture_output=True, text=True)
    if ret.returncode == 0:
        print("skidl installed successfully.\n")
        return
    if "externally-managed" in ret.stderr:
        print("Detected externally-managed Python. Retrying with --break-system-packages...")
        subprocess.check_call([sys.executable, "-m", "pip", "install",
                               "--break-system-packages", "skidl"])
        print("skidl installed successfully.\n")
        return
    print(ret.stderr)
    sys.exit(1)

try:
    import skidl
except ModuleNotFoundError:
    install_skidl()

from skidl import *

# ============================================================
# Component templates
# ============================================================
tigard_lib = SchLib(tool=SKIDL)

# Connector:TestPoint
tmpl_Connector_TestPoint = Part(name="TestPoint", dest=SKIDL, tool=SKIDL)
tmpl_Connector_TestPoint += Pin(num="1", name="p1", func=Pin.types.PASSIVE)
tmpl_Connector_TestPoint.ref_prefix = "TP"
tigard_lib += tmpl_Connector_TestPoint

# Connector:USB_C_Receptacle_USB2.0
tmpl_Connector_USB_C_Receptacle_USB2_0 = Part(name="USB_C_Receptacle_USB2.0", dest=SKIDL, tool=SKIDL)
tmpl_Connector_USB_C_Receptacle_USB2_0 += Pin(num="A1", name="pA1", func=Pin.types.PASSIVE)
tmpl_Connector_USB_C_Receptacle_USB2_0 += Pin(num="A4", name="pA4", func=Pin.types.PASSIVE)
tmpl_Connector_USB_C_Receptacle_USB2_0 += Pin(num="A5", name="pA5", func=Pin.types.PASSIVE)
tmpl_Connector_USB_C_Receptacle_USB2_0 += Pin(num="A6", name="pA6", func=Pin.types.PASSIVE)
tmpl_Connector_USB_C_Receptacle_USB2_0 += Pin(num="A7", name="pA7", func=Pin.types.PASSIVE)
tmpl_Connector_USB_C_Receptacle_USB2_0 += Pin(num="A8", name="pA8", func=Pin.types.PASSIVE)
tmpl_Connector_USB_C_Receptacle_USB2_0 += Pin(num="A9", name="pA9", func=Pin.types.PASSIVE)
tmpl_Connector_USB_C_Receptacle_USB2_0 += Pin(num="B1", name="pB1", func=Pin.types.PASSIVE)
tmpl_Connector_USB_C_Receptacle_USB2_0 += Pin(num="B4", name="pB4", func=Pin.types.PASSIVE)
tmpl_Connector_USB_C_Receptacle_USB2_0 += Pin(num="B5", name="pB5", func=Pin.types.PASSIVE)
tmpl_Connector_USB_C_Receptacle_USB2_0 += Pin(num="B6", name="pB6", func=Pin.types.PASSIVE)
tmpl_Connector_USB_C_Receptacle_USB2_0 += Pin(num="B7", name="pB7", func=Pin.types.PASSIVE)
tmpl_Connector_USB_C_Receptacle_USB2_0 += Pin(num="B8", name="pB8", func=Pin.types.PASSIVE)
tmpl_Connector_USB_C_Receptacle_USB2_0 += Pin(num="B9", name="pB9", func=Pin.types.PASSIVE)
tmpl_Connector_USB_C_Receptacle_USB2_0 += Pin(num="S1", name="pS1", func=Pin.types.PASSIVE)
tmpl_Connector_USB_C_Receptacle_USB2_0 += Pin(num="A12", name="pA12", func=Pin.types.PASSIVE)
tmpl_Connector_USB_C_Receptacle_USB2_0 += Pin(num="B12", name="pB12", func=Pin.types.PASSIVE)
tmpl_Connector_USB_C_Receptacle_USB2_0.ref_prefix = "J"
tigard_lib += tmpl_Connector_USB_C_Receptacle_USB2_0

# Connector_Generic:Conn_01x09
tmpl_Connector_Generic_Conn_01x09 = Part(name="Conn_01x09", dest=SKIDL, tool=SKIDL)
tmpl_Connector_Generic_Conn_01x09 += Pin(num="1", name="p1", func=Pin.types.PASSIVE)
tmpl_Connector_Generic_Conn_01x09 += Pin(num="2", name="p2", func=Pin.types.PASSIVE)
tmpl_Connector_Generic_Conn_01x09 += Pin(num="3", name="p3", func=Pin.types.PASSIVE)
tmpl_Connector_Generic_Conn_01x09 += Pin(num="4", name="p4", func=Pin.types.PASSIVE)
tmpl_Connector_Generic_Conn_01x09 += Pin(num="5", name="p5", func=Pin.types.PASSIVE)
tmpl_Connector_Generic_Conn_01x09 += Pin(num="6", name="p6", func=Pin.types.PASSIVE)
tmpl_Connector_Generic_Conn_01x09 += Pin(num="7", name="p7", func=Pin.types.PASSIVE)
tmpl_Connector_Generic_Conn_01x09 += Pin(num="8", name="p8", func=Pin.types.PASSIVE)
tmpl_Connector_Generic_Conn_01x09 += Pin(num="9", name="p9", func=Pin.types.PASSIVE)
tmpl_Connector_Generic_Conn_01x09.ref_prefix = "J"
tigard_lib += tmpl_Connector_Generic_Conn_01x09

# Connector_Generic:Conn_02x04_Odd_Even
tmpl_Connector_Generic_Conn_02x04_Odd_Even = Part(name="Conn_02x04_Odd_Even", dest=SKIDL, tool=SKIDL)
tmpl_Connector_Generic_Conn_02x04_Odd_Even += Pin(num="1", name="p1", func=Pin.types.PASSIVE)
tmpl_Connector_Generic_Conn_02x04_Odd_Even += Pin(num="2", name="p2", func=Pin.types.PASSIVE)
tmpl_Connector_Generic_Conn_02x04_Odd_Even += Pin(num="3", name="p3", func=Pin.types.PASSIVE)
tmpl_Connector_Generic_Conn_02x04_Odd_Even += Pin(num="4", name="p4", func=Pin.types.PASSIVE)
tmpl_Connector_Generic_Conn_02x04_Odd_Even += Pin(num="5", name="p5", func=Pin.types.PASSIVE)
tmpl_Connector_Generic_Conn_02x04_Odd_Even += Pin(num="6", name="p6", func=Pin.types.PASSIVE)
tmpl_Connector_Generic_Conn_02x04_Odd_Even += Pin(num="7", name="p7", func=Pin.types.PASSIVE)
tmpl_Connector_Generic_Conn_02x04_Odd_Even += Pin(num="8", name="p8", func=Pin.types.PASSIVE)
tmpl_Connector_Generic_Conn_02x04_Odd_Even.ref_prefix = "J"
tigard_lib += tmpl_Connector_Generic_Conn_02x04_Odd_Even

# Connector_Generic:Conn_02x05_Odd_Even
tmpl_Connector_Generic_Conn_02x05_Odd_Even = Part(name="Conn_02x05_Odd_Even", dest=SKIDL, tool=SKIDL)
tmpl_Connector_Generic_Conn_02x05_Odd_Even += Pin(num="1", name="p1", func=Pin.types.PASSIVE)
tmpl_Connector_Generic_Conn_02x05_Odd_Even += Pin(num="2", name="p2", func=Pin.types.PASSIVE)
tmpl_Connector_Generic_Conn_02x05_Odd_Even += Pin(num="3", name="p3", func=Pin.types.PASSIVE)
tmpl_Connector_Generic_Conn_02x05_Odd_Even += Pin(num="4", name="p4", func=Pin.types.PASSIVE)
tmpl_Connector_Generic_Conn_02x05_Odd_Even += Pin(num="5", name="p5", func=Pin.types.PASSIVE)
tmpl_Connector_Generic_Conn_02x05_Odd_Even += Pin(num="6", name="p6", func=Pin.types.PASSIVE)
tmpl_Connector_Generic_Conn_02x05_Odd_Even += Pin(num="7", name="p7", func=Pin.types.PASSIVE)
tmpl_Connector_Generic_Conn_02x05_Odd_Even += Pin(num="8", name="p8", func=Pin.types.PASSIVE)
tmpl_Connector_Generic_Conn_02x05_Odd_Even += Pin(num="9", name="p9", func=Pin.types.PASSIVE)
tmpl_Connector_Generic_Conn_02x05_Odd_Even += Pin(num="10", name="p10", func=Pin.types.PASSIVE)
tmpl_Connector_Generic_Conn_02x05_Odd_Even.ref_prefix = "J"
tigard_lib += tmpl_Connector_Generic_Conn_02x05_Odd_Even

# Connector_Generic:Conn_02x07_Odd_Even
tmpl_Connector_Generic_Conn_02x07_Odd_Even = Part(name="Conn_02x07_Odd_Even", dest=SKIDL, tool=SKIDL)
tmpl_Connector_Generic_Conn_02x07_Odd_Even += Pin(num="1", name="p1", func=Pin.types.PASSIVE)
tmpl_Connector_Generic_Conn_02x07_Odd_Even += Pin(num="2", name="p2", func=Pin.types.PASSIVE)
tmpl_Connector_Generic_Conn_02x07_Odd_Even += Pin(num="3", name="p3", func=Pin.types.PASSIVE)
tmpl_Connector_Generic_Conn_02x07_Odd_Even += Pin(num="4", name="p4", func=Pin.types.PASSIVE)
tmpl_Connector_Generic_Conn_02x07_Odd_Even += Pin(num="5", name="p5", func=Pin.types.PASSIVE)
tmpl_Connector_Generic_Conn_02x07_Odd_Even += Pin(num="6", name="p6", func=Pin.types.PASSIVE)
tmpl_Connector_Generic_Conn_02x07_Odd_Even += Pin(num="7", name="p7", func=Pin.types.PASSIVE)
tmpl_Connector_Generic_Conn_02x07_Odd_Even += Pin(num="8", name="p8", func=Pin.types.PASSIVE)
tmpl_Connector_Generic_Conn_02x07_Odd_Even += Pin(num="9", name="p9", func=Pin.types.PASSIVE)
tmpl_Connector_Generic_Conn_02x07_Odd_Even += Pin(num="10", name="p10", func=Pin.types.PASSIVE)
tmpl_Connector_Generic_Conn_02x07_Odd_Even += Pin(num="11", name="p11", func=Pin.types.PASSIVE)
tmpl_Connector_Generic_Conn_02x07_Odd_Even += Pin(num="12", name="p12", func=Pin.types.PASSIVE)
tmpl_Connector_Generic_Conn_02x07_Odd_Even += Pin(num="13", name="p13", func=Pin.types.PASSIVE)
tmpl_Connector_Generic_Conn_02x07_Odd_Even += Pin(num="14", name="p14", func=Pin.types.PASSIVE)
tmpl_Connector_Generic_Conn_02x07_Odd_Even.ref_prefix = "J"
tigard_lib += tmpl_Connector_Generic_Conn_02x07_Odd_Even

# Connector_Generic_MountingPin:Conn_01x04_MountingPin
tmpl_Connector_Generic_MountingPin_Conn_01x04_MountingPin = Part(name="Conn_01x04_MountingPin", dest=SKIDL, tool=SKIDL)
tmpl_Connector_Generic_MountingPin_Conn_01x04_MountingPin += Pin(num="1", name="p1", func=Pin.types.PASSIVE)
tmpl_Connector_Generic_MountingPin_Conn_01x04_MountingPin += Pin(num="2", name="p2", func=Pin.types.PASSIVE)
tmpl_Connector_Generic_MountingPin_Conn_01x04_MountingPin += Pin(num="3", name="p3", func=Pin.types.PASSIVE)
tmpl_Connector_Generic_MountingPin_Conn_01x04_MountingPin += Pin(num="4", name="p4", func=Pin.types.PASSIVE)
tmpl_Connector_Generic_MountingPin_Conn_01x04_MountingPin += Pin(num="MP", name="pMP", func=Pin.types.PASSIVE)
tmpl_Connector_Generic_MountingPin_Conn_01x04_MountingPin.ref_prefix = "J"
tigard_lib += tmpl_Connector_Generic_MountingPin_Conn_01x04_MountingPin

# Device:C_Small
tmpl_Device_C_Small = Part(name="C_Small", dest=SKIDL, tool=SKIDL)
tmpl_Device_C_Small += Pin(num="1", name="p1", func=Pin.types.PASSIVE)
tmpl_Device_C_Small += Pin(num="2", name="p2", func=Pin.types.PASSIVE)
tmpl_Device_C_Small.ref_prefix = "C"
tigard_lib += tmpl_Device_C_Small

# Device:Crystal_GND24
tmpl_Device_Crystal_GND24 = Part(name="Crystal_GND24", dest=SKIDL, tool=SKIDL)
tmpl_Device_Crystal_GND24 += Pin(num="1", name="p1", func=Pin.types.PASSIVE)
tmpl_Device_Crystal_GND24 += Pin(num="2", name="p2", func=Pin.types.PASSIVE)
tmpl_Device_Crystal_GND24 += Pin(num="3", name="p3", func=Pin.types.PASSIVE)
tmpl_Device_Crystal_GND24 += Pin(num="4", name="p4", func=Pin.types.PASSIVE)
tmpl_Device_Crystal_GND24.ref_prefix = "Y"
tigard_lib += tmpl_Device_Crystal_GND24

# Device:Ferrite_Bead_Small
tmpl_Device_Ferrite_Bead_Small = Part(name="Ferrite_Bead_Small", dest=SKIDL, tool=SKIDL)
tmpl_Device_Ferrite_Bead_Small += Pin(num="1", name="p1", func=Pin.types.PASSIVE)
tmpl_Device_Ferrite_Bead_Small += Pin(num="2", name="p2", func=Pin.types.PASSIVE)
tmpl_Device_Ferrite_Bead_Small.ref_prefix = "FB"
tigard_lib += tmpl_Device_Ferrite_Bead_Small

# Device:Jumper_NC_Small
tmpl_Device_Jumper_NC_Small = Part(name="Jumper_NC_Small", dest=SKIDL, tool=SKIDL)
tmpl_Device_Jumper_NC_Small += Pin(num="1", name="p1", func=Pin.types.PASSIVE)
tmpl_Device_Jumper_NC_Small += Pin(num="2", name="p2", func=Pin.types.PASSIVE)
tmpl_Device_Jumper_NC_Small.ref_prefix = "JP"
tigard_lib += tmpl_Device_Jumper_NC_Small

# Device:Jumper_NO_Small
tmpl_Device_Jumper_NO_Small = Part(name="Jumper_NO_Small", dest=SKIDL, tool=SKIDL)
tmpl_Device_Jumper_NO_Small += Pin(num="1", name="p1", func=Pin.types.PASSIVE)
tmpl_Device_Jumper_NO_Small += Pin(num="2", name="p2", func=Pin.types.PASSIVE)
tmpl_Device_Jumper_NO_Small.ref_prefix = "JP"
tigard_lib += tmpl_Device_Jumper_NO_Small

# Device:LED
tmpl_Device_LED = Part(name="LED", dest=SKIDL, tool=SKIDL)
tmpl_Device_LED += Pin(num="1", name="p1", func=Pin.types.PASSIVE)
tmpl_Device_LED += Pin(num="2", name="p2", func=Pin.types.PASSIVE)
tmpl_Device_LED.ref_prefix = "D"
tigard_lib += tmpl_Device_LED

# Device:LED_Small
tmpl_Device_LED_Small = Part(name="LED_Small", dest=SKIDL, tool=SKIDL)
tmpl_Device_LED_Small += Pin(num="1", name="p1", func=Pin.types.PASSIVE)
tmpl_Device_LED_Small += Pin(num="2", name="p2", func=Pin.types.PASSIVE)
tmpl_Device_LED_Small.ref_prefix = "D"
tigard_lib += tmpl_Device_LED_Small

# Device:Q_NMOS_GSD
tmpl_Device_Q_NMOS_GSD = Part(name="Q_NMOS_GSD", dest=SKIDL, tool=SKIDL)
tmpl_Device_Q_NMOS_GSD += Pin(num="1", name="p1", func=Pin.types.PASSIVE)
tmpl_Device_Q_NMOS_GSD += Pin(num="2", name="p2", func=Pin.types.PASSIVE)
tmpl_Device_Q_NMOS_GSD += Pin(num="3", name="p3", func=Pin.types.PASSIVE)
tmpl_Device_Q_NMOS_GSD.ref_prefix = "Q"
tigard_lib += tmpl_Device_Q_NMOS_GSD

# Device:R
tmpl_Device_R = Part(name="R", dest=SKIDL, tool=SKIDL)
tmpl_Device_R += Pin(num="1", name="p1", func=Pin.types.PASSIVE)
tmpl_Device_R += Pin(num="2", name="p2", func=Pin.types.PASSIVE)
tmpl_Device_R.ref_prefix = "R"
tigard_lib += tmpl_Device_R

# Device:R_Pack04
tmpl_Device_R_Pack04 = Part(name="R_Pack04", dest=SKIDL, tool=SKIDL)
tmpl_Device_R_Pack04 += Pin(num="1", name="p1", func=Pin.types.PASSIVE)
tmpl_Device_R_Pack04 += Pin(num="2", name="p2", func=Pin.types.PASSIVE)
tmpl_Device_R_Pack04 += Pin(num="3", name="p3", func=Pin.types.PASSIVE)
tmpl_Device_R_Pack04 += Pin(num="4", name="p4", func=Pin.types.PASSIVE)
tmpl_Device_R_Pack04 += Pin(num="5", name="p5", func=Pin.types.PASSIVE)
tmpl_Device_R_Pack04 += Pin(num="6", name="p6", func=Pin.types.PASSIVE)
tmpl_Device_R_Pack04 += Pin(num="7", name="p7", func=Pin.types.PASSIVE)
tmpl_Device_R_Pack04 += Pin(num="8", name="p8", func=Pin.types.PASSIVE)
tmpl_Device_R_Pack04.ref_prefix = "RN"
tigard_lib += tmpl_Device_R_Pack04

# Device:R_Small
tmpl_Device_R_Small = Part(name="R_Small", dest=SKIDL, tool=SKIDL)
tmpl_Device_R_Small += Pin(num="1", name="p1", func=Pin.types.PASSIVE)
tmpl_Device_R_Small += Pin(num="2", name="p2", func=Pin.types.PASSIVE)
tmpl_Device_R_Small.ref_prefix = "R"
tigard_lib += tmpl_Device_R_Small

# Interface_USB:FT2232HQ
tmpl_Interface_USB_FT2232HQ = Part(name="FT2232HQ", dest=SKIDL, tool=SKIDL)
tmpl_Interface_USB_FT2232HQ += Pin(num="1", name="p1", func=Pin.types.PASSIVE)
tmpl_Interface_USB_FT2232HQ += Pin(num="2", name="p2", func=Pin.types.PASSIVE)
tmpl_Interface_USB_FT2232HQ += Pin(num="3", name="p3", func=Pin.types.PASSIVE)
tmpl_Interface_USB_FT2232HQ += Pin(num="4", name="p4", func=Pin.types.PASSIVE)
tmpl_Interface_USB_FT2232HQ += Pin(num="5", name="p5", func=Pin.types.PASSIVE)
tmpl_Interface_USB_FT2232HQ += Pin(num="6", name="p6", func=Pin.types.PASSIVE)
tmpl_Interface_USB_FT2232HQ += Pin(num="7", name="p7", func=Pin.types.PASSIVE)
tmpl_Interface_USB_FT2232HQ += Pin(num="8", name="p8", func=Pin.types.PASSIVE)
tmpl_Interface_USB_FT2232HQ += Pin(num="9", name="p9", func=Pin.types.PASSIVE)
tmpl_Interface_USB_FT2232HQ += Pin(num="10", name="p10", func=Pin.types.PASSIVE)
tmpl_Interface_USB_FT2232HQ += Pin(num="11", name="p11", func=Pin.types.PASSIVE)
tmpl_Interface_USB_FT2232HQ += Pin(num="12", name="p12", func=Pin.types.PASSIVE)
tmpl_Interface_USB_FT2232HQ += Pin(num="13", name="p13", func=Pin.types.PASSIVE)
tmpl_Interface_USB_FT2232HQ += Pin(num="14", name="p14", func=Pin.types.PASSIVE)
tmpl_Interface_USB_FT2232HQ += Pin(num="15", name="p15", func=Pin.types.PASSIVE)
tmpl_Interface_USB_FT2232HQ += Pin(num="16", name="p16", func=Pin.types.PASSIVE)
tmpl_Interface_USB_FT2232HQ += Pin(num="17", name="p17", func=Pin.types.PASSIVE)
tmpl_Interface_USB_FT2232HQ += Pin(num="18", name="p18", func=Pin.types.PASSIVE)
tmpl_Interface_USB_FT2232HQ += Pin(num="19", name="p19", func=Pin.types.PASSIVE)
tmpl_Interface_USB_FT2232HQ += Pin(num="20", name="p20", func=Pin.types.PASSIVE)
tmpl_Interface_USB_FT2232HQ += Pin(num="21", name="p21", func=Pin.types.PASSIVE)
tmpl_Interface_USB_FT2232HQ += Pin(num="22", name="p22", func=Pin.types.PASSIVE)
tmpl_Interface_USB_FT2232HQ += Pin(num="23", name="p23", func=Pin.types.PASSIVE)
tmpl_Interface_USB_FT2232HQ += Pin(num="24", name="p24", func=Pin.types.PASSIVE)
tmpl_Interface_USB_FT2232HQ += Pin(num="25", name="p25", func=Pin.types.PASSIVE)
tmpl_Interface_USB_FT2232HQ += Pin(num="26", name="p26", func=Pin.types.PASSIVE)
tmpl_Interface_USB_FT2232HQ += Pin(num="27", name="p27", func=Pin.types.PASSIVE)
tmpl_Interface_USB_FT2232HQ += Pin(num="28", name="p28", func=Pin.types.PASSIVE)
tmpl_Interface_USB_FT2232HQ += Pin(num="29", name="p29", func=Pin.types.PASSIVE)
tmpl_Interface_USB_FT2232HQ += Pin(num="30", name="p30", func=Pin.types.PASSIVE)
tmpl_Interface_USB_FT2232HQ += Pin(num="31", name="p31", func=Pin.types.PASSIVE)
tmpl_Interface_USB_FT2232HQ += Pin(num="32", name="p32", func=Pin.types.PASSIVE)
tmpl_Interface_USB_FT2232HQ += Pin(num="33", name="p33", func=Pin.types.PASSIVE)
tmpl_Interface_USB_FT2232HQ += Pin(num="34", name="p34", func=Pin.types.PASSIVE)
tmpl_Interface_USB_FT2232HQ += Pin(num="35", name="p35", func=Pin.types.PASSIVE)
tmpl_Interface_USB_FT2232HQ += Pin(num="36", name="p36", func=Pin.types.PASSIVE)
tmpl_Interface_USB_FT2232HQ += Pin(num="37", name="p37", func=Pin.types.PASSIVE)
tmpl_Interface_USB_FT2232HQ += Pin(num="38", name="p38", func=Pin.types.PASSIVE)
tmpl_Interface_USB_FT2232HQ += Pin(num="39", name="p39", func=Pin.types.PASSIVE)
tmpl_Interface_USB_FT2232HQ += Pin(num="40", name="p40", func=Pin.types.PASSIVE)
tmpl_Interface_USB_FT2232HQ += Pin(num="41", name="p41", func=Pin.types.PASSIVE)
tmpl_Interface_USB_FT2232HQ += Pin(num="42", name="p42", func=Pin.types.PASSIVE)
tmpl_Interface_USB_FT2232HQ += Pin(num="43", name="p43", func=Pin.types.PASSIVE)
tmpl_Interface_USB_FT2232HQ += Pin(num="44", name="p44", func=Pin.types.PASSIVE)
tmpl_Interface_USB_FT2232HQ += Pin(num="45", name="p45", func=Pin.types.PASSIVE)
tmpl_Interface_USB_FT2232HQ += Pin(num="46", name="p46", func=Pin.types.PASSIVE)
tmpl_Interface_USB_FT2232HQ += Pin(num="47", name="p47", func=Pin.types.PASSIVE)
tmpl_Interface_USB_FT2232HQ += Pin(num="48", name="p48", func=Pin.types.PASSIVE)
tmpl_Interface_USB_FT2232HQ += Pin(num="49", name="p49", func=Pin.types.PASSIVE)
tmpl_Interface_USB_FT2232HQ += Pin(num="50", name="p50", func=Pin.types.PASSIVE)
tmpl_Interface_USB_FT2232HQ += Pin(num="51", name="p51", func=Pin.types.PASSIVE)
tmpl_Interface_USB_FT2232HQ += Pin(num="52", name="p52", func=Pin.types.PASSIVE)
tmpl_Interface_USB_FT2232HQ += Pin(num="53", name="p53", func=Pin.types.PASSIVE)
tmpl_Interface_USB_FT2232HQ += Pin(num="54", name="p54", func=Pin.types.PASSIVE)
tmpl_Interface_USB_FT2232HQ += Pin(num="55", name="p55", func=Pin.types.PASSIVE)
tmpl_Interface_USB_FT2232HQ += Pin(num="56", name="p56", func=Pin.types.PASSIVE)
tmpl_Interface_USB_FT2232HQ += Pin(num="57", name="p57", func=Pin.types.PASSIVE)
tmpl_Interface_USB_FT2232HQ += Pin(num="58", name="p58", func=Pin.types.PASSIVE)
tmpl_Interface_USB_FT2232HQ += Pin(num="59", name="p59", func=Pin.types.PASSIVE)
tmpl_Interface_USB_FT2232HQ += Pin(num="60", name="p60", func=Pin.types.PASSIVE)
tmpl_Interface_USB_FT2232HQ += Pin(num="61", name="p61", func=Pin.types.PASSIVE)
tmpl_Interface_USB_FT2232HQ += Pin(num="62", name="p62", func=Pin.types.PASSIVE)
tmpl_Interface_USB_FT2232HQ += Pin(num="63", name="p63", func=Pin.types.PASSIVE)
tmpl_Interface_USB_FT2232HQ += Pin(num="64", name="p64", func=Pin.types.PASSIVE)
tmpl_Interface_USB_FT2232HQ += Pin(num="65", name="p65", func=Pin.types.PASSIVE)
tmpl_Interface_USB_FT2232HQ.ref_prefix = "U"
tigard_lib += tmpl_Interface_USB_FT2232HQ

# Mechanical:MountingHole
tmpl_Mechanical_MountingHole = Part(name="MountingHole", dest=SKIDL, tool=SKIDL)
tmpl_Mechanical_MountingHole += Pin(num="1", name="pad", func=Pin.types.PASSIVE)
tmpl_Mechanical_MountingHole.ref_prefix = "H"
tigard_lib += tmpl_Mechanical_MountingHole

# Memory_EEPROM:93LCxxBxxOT
tmpl_Memory_EEPROM_93LCxxBxxOT = Part(name="93LCxxBxxOT", dest=SKIDL, tool=SKIDL)
tmpl_Memory_EEPROM_93LCxxBxxOT += Pin(num="1", name="p1", func=Pin.types.PASSIVE)
tmpl_Memory_EEPROM_93LCxxBxxOT += Pin(num="2", name="p2", func=Pin.types.PASSIVE)
tmpl_Memory_EEPROM_93LCxxBxxOT += Pin(num="3", name="p3", func=Pin.types.PASSIVE)
tmpl_Memory_EEPROM_93LCxxBxxOT += Pin(num="4", name="p4", func=Pin.types.PASSIVE)
tmpl_Memory_EEPROM_93LCxxBxxOT += Pin(num="5", name="p5", func=Pin.types.PASSIVE)
tmpl_Memory_EEPROM_93LCxxBxxOT += Pin(num="6", name="p6", func=Pin.types.PASSIVE)
tmpl_Memory_EEPROM_93LCxxBxxOT.ref_prefix = "U"
tigard_lib += tmpl_Memory_EEPROM_93LCxxBxxOT

# tigard:AP7365-18
tmpl_tigard_AP7365_18 = Part(name="AP7365-18", dest=SKIDL, tool=SKIDL)
tmpl_tigard_AP7365_18 += Pin(num="1", name="p1", func=Pin.types.PASSIVE)
tmpl_tigard_AP7365_18 += Pin(num="2", name="p2", func=Pin.types.PASSIVE)
tmpl_tigard_AP7365_18 += Pin(num="3", name="p3", func=Pin.types.PASSIVE)
tmpl_tigard_AP7365_18 += Pin(num="4", name="p4", func=Pin.types.PASSIVE)
tmpl_tigard_AP7365_18 += Pin(num="5", name="p5", func=Pin.types.PASSIVE)
tmpl_tigard_AP7365_18.ref_prefix = "U"
tigard_lib += tmpl_tigard_AP7365_18

# tigard:AP7365-33
tmpl_tigard_AP7365_33 = Part(name="AP7365-33", dest=SKIDL, tool=SKIDL)
tmpl_tigard_AP7365_33 += Pin(num="1", name="p1", func=Pin.types.PASSIVE)
tmpl_tigard_AP7365_33 += Pin(num="2", name="p2", func=Pin.types.PASSIVE)
tmpl_tigard_AP7365_33 += Pin(num="3", name="p3", func=Pin.types.PASSIVE)
tmpl_tigard_AP7365_33 += Pin(num="4", name="p4", func=Pin.types.PASSIVE)
tmpl_tigard_AP7365_33 += Pin(num="5", name="p5", func=Pin.types.PASSIVE)
tmpl_tigard_AP7365_33.ref_prefix = "U"
tigard_lib += tmpl_tigard_AP7365_33

# tigard:SN74LVC8T245
tmpl_tigard_SN74LVC8T245 = Part(name="SN74LVC8T245", dest=SKIDL, tool=SKIDL)
tmpl_tigard_SN74LVC8T245 += Pin(num="1", name="p1", func=Pin.types.PASSIVE)
tmpl_tigard_SN74LVC8T245 += Pin(num="2", name="p2", func=Pin.types.PASSIVE)
tmpl_tigard_SN74LVC8T245 += Pin(num="3", name="p3", func=Pin.types.PASSIVE)
tmpl_tigard_SN74LVC8T245 += Pin(num="4", name="p4", func=Pin.types.PASSIVE)
tmpl_tigard_SN74LVC8T245 += Pin(num="5", name="p5", func=Pin.types.PASSIVE)
tmpl_tigard_SN74LVC8T245 += Pin(num="6", name="p6", func=Pin.types.PASSIVE)
tmpl_tigard_SN74LVC8T245 += Pin(num="7", name="p7", func=Pin.types.PASSIVE)
tmpl_tigard_SN74LVC8T245 += Pin(num="8", name="p8", func=Pin.types.PASSIVE)
tmpl_tigard_SN74LVC8T245 += Pin(num="9", name="p9", func=Pin.types.PASSIVE)
tmpl_tigard_SN74LVC8T245 += Pin(num="10", name="p10", func=Pin.types.PASSIVE)
tmpl_tigard_SN74LVC8T245 += Pin(num="11", name="p11", func=Pin.types.PASSIVE)
tmpl_tigard_SN74LVC8T245 += Pin(num="12", name="p12", func=Pin.types.PASSIVE)
tmpl_tigard_SN74LVC8T245 += Pin(num="13", name="p13", func=Pin.types.PASSIVE)
tmpl_tigard_SN74LVC8T245 += Pin(num="14", name="p14", func=Pin.types.PASSIVE)
tmpl_tigard_SN74LVC8T245 += Pin(num="15", name="p15", func=Pin.types.PASSIVE)
tmpl_tigard_SN74LVC8T245 += Pin(num="16", name="p16", func=Pin.types.PASSIVE)
tmpl_tigard_SN74LVC8T245 += Pin(num="17", name="p17", func=Pin.types.PASSIVE)
tmpl_tigard_SN74LVC8T245 += Pin(num="18", name="p18", func=Pin.types.PASSIVE)
tmpl_tigard_SN74LVC8T245 += Pin(num="19", name="p19", func=Pin.types.PASSIVE)
tmpl_tigard_SN74LVC8T245 += Pin(num="20", name="p20", func=Pin.types.PASSIVE)
tmpl_tigard_SN74LVC8T245 += Pin(num="21", name="p21", func=Pin.types.PASSIVE)
tmpl_tigard_SN74LVC8T245 += Pin(num="22", name="p22", func=Pin.types.PASSIVE)
tmpl_tigard_SN74LVC8T245 += Pin(num="23", name="p23", func=Pin.types.PASSIVE)
tmpl_tigard_SN74LVC8T245 += Pin(num="24", name="p24", func=Pin.types.PASSIVE)
tmpl_tigard_SN74LVC8T245.ref_prefix = "U"
tigard_lib += tmpl_tigard_SN74LVC8T245

# tigard:SW_DP4T
tmpl_tigard_SW_DP4T = Part(name="SW_DP4T", dest=SKIDL, tool=SKIDL)
tmpl_tigard_SW_DP4T += Pin(num="1", name="p1", func=Pin.types.PASSIVE)
tmpl_tigard_SW_DP4T += Pin(num="2", name="p2", func=Pin.types.PASSIVE)
tmpl_tigard_SW_DP4T += Pin(num="3", name="p3", func=Pin.types.PASSIVE)
tmpl_tigard_SW_DP4T += Pin(num="4", name="p4", func=Pin.types.PASSIVE)
tmpl_tigard_SW_DP4T += Pin(num="5", name="p5", func=Pin.types.PASSIVE)
tmpl_tigard_SW_DP4T += Pin(num="6", name="p6", func=Pin.types.PASSIVE)
tmpl_tigard_SW_DP4T += Pin(num="7", name="p7", func=Pin.types.PASSIVE)
tmpl_tigard_SW_DP4T += Pin(num="8", name="p8", func=Pin.types.PASSIVE)
tmpl_tigard_SW_DP4T += Pin(num="9", name="p9", func=Pin.types.PASSIVE)
tmpl_tigard_SW_DP4T += Pin(num="10", name="p10", func=Pin.types.PASSIVE)
tmpl_tigard_SW_DP4T.ref_prefix = "SW"
tigard_lib += tmpl_tigard_SW_DP4T

# tigard:SW_DPDT
tmpl_tigard_SW_DPDT = Part(name="SW_DPDT", dest=SKIDL, tool=SKIDL)
tmpl_tigard_SW_DPDT += Pin(num="1", name="p1", func=Pin.types.PASSIVE)
tmpl_tigard_SW_DPDT += Pin(num="2", name="p2", func=Pin.types.PASSIVE)
tmpl_tigard_SW_DPDT += Pin(num="3", name="p3", func=Pin.types.PASSIVE)
tmpl_tigard_SW_DPDT += Pin(num="4", name="p4", func=Pin.types.PASSIVE)
tmpl_tigard_SW_DPDT += Pin(num="5", name="p5", func=Pin.types.PASSIVE)
tmpl_tigard_SW_DPDT += Pin(num="6", name="p6", func=Pin.types.PASSIVE)
tmpl_tigard_SW_DPDT.ref_prefix = "SW"
tigard_lib += tmpl_tigard_SW_DPDT

# ============================================================
# Nets
# ============================================================
net_P1V8 = Net("+1V8")
net_P3V3 = Net("+3V3")
net_P5V = Net("+5V")
net_AD0 = Net("AD0")
net_AD1 = Net("AD1")
net_AD2 = Net("AD2")
net_AD3 = Net("AD3")
net_AD4 = Net("AD4")
net_AD5 = Net("AD5")
net_AD6 = Net("AD6")
net_BD0 = Net("BD0")
net_BD1 = Net("BD1")
net_BD2 = Net("BD2")
net_BD3 = Net("BD3")
net_BD4 = Net("BD4")
net_BD6 = Net("BD6")
net_CIPO = Net("CIPO")
net_COPI = Net("COPI")
net_CORTEX_PIN2 = Net("CORTEX_PIN2")
net_CS = Net("CS")
net_DI = Net("DI")
net_DO = Net("DO")
net_EECLK = Net("EECLK")
net_EECS = Net("EECS")
net_EEDATA = Net("EEDATA")
net_GND = Net("GND")
net_ICE_CDONE = Net("ICE_CDONE")
net_Net_1 = Net("Net_1")
net_Net_10 = Net("Net_10")
net_Net_11 = Net("Net_11")
net_Net_12 = Net("Net_12")
net_Net_13 = Net("Net_13")
net_Net_14 = Net("Net_14")
net_Net_15 = Net("Net_15")
net_Net_16 = Net("Net_16")
net_Net_17 = Net("Net_17")
net_Net_18 = Net("Net_18")
net_Net_19 = Net("Net_19")
net_Net_2 = Net("Net_2")
net_Net_20 = Net("Net_20")
net_Net_21 = Net("Net_21")
net_Net_22 = Net("Net_22")
net_Net_23 = Net("Net_23")
net_Net_24 = Net("Net_24")
net_Net_25 = Net("Net_25")
net_Net_26 = Net("Net_26")
net_Net_27 = Net("Net_27")
net_Net_28 = Net("Net_28")
net_Net_29 = Net("Net_29")
net_Net_3 = Net("Net_3")
net_Net_30 = Net("Net_30")
net_Net_31 = Net("Net_31")
net_Net_32 = Net("Net_32")
net_Net_33 = Net("Net_33")
net_Net_34 = Net("Net_34")
net_Net_35 = Net("Net_35")
net_Net_36 = Net("Net_36")
net_Net_37 = Net("Net_37")
net_Net_38 = Net("Net_38")
net_Net_39 = Net("Net_39")
net_Net_4 = Net("Net_4")
net_Net_40 = Net("Net_40")
net_Net_41 = Net("Net_41")
net_Net_42 = Net("Net_42")
net_Net_43 = Net("Net_43")
net_Net_44 = Net("Net_44")
net_Net_45 = Net("Net_45")
net_Net_46 = Net("Net_46")
net_Net_47 = Net("Net_47")
net_Net_48 = Net("Net_48")
net_Net_49 = Net("Net_49")
net_Net_5 = Net("Net_5")
net_Net_50 = Net("Net_50")
net_Net_51 = Net("Net_51")
net_Net_52 = Net("Net_52")
net_Net_53 = Net("Net_53")
net_Net_54 = Net("Net_54")
net_Net_55 = Net("Net_55")
net_Net_56 = Net("Net_56")
net_Net_57 = Net("Net_57")
net_Net_58 = Net("Net_58")
net_Net_59 = Net("Net_59")
net_Net_6 = Net("Net_6")
net_Net_60 = Net("Net_60")
net_Net_61 = Net("Net_61")
net_Net_62 = Net("Net_62")
net_Net_63 = Net("Net_63")
net_Net_64 = Net("Net_64")
net_Net_65 = Net("Net_65")
net_Net_66 = Net("Net_66")
net_Net_67 = Net("Net_67")
net_Net_68 = Net("Net_68")
net_Net_69 = Net("Net_69")
net_Net_7 = Net("Net_7")
net_Net_70 = Net("Net_70")
net_Net_71 = Net("Net_71")
net_Net_72 = Net("Net_72")
net_Net_73 = Net("Net_73")
net_Net_74 = Net("Net_74")
net_Net_75 = Net("Net_75")
net_Net_76 = Net("Net_76")
net_Net_77 = Net("Net_77")
net_Net_78 = Net("Net_78")
net_Net_79 = Net("Net_79")
net_Net_8 = Net("Net_8")
net_Net_80 = Net("Net_80")
net_Net_81 = Net("Net_81")
net_Net_82 = Net("Net_82")
net_Net_83 = Net("Net_83")
net_Net_84 = Net("Net_84")
net_Net_85 = Net("Net_85")
net_Net_86 = Net("Net_86")
net_Net_87 = Net("Net_87")
net_Net_88 = Net("Net_88")
net_Net_89 = Net("Net_89")
net_Net_9 = Net("Net_9")
net_Net_90 = Net("Net_90")
net_Net_91 = Net("Net_91")
net_Net_92 = Net("Net_92")
net_Net_93 = Net("Net_93")
net_Net_94 = Net("Net_94")
net_PWR_FLAG = Net("PWR_FLAG")
net_SWDIO = Net("SWDIO")
net_TCK = Net("TCK")
net_TDI = Net("TDI")
net_TDO = Net("TDO")
net_TMS = Net("TMS")
net_UART_TX = Net("UART_TX")
net_USB_DN = Net("USB_DN")
net_USB_DP = Net("USB_DP")
net_VREF = Net("VREF")
net_VREG = Net("VREG")
net_VTARGET = Net("VTARGET")
net_xPB0 = Net("xPB0")
net_xPB1 = Net("xPB1")
net_xPB2 = Net("xPB2")
net_xPB3 = Net("xPB3")
net_xPB4 = Net("xPB4")
net_xPB5 = Net("xPB5")
net_xPB6 = Net("xPB6")
net_xPB7 = Net("xPB7")
net_n_ENABLE = Net("~ENABLE")
net_n_SRST = Net("~SRST")
net_n_TRST = Net("~TRST")
net_n_UART_CTS = Net("~UART_CTS")
net_n_UART_DCD = Net("~UART_DCD")
net_n_UART_DSR = Net("~UART_DSR")
net_n_UART_DTR = Net("~UART_DTR")
net_n_UART_RTS = Net("~UART_RTS")

# ============================================================
# Components
# ============================================================

# C1 - 2u2
C1 = Part(lib=tigard_lib, name="C_Small", ref="C1",
    value="2u2", footprint="Capacitor_SMD:C_0402_1005Metric")
net_P5V += C1["1"]
net_GND += C1["2"]

# C10 - 2u2
C10 = Part(lib=tigard_lib, name="C_Small", ref="C10",
    value="2u2", footprint="Capacitor_SMD:C_0402_1005Metric")
net_VREG += C10["1"]
net_GND += C10["2"]

# C11 - 100n
C11 = Part(lib=tigard_lib, name="C_Small", ref="C11",
    value="100n", footprint="Capacitor_SMD:C_0402_1005Metric")
net_VREG += C11["1"]
net_GND += C11["2"]

# C12 - 100n
C12 = Part(lib=tigard_lib, name="C_Small", ref="C12",
    value="100n", footprint="Capacitor_SMD:C_0402_1005Metric")
net_VREG += C12["1"]
net_GND += C12["2"]

# C13 - 100n
C13 = Part(lib=tigard_lib, name="C_Small", ref="C13",
    value="100n", footprint="Capacitor_SMD:C_0402_1005Metric")
net_VREG += C13["1"]
net_GND += C13["2"]

# C14 - 100n
C14 = Part(lib=tigard_lib, name="C_Small", ref="C14",
    value="100n", footprint="Capacitor_SMD:C_0402_1005Metric")
net_P3V3 += C14["1"]
net_GND += C14["2"]

# C15 - 100n
C15 = Part(lib=tigard_lib, name="C_Small", ref="C15",
    value="100n", footprint="Capacitor_SMD:C_0402_1005Metric")
net_P3V3 += C15["1"]
net_GND += C15["2"]

# C16 - 100n
C16 = Part(lib=tigard_lib, name="C_Small", ref="C16",
    value="100n", footprint="Capacitor_SMD:C_0402_1005Metric")
net_P3V3 += C16["1"]
net_GND += C16["2"]

# C17 - 100n
C17 = Part(lib=tigard_lib, name="C_Small", ref="C17",
    value="100n", footprint="Capacitor_SMD:C_0402_1005Metric")
net_P3V3 += C17["1"]
net_GND += C17["2"]

# C18 - 100n
C18 = Part(lib=tigard_lib, name="C_Small", ref="C18",
    value="100n", footprint="Capacitor_SMD:C_0402_1005Metric")
net_P3V3 += C18["1"]
net_GND += C18["2"]

# C19 - 100n
C19 = Part(lib=tigard_lib, name="C_Small", ref="C19",
    value="100n", footprint="Capacitor_SMD:C_0402_1005Metric")
net_P3V3 += C19["1"]
net_GND += C19["2"]

# C2 - 2u2
C2 = Part(lib=tigard_lib, name="C_Small", ref="C2",
    value="2u2", footprint="Capacitor_SMD:C_0402_1005Metric")
net_P1V8 += C2["1"]
net_GND += C2["2"]

# C20 - 100n
C20 = Part(lib=tigard_lib, name="C_Small", ref="C20",
    value="100n", footprint="Capacitor_SMD:C_0402_1005Metric")
net_P3V3 += C20["1"]
net_GND += C20["2"]

# C21 - 100n
C21 = Part(lib=tigard_lib, name="C_Small", ref="C21",
    value="100n", footprint="Capacitor_SMD:C_0402_1005Metric")
net_VREF += C21["1"]
net_GND += C21["2"]

# C22 - 100n
C22 = Part(lib=tigard_lib, name="C_Small", ref="C22",
    value="100n", footprint="Capacitor_SMD:C_0402_1005Metric")
net_VREF += C22["1"]
net_GND += C22["2"]

# C23 - 30pF
C23 = Part(lib=tigard_lib, name="C_Small", ref="C23",
    value="30pF", footprint="Capacitor_SMD:C_0402_1005Metric")
net_Net_17 += C23["1"]
net_GND += C23["2"]

# C24 - 30pF
C24 = Part(lib=tigard_lib, name="C_Small", ref="C24",
    value="30pF", footprint="Capacitor_SMD:C_0402_1005Metric")
net_Net_18 += C24["1"]
net_GND += C24["2"]

# C25 - NF
C25 = Part(lib=tigard_lib, name="C_Small", ref="C25",
    value="NF", footprint="Capacitor_SMD:C_0402_1005Metric")
net_GND += C25["1"]
net_Net_77 += C25["2"]

# C26 - 100n
C26 = Part(lib=tigard_lib, name="C_Small", ref="C26",
    value="100n", footprint="Capacitor_SMD:C_0402_1005Metric")
net_PWR_FLAG += C26["1"]
net_GND += C26["2"]

# C3 - 2u2
C3 = Part(lib=tigard_lib, name="C_Small", ref="C3",
    value="2u2", footprint="Capacitor_SMD:C_0402_1005Metric")
net_P5V += C3["1"]
net_GND += C3["2"]

# C4 - 2u2
C4 = Part(lib=tigard_lib, name="C_Small", ref="C4",
    value="2u2", footprint="Capacitor_SMD:C_0402_1005Metric")
net_P3V3 += C4["1"]
net_GND += C4["2"]

# C5 - 100n
C5 = Part(lib=tigard_lib, name="C_Small", ref="C5",
    value="100n", footprint="Capacitor_SMD:C_0402_1005Metric")
net_PWR_FLAG += C5["1"]
net_GND += C5["2"]

# C6 - 2u2
C6 = Part(lib=tigard_lib, name="C_Small", ref="C6",
    value="2u2", footprint="Capacitor_SMD:C_0402_1005Metric")
net_PWR_FLAG += C6["1"]
net_GND += C6["2"]

# C7 - 2u2
C7 = Part(lib=tigard_lib, name="C_Small", ref="C7",
    value="2u2", footprint="Capacitor_SMD:C_0402_1005Metric")
net_Net_20 += C7["1"]
net_GND += C7["2"]

# C8 - 100n
C8 = Part(lib=tigard_lib, name="C_Small", ref="C8",
    value="100n", footprint="Capacitor_SMD:C_0402_1005Metric")
net_Net_20 += C8["1"]
net_GND += C8["2"]

# C9 - 2u2
C9 = Part(lib=tigard_lib, name="C_Small", ref="C9",
    value="2u2", footprint="Capacitor_SMD:C_0402_1005Metric")
net_VREG += C9["1"]
net_GND += C9["2"]

# D1 - YELLOW
D1 = Part(lib=tigard_lib, name="LED", ref="D1",
    value="YELLOW", footprint="LED_SMD:LED_0603_1608Metric")
net_GND += D1["1"]
net_Net_54 += D1["2"]

# D2 - BLUE
D2 = Part(lib=tigard_lib, name="LED", ref="D2",
    value="BLUE", footprint="LED_SMD:LED_0603_1608Metric")
net_Net_12 += D2["1"]
net_Net_13 += D2["2"]

# D3 - GREEN
D3 = Part(lib=tigard_lib, name="LED_Small", ref="D3",
    value="GREEN", footprint="LED_SMD:LED_0603_1608Metric")
net_Net_26 += D3["1"]
net_Net_51 += D3["2"]

# D4 - YELLOW
D4 = Part(lib=tigard_lib, name="LED_Small", ref="D4",
    value="YELLOW", footprint="LED_SMD:LED_0603_1608Metric")
net_Net_27 += D4["1"]
net_Net_52 += D4["2"]

# D5 - GREEN
D5 = Part(lib=tigard_lib, name="LED_Small", ref="D5",
    value="GREEN", footprint="LED_SMD:LED_0603_1608Metric")
net_Net_42 += D5["1"]
net_Net_53 += D5["2"]

# FB1 - 600R, 0.5A
FB1 = Part(lib=tigard_lib, name="Ferrite_Bead_Small", ref="FB1",
    value="600R, 0.5A", footprint="Inductor_SMD:L_0402_1005Metric")
net_P3V3 += FB1["1"]
net_PWR_FLAG += FB1["2"]

# FB2 - 600R, 0.5A
FB2 = Part(lib=tigard_lib, name="Ferrite_Bead_Small", ref="FB2",
    value="600R, 0.5A", footprint="Inductor_SMD:L_0402_1005Metric")
net_P3V3 += FB2["1"]
net_Net_20 += FB2["2"]

# FB3 - 600R, 0.5A
FB3 = Part(lib=tigard_lib, name="Ferrite_Bead_Small", ref="FB3",
    value="600R, 0.5A", footprint="Inductor_SMD:L_0402_1005Metric")
net_PWR_FLAG += FB3["1"]
net_PWR_FLAG += FB3["2"]

# H1 - MountingHole
H1 = Part(lib=tigard_lib, name="MountingHole", ref="H1",
    value="MountingHole", footprint="MountingHole:MountingHole_3.2mm_M3_ISO7380")

# H2 - MountingHole
H2 = Part(lib=tigard_lib, name="MountingHole", ref="H2",
    value="MountingHole", footprint="MountingHole:MountingHole_3.2mm_M3_ISO7380")

# H3 - MountingHole
H3 = Part(lib=tigard_lib, name="MountingHole", ref="H3",
    value="MountingHole", footprint="MountingHole:MountingHole_3.2mm_M3_ISO7380")

# H4 - MountingHole
H4 = Part(lib=tigard_lib, name="MountingHole", ref="H4",
    value="MountingHole", footprint="MountingHole:MountingHole_3.2mm_M3_ISO7380")

# J1 - USB_C_Receptacle_USB2.0
J1 = Part(lib=tigard_lib, name="USB_C_Receptacle_USB2.0", ref="J1",
    value="USB_C_Receptacle_USB2.0", footprint="Connector_USB:USB_C_Receptacle_USB2.0")
net_PWR_FLAG += J1["A1"]
net_Net_1 += J1["A4"]
net_Net_2 += J1["A5"]
net_USB_DN += J1["A6"]
net_USB_DN += J1["A7"]
net_USB_DP += J1["A8"]
net_USB_DP += J1["A9"]
net_Net_4 += J1["B1"]
net_Net_5 += J1["B4"]
net_Net_6 += J1["B5"]
net_USB_DN += J1["B6"]
net_USB_DN += J1["B7"]
net_USB_DP += J1["B8"]
net_USB_DP += J1["B9"]
net_Net_7 += J1["S1"]
net_Net_3 += J1["A12"]
net_Net_3 += J1["B12"]

# J2 - JTAG
J2 = Part(lib=tigard_lib, name="Conn_01x09", ref="J2",
    value="JTAG", footprint="Connector_PinHeader_2.54mm:PinHeader_1x09_P2.54mm_Vertical")
net_VTARGET += J2["1"]
net_GND += J2["2"]
net_TCK += J2["3"]
net_TDI += J2["4"]
net_TDO += J2["5"]
net_TMS += J2["6"]
net_n_TRST += J2["7"]
net_n_SRST += J2["8"]
net_ICE_CDONE += J2["9"]

# J3 - UART
J3 = Part(lib=tigard_lib, name="Conn_01x09", ref="J3",
    value="UART", footprint="Connector_PinHeader_2.54mm:PinHeader_1x09_P2.54mm_Vertical")
net_VTARGET += J3["1"]
net_GND += J3["2"]
net_UART_TX += J3["3"]
net_ICE_CDONE += J3["4"]
net_n_UART_RTS += J3["5"]
net_n_UART_CTS += J3["6"]
net_n_UART_DTR += J3["7"]
net_n_UART_DSR += J3["8"]
net_n_UART_DCD += J3["9"]

# J4 - SPI
J4 = Part(lib=tigard_lib, name="Conn_02x04_Odd_Even", ref="J4",
    value="SPI", footprint="Connector_PinHeader_2.54mm:PinHeader_2x04_P2.54mm_Vertical")
net_CS += J4["1"]
net_VTARGET += J4["2"]
net_CIPO += J4["3"]
net_Net_14 += J4["4"]
net_Net_15 += J4["5"]
net_TCK += J4["6"]
net_GND += J4["7"]
net_COPI += J4["8"]

# J5 - CORTEX
J5 = Part(lib=tigard_lib, name="Conn_02x05_Odd_Even", ref="J5",
    value="CORTEX", footprint="Connector_PinHeader_1.27mm:PinHeader_2x05_P1.27mm_Vertical_SMD")
net_VTARGET += J5["1"]
net_CORTEX_PIN2 += J5["2"]
net_GND += J5["3"]
net_TCK += J5["4"]
net_GND += J5["5"]
net_TDO += J5["6"]
net_Net_16 += J5["7"]
net_TDI += J5["8"]
net_GND += J5["9"]
net_n_SRST += J5["10"]

# J6 - LA
J6 = Part(lib=tigard_lib, name="Conn_02x07_Odd_Even", ref="J6",
    value="LA", footprint="Connector_PinHeader_1.27mm:PinHeader_2x07_P1.27mm_Vertical_SMD")
net_xPB0 += J6["1"]
net_xPB1 += J6["2"]
net_xPB2 += J6["3"]
net_xPB3 += J6["4"]
net_xPB4 += J6["5"]
net_xPB5 += J6["6"]
net_xPB6 += J6["7"]
net_xPB7 += J6["8"]
net_GND += J6["9"]
net_GND += J6["10"]
net_Net_91 += J6["11"]
net_Net_92 += J6["12"]
net_Net_93 += J6["13"]
net_Net_94 += J6["14"]

# J7 - I2C
J7 = Part(lib=tigard_lib, name="Conn_01x04_MountingPin", ref="J7",
    value="I2C", footprint="Connector_JST:JST_SH_SM04B-SRSS-TB_1x04-1MP_P1.00mm_Horizontal")
net_GND += J7["1"]
net_VTARGET += J7["2"]
net_COPI += J7["3"]
net_TCK += J7["4"]
net_GND += J7["MP"]

# JP1 - ISO
JP1 = Part(lib=tigard_lib, name="Jumper_NC_Small", ref="JP1",
    value="ISO", footprint="Jumper:SolderJumper-2_P1.3mm_Bridged_RoundedPad1.0x1.5mm")
net_VTARGET += JP1["1"]
net_VREF += JP1["2"]

# JP2 - HACK
JP2 = Part(lib=tigard_lib, name="Jumper_NO_Small", ref="JP2",
    value="HACK", footprint="Jumper:SolderJumper-2_P1.3mm_Open_RoundedPad1.0x1.5mm")
net_DO += JP2["1"]
net_Net_50 += JP2["2"]

# Q1 - BSH103
Q1 = Part(lib=tigard_lib, name="Q_NMOS_GSD", ref="Q1",
    value="BSH103", footprint="Package_TO_SOT_SMD:SOT-23")
net_VREF += Q1["1"]
net_GND += Q1["2"]
net_Net_12 += Q1["3"]

# R1 - 5k1
R1 = Part(lib=tigard_lib, name="R_Small", ref="R1",
    value="5k1", footprint="Resistor_SMD:R_0402_1005Metric")
net_GND += R1["1"]
net_Net_8 += R1["2"]

# R10 - 10k
R10 = Part(lib=tigard_lib, name="R_Small", ref="R10",
    value="10k", footprint="Resistor_SMD:R_0402_1005Metric")
net_P3V3 += R10["1"]
net_Net_42 += R10["2"]

# R11 - 330
R11 = Part(lib=tigard_lib, name="R_Small", ref="R11",
    value="330", footprint="Resistor_SMD:R_0402_1005Metric")
net_Net_53 += R11["1"]
net_P3V3 += R11["2"]

# R12 - 10k
R12 = Part(lib=tigard_lib, name="R_Small", ref="R12",
    value="10k", footprint="Resistor_SMD:R_0402_1005Metric")
net_P3V3 += R12["1"]
net_EECS += R12["2"]

# R13 - 10k
R13 = Part(lib=tigard_lib, name="R_Small", ref="R13",
    value="10k", footprint="Resistor_SMD:R_0402_1005Metric")
net_P3V3 += R13["1"]
net_Net_43 += R13["2"]

# R14 - 10k
R14 = Part(lib=tigard_lib, name="R_Small", ref="R14",
    value="10k", footprint="Resistor_SMD:R_0402_1005Metric")
net_P3V3 += R14["1"]
net_EECLK += R14["2"]

# R15 - 2.2k
R15 = Part(lib=tigard_lib, name="R_Small", ref="R15",
    value="2.2k", footprint="Resistor_SMD:R_0402_1005Metric")
net_EEDATA += R15["1"]
net_Net_43 += R15["2"]

# R16 - 330
R16 = Part(lib=tigard_lib, name="R_Small", ref="R16",
    value="330", footprint="Resistor_SMD:R_0402_1005Metric")
net_Net_50 += R16["1"]
net_DO += R16["2"]

# R17 - 1M
R17 = Part(lib=tigard_lib, name="R_Small", ref="R17",
    value="1M", footprint="Resistor_SMD:R_0402_1005Metric")
net_VREF += R17["1"]
net_GND += R17["2"]

# R18 - 10k
R18 = Part(lib=tigard_lib, name="R_Small", ref="R18",
    value="10k", footprint="Resistor_SMD:R_0402_1005Metric")
net_P3V3 += R18["1"]
net_Net_44 += R18["2"]

# R19 - 10k
R19 = Part(lib=tigard_lib, name="R_Small", ref="R19",
    value="10k", footprint="Resistor_SMD:R_0402_1005Metric")
net_Net_45 += R19["1"]
net_GND += R19["2"]

# R2 - 5k1
R2 = Part(lib=tigard_lib, name="R_Small", ref="R2",
    value="5k1", footprint="Resistor_SMD:R_0402_1005Metric")
net_Net_9 += R2["1"]
net_GND += R2["2"]

# R20 - 10k
R20 = Part(lib=tigard_lib, name="R_Small", ref="R20",
    value="10k", footprint="Resistor_SMD:R_0402_1005Metric")
net_Net_15 += R20["1"]
net_VTARGET += R20["2"]

# R21 - 10k
R21 = Part(lib=tigard_lib, name="R_Small", ref="R21",
    value="10k", footprint="Resistor_SMD:R_0402_1005Metric")
net_VTARGET += R21["1"]
net_Net_14 += R21["2"]

# R22 - 2k2
R22 = Part(lib=tigard_lib, name="R_Small", ref="R22",
    value="2k2", footprint="Resistor_SMD:R_0402_1005Metric")
net_Net_32 += R22["1"]
net_Net_33 += R22["2"]

# R24 - 10k
R24 = Part(lib=tigard_lib, name="R_Small", ref="R24",
    value="10k", footprint="Resistor_SMD:R_0402_1005Metric")
net_GND += R24["1"]
net_VREF += R24["2"]

# R3 - 1M
R3 = Part(lib=tigard_lib, name="R_Small", ref="R3",
    value="1M", footprint="Resistor_SMD:R_0402_1005Metric")
net_GND += R3["1"]
net_Net_77 += R3["2"]

# R4 - 330
R4 = Part(lib=tigard_lib, name="R", ref="R4",
    value="330", footprint="Resistor_SMD:R_0402_1005Metric")
net_P3V3 += R4["1"]
net_Net_54 += R4["2"]

# R5 - 330
R5 = Part(lib=tigard_lib, name="R", ref="R5",
    value="330", footprint="Resistor_SMD:R_0402_1005Metric")
net_P3V3 += R5["1"]
net_Net_13 += R5["2"]

# R6 - 12k, 1%
R6 = Part(lib=tigard_lib, name="R_Small", ref="R6",
    value="12k, 1%", footprint="Resistor_SMD:R_0402_1005Metric")
net_GND += R6["1"]
net_Net_19 += R6["2"]

# R7 - 10k
R7 = Part(lib=tigard_lib, name="R_Small", ref="R7",
    value="10k", footprint="Resistor_SMD:R_0402_1005Metric")
net_P3V3 += R7["1"]
net_Net_21 += R7["2"]

# R8 - 330
R8 = Part(lib=tigard_lib, name="R_Small", ref="R8",
    value="330", footprint="Resistor_SMD:R_0402_1005Metric")
net_Net_51 += R8["1"]
net_P3V3 += R8["2"]

# R9 - 330
R9 = Part(lib=tigard_lib, name="R_Small", ref="R9",
    value="330", footprint="Resistor_SMD:R_0402_1005Metric")
net_Net_52 += R9["1"]
net_P3V3 += R9["2"]

# RN1 - 100k
RN1 = Part(lib=tigard_lib, name="R_Pack04", ref="RN1",
    value="100k", footprint="Resistor_SMD:R_Array_Convex_4x0402")
net_P3V3 += RN1["1"]
net_P3V3 += RN1["2"]
net_P3V3 += RN1["3"]
net_P3V3 += RN1["4"]
net_Net_69 += RN1["5"]
net_Net_70 += RN1["6"]
net_Net_71 += RN1["7"]
net_Net_72 += RN1["8"]

# RN2 - 100k
RN2 = Part(lib=tigard_lib, name="R_Pack04", ref="RN2",
    value="100k", footprint="Resistor_SMD:R_Array_Convex_4x0402")
net_P3V3 += RN2["1"]
net_P3V3 += RN2["2"]
net_P3V3 += RN2["3"]
net_P3V3 += RN2["4"]
net_Net_73 += RN2["5"]
net_Net_74 += RN2["6"]
net_Net_75 += RN2["7"]
net_Net_76 += RN2["8"]

# RN3 - 100
RN3 = Part(lib=tigard_lib, name="R_Pack04", ref="RN3",
    value="100", footprint="Resistor_SMD:R_Array_Convex_4x0402")
net_Net_46 += RN3["1"]
net_Net_47 += RN3["2"]
net_Net_48 += RN3["3"]
net_Net_49 += RN3["4"]
net_n_TRST += RN3["5"]
net_CS += RN3["6"]
net_DO += RN3["7"]
net_TCK += RN3["8"]

# RN4 - 100
RN4 = Part(lib=tigard_lib, name="R_Pack04", ref="RN4",
    value="100", footprint="Resistor_SMD:R_Array_Convex_4x0402")
net_Net_55 += RN4["1"]
net_Net_56 += RN4["2"]
net_Net_57 += RN4["3"]
net_Net_58 += RN4["4"]
net_UART_TX += RN4["5"]
net_n_UART_RTS += RN4["6"]
net_n_UART_DTR += RN4["7"]
net_n_SRST += RN4["8"]

# RN5 - 100
RN5 = Part(lib=tigard_lib, name="R_Pack04", ref="RN5",
    value="100", footprint="Resistor_SMD:R_Array_Convex_4x0402")
net_AD1 += RN5["1"]
net_AD3 += RN5["2"]
net_AD5 += RN5["3"]
net_AD6 += RN5["4"]
net_Net_59 += RN5["5"]
net_Net_60 += RN5["6"]
net_Net_61 += RN5["7"]
net_Net_62 += RN5["8"]

# RN6 - 100
RN6 = Part(lib=tigard_lib, name="R_Pack04", ref="RN6",
    value="100", footprint="Resistor_SMD:R_Array_Convex_4x0402")
net_BD2 += RN6["1"]
net_BD6 += RN6["2"]
net_Net_63 += RN6["3"]
net_Net_64 += RN6["4"]
net_Net_65 += RN6["5"]
net_Net_66 += RN6["6"]
net_Net_67 += RN6["7"]
net_Net_68 += RN6["8"]

# RN7 - 100k
RN7 = Part(lib=tigard_lib, name="R_Pack04", ref="RN7",
    value="100k", footprint="Resistor_SMD:R_Array_Convex_4x0402")
net_Net_90 += RN7["1"]
net_Net_89 += RN7["2"]
net_Net_88 += RN7["3"]
net_Net_87 += RN7["4"]
net_VREF += RN7["5"]
net_VREF += RN7["6"]
net_VREF += RN7["7"]
net_VREF += RN7["8"]

# RN8 - 100k
RN8 = Part(lib=tigard_lib, name="R_Pack04", ref="RN8",
    value="100k", footprint="Resistor_SMD:R_Array_Convex_4x0402")
net_Net_86 += RN8["1"]
net_Net_85 += RN8["2"]
net_Net_84 += RN8["3"]
net_Net_83 += RN8["4"]
net_VREF += RN8["5"]
net_VREF += RN8["6"]
net_VREF += RN8["7"]
net_VREF += RN8["8"]

# SW1 - TARGET
SW1 = Part(lib=tigard_lib, name="SW_DP4T", ref="SW1",
    value="TARGET", footprint="Button_Switch_SMD:SW_SP4T_PCM13")
net_Net_78 += SW1["1"]
net_Net_79 += SW1["2"]
net_Net_80 += SW1["3"]
net_Net_81 += SW1["4"]
net_Net_82 += SW1["5"]
net_P5V += SW1["6"]
net_P3V3 += SW1["7"]
net_PWR_FLAG += SW1["8"]
net_P1V8 += SW1["9"]
net_PWR_FLAG += SW1["10"]

# SW2 - MODE
SW2 = Part(lib=tigard_lib, name="SW_DPDT", ref="SW2",
    value="MODE", footprint="Button_Switch_SMD:SW_DPDT_CK_JS202011CQN")
net_CS += SW2["1"]
net_CORTEX_PIN2 += SW2["2"]
net_SWDIO += SW2["3"]
net_CIPO += SW2["4"]
net_DI += SW2["5"]
net_Net_50 += SW2["6"]

# TP1 - GND
TP1 = Part(lib=tigard_lib, name="TestPoint", ref="TP1",
    value="GND", footprint="TestPoint:TestPoint_Keystone_5000-5004_Miniature")
net_GND += TP1["1"]

# U1 - AP7365-18
U1 = Part(lib=tigard_lib, name="AP7365-18", ref="U1",
    value="AP7365-18", footprint="Package_TO_SOT_SMD:SOT-23-5")
net_P5V += U1["1"]
net_GND += U1["2"]
net_P5V += U1["3"]
net_Net_10 += U1["4"]
net_P1V8 += U1["5"]

# U2 - AP7365-33
U2 = Part(lib=tigard_lib, name="AP7365-33", ref="U2",
    value="AP7365-33", footprint="Package_TO_SOT_SMD:SOT-23-5")
net_P5V += U2["1"]
net_GND += U2["2"]
net_P5V += U2["3"]
net_Net_11 += U2["4"]
net_P3V3 += U2["5"]

# U3 - FT2232HQ
U3 = Part(lib=tigard_lib, name="FT2232HQ", ref="U3",
    value="FT2232HQ", footprint="Package_DFN_QFN:QFN-64-1EP_9x9mm_P0.5mm_EP4.35x4.35mm_ThermalVias")
net_GND += U3["1"]
net_Net_17 += U3["2"]
net_Net_18 += U3["3"]
net_PWR_FLAG += U3["4"]
net_GND += U3["5"]
net_Net_19 += U3["6"]
net_USB_DN += U3["7"]
net_USB_DP += U3["8"]
net_Net_20 += U3["9"]
net_GND += U3["10"]
net_GND += U3["11"]
net_VREG += U3["12"]
net_GND += U3["13"]
net_Net_21 += U3["14"]
net_GND += U3["15"]
net_AD0 += U3["16"]
net_AD1 += U3["17"]
net_AD2 += U3["18"]
net_AD3 += U3["19"]
net_P3V3 += U3["20"]
net_AD4 += U3["21"]
net_AD5 += U3["22"]
net_AD6 += U3["23"]
net_Net_22 += U3["24"]
net_GND += U3["25"]
net_Net_23 += U3["26"]
net_Net_24 += U3["27"]
net_Net_25 += U3["28"]
net_Net_26 += U3["29"]
net_Net_27 += U3["30"]
net_P3V3 += U3["31"]
net_Net_28 += U3["32"]
net_Net_29 += U3["33"]
net_Net_30 += U3["34"]
net_GND += U3["35"]
net_Net_31 += U3["36"]
net_VREG += U3["37"]
net_BD0 += U3["38"]
net_BD1 += U3["39"]
net_BD2 += U3["40"]
net_BD3 += U3["41"]
net_P3V3 += U3["42"]
net_BD4 += U3["43"]
net_Net_32 += U3["44"]
net_BD6 += U3["45"]
net_Net_33 += U3["46"]
net_GND += U3["47"]
net_Net_34 += U3["48"]
net_VREG += U3["49"]
net_P3V3 += U3["50"]
net_GND += U3["51"]
net_Net_35 += U3["52"]
net_Net_36 += U3["53"]
net_Net_37 += U3["54"]
net_Net_38 += U3["55"]
net_P3V3 += U3["56"]
net_Net_39 += U3["57"]
net_Net_40 += U3["58"]
net_Net_41 += U3["59"]
net_Net_42 += U3["60"]
net_EEDATA += U3["61"]
net_EECLK += U3["62"]
net_EECS += U3["63"]
net_VREG += U3["64"]
net_GND += U3["65"]

# U4 - 93LC46BT-I/OT
U4 = Part(lib=tigard_lib, name="93LCxxBxxOT", ref="U4",
    value="93LC46BT-I/OT", footprint="Package_TO_SOT_SMD:SOT-23-6")
net_Net_43 += U4["1"]
net_GND += U4["2"]
net_EEDATA += U4["3"]
net_EECLK += U4["4"]
net_EECS += U4["5"]
net_P3V3 += U4["6"]

# U5 - SN74LVC8T245
U5 = Part(lib=tigard_lib, name="SN74LVC8T245", ref="U5",
    value="SN74LVC8T245", footprint="Package_SO:TSSOP-24_4.4x7.8mm_P0.65mm")
net_P3V3 += U5["1"]
net_Net_44 += U5["2"]
net_Net_72 += U5["3"]
net_Net_71 += U5["4"]
net_Net_70 += U5["5"]
net_Net_69 += U5["6"]
net_Net_76 += U5["7"]
net_Net_75 += U5["8"]
net_Net_74 += U5["9"]
net_Net_73 += U5["10"]
net_GND += U5["11"]
net_GND += U5["12"]
net_GND += U5["13"]
net_Net_58 += U5["14"]
net_Net_57 += U5["15"]
net_Net_56 += U5["16"]
net_Net_55 += U5["17"]
net_Net_49 += U5["18"]
net_Net_48 += U5["19"]
net_Net_47 += U5["20"]
net_Net_46 += U5["21"]
net_n_ENABLE += U5["22"]
net_VREF += U5["23"]
net_VREF += U5["24"]

# U6 - SN74LVC8T245
U6 = Part(lib=tigard_lib, name="SN74LVC8T245", ref="U6",
    value="SN74LVC8T245", footprint="Package_SO:TSSOP-24_4.4x7.8mm_P0.65mm")
net_P3V3 += U6["1"]
net_Net_45 += U6["2"]
net_Net_62 += U6["3"]
net_Net_61 += U6["4"]
net_Net_60 += U6["5"]
net_Net_59 += U6["6"]
net_Net_68 += U6["7"]
net_Net_67 += U6["8"]
net_Net_66 += U6["9"]
net_Net_65 += U6["10"]
net_GND += U6["11"]
net_GND += U6["12"]
net_GND += U6["13"]
net_Net_83 += U6["14"]
net_Net_84 += U6["15"]
net_Net_85 += U6["16"]
net_Net_86 += U6["17"]
net_Net_87 += U6["18"]
net_Net_88 += U6["19"]
net_Net_89 += U6["20"]
net_Net_90 += U6["21"]
net_n_ENABLE += U6["22"]
net_VREF += U6["23"]
net_VREF += U6["24"]

# Y1 - 12MHz
Y1 = Part(lib=tigard_lib, name="Crystal_GND24", ref="Y1",
    value="12MHz", footprint="Crystal:Crystal_SMD_3225-4Pin_3.2x2.5mm")
net_Net_17 += Y1["1"]
net_GND += Y1["2"]
net_Net_18 += Y1["3"]
net_GND += Y1["4"]

# ============================================================
# Generate netlist
# ============================================================
ERC()
generate_netlist(file_="tigard.net")
print("Netlist generated: tigard.net")