class Animal:
  species = "Mammal"

  def __init__(self, name):
    self.name = name

ob1 = Animal("Leo")
ob2 = Animal("Melo")

ob1.species = "Reptile"

print(ob1.name)
print(ob1.species)
print()
print(ob2.name)
print(ob2.species)

