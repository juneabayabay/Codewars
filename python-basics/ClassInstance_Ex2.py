class Dog:
  species = "Canine"

  def __init__(self, name):
    self.name = name

dog1 = Dog("Max")
dog2 = Dog("Bella")

Dog.species = "Example only "
print(Dog.species)

print(dog1.name)
print(dog2.name)
