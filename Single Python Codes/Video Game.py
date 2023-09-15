"""
Author: Gabriel Edid Harari
Date: August 26th 2022
Description: Video Game 
"""
#variables section
new_games = 0
old_games = 0
result = 0

#Process Starts Here
print("Hello! Welcome to GameStore!")
new_games = int(input("How many new games did you pick? "))
old_games = int(input("How many old games did you pick? "))
result = (new_games * 1000) + (old_games * 350)
print("Your total for", new_games, "new games and", old_games, "old games is", result, "$.")
#Code Finishes Here
