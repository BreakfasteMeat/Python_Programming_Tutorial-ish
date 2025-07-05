x = 5
y = 6
hello = 'Hello'
world = 'World'
# Variables can be outputted using the print function

print(x)
print(y)

# To output multiple variables in the same print statement, separate it with a comma
print(x,y)
print(hello,world)

# - THE + OPERATOR
print(3 + 5)  # OUTPUT: 8 (numeric addition)
print('3' + '5')  # OUTPUT: "35" (string concatenation)

# The + Operator works differently when used between numeric data types and strings
# For numeric, it adds both the values, as if it is doing normal addition (more in 06_operators)
# For strings, it 'merges' both strings. This process is called String Concatenation

# But be careful, using the + Operator on a string and an Integer will cause an error

# print("Number: " + first_number)  # This will cause a TypeError
# Instead, cast it:
print("Number: " + str(first_number))


# - CASTING -
# This allows the conversion of one data type to another

first_number = 21
second_number = 32

print(first_number + second_number)      # Output: 53 (numeric addition)
print(str(first_number) + str(second_number))  # Output: "2132" (string concatenation)

# int() - converts to integer
# float() - converts to decimal number
# str() - converts to string



# -- Notes --
# Although '+' and ',' are used the same in some case, it is worth to point out that
# '+' String concatenation does not automatically add a space between the two strings, while
# ',' does add a space in between
