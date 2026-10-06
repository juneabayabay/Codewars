class Animal:
    def eat(self):
        print("The animal is eating")


class Dog(Animal):
    def bark(self):
        print("The dog is barking")


dog = Dog()

dog.eat()
dog.bark()
