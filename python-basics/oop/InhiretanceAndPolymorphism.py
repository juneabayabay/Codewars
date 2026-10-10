# inheritance + polymorphism 
class Animal:
    def make_sound(self):
        print("Animal makes a sound.")


class Dog(Animal):
    def make_sound(self):
        print("Woof!")


class Cat(Animal):
    def make_sound(self):
        print("Meow!")


dog = Dog()
cat = Cat()
animal = Animal()

animal.make_sound()
dog.make_sound()
cat.make_sound()
