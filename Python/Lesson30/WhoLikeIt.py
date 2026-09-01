def likes(names):
    # We check how many people are in the list because the
    # sentence changes depending on whether there are 0, 1, 2, 3,
    # or 4+ people.

    if len(names) == 0:
        # If nobody liked it, return this exact message.
        return "no one likes this"

    elif len(names) == 1:
        # If exactly one person liked it, use their name.
        return f"{names[0]} likes this"

    elif len(names) == 2:
        # With two people, put "and" between their names.
        return f"{names[0]} and {names[1]} like this"

    elif len(names) == 3:
        # With three people, separate the first two names with commas
        # and put "and" before the final name.
        return f"{names[0]}, {names[1]} and {names[2]} like this"

    else:
        # For 4 or more people, show the first name, the second name,
        # and then say how many additional people liked it.
        # Example:
        # ["Alex", "Jacob", "Mark", "Max"]
        # becomes:
        # "Alex, Jacob and 2 others like this"
        return f"{names[0]}, {names[1]} and {len(names) - 2} others like this"
