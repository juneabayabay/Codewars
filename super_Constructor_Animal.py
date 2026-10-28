class Animal:
    def __init__(self, name):
        self.name = name # attribute assignment 

class Dog(Animal):
    def __init__(self, name, color): # created a new paramater and needed a new consturtor
        super().__init__(name) # add the super with the contructor and poarametere name
        self.color = color # Then the new parameter we should put here for attribute assignment

dog = Dog("cow", "Black") # we created a new object and the value

print(dog.name) # we print name and color of the cow
print(dog.color)
