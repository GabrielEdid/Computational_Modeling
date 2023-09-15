"""
Author: Gabriel Edid Harari
Date: August 30th 2022
Description: For Loop Example Version 1
"""
#variables section
number = 0
result = 0 #this is my acum variable
count = 0 #my control variable
limit = 0

#Process Starts Here
limit = int(input("Please enter the amount of numbers you want to sum: "))

for count in range(limit):
    number = float(input("Please enter a number " + str(count+1) + ": "))
    result = result + number
#end of my loop
print("The sum of the", limit, "numbers is:", result)
#Code Finishes Here

