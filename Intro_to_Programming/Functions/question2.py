# You are thinking about buying a home and want to get an idea of how much you will spend, based on the number of bedrooms and bathrooms. You are trying to decide between four different options:

# Option 1: house with two bedrooms and three bathrooms
# Option 2: house with three bedrooms and two bathrooms
# Option 3: house with three bedrooms and three bathrooms
# Option 4: house with three bedrooms and four bathrooms
# Use the get_expected_cost() function you defined in question 1 to set option_1, option_2, option_3, and option_4 to the expected cost of each option.

# TODO: Use the get_expected_cost function to fill in each value
#from question 1 import get_expected_cost to run this file independently

# def get_expected_cost(beds, baths):
#     value = 80000 + (beds * 30000) + (baths * 10000)
#     return value

option_one = get_expected_cost(2, 3)
option_two = get_expected_cost(3, 2)
option_three = get_expected_cost(3, 3)
option_four = get_expected_cost(3, 4)

print(option_one)
print(option_two)
print(option_three)
print(option_four)

# Check your answer
#q2.check()