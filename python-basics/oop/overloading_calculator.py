class Calculator: # class name

    def add(self, a, b=0, c=0): # create a funtion and method name called add
        return a + b + c # we return the parameters 

obj = Calculator() # we create a new object for the parent class

print(obj.add(5, 10)) # we print and we add value
print(obj.add(5, 10, 15))

# overloading
