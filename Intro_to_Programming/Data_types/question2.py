# In the tutorial, you learned about booleans (which can take a value of True or False),
# in addition to integers, floats, and strings. For this question, your goal is to determine what happens when you multiply a boolean by any of these data types. Specifically,

# What happens when you multiply an integer or float by True? 
# What happens when you multiply them by False? 
# How does the answer change if the numbers are positive or negative?
# What happens when you multiply a string by True? By False?

print(3 * True)
print(-3.1 * True)
print(type("abc" * False))
print(len("abc" * False))

# When you multiple an integer or float by a boolean with value True, it just returns that same integer or float (and is equivalent to multiplying by 1). 
# If you multiply an integer or float by a boolean with value False, it always returns 0. This is true for both positive and negative numbers. 
# If you multiply a string by a boolean with value True, it just returns that same string. 
# And if you multiply a string by a boolean with value False, it returns an empty string (or a string with length zero).