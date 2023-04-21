"""
    This file defines objects to represent carpet layers and materials
"""
import typing # For data type specification

class Material:
    def __init__(self, name: str, rec: float, proc_cost: float, mkt_value: float):
        self.name = name
        self.rec = rec
        self.proc_cost = proc_cost
        self.mkt_value = mkt_value

class Layer:
    def __init__(self, name: str, materials: list[Material]):
        self.materials = materials
        self.name = name