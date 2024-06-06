class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def drive(self):
        pass

class Car(Vehicle):
    def drive(self):
        return f"Driving a car: {self.make} {self.model}"

class Motorcycle(Vehicle):
    def drive(self):
        return f"Riding a motorcycle: {self.make} {self.model}"

# Kullanım
car = Car("Toyota", "Camry")
motorcycle = Motorcycle("Honda", "CBR")

print(car.drive())  # Driving a car: Toyota Camry
print(motorcycle.drive())  # Riding a motorcycle: Honda CBR


