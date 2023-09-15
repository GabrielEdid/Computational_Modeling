"""
Author: Gabriel Edid Harari
Date: August 26th 2022
Description: Area of a Triangle
"""
#variables section
base = 0
height = 0
result = 0

#Process Starts Here
base = float(input("Please give the size of the base of the triangle (in meters):"))
height = float(input("Please give the size of the height of the triangle (in meters):"))
result = (base * height) / 2
print("The area of the triangle is:", result)
#Code Finishes Here

"""
Author: Gabriel Edid Harari
Date: August 26th 2022
Description: Average of 4 Subjects
"""
#variables section
grade_1 = 0
grade_2 = 0
grade_3 = 0
grade_4 = 0
result = 0

#Process Starts Here
grade_1 = float(input("What’s the grade of your first class? "))
grade_2 = float(input("What’s the grade of your second class? "))
grade_3 = float(input("What’s the grade of your third class? "))
grade_4 = float(input("What’s the grade of your last class? "))
result = (grade_1 + grade_2 + grade_3 + grade_4) / 4
print("The average of your four classes is:", result)
#Code Finishes Here

"""
Author: Gabriel Edid Harari
Date: August 26th 2022
Description: 100 Years 
"""
#variables section
age = 0
year = 0
years_100 = 0
result = 0

#Process Starts Here
age = int(input("What is your age: "))
year = int(input("What year are we in: "))
while age or year < 0:
    print("Both numbers have to be Positive!")
    age = int(input("Please give your age again (Make sure it’s a positive number!): "))
    year = int(input("Please tell me what year are we in (Make sure it’s a positive number!): "))
years_100 = 100 - age
result = year + years_100
if years_100 <= 0:
    print("You are already 100 years old!")
else:
    print("You will be 100 years old in", result)
#Code Finishes Here

"""
Author: Gabriel Edid Harari
Date: August 26th 2022
Description: Decades 
"""
#variables section
age = 0
year_of_birth = 0
decades = 0
result = 0

#Process Starts Here
year_of_birth = int(input("What year were your born: "))
year = int(input("What year are we in: "))
while year_of_birth and year < 0:
    print("Both numbers have to be Positive!")
    year_of_birth = int(input("Please tell me what year were you born (Make sure it’s a positive number!): "))
    year = int(input("Please tell me what year are we in (Make sure it’s a positive number!): "))
decades = year - year_of_birth
result = decades/10
print(result)
#Code Finishes Here

"""
Author: Gabriel Edid Harari
Date: August 26th 2022
Description: Weight 
"""
#variables section
starting_weight = 0
goal_weight = 0
months = 0
result = 0

#Process Starts Here
print("Hello! Let’s see how much weight you should lose!")
starting_weight = float(input("Please tell me your actual weight: "))
goal_weight = float(input("Please tell me your goal weight: "))
months = int(input("Please tell me for how many months you’re going to be trying to lose weight: "))
result = (starting_weight - goal_weight)/months
print("You will need to lose", result, "per month.")
#Code Finishes Here

"""
Author: Gabriel Edid Harari
Date: August 26th 2022
Description: Slope of a Line 
"""
#variables section
X1 = 0
Y1 = 0
X2 = 0
Y2 = 0
result = 0

#Process Starts Here
print("Let’s calculate the slope between two points!")
X1 = float(input("Please give the X coordinate of your first point: "))
Y1 = float(input("Please give the Y coordinate of your first point: "))
X2 = float(input("Please give the X coordinate of your second point: "))
Y2 = float(input("Please give the Y coordinate of your second point: "))
result = (Y2 - Y1) / (X2 -X1)
print("The slope between (", X1, ",",Y1,") and (", X2, ",", Y2, ") is", result)
#Code Finishes Here

"""
Author: Gabriel Edid Harari
Date: August 26th 2022
Description: Distance Traveled by a Snail 
"""
#variables section
minutes = 0
result = 0

#Process Starts Here
print("Let's see how many centimiters will a snail travel!")
minutes = int(input("For how many minutes will the snail be traveling? "))
result = ((minutes * 60) * 5.7) / 10
print("The snail will travel", result, "cm.")
#Code Finishes Here

"""
Author: Gabriel Edid Harari
Date: August 26th 2022
Description: Telephone Cost 
"""
#variables section
messages = 0
megabytes = 0
minutes = 0
result = 0

#Process Starts Here
messages = int(input("How many messages have you sent? "))
megabytes = float(input("How many megabytes have you consumed? "))
minutes = int(input("How many minutes have you consumed? "))
result = (messages + megabytes + minutes) * 0.80
print("Your Telephone Plan cost is:", result)
#Code Finishes Here

"""
Author: Gabriel Edid Harari
Date: August 26th 2022
Description: Cement Cost 
"""
#variables section
number_of_bags = 0
price_per_bag = 0
result = 0 
taxes = 0
price_with_tax = 0

#Process Starts Here
price_per_bag = float(input("How much is the price per cement bag? "))
number_of_bags = int(input("How many bags of cement will you need? " ))
result = price_per_bag * number_of_bags
print("The price before taxes is:", result)
taxes = (result * 16)/100
print("The 16% tax will be:", taxes)
price_with_tax = result + taxes
print("The price of", number_of_bags, "bags of cement is:", price_with_tax)
#Code Finishes Here

"""
Author: Gabriel Edid Harari
Date: August 26th 2022
Description: Video Game 
"""
#variables section
new_games = 0
old_games = 0
result = 0

#Process Starts Here
print("Hello! Welcome to GameStore!")
new_games = int(input("How many new games did you pick? "))
old_games = int(input("How many old games did you pick? "))
result = (new_games * 1000) + (old_games * 350)
print("Your total for", new_games, "new games and", old_games, "old games is", result, "$.")
#Code Finishes Here
