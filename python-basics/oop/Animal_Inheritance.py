# MAIN TEMPLATE (Parent Class)
class Animal():
    
    # SHARED TRAIT (Attribute)
    alive = True
    
    # ACTION (Method)
    def eat(self):
        print("This animal is eating")
    
    # ACTION (Method)
    def sleeping(self):
        print("This animal is Sleeping")
        
# COPIES THE TEMPLATE (Child Class)
class Cat(Animal):
    pass

# COPIES THE TEMPLATE (Child Class)
class Dog(Animal):
    pass


# CREATING THE ACTUAL ANIMALS (Objects)
cat = Cat()
dog = Dog()

# CHECKING THEIR TRAITS
print(dog.alive)
print(cat.alive)

# MAKING THEM DO ACTIONS
cat.eat()
dog.sleeping()
