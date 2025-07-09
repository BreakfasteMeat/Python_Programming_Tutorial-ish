# !! MUST UNDERSTAND CONDITIONALS FIRST !!
# (Things boutta be extra complicated)

age = 18
has_id = True

if age >= 18:
    if has_id: # Has an indent, is part of the "age >= 18" block
        print("You can enter.") # another indent! this is in the "has_id" block
    else:
        print("You need an ID to enter.")
else:
    print("You are too young to enter.")

# You can put conditional statements inside other conditional statements!
# This is called "nesting".
# Make sure to use correct indentation to show which blocks belong together.
# In Python, indentation (usually 4 spaces) tells the interpreter what code is inside which block.
# Without proper indentation, Python will give an error or run the code incorrectly.

# Nesting has no limit! so you can get code that looks like this:

username = "admin"
password = "1234"
has_2fa = True
security_question_answer = "blue"

if username == "admin":
    if password == "1234":
        if has_2fa:
            if security_question_answer.lower() == "blue":
                print("Access granted. All checks passed.")
            else:
                print("Security question answer incorrect.")
        else:
            print("Access denied. 2FA is required.")
    else:
        print("Incorrect password.")
else:
    print("Unknown user.")

# This is nested 4 levels deep!


