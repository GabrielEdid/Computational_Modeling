"""
Author: Gabriel Edid Harari
Date: August 26th 2022
Description: Slope of a Line 
"""
#variables section
X1 = 0
Y1 = 0
X2 = 0
Y2 = 0
result = 0

#Process Starts Here
print("Let’s calculate the slope between two points!")
X1 = float(input("Please give the X coordinate of your first point: "))
Y1 = float(input("Please give the Y coordinate of your first point: "))
X2 = float(input("Please give the X coordinate of your second point: "))
Y2 = float(input("Please give the Y coordinate of your second point: "))
result = (Y2 - Y1) / (X2 -X1)
print("The slope between (", X1, ",",Y1,") and (", X2, ",", Y2, ") is", result)
#Code Finishes Here
