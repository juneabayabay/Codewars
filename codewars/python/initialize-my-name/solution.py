def initialize_names(name):
    # Split the full name into a list of words.
    # Example: "Lois Mary Lane" -> ["Lois", "Mary", "Lane"]
    parts = name.split()

    # If there are only 1 or 2 names (first name only, or first + last),
    # there are no middle names to initialize, so return the original name.
    if len(parts) <= 2:
        return name

    # Start the result list with the first name.
    # Example: ["Alice"]
    result = [parts[0]]

    # Loop through all the middle names.
    # parts[1:-1] means:
    #   Start at index 1 (the second word)
    #   Stop before the last word
    # Example:
    # ["Alice", "Betty", "Catherine", "Davis"]
    # becomes ["Betty", "Catherine"]
    for middle in parts[1:-1]:

        # Take only the first letter of each middle name
        # and add a period.
        # "Betty" -> "B."
        # "Catherine" -> "C."
        result.append(middle[0] + ".")

    # Add the last name to the result.
    # parts[-1] always refers to the last item in the list.
    result.append(parts[-1])

    # Join the list back into one string with spaces.
    # Example:
    # ["Alice", "B.", "C.", "Davis"]
    # becomes
    # "Alice B. C. Davis"
    return " ".join(result)
