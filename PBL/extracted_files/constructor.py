# Constructor
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0
        print(f"A new car has been created: {year} {make} {model}")

    def display_info(self):
        return f"{self.year} {self.make} {self.model}, Odometer: {self.odometer} kms"

    def drive(self, kms):
        self.odometer += kms
        print(f"The car has been driven for {kms} kms. Total: {self.odometer} kms")


# Creating instances of the Car class
car1 = Car("Toyota", "Corolla", 2022)
car2 = Car("Hyundai", "i10", 2017)

# Displaying car information
print(car1.display_info())
print(car2.display_info())

# Driving the cars
car1.drive(1000)
car2.drive(500)

# Displaying updated car information
print(car1.display_info())
print(car2.display_info())
