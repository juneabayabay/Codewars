
class Character:
    def attack(self):
        print()

class Warrior(Character):
    def attack(self):
        print("Warrior attacks with a sword")

class Mage(Character):
    def attack(self):
        print("Mage cast spell")

class Archer(Character):
    def attack(self):
        print("Archer shoots an arrow!")

warrior = Warrior()
mage = Mage()
archer = Archer()

character = [warrior, mage, archer]

for characters in character:
     characters.attack()
