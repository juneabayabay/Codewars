try:
    number = int(input("Enter a number: "))
    result = 100 / number # If the input number is divided is will show the result

except ValueError:
    print("Please enter a valid number.") # input unproperly this line will show except zero

except ZeroDivisionError:
    print("Zero is not allowed.") # if you enter zero

else:
    print("Result:", result # input properly will showed the result

finally:
    print("Program finished.") # default line 
