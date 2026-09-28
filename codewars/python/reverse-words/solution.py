def reverse_words(text):
    # Split the string by spaces (keeps multiple spaces)
    words = text.split(" ")

    # Create a new list for the reversed words
    reversed_words = []

    # Reverse each word
    for word in words:
        reversed_words.append(word[::-1])

    # Join the words back together with spaces
    return " ".join(reversed_words)
