"""
Author: Gabriel Edid Harari
Date: September 1st 2022
Description: Even Numbers
"""
#variables section
number = 0
result = 0
count = 0
number1 = 0
#Process Starts Here
number = int(input("Please give the number of variables you want: "))
#For Loop Starts Here
for count in range(1, number+1):
    number1 = int(input("Please give a number: "))
    if number1%2==0:
       result = result + 1
    else:
        result = result
#For Loop Ends Here
print("There are", result, "even numbers.")
#Code Ends Here