class Warrior:
    def use_ability(self):
        print("This ability if for warrior ")
        
class Mage(Warrior):
    def use_ability(self):
        print("This is for the mage ")

class Healer(Warrior):
    def use_ability(self):
        print("healer for everyone ")

warrior = Warrior()
mage = Mage()
healer = Healer()

characters = [warrior, mage, healer]

for character in characters:
    character.use_ability()
