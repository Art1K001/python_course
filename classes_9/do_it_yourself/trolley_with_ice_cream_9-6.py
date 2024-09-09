class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.name.title()} have a very specific {self.type.title()} food")

    def open_restaurant(self):
        print(f"{self.name.title()} is open")

""" Написати класс візочок з морозивом , має наслідувати клас Ресторан """
class IceCreamStand(Restaurant):
    """додати атрибут Наповнювачі(має містити список)"""
    def __init__(self, restaurant_name, cuisine_type ,flavors):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors
    def show_flavors(self):
        print("avaluable list of ice cream: ")
        for flavor in self.flavors:
            print(f"{flavor}")
my_icecream_stand = IceCreamStand("Cool Ice", "ice cream", ["vanilla", "mango", "pistacho"] )
my_icecream_stand.show_flavors()
