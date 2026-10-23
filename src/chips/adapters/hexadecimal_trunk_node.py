"""
RT-UNIVAC Bridge Adapter: hexadecimal_trunk_node.py
===================================================
Establishes a bidirectional data trunk between the legacy 36-bit/6-bit UNIVAC IX 
fabric and the Revolutionary Technology (RT) 16-state analog motherboard bus.
"""

import os
from typing import List

class SwedishHospitalTrunkNode:
    def __init__(self):
        # 16-state analog logic voltage array mapped from 0.0V to 1.0V (0.0625V intervals)
        self.hex_voltage_steps = [i * 0.0625 for i in range(16)]
        
        # Standard UNIVAC 6-bit FIELDATA to Hexadecimal structural translation matrix
        self.fieldata_to_hex_mask = 0x0F # Isolate lower 4-bit nibble for analog injection

    def slice_36bit_word_to_hex_nibbles(self, word_36bit: int) -> List[int]:
        """
        Slices a single legacy 36-bit mainframe word into nine distinct 4-bit 
        hexadecimal nibbles for native analog bus compatibility.
        """
        nibbles = []
        for i in range(9):
            # Shift right and mask out the 4-bit segment
            nibble = (word_36bit >> (i * 4)) & 0x0F
            nibbles.append(nibble)
        return nibbles[::-1] # Retain big-endian alignment

    def map_nibbles_to_rt_voltages(self, nibbles: List[int]) -> List[float]:
        """
        Converts 4-bit digital hex nibbles into precise analog voltage signals 
        conforming to RT Physical Infrastructure standards.
        """
        voltage_stream = []
        for nibble in nibbles:
            voltage = self.hex_voltage_steps[nibble]
            voltage_stream.append(voltage)
        return voltage_stream

    def execute_trunk_injection(self, raw_mainframe_buffer: List[int]) -> int:
        """
        Processes a block of mainframe code and injects it straight into the 
        RT virtual logic board.
        """
        total_injected_packets = 0
        for word in raw_mainframe_buffer:
            hex_nibbles = self.slice_36bit_word_to_hex_nibbles(word)
            analog_voltages = self.map_nibbles_to_rt_voltages(hex_nibbles)
            
            # Hardware abstraction layer output simulation
            # In a live environment, this pipes to: src/hex_voltage_controller.py --inject-hex
            total_injected_packets += len(analog_voltages)
            
        return total_injected_packets

if __name__ == "__main__":
    print("================================================================")
    print("INITIALIZING SWEDISH HOSPITAL UNIVAC-HX TRUNK COMPLIANCE AUDIT")
    print("================================================================\n")
    
    node = SwedishHospitalTrunkNode()
    
    # Mocking an un-carved 36-bit buffer sector from a Swedish Hospital Uniservo Tape reel
    sample_mainframe_buffer = [0x7FFFFFFFC, 0x123456789]
    
    for idx, sample_word in enumerate(sample_mainframe_buffer):
        nibbles = node.slice_36bit_word_to_hex_nibbles(sample_word)
        voltages = node.map_nibbles_to_rt_voltages(nibbles)
        
        print(f"Mainframe Word [{idx}]: {hex(sample_word).upper()}")
        print(f"  -> Extracted Hexadecimal Nibbles: {nibbles}")
        print(f"  -> Injected RT Analog Bus Voltages: {[f'{v:.4f}V' for v in voltages]}\n")
