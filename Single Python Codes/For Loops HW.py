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


"""
Author: Gabriel Edid Harari
Date: September 1st 2022
Description: Even Numbers
"""
#variables section
number = 0
result = 0
count = 0
number1 = 0
#Process Starts Here
number = int(input("Please give the number of variables you want: "))
#For Loop Starts Here
for count in range(1, number+1):
    number1 = int(input("Please give a number: "))
    if number1%2==0:
       result = result + 1
    else:
        result = result
#For Loop Ends Here
print("There are", result, "even numbers.")
#Code Ends Here


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
    elif given_number%3 or 5 or 7 or 11 or 13 == 0:
        result = result + 1
#For Loop Ends Here
print("There are", result, "prime numbers.")
#Code Ends Here