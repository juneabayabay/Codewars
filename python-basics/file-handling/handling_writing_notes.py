
note = input("Write your note: ")


with open("notes.txt", "r") as file:


    file.write(note + "\n")


print("Your note has been saved!")
