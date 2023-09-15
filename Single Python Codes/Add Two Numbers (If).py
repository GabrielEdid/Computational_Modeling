"""
Author: Gabriel Edid Harari
Date: August 19th 2022
Description: This is my first program in Gerardo's class
"""
#variables section
numberA = 0
numberB = 0
result = 0

#Code Starts Here... Start my Process
numberA = int(input("Please give a Number: "))
if numberA > 0:
    numberB = int(input("Please give a second Number: "))
else:
    print('All Numbers Must be Positive')
    numberA = int(input("Please give a Number again: "))
    numberB = int(input("Please give a second Number: "))
result = numberA + numberB
print('The Result is:', result, '.')
#Code Finishes Here
