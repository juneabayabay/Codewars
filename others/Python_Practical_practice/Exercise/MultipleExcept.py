try:
  number = int(input("Enter a number: "))
  result = 100 / number # Number accurately will print out 

  print(result)

except ValueError:
  print("You must enter a number") # This line is for Ramdom string or special symbols

except ZeroDivisionError: 
  print("You cannot enter a zero") # this line will print zero entered

