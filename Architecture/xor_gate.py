from nand import NANAD_gate
from not_gate import NOT_gate
from and_gate import AND_gate
from or_gate import OR_gate

def XOR_gate(a, b):
    return AND_gate(NANAD_gate(a,b), OR_gate(a, b))