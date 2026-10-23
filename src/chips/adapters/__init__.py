"""
Revolutionary Technology (RT) Adapter Architecture
===================================================
Initialization manifest for the peripheral translation bridges. Formally registers
and exposes legacy system adapters for real-time mainframe trunking.
"""

# Explicitly import the trunk node from our custom logic file
from .hexadecimal_trunk_node import SwedishHospitalTrunkNode

# Define the package's public interface export list
__all__ = [
    "SwedishHospitalTrunkNode"
]

def initialize_adapter_subsystem() -> dict:
    """
    Core manifest registration function called by main.py during the 
    Virtual BIOS hardware discovery phase.
    """
    return {
        "node_id": "SWEDISH_HOSPITAL_UNIVAC_HX",
        "interface_protocol": "MIL-STD-1397-HEX",
        "bus_coupling": "NATIVE_ANALOG_TRUNK",
        "class_reference": SwedishHospitalTrunkNode
    }
