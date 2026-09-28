
# NOTES MANAGER

def add_note():

   
    note = input("Enter your note: ")

    with open("notes.txt", "a") as file: # a is append mode which means we are adding to the file

        file.write(note + "\n") # \n is a new line

    print("Note saved!") # this is a message that appear afte the note is saved


def show_notes(): # this funtions to show the notes 


    try: # try is uses to catch the error if the file in not found 

        with open("notes.txt", "r") as file: # r is read mode which means we are reading the file

            notes = file.read()

        print()
        print("========== YOUR NOTES ==========")
        print(notes)
        print("================================")

    except FileNotFoundError:

        # This happens if notes.txt doesn't exist yet.

        print("You don't have any notes yet.")



# MAIN MENU

while True:

    print()
    print("========== NOTES MANAGER ==========")
    print("1. Add note")
    print("2. Show notes")
    print("3. Exit")

    choice = input("Choose an option: ")


    
    # OPTION 1
    
    if choice == "1":

        add_note()


    # OPTION 2
    
    elif choice == "2":

        show_notes()


# OPTION 3

    elif choice == "3":

        print("Thank you for using the notes manager!")

        break # this is a break statement that breaks the loop


    else:

        print("Invalid choice. Try again.") # this is a message that appear if the choice is invalid
