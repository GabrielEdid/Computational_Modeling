"""
Author: Gabriel Edid Harari
Date: August 30th 2022
Description: Factorial of X
"""
#variables section
limit = 0
count = 1
result = 1

#Process Starts Here
limit = int(input("Please give the X value: "))
#For Loop Starts Here
for count in range(1, limit+1, 1):
    print(count, end=" ")
    result = result * count
#For Loop Ends Here
print("\n The final result is:", result)
