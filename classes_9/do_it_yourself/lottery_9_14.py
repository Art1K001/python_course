import random

my_tuple = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "A", "B", "C", "D", "E")

ticket = random.sample(my_tuple, 4)

print(f"Ticket with number: {ticket} win")
