class Animal:
    def make_sound(self):
        print("Animal makes a sound")


class Dog(Animal):
    def make_sound(self):
        print("Woof!")


class Cat(Animal):
    def make_sound(self):
        print("Meow!")


class Cow(Animal):
    def make_sound(self):
        print("Moo!")


animals = [Dog(), Cat(), Cow()]

for animal in animals:
    animal.make_sound()
