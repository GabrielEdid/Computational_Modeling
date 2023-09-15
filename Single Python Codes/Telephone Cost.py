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
