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
