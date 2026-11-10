
class Character(): # main template 
    def __init__(self, health, damage, speed):# def is a function,  __init__ is the constructor and the parameters 
        self.health = health # 4 - 6 lines are attributes 
        self.damage = damage
        self.speed = speed
        
    def take_damage(self, amount): # we create another functiok method called take_damage
        self.health -= amount # we set an assignments for the amount 

# CHILD CLASS
class Warrior(Character):
    pass

# we initialize and we add  the values
warrior = Warrior(500, 50, 60)

# TEST THE ACTIONS
print(f"Initial health {warrior.health}")
warrior.take_damage(50)
print(f"Health remaining after attack {warrior.health}")
