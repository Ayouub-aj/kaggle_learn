# You have seen how to convert a float to an integer with the `int` function.  Try this out yourself by running the code cell below.

# Define a float
y = 1.
print(y)
print(type(y))

# Convert float to integer with the int function
z = int(y)
print(z)
print(type(z))

# Negative floats are always rounded UP to the closest integer (for instance, both -1.1 and -1.9 are rounded up to -1). 
# Positive floats are always rounded DOWN to the closest integer (for instance, 2.1 and 2.9 are rounded down to 2).