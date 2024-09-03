from stack import Stack

print("\nLet's play Towers of Hanoi!!")

stacks = []

left_stack = Stack("Left")
middle_stack = Stack("Middle")
right_stack = Stack("Right")

stacks.append(left_stack)
stacks.append(middle_stack)
stacks.append(right_stack)

num_disks = input("How many disks do you want to play with?")
while int(num_disks) < 3:
    num_disks = input("Enter a number greater than or equal to 3\n")

for i in range(len(num_disks), 0, -1):
    left_stack.push(i)


