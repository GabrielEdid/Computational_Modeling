"""
Author: Gabriel Edid Harari
Date: September 1st 2022
Description: Prime Numbers
"""
#variables section
number = 0
result = 0
count = 0
given_number = 0
#Process Starts Here
number = int(input("Please give the number of variables you want: "))
#For Loop Starts Here
for count in range(1, number+1):
    given_number = int(input("Please give a number: "))
    if given_number == 2:
        result = result + 1
    elif given_number%2 == 0:
        result = result 
    elif given_number%3 != 0 or given_number%5 != 0 or given_number%7 != 0 or given_number%11 != 0 or given_number%13 != 0:
        result = result + 1
#For Loop Ends Here
print("There are", result, "prime numbers.")
#Code Ends Here