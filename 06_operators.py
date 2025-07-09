# Operators are used to perform operations on variables and values (duh)


# ------ BASIC MATH OPERATIONS -----
print(10 + 5)
print(10 - 5)
print(10 * 5)
print(10 / 5) # Returns 2.0 (a float), even though the result is a whole number

# ----- ADVANCED OPERATIONS -----
# Normal division for control
print(7 / 2)

# Modulus Operator
# The result will be the REMAINDER of a division operator
print(7 % 2)
# Since 7 / 2 would be 3 remainder 1, the statement will output 1

# Exponentiation Operator
print(7 ** 2)
# For any operation x ** y, the result will be equal to x to the power of y

# Floor Division
print(7 // 2)
# This gives the largest possible INTEGER that is less than or equal to the result of the division
# E.G. 7 / 2 = 3.5, closest integer would be 3

## ---------- CHALLENGES ----------
# 1. (MEDIUM)
# Create a program that asks the user for:
# How much money they have (money)
# How much a ticket costs (ticket_price)
# How much food will cost (food_cost)
# Then calculate the total expenses and money left after the trip
#
# Example Output:
# Enter your money: 1000
# Enter ticket price: 300
# Enter food cost: 250
#
# Total expenses: 550
# Money left: 450
#
# ----------------------------------------------------------------------------------------


#
# 2. (MEDIUM)
# Create a program that asks for 2 numerical inputs, and calculates
# their sum, difference, product, and quotient
#
# Example Output:
# Enter first number: 8
# Enter second number: 2
#
# Sum: 10
# Difference: 6
# Product: 16
# Quotient: 4.0
#
#
# -- hmmm i wonder what happens if you divide by zero?? --