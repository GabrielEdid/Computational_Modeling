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

           