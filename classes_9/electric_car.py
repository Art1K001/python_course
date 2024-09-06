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

class ElectricCar(Car):
    """ Змоделювати властивості, притаманні електрокарами """

    def __init__(self, make, model, year):
        """ Започаткувати атрибути батьківського класу """
        super().__init__(make, model, year)


my_tesla = ElectricCar("tesla", "model s", "2019")
print(my_tesla.get_descriptive_name())
