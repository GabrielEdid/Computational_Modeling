"""
Author: Gabriel Edid Harari
Date: September 1st 2022
Description: Number of the Year
"""
#variables section
month = 0
day = 0
count = 0
monthdays = 0
result = 0

#Process Starts Here
month = int(input("Please give the month of the year in number: "))
day = int(input("Please give the day of the month in number: "))
#For Loop Starts Here
for count in range(1,month,1):
    if count == 1 or count == 3 or count == 5 or count == 7 or count == 8 or count == 10 or count == 12:
        monthdays = 31
    elif count == 2:
        monthdays = 28
    elif count == 4 or count == 6 or count == 9 or count == 11:
        monthdays = 30
    result = result + monthdays
#For Loop Ends Here
print("The", month, "month and the", day, "day is the", result + day, "day of the year.")
#Code Ends Here