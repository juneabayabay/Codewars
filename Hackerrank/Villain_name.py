from datetime import datetime # we import thefunction to get the current date and time
# we define a function to get the villain name based on the birthday
def get_villain_name(birthday):

    # First names based on the month
    first_names = [
        "The Evil", "The Vile", "The Cruel",
        "The Trashy", "The Despicable", "The Embarrassing",
        "The Disreputable", "The Atrocious", "The Twirling",
        "The Orange", "The Terrifying", "The Awkward"
    ] # the index of this is until 11 because there are 12 months index are always on 0

    # Last names based on the last digit
    last_names = [
        "Mustache", "Pickle", "Hood Ornament",
        "Raisin", "Recycling Bin", "Potato",
        "Tomato", "House Cat", "Teaspoon",
        "Laundry Basket"
    ]

    # Get the month and day
    month = birthday.month - 1
    day = birthday.day % 10

    # Combine and return the villain name
    return f"{first_names[month]} {last_names[day]}"


# Test the function
birthday = datetime(2004, 11, 18)

print(get_villain_name(birthday))

# Output: The Terrifying Teaspoon
