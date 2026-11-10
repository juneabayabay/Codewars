class Device:
    def turn_on(self):
        print("Device is now on.")

class Smartphone(Device):
    def turn_on(self):
        print("Smartphone OS is booting up...")

# Create an instance of Smartphone
my_phone = Smartphone()

# Call the overridden method
my_phone.turn_on()
