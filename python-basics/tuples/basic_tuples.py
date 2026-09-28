# ==========================================
# BASIC KINDS OF TUPLES IN PYTHON
# ==========================================

# 1. Empty Tuple
# A tuple with no items
empty_tuple = ()

print("1. Empty Tuple:")
print(empty_tuple)


# 2. Single-Item Tuple
# A tuple with only one item.
# IMPORTANT: We need a comma after the item!
single_tuple = (10,)

print("\n2. Single-Item Tuple:")
print(single_tuple)


# 3. Multiple-Item Tuple
# A tuple containing several items
numbers = (10, 20, 30, 40)

print("\n3. Multiple-Item Tuple:")
print(numbers)


# 4. Tuple with Different Data Types
# A tuple can contain different kinds of data
mixed_tuple = (10, "Hello", 3.14, True)

print("\n4. Mixed Tuple:")
print(mixed_tuple)


# 5. Nested Tuple
# A tuple can contain other tuples
nested_tuple = ((1, 2), (3, 4))

print("\n5. Nested Tuple:")
print(nested_tuple)


# 6. Tuple Without Parentheses
# Parentheses are optional when creating a tuple
no_parentheses = 10, 20, 30

print("\n6. Tuple Without Parentheses:")
print(no_parentheses)


# 7. Creating a Tuple Using tuple()
# We can convert a list into a tuple
my_list = [1, 2, 3]
converted_tuple = tuple(my_list)

print("\n7. Tuple Using tuple():")
print(converted_tuple)


# ==========================================
# ACCESSING ITEMS IN A TUPLE
# ==========================================

fruits = ("apple", "banana", "orange")

print("\n--- Accessing Tuple Items ---")

print(fruits[0])  # First item
print(fruits[1])  # Second item
print(fruits[2])  # Third item


# ==========================================
# TUPLES ARE IMMUTABLE
# ==========================================

numbers = (10, 20, 30)

# This will cause an ERROR:
# numbers[0] = 100

# Why?
# Because we cannot change an existing item in a tuple.

print("\nTuples cannot be changed after creation.")
