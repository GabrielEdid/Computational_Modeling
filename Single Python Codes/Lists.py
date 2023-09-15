"""
Author: Gabriel Edid Harari
Date: October 4th 2022
Description: Lists
"""
#Variables
my_list = [0,0,0,0,0] #This Creates a List of 5 Zeros
second_list = [0]*5 #This is another way to create a list
elements = 0
counter = 0
replace_value = 0
#Code Starts Here
#---------> Update all the list
#Start of For Loop
for counter in range(len(my_list)):
    replace_value = int(input("Please give the new value: "))
    my_list[counter] = replace_value
#End of For Loop
which_one=int(input("Please give the value you want to replace: "))
replace_value = int(input("Please give the new value: "))
my_list[which_one] = replace_value
#---------> print the content of a list
print(my_list)

#Start of For Loop
#Phyton Way
for elements in my_list:
    print(elements, end=" ") #end= " " puts a space in between every number, otherwise they will print in the same line.

print() #This makes an Enter in between both loops/lines

#Universal Way
#Start of For Loop
for counter in range(len(my_list)):
    print("Element", counter+1,": ", my_list[counter])
#End of For Loop
 
my_list.remove(int(input("Which Value do You Want to remove: ")))
#Re-Do For Loop to see if it removed
#Start of For Loop
for counter in range(len(my_list)):
    print("Element", counter+1,": ", my_list[counter])
#End of For Loop