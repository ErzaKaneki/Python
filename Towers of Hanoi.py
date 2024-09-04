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

num_optimal_moves = (2 * int(num_disks)) - 1

print("\nThe fastest you can solve this game is in {m} moves.".format(m = num_optimal_moves))

def get_input():
    choices = [stack.get_name()[0] for stack in stacks]
    while True:
        for i in range(len(stacks)):
            name = stacks[i].get_name()
            letter = choices[i]
            print("\nEnter {L} for {N}.".format(L = letter, N = name))
        user_input = input("")    
        if user_input.upper() in choices:
            for i in range(len(stacks)):
                if user_input.upper() == choices[i]:
                    return print(stacks[i])
                