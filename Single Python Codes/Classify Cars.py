"""
Author: Gabriel Edid Harari
Date: September 1st 2022
Description: Classify Cars
"""
#variables section
count = 0
limit = 0
result = 0
hybrid = 0
gas = 0
electric = 0
cars = 0
#Process Starts Here
limit = int(input("How many cars do you want to classify? "))
print("For a Hybrid Car Press H, for a Gas Car Press G and for an Electric Car Press E")
#For Loop Starts Here
for count in range(1,limit+1,1):
    cars = input("What type of car is it? ")
    if cars == "H" or cars == "h":
        hybrid = hybrid + 1
    elif cars == "G" or cars == "g":
        gas = gas + 1
    elif cars == "E" or cars == "e":
        electric = electric + 1
#For Loop Ends Here
print("There are", hybrid, "Hybrid cars.")
print("There are", gas, "Gas cars.")
print("There are", electric, "Electric cars.")
#Code Ends Here