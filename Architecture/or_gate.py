from nand import NANAD_gate
from not_gate import NOT_gate
from and_gate import AND_gate

def OR_gate(a, b):
    return NANAD_gate(NANAD_gate(a, a), NANAD_gate(b, b))