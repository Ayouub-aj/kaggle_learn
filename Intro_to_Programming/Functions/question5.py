# Now say you can no longer buy fractions of a gallon. (For instance, if you need 4.3 gallons to do a project, then you have to buy 5 gallons of paint.)

# With this new scenario,
# you will create a new function get_actual_cost that uses the same inputs and calculates the cost of your project.

# One function that you'll need to use to do this is math.ceil(). 
# We demonstrate usage of this function in the code cell below. 
# It takes as a number as input and rounds the number up to the nearest integer.

# Run the next code cell to test this function for yourself. 
# Feel free to change the value of test_value and make sure math.ceil() returns the number you expect.

#you should import math module here to use math.ceil()

import math

# test_value = 2.17

# rounded_value = math.ceil(test_value)
# print(rounded_value)

def get_actual_cost(sqft_walls, sqft_ceiling, sqft_per_gallon, cost_per_gallon):
    total_sqft     = sqft_walls + sqft_ceiling
    cost_sqft      = total_sqft / sqft_per_gallon
    gallon_needed = math.ceil(cost_sqft)
    cost           = gallon_needed * cost_per_gallon
    return cost

print(get_actual_cost(432, 144, 400, 15))
print(get_actual_cost(594, 288, 400, 15))

    
# Check your answer
# q5.check()