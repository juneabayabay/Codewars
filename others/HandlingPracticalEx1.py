
with open("notes.txt", "w") as file: # note.txt is the name of the file with "w" the mode which means write as file

    file.write("This is my first note.\n") # since this is write mode we are just writing the context based on your topic

    file.write("I am learning Python.\n")

    file.write("File handling is actually pretty cool!\n")



print("Notes saved!") # This line tell us the user that their notes have been saved
