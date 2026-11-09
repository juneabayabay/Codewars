
if __name__ == '__main__':
    n = int(input().strip())

    if n % 2 != 0:
        print("Weird")
    elif n >= 2 and n <= 5:
        print("Not Weird")
    elif n >= 6 and n <= 20:
        print("Weird")
    else:
        print("Not Weird")


# ==============================
# EXPLANATION OF THE CODE
# ==============================

# if = Conditional statement (checks if a condition is TRUE or FALSE)

# __name__ = Special built-in variable (stores the current module name)

# == = Equality comparison operator (checks if two values are equal)

# '__main__' = String value (special name when the Python file runs directly)

# : = Colon (indicates the beginning of a code block)


# n = Variable (stores the user's input)

# = = Assignment operator (assigns a value to a variable)

# int() = Built-in function (converts a value into an integer)

# input() = Built-in function (receives input from the user)

# . = Dot operator (accesses a method or attribute)

# strip() = String method (removes extra spaces at the beginning and end)


# if n % 2 != 0:

# if = Checks a condition

# % = Modulo operator (gets the remainder after division)

# 2 = Integer (divisor)

# != = Not equal operator (checks if two values are different)

# 0 = Integer zero

# Purpose: Checks if the number is ODD.

# Example: 7 % 2 = 1
# Since 1 is not equal to 0, the condition is TRUE.


# print("Weird")

# print() = Built-in function (displays output)

# "Weird" = String value (text to display)

# Purpose: Displays Weird if the number is odd.


# elif n >= 2 and n <= 5:

# elif = Else-if statement (checks another condition if the previous is FALSE)

# >= = Greater than or equal to

# 2 = Integer

# and = Logical operator (both conditions must be TRUE)

# <= = Less than or equal to

# 5 = Integer

# Purpose: Checks if the number is between 2 and 5.


# print("Not Weird")

# print() = Displays output

# "Not Weird" = String value

# Purpose: Displays Not Weird if the number is even and between 2 and 5.


# elif n >= 6 and n <= 20:

# elif = Checks another condition

# >= = Greater than or equal to

# 6 = Integer

# and = Both conditions must be TRUE

# <= = Less than or equal to

# 20 = Integer

# Purpose: Checks if the number is between 6 and 20.


# print("Weird")

# print() = Displays output

# "Weird" = String value

# Purpose: Displays Weird if the number is even and between 6 and 20.


# else:

# else = Executes when all previous conditions are FALSE.

# print("Not Weird")

# print() = Displays output

# "Not Weird" = String value

# Purpose: Displays Not Weird if the number is even and greater than 20.
