# EXERCISE: Create a function that adds two numbers together.

# "def" is used to create a function.
# "add_numbers" is the name of our function.
# "a" and "b" are parameters (the values we give to the function).
def add_numbers(a, b):

    # "return" sends the result back to wherever the function was called.
    return a + b


# Now we call (use) our function.
# We give it 5 and 3 as the values for a and b.
result = add_numbers(5, 3)

# Print the result so we can see it.
print(result)