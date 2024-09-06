class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"{self.name.title()} have a very specific {self.type.title()} food")

    def open_restaurant(self):
        print(f"{self.name.title()} is open")

    def restaurant(self):
        print(f"At that moment, we have {self.number_served} customers")

    def set_number_served(self, customers):
        self.number_served = customers

    def increment_number_served(self, customeres):
        self.number_served += customeres

my_restaurant = Restaurant("сhina town", "italiano")
my_restaurant.open_restaurant()
my_restaurant.describe_restaurant()

my_restaurant.set_number_served(543)
my_restaurant.restaurant()

my_restaurant.increment_number_served(50)
my_restaurant.restaurant()
