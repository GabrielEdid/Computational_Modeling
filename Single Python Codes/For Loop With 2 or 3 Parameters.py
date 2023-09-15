"""
Author: Gabriel Edid Harari
Date: August 30th 2022
Description: For Loop With 2 or 3 Parameters
"""
#variables section
count = 0 
limit = 0

#Process Starts Here
limit = int(input("Please give the limit: "))
for count in range(0,limit+1,2): #First one is where we start, second is the limit, third one is by how many it goes (1 by 1, 2 by 2, etc...)
    print(count)