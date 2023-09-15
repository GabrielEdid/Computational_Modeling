"""
Author: Gabriel Edid Harari
Date: August 26th 2022
Description: Cement Cost 
"""
#variables section
number_of_bags = 0
price_per_bag = 0
result = 0 
taxes = 0
price_with_tax = 0

#Process Starts Here
price_per_bag = float(input("How much is the price per cement bag? "))
number_of_bags = int(input("How many bags of cement will you need? " ))
result = price_per_bag * number_of_bags
print("The price before taxes is:", result)
taxes = (result * 16)/100
print("The 16% tax will be:", taxes)
price_with_tax = result + taxes
print("The price of", number_of_bags, "bags of cement is:", price_with_tax)
#Code Finishes Here
