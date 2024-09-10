class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.type = cuisine_type

    def describe_restaurant(self):
        print(f"\nOur restaurant named {self.name.title()} and we cook only {self.type.title()}")

    def open_restaurant(self):
        print(f"\t{self.name.title()}open 16/7 for week")

my_restaurant = Restaurant("china town", "italian")
print(f"\t{my_restaurant.name.title()} restaurant with {my_restaurant.type} food")
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

your_restaurant = Restaurant("galicia", "ukrainian")
print(f"\t{your_restaurant.name.title()} restaurant with {your_restaurant.type} food")
your_restaurant.describe_restaurant()
your_restaurant.open_restaurant()

their_restaurant = Restaurant("chveni", "georgian")
print(f"\t{their_restaurant.name.title()} restaurant with {their_restaurant.type} food")
their_restaurant.describe_restaurant()
their_restaurant.open_restaurant()
