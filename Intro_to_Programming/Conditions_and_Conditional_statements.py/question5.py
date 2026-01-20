# In Mexico, foods and beverages that are high in saturated fat, trans fat, sugar, sodium,
# and/or calories appear with warning labels that are designed to help consumers make healthy food choices.

# For instance, the box of cookies in the image below appears with two labels (in the upper right corner):

# EXCESO CALORÍAS (in English, EXCESS CALORIES)
# EXCESO AZÚCARES (in English, EXCESS SUGAR)


# In this question, you'll work with a function get_labels() that takes the nutritional details about a food item and prints the needed warning labels. 
# This function takes several inputs:

# food_type = one of "solid" or "liquid"
# serving_size = size of one serving (if solid, in grams; if liquid, in milliliters)
# calories_per_serving = calories in one serving
# saturated_fat_g = grams of saturated fat in one serving
# trans_fat_g = grams of trans fat in one serving
# sodium_mg = mg of sodium in one serving
# sugars_g = grams of sugar in one serving


# Note that some of the code here should feel unfamiliar to you, since we have not shared the details of how some of the functions like excess_sugar() or excess_saturated_fat() work. 
# But at a high level, these are functions that return a value of True if the food is deemed to have an excess of sugar or saturated fat, respectively. 
# These functions are used within the get_labels() function, and whenever there is an excess (of sugar or saturated fat, but also of trans fat, sodium, or calories), 
# it prints the corresponding label.

# import functions needed to make get_labels work
from learntools.intro_to_programming.ex4q5 import excess_sugar, excess_saturated_fat, excess_trans_fat, excess_sodium, excess_calories

def get_labels(food_type, serving_size, calories_per_serving, saturated_fat_g, trans_fat_g, sodium_mg, sugars_g):
    # Print messages based on findings
    if excess_sugar(sugars_g, calories_per_serving) == True:
        print("EXCESO AZÚCARES / EXCESS SUGAR")
    if excess_saturated_fat(saturated_fat_g, calories_per_serving) == True:
        print("EXCESO GRASAS SATURADAS / EXCESS SATURATED FAT")
    if excess_trans_fat(trans_fat_g, calories_per_serving) == True:
        print("EXCESO GRASAS TRANS / EXCESS TRANS FAT")
    if excess_sodium(calories_per_serving, sodium_mg) == True:
        print("EXCESO SODIO / EXCESS SODIUM")
    if excess_calories(food_type, calories_per_serving, serving_size) == True:
        print("EXCESO CALORÍAS / EXCESS CALORIES")

# bologna https://world.openfoodfacts.org/product/4099100179378/bologna
get_labels("solid", 32, 110, 2.5, 0, 400, 1)
# Output:

# EXCESO GRASAS SATURADAS / EXCESS SATURATED FAT
# EXCESO SODIO / EXCESS SODIUM
# EXCESO CALORÍAS / EXCESS CALORIES

# This bologna has three labels, printed in the output above.

# For the rest of this question, you will use the same get_labels() function to determine the labels for more foods. 
# This question is designed to help you get practice with feeling comfortable with code that other people have written, 
# and where you don't have time to review every single line of code before interacting with it. For instance, 
# when you take the Intro to Machine Learning course, you'll work with a Python package called "scikit-learn", '
# 'which is a large collection of code that you'll learn how to run without reviewing all of the code in detail 
# (as it would take too long, and you can trust that it was implemented correctly).

# In general, as you continue coding in Python, you will often be running code that other people have written. 
# This is common practice for advanced programmers.
# In the next code cell, fill in the values for this cereal. Here is an image with all of the nutritional information.
# Note: running the line of code below as-is will return an error. You have to fill in the nutritional values first.

# zucaritas cereal https://world.openfoodfacts.org/product/7501008023624/zucaritas-kellogg-s
get_labels("solid", 40, 647, 0, 0, 150, 6.4)
# Output:

# EXCESO CALORÍAS / EXCESS CALORIES

# mozzarella sticks https://world-es.openfoodfacts.org/producto/0062325540104/mozzarella-cheese-sticks
get_labels("solid", 21, 68, 3, 0.2, 202, 0)
# Output:

# EXCESO GRASAS SATURADAS / EXCESS SATURATED FAT
# EXCESO GRASAS TRANS / EXCESS TRANS FAT
# EXCESO SODIO / EXCESS SODIUM
# EXCESO CALORÍAS / EXCESS CALORIES

# pillsbury cookies https://world.openfoodfacts.org/product/0069700118545/biscuits-au-sucre-pretraches
get_labels("solid", 30, 120, 1.5, 0.1, 110, 9)
# Output:

# EXCESO AZÚCARES / EXCESS SUGAR
# EXCESO GRASAS SATURADAS / EXCESS SATURATED FAT
# EXCESO CALORÍAS / EXCESS CALORIES

# sunkist orange soda https://world-es.openfoodfacts.org/producto/0078000113464/orange-soda-sunkist
get_labels("liquid", 355, 160, 0, 0, 0.65, 44)
# Output:

# EXCESO AZÚCARES / EXCESS SUGAR