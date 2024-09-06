class Car:
    """ Проста спроба змоделювати машину """
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """ Повернути відформатоване змістовне імʼя """
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it")

    def update_odometer(self, mileage):
        """
        Задати значення одометра
        Відкинути зміну в разі спроби відмотати показники одометра
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer")

    def increment_odometer(self, miles):
        """
        Додати задане значення до показників одометра
        """
        self.odometer_reading += miles

my_new_car = Car("subaru", "impreza", 2009)
print(my_new_car.get_descriptive_name())

my_new_car.update_odometer(23_500)
my_new_car.read_odometer()

my_new_car.increment_odometer(100)
my_new_car.read_odometer()