"""
    This file defines objects to represent carpet layers and materials
"""

class Material:
    # `name`:str, `rec`: float, `proc_cost`: float, `mkt_value`: float
    def __init__(self, name, rec, proc_cost, mkt_value):
        self.name = name
        self.rec = rec
        self.proc_cost = proc_cost
        self.mkt_value = mkt_value

class Layer:
    # `name`: str, `materials`: list[Material], `prop`: float
    def __init__(self, name: str, materials: list[Material], prop: float):
        self.materials = materials
        self.name = name
        self.prop = prop