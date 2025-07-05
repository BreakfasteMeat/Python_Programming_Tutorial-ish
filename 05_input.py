# To accept user inputs, you do this:

input_variable = input()
print(input_variable)

# When the code is ran, you can type anything in the console
# Once you press enter, what you have typed will be stored
# in the variable (in this case input_variable) as a String
# E.G. typing "abc 123" into it will store "abc 123" into the input_variable variable

number = int(input("Enter a number: "))
print("Your number", number,"plus 5 is :", number + 5)

# In this example, a message will be displayed right before allowing the user
# to input any value
# You can also cast the input itself to restrict only storing a specific datatype
# instead of defaulting to a String Datatype

# !! DO NOTE THAT INPUTTING INVALID CHARACTERS INTO A CAST INPUT WILL CAUSE ERRORS !!
# !! E.G. TYPING 'ABCDEFGHIJ' INTO AN INPUT THAT IS CAST INTO AN INTEGER DATA TYPE !!

## ---------- CHALLENGES ----------
# 1. (EASY)
# Ask the user for their first name, last name, and favorite color. Then print a sentence using all three.
# Example Output:
# What is your first name?: Alex
# What is your last name?: Rivera
# What is your favorite color?: Blue
#
# Hello, Alex Rivera! Your favorite color is Blue.
#
# --------------------------------------------------------------------------------------------------------------------------------------------
#
# 2. (MEDIUM)
# Ask the user to type any object, then ask what sound it makes. Finally, print a fun machine-style output showing the object and the sound.
# Enter any object: cat
# What sound does it make? meow
#
# [ Booting Sound Machine... ]
# Detected object: cat
# Emitting sound: meow! meow! meow!

