class Vehicle:
    def start(self):
        print("Vehicle is starting.")

class Car(Vehicle):
    def start(self):
        print("Car engine is starting.")

class Motorcycle(Vehicle):
    def start(self):
        print("Motorcycle engine is starting.")

car = Car()
motorcycle = Motorcycle()

car.start()
motorcycle.start()

# My understanding of method overriding is that it allow a child class to override the method,
# we created a parent class called Vehicle and two child classes called car and motorcycle.
# then each of it has on data and we can override the method start()

