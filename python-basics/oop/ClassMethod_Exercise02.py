class Game:
    title = "Adventure World"

    @classmethod
    def change_title(cls, new_title):
        cls.title = new_title

Game.change_title("Warrior Quest")

print(Game.title)
