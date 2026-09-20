correct_password = "qwerty123" # This is the password

try: #  we with try and except handling
  password = input("Enter password: ") # user input data

if password != correct_password: # condition or checking the data if right
  raise ValueError("Wrong Password") # raise meaning allow to create error

except ValueError as error: # This line will show the result of ValueError
  print(error)

else:
print("Logins Succesful!") # If everything is right it will print the output
