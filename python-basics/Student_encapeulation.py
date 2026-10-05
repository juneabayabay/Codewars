class Cat: #blue print
    def __init__(self, name, age): # constructor, reference, parameters 
        self.name = name
        self.__age = age

    def get_age(self):
        return self.__age

    def get_name(self):
        return self.name


cat = Cat("Ming", 3)

print(cat.name)
print(cat.get_age())
print(cat.get_name())
