class Car:
    """A simple class car"""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0

    def get_descriptive_name(self):
        """return a neatly formated descriptive name"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        """Imprime algo relacionado con la velocidad"""
        print(f"this car has {self.odometer} miles on it")

    def update_odometer(self, mileage):
        """Set odometer"""
        self.odometer = mileage

    def increment_odometer(self, mileage):
        """increment odometer"""
        self.odometer += mileage
    
    def fill_gas_tak(self):
        """llegar el combustible, solo aplica para diese y gasolina"""
        print(f"El tanque del '{self.get_descriptive_name()}' ha sido llenado")

class Electric(Car):
    """Represents aspect of electric cars"""
    def __init__(self, make, model, year):
        """Initialize attributes from the parent class"""
        super().__init__(make, model, year)
        self.battery = Battery()

    def fill_gas_tak(self):
        """llegar el combustible, solo aplica para diese y gasolina"""
        print(f"El '{self.get_descriptive_name()}' es electrico por lo que no puede repostar")

class Battery:
    """Definiendo una simple bateria"""
    def __init__(self, battery_size = 40):
        self.battery_size = battery_size

    def describer_battery(self):
        """Sorry, me faltaba el docstring"""
        print(f"This car has a {self.battery_size}-kwh battery")



    
my_new_car = Car("audi", "a4", 2014)
print(my_new_car.get_descriptive_name())
print(my_new_car.read_odometer())
print("\n")
my_new_car.odometer  = 20
print(my_new_car.read_odometer())
print("\n")
my_new_car.update_odometer(40)
print(my_new_car.read_odometer())


my_leaf = Electric("Nissan", "Leaf", 2024)
print(my_leaf.get_descriptive_name())

my_new_car.fill_gas_tak()
my_leaf.fill_gas_tak()
print("\n\n")
my_leaf.battery.describer_battery()