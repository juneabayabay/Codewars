from abc import ABC, abstractmethod  # Import abstraction tools

class Payment(ABC):  # Abstract class

    @abstractmethod
    def pay(self):  # Required method for child classes
        pass  # Placeholder; no implementation


class Gcash(Payment):  # Inherits Payment

    def pay(self):  # Implements the required method
        print("Payment successful using GCash!")


gcash = Gcash()  # Create an object
gcash.pay()      # Call the method
