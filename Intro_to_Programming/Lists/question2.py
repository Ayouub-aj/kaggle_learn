# The list num_customers contains the number of customers who came into your restaurant every day over the last month (which lasted thirty days). 
# Fill in values for each of the following:

# avg_first_seven - average number of customers who visited in the first seven days
# avg_last_seven - average number of customers who visited in the last seven days
# max_month - number of customers on the day that got the most customers in the last month
# min_month - number of customers on the day that got the least customers in the last month
# Answer this question by writing code. For instance, if you have to find the minimum value in a list, use min() instead of scanning for the smallest value and directly filling in a number.

# Do not change: Number of customers each day for the last month
num_customers = [137, 147, 135, 128, 170, 174, 165, 146, 126, 159,
                 141, 148, 132, 147, 168, 153, 170, 161, 148, 152,
                 141, 151, 131, 149, 164, 163, 143, 143, 166, 171]

# TODO: Fill in values for the variables below
avg_first_seven = sum(num_customers[:7]) / 7
avg_last_seven = sum(num_customers[-7:]) / 7
max_month = max(num_customers)
min_month = min(num_customers)

#run on your own terminal to see results

print(avg_first_seven)
print(avg_last_seven)
print(max_month)
print(min_month)