class Animal:
    animal = "Sample data for Animal"
    
    def __init__(self, name):
        self.name = name
    
    @classmethod
    def show(cls):
        print(cls.animal)
        
Animal.show()
