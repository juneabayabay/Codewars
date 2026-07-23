def remove_smallest(numbers):
    # If the list is empty, return an empty list.
    if not numbers:
        return []

    # Find the smallest number in the list.
    smallest = min(numbers)

    # Find the position (index) of the first smallest number.
    index = numbers.index(smallest)

    # Make a copy so we don't change the original list.
    result = numbers.copy()

    # Remove the smallest number using its index.
    result.pop(index)

    # Return the new list.
    return result


# --------------------
# Test Examples
# --------------------

print(remove_smallest([1, 2, 3, 4, 5]))   # [2, 3, 4, 5]

print(remove_smallest([5, 3, 2, 1, 4]))   # [5, 3, 2, 4]

print(remove_smallest([2, 2, 1, 2, 1]))   # [2, 2, 2, 1]

print(remove_smallest([]))                # []
