def words_to_marks(word):
    total = 0

    for letter in word:
        total += ord(letter) - ord('a') + 1

    return total


# Example usage
print(words_to_marks("love"))        # 54
print(words_to_marks("friendship"))  # 108
print(words_to_marks("attitude"))    # 100