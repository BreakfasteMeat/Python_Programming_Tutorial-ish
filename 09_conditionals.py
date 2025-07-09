# !! MUST UNDERSTAND BOOLEANS AND EVALUATING BOOLEAN ARITHMETIC BEFORE CONTINUING !!
# (things are aboutta get complicated here)

# If statements can be used to run sections of code when a statement is true

x = 10
y = 5

# In Python, indentation (usually 4 spaces) defines what code belongs to each block.
# In other languages (C, Java) code blocks are defined by {} instead

if x < y:
    print("x is less than y") # This is a separate code block from the others because of the indent
elif x > y:
    print("x is greater than y")
else:
    print("x is equal to y")

# Statement/s in the if statement runs if the statement is true
# If the first statment is false, it will evaluate the next elif statement
# if none of the if and elif statments is true, it will then run the else statement

# Another example

temp = 30
if temp > 35:
    print("It's too hot!")
elif temp < 15:
    print("It's too cold!")
else:
    print("Weather is nice.")

# I suggest changing the values around and experiment!

