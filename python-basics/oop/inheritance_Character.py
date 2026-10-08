class Character:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def introduce(self):
        return f"Hi, I am {self.name} and I have {self.health} HP."


class Warrior(Character):
    def __init__(self, name, health, weapon):
        super().__init__(name, health)
        self.weapon = weapon

    def attack(self):
        return f"{self.name} attacks with their {self.weapon}!"


my_warrior = Warrior("June", 100, "Sword")

print(my_warrior.introduce())
print(my_warrior.attack())
