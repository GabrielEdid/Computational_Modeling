"""
Author: Gabriel Edid Harari
Date: August 21st 2022
Description: Check If Price is Valid
"""
#variables section
priceA = 0

#Code Starts Here... Start my Process
priceA= float(input("Please give the price: "))
if priceA>=0:
    print("The price is valid")
else:
    print("The price is invalid")
#Code Finishes Here


"""
Author: Gabriel Edid Harari
Date: August 21st 2022
Description: Calculate Meters to Feet
"""
#variables section
meters = 0
feet = 3.28084
result = 0

#Code Starts Here... Start my Process
meters = float(input("Please give a measure in meters: "))
result = meters*feet
print(meters, "meters is", result, "feet.")
#Code Finishes Here


"""
Author: Gabriel Edid Harari
Date: August 21st 2022
Description: Car's Average Speed
"""
#variables section
time = 0
distance = 0
result = 0

#Code Starts Here... Start my Process
time = float(input("Please give the time the car has been traveling in Hours: "))
distance = float(input("Please give the distance the car has traveled in Kilometers: "))
result = distance/time
print("The speed of the car is", result, "km/h")
#Code Finishes Here


"""
Author: Gabriel Edid Harari
Date: August 21st 2022
Description: Driver's License
"""
#variables section
age = 0
document = 0

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