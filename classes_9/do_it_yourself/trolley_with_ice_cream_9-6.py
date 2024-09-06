class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.name.title()} have a very specific {self.type.title()} food")

    def open_restaurant(self):
        print(f"{self.name.title()} is open")

class IceCreamStand(Restaurant):

    def __init__(self, flavors):
        self.flavors = flavors

my_restaurant = Restaurant("сhina town", "italiano")
print(f"{my_restaurant.name.title()} at this restaurant you feel like chinese people")
print(f"{my_restaurant.type.title()} food like mafia")
my_restaurant.open_restaurant()
my_restaurant.describe_restaurant()

