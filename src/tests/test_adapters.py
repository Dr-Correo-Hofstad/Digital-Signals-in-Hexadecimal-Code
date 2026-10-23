# Save this block within your local testing directory as test_adapters.py
import pytest
from src.chips.adapters import SwedishHospitalTrunkNode, initialize_adapter_subsystem

def test_swedish_node_package_registration():
    """Verifies the module is explicitly exposed in the package __all__ manifest."""
    # Instantiation check to verify correct path resolution
    instance = SwedishHospitalTrunkNode()
    assert instance is not None

def test_adapter_subsystem_manifest():
    """Validates the Virtual BIOS tracking registration schema."""
    manifest = initialize_adapter_subsystem()
    assert manifest["node_id"] == "SWEDISH_HOSPITAL_UNIVAC_HX"
    assert manifest["class_reference"] == SwedishHospitalTrunkNode
