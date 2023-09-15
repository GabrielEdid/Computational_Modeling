"""
Author: Gabriel Edid Harari
Date: August 21st 2022
Description: Homework on Algorithms
"""
#variables section
age = 0
document = ""

#Code Starts Here... Start my Process
age = int(input("What's your age? "))
if age >= 18:
    print("Great! Just one more thing.")
else:
    print("I’m sorry you can’t get a Driver’s License yet. You must be at least 18 years old.")
    exit()
document = input("Did you bring your ID? ")
if document == "Yes" or document == "yes":
    print("Great! You’re all set! Please go to the next window to process your Driver's License.")
else:
    print("Yikes! You must bring an ID with you, please come back later.")
    exit()
#Code Finishes Here
