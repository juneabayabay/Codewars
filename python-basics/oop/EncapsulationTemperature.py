class Thermostat:
    def __init__(self, temperature):
        self.__temperature = temperature

    def get_temperature(self):
        return self.__temperature

    def set_temperature(self, new_temp):
        if 10 <= new_temp <= 30:
            self.__temperature = new_temp
        else:
            print("Invalid temperature")


t = Thermostat(20)

print(t.get_temperature())

t.set_temperature(25)
print(t.get_temperature())

t.set_temperature(40)
print(t.get_temperature())
