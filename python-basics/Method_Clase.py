from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def make_sound(self):
        pass


class Dog(Animal):

    def make_sound(self):
        print("The dog barks!")


class Cat(Animal):

    def make_sound(self):
        print("The cat meows!")


dog = Dog()
cat = Cat()

dog.make_sound()
cat.make_sound()
