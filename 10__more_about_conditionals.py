

value = 100

if(value < 50):
    print("Less than half")
elif(value > 50 and value < 100):
    print("More than half")
elif(value == 50):
    print("At the halfway point")
elif(value == 100):
    print("Whew, almost overflowed")
elif(value >= 100):
    print("There is too much!")

print("Value evaluation done!")


# In this example, even if 100 satisfies both of the last 2 elif statements (assuming you did not change the value yet),
# it evaluates the "value == 100" first, and since in the elif chain, it has evaluated
# a statement once, it will no longer evaluate any succeeding value checks, and
# immediately terminates outside the elif chain, continuing to the rest of the code

# Also observe how we used boolean arithmetic in the 2nd value check!

# Now, try changing around the values!

