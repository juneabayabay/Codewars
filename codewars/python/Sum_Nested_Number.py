
def sum_nested_numbers(arr, level=1):
    # We create a function named sum_nested_numbers.
    # arr receives the nested array (list).
    # level = 1 means we start at nesting level 1.

    total = 0
    # We create a variable to store the total sum.
    # It starts at 0.

    for item in arr:
        # We loop through every item in the array.
        # item represents the current element.

        if isinstance(item, list):
            # We check if the current item is another list.
            # If true, we found a nested list.

            total += sum_nested_numbers(item, level + 1)
            # We call the same function again (recursion).
            # We pass the nested list as the new argument.
            # We increase the nesting level by 1.

        else:
            # If the item is not a list, it is a number.

            total += item ** level
            # We raise the number to its nesting level.
            # Example: 2 ** 2 = 4.
            # We add the result to total.

    return total
    # Return the final sum.


# Example:
print(sum_nested_numbers([1, [2], 3, [4, [5]]]))

# Expected output: 149
# 1 + 2² + 3 + 4² + 5³ = 149
