"""
Author: Gabriel Edid
Date: October 21, 2022
Description: Final Exam - Sales by Quarter
"""

#Variables Section Starts Here
my_list = [["Q1",1164,1000],["Q2",2341,9050],["Q3",1233,3564],["Q4",6587,6500]]
all_replace = 0
to_replace = 0
one_or_the_other = 0
new_value = 0
#Variables Section Ends Here

#Process Starts Here
#The program asks the user the value he wants all the numbers to be repalced with 
all_replace = int(input("Please give the value you want to replace everything with "))

#For loop starts here, this will go value by value and replace all of them to the input by the user
for quarter in my_list:
    for element in quarter:
        if element == quarter[1]:
            quarter[1] = all_replace
            quarter[2] = all_replace
#For loop ends here


#For loop starts here, This will go value by value and print the upadated table with the replace value of the user
for quarter in my_list:
    for element in quarter:
        if element == quarter[0]:
            print(element, end = " | ")
        elif element == quarter[1]:
            print("Sales:", element, end = " | ")
        elif element == quarter[2]:
            print("Sales:", element, end = " | ")
    #Print a space for it to look nice
    print()
#For loop ends here

#Inputs for the program to work with and to know what to change        
to_replace = input("Please write the quarter where you want to change: ").upper()
one_or_the_other = int(input("Please write if you want to update the value from 2020 or 2021: "))
new_value = int(input("What will be the new value: "))

#For loop starts here and goes product by product and looks for the value to change
for quarter in my_list:
    for element in quarter:
        #if the product is found the value will be repalced printed
        if element == to_replace:
            indx = my_list.index(quarter)
            print(element, end = " | ")
            if one_or_the_other == 2020:
                indx2 = quarter.index(element) + 1
                quarter[1] = new_value
            elif one_or_the_other == 2021:
                quarter[2] = new_value
        #Now it will go element by element and print it according to its index for them to be in the correct column
        elif element == new_value:
            print("Sales: ", element, end = " | ")
        elif element == quarter[0]:
            print(element, end = " | ")
        elif element == quarter[1] or element ==  quarter[2]:
            print("Sales:", element, end = " | ")
    #Print a space for it to look nice
    print()
#For loop ends here
            
#Process Ends Here               


    


        
            
        
        
