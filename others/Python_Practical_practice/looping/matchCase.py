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