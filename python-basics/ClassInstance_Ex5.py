class GameCharacter:
game_name = "Adventure Quest"

def __init__(self, name):
self.name = name
self.health = 100


knight = GameCharacter("Knight")
wizard = GameCharacter("Wizard")

knight.health = 70

GameCharacter.game_name = "Legends of Python"

print("Character:", knight.name)
print("Health:", knight.health)
print("Game:", knight.game_name)

print()

print("Character:", wizard.name)
print("Health:", wizard.health)
print("Game:", wizard.game_name)
