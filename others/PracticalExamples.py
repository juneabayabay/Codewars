# The program ask the user for their name and a sentence, then it cleans the input and display information about it.

name = input("Enter you name: ")
sentence = input("Enter a sentence: ")

name = name.strip() 
sentence = sentence.strip()
# in this part if the data is not organized it will automatically clean, same thing is Sentence variable name

# creating aformatted greeting.
print(f"\nHello, {name.title()}!")

# show the number of characters
print("Number of characters:", len(sentence))

# conver the sentence to  and uppercase
lower_sentence = sentence.lower()
upper_sentence = sentence.upper()

print("Lowercase: ", lower_sentence)
print("uppercase: ", upper_sentence)

# printing the number of words
words = sentence.split()
print("Numbers of words ", len(words))

print("Reversed: ", sentence[::-1])

if "python" in lower_sentence:
  print("The sentence contains the word 'Python'.")
else:
  print("The sentence does not contain the word 'Python'.")

vowels = "aieuo"
vowel_count = 0

for character in lower_sentence:
  if character in vowels:
    vowel_count += 1

print("Number of vowels:", vowel_count)

print("\n==============================")
print("        PROGRAM END")
print("==============================")


# OURPUT
# Enter your name: June abay abay
# Enter a sentence: Jesus Christ is my savior and refuge
#
# Hello, June Abay Abay!
# Number of characters: 36
# Lowercase: jesus christ is my savior and refuge
# Uppercase: JESUS CHRIST IS MY SAVIOR AND REFUGE
# Number of words: 7
# Reversed: egufer dna roivas ym si tsirhC suseJ
# The sentence does not contain the word 'Python'.
# Number of vowels: 11
#
# ==============================
#         PROGRAM END
# ==============================
#
# === Code Execution Successful ===




