from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass


class Car(Vehicle):

    def start(self):
        print("Car engine is starting...")


class Motorcycle(Vehicle):

    def start(self):
        print("Motorcycle engine is starting...")


car = Car()
motorcycle = Motorcycle()

car.start()
motorcycle.start()
