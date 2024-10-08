from nand import NANAD_gate
from not_gate import NOT_gate
from and_gate import AND_gate
from or_gate import OR_gate
from xor_gate import XOR_gate

def half_adder(a, b):
    s = XOR_gate(a, b)
    c = AND_gate(a, b)
    return (s, c)

# print(half_adder(0, 0))  Test variants
# print(half_adder(0, 1))
# print(half_adder(1, 0))
# print(half_adder(1, 1))

def full_adder(a, b, c):
    s_1, c_out_1 = half_adder(a, b)
    s, c_out_2 = half_adder(s_1, c)
    c_out = OR_gate(c_out_1, c_out_2) 
    return (s, c_out)

print(full_adder(0, 0, 0))
print(full_adder(1, 1, 1))
print(full_adder(0, 1, 1))
print(full_adder(1, 1, 0))