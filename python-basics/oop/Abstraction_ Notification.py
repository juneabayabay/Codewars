from abc import ABC, abstractmethod

class Notification:
    @abstractmethod
    def send(self):
        print()
    
class Email(Notification):
     def send(self):
         print("Sending an email notification")
         
email = Email()
email.send()

class Logout(Notification):
    def send(self):
        print("Thanks for the visit")
        

logout = Logout()
logout.send()

