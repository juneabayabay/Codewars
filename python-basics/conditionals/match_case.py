print("Match case method")

day = 1 # variable declaration

match day:  # match case statement
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")

print()
print("if/elif method")

# if elif statement


day = 2

if day == 1:
    print("Monday")
elif day == 2:
    print("Tuesday")
elif day == 3:
    print("Wednesday")
else:
    print("Invalid")

    # The difference between match case and if elif statement 
    # match case good for matching pattern and values and specific case nad structure
    # if/elif great for checking conditions  more flexible and complex situations
    # addittional ideas mathc and if/elif had able to use string type

print()
print("Challenge 1")

command = input("Enter a command: ")

if command == "Start":
    print("Game Start! ")
elif command == "stop":
    print("Game stopped! ")
elif command == "help":
    print("select Options ")
elif command == "quit":
    print("Quit")
else:
    print("Unknown Command")

print()
print("Challegen 2")
# convert into match case

command = input("Enter a command: ")

match command:
  case "start":
    print("Game started")
  case "stop":
    print("Game stopped")
  case "help":
    print("How can help you? ")
  case ("quit"):
    print("The game is Done!")
  case _:
    print("unknown command")

print()
print("Challenge 3")
# the temperature

temperature = 7

if temperature >= 29:
  print("Hot Coffee")
elif 20 <= temperature <= 29:
  print("Warm coffee")
elif 10 <= temperature <= 19:
  print(" Cool coffee")
else:
  print("Cold Coffee")


print("")
print("Challenge 4")
print("match the string")

command = "quit"

match command:
  case "save":
    print("The command is already saved")
  case "stop":
    print("The command is already stop")
  case "start":
    print("The command is already stop")
  case "load":
    print("Loading wait for a moment")
  case "quit":
    print("exit")