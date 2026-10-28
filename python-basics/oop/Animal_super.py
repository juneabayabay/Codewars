class Animal:
  def speak(self):
    print("Animal make sounds")

class Dog(Animal):
  def speak(self):
    super().speak()
    print("The dog says woof!")

dog = Dog()
dog.speak()


# My understanding
# First we created a parent class, next the method name called speak(self) for our parameter it will be our reference when we call the data of this method

# next the child class is Dog(Animal) which we call the parent class and same method called speak

# the we put the super().speak() to print as both parent and child

# we created new object 
