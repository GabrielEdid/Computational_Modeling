"""
Author: Gabriel Edid Harari
Date: August 26th 2022
Description: Average of 4 Subjects
"""
#variables section
grade_1 = 0
grade_2 = 0
grade_3 = 0
grade_4 = 0
result = 0

#Process Starts Here
grade_1 = float(input("What’s the grade of your first class? "))
grade_2 = float(input("What’s the grade of your second class? "))
grade_3 = float(input("What’s the grade of your third class? "))
grade_4 = float(input("What’s the grade of your last class? "))
result = (grade_1 + grade_2 + grade_3 + grade_4) / 4
print("The average of your four classes is:", result)
#Code Finishes Here
