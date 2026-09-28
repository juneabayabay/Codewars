def letters_to_numbers(s):
    total = 0

    for char in s:
        if char.islower():
            total += ord(char) - ord('a') + 1
        elif char.isupper():
            total += (ord(char) - ord('A') + 1) * 2
        elif char.isdigit():
            total += int(char)

    return total