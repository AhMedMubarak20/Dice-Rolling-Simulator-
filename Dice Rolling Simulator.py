import random

def roll_dice():
    return random.randint(1, 6)

print("Dice Rolling Simulator")
print("Press Enter to roll or 'q' to quit")

while True:
    user_input = input()
    if user_input.lower() == 'q':
        break
    print("Dice 1:", roll_dice())
    print("Dice 2:", roll_dice())
