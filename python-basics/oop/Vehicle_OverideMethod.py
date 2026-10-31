class Vehicle:
  def start(self):
    print("Vehicle is starting...")

class Car(Vehicle):
  def start(self):
    print("Car engine is starting")

class Motorcycle:
  def start(self):
    print("Motorcycle engin is starting")

v = Vehicle()
c = Car()
m = Motorcycle()

v.start()
c.start()
m.start()
