import random

class Die:

    def __init__(self, sides=6):
        self.sides = sides

    def roll(self):
        return random.randint(1, self.sides)

six_sided_die = Die()
print("Six times:")
for die in range(10):
    print(f"\t{six_sided_die.roll()}")

ten_sided_die = Die(10)
print("Ten times:")
for die in range(10):
    print(f"\t{ten_sided_die.roll()}")

twenty_sided_die = Die(20)
print("Twenty times:")
for die in range(10):
    print(f"\t{twenty_sided_die.roll()}")