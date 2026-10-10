class Vehicle:
    def move(self):
        print("The vehicle is moving ")
class Car:
    def move(Vehicle):
        print("The Car is Driving")
class Airplane:
    def move(Vehicle):
        print("The airplane is flying")
class Boat:
    def move(Vehicle):
        print("The boat sailing")

v = Vehicle()
c = Car()
a = Airplane()
b = Boat()

Vehicles = [v, c, a, b]

for vehicle in Vehicles:
    vehicle.move()
  
