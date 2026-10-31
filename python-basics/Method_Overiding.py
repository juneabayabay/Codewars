class Animal:
    def sound(self):
        print("Animal makes a sound")


class Dog(Animal):
    def sound(self):
        print("Dog says Woof!")


class Cat(Animal):
    def sound(self):
        print("Cat says Meow!")


# Creating objects
animal = Animal()
dog = Dog()
cat = Cat()


# Calling methods
animal.sound()
dog.sound()
cat.sound()
