"""
Author: Gabriel Edid Harari
Date: September 1st 2022
Description: Biggest Number
"""
#variables section
number = 0
result = 0
given_number = 0

#Process Starts Here
number = int(input("Please give the number of variables you want: "))
#For Loop Starts Here
for result in range(1, number+1):
    given_number = int(input("Please give a number: "))
    if given_number > result:
       result = given_number
#For Loop Ends Here
print("The Biggest number is:", result)
#Code Ends Here