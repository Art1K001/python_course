class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.name.title()} have a very specific {self.type.title()} food")

    def open_restaurant(self):
        print(f"{self.name.title()} is open")