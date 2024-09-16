import random

def generate_ticket():
    my_tuple = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "A", "B", "C", "D", "E")
    return random.sample(my_tuple, 4)

def simulate_lottery(ticket):
    attempts = 0
    while True:
        attempts += 1
        lottery_ticket = generate_ticket()
        if lottery_ticket == ticket:
            break
    return attempts

my_ticket = ["A", 2, 6, "B"]
attempts = simulate_lottery(my_ticket)
print(f"After {attempts} tries, you win")


