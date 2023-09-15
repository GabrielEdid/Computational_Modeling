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
