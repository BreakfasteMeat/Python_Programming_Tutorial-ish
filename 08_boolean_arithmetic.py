# In boolean arithmetic, there are three operators mainly used
# AND, OR, and NOT
# This is used in conjunction with TWO boolean values (or even boolean statements!)

# AND Operator
# Returns True if both operands are True, otherwise False
print('-------- AND OPERATOR ---------')
print(True and True)
print(True and False)
print(False and False)



print('-------- OR OPERATOR ---------')
# OR Operator
# Returns True if AT LEAST ONE operand is True, otherwise False
print(True or True)
print(True or False)
print(False or False)


print('-------- NOT OPERATOR ---------')
# NOT Operator
# Inverts the Boolean value of its operand
print(not True)
print(not False)

# Example:
# You can go outside IF it’s not raining AND you finished your homework
raining = False
homework_done = True
can_go_out = not raining and homework_done
print("Can go out:", can_go_out)  # True

# --- OPERATOR PRECEDENCE ---
# Just like how math has PEMDAS, we also have that in Boolean Arithmetic
# the order of evaluation is:

# 1. NOT
# 2. AND
# 3. OR

print(True or False and False)  # Evaluates as True or (False and False) -> True
# Since AND has a higher precedence, it is evaluated first before evaluating OR
