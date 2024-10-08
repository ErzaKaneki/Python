from nand import NANAD_gate
from not_gate import NOT_gate

def AND_gate(a, b):
    return NOT_gate(NANAD_gate(a, b))