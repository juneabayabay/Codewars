text = " My name is June"

vowels = "aeiou"
count = 0

for character in text.lower():
    if character in vowels:
      count += 1

print("Numbers of vowels:", count)

# Output:
# Numbers of vowels: 5
