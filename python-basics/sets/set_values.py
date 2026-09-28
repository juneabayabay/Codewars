# CREATING A SET

numbers = {1, 2, 3, 4}
print(numbers)

# EMPTY SET

empty = set()

# set() creates an empty set
print(empty)


# -----------------------------
# DUPLICATES
# -----------------------------

nums = {1, 2, 2, 3}

# The second 2 is removed automatically
# because sets do not allow duplicates
print(nums)

# Output:
# {1, 2, 3}


# -----------------------------
# ADDING A VALUE
# -----------------------------

numbers.add(5)

# add() puts a new value into the set
print(numbers)

# Output:
# {1, 2, 3, 4, 5}


# -----------------------------
# REMOVING A VALUE
# -----------------------------

numbers.remove(2)

# remove() removes 2 from the set
print(numbers)

# Output:
# {1, 3, 4, 5}


# -----------------------------
# DISCARDING A VALUE
# -----------------------------

numbers.discard(10)

# discard() tries to remove 10
# 10 is not in the set
# So, nothing happens and NO ERROR occurs
print(numbers)

# Output:
# {1, 3, 4, 5}
