"""
Author: Gabriel Edid
Date: September 28th 2022
Description: String Length
"""
#variables section
main1 = ""
main2 = ""
size1 = 0
size2 = 0

#Process Starts Here
main1=input("Please give a Sentence or Word: ")
main2=input("Please give a Second Sentence or Word: ")
size1=len(main1)
size2=len(main2)

if size1>size2:
    print(main1)    
elif size2>size1:
    print(main2)
else:
    print(main1)
    print(main2)
#Code Ends Here

"""
Author: Gabriel Edid
Date: September 28th 2022
Description: String Fragments
"""
#variables section
main = 0
lenmain = 0

#Process Starts Here
main = input("Please give a Sentence or Word: ")
lenmain = len(main)
print("The Length of Your Sentence is:", lenmain)
print("The First Charachter of Your Sentence is:", main[0])
print("The Last Charachter of Your Sentence is:", main[-1])
print("The Odd Index Charachetrs of Your Sentence are:")
#For Loop Starts Here
for count in range(len(main)):
  if count == (lenmain - 1):
    continue
  elif count%2 == 0:
    print(main[1])
  main = main[1:]
#For Loop Ends Here
#Code Ends Here

"""
Author: Gabriel Edid
Date: September 28th 2022
Description: Reversed
"""
#variables section
main = 0

#Process Starts Here
main = input("Please give a Sentence or Word: ").upper()
print(main[::-1])
#Code Ends Here

"""
Author: Gabriel Edid
Date: September 28th 2022
Description: Mixing Words
"""
#variables section
main1 = 0
main2 = 0
main1half1 = 0
main1half2 = 0
main2half1 = 0
main2half2 = 0
#Process Starts Here
main1 = input("Please give a Sentence or Word: ").lower()
main2 = input("Please give a Second Sentence or Word: ").lower()
if len(main1) % 2 != 0:
  main1half1 = main1[:(int(len(main1) / 2 + 1 ))]
  main1half2 = main1[(int(len(main1) / 2 + 1)):]
else: 
  main1half1 = main1[:(int(len(main1) / 2))]
  main1half2 = main1[(int(len(main1) / 2)):]
if len(main2) % 2 != 0:
  main2half1 = main2[:(int(len(main2) / 2 + 1 ))]
  main2half2 = main2[(int(len(main2) / 2 + 1)):]
else: 
  main2half1 = main2[:(int(len(main2) / 2))]
  main2half2 = main2[(int(len(main2) / 2)):]
print(main1half1 + main2half2)
print(main1half2 + main2half1)
#Code Ends Here

"""
Author: Gabriel Edid
Date: September 28th 2022
Description: Endpoints of a String
"""
#variables section
main = 0
#Process Starts Here
main = input("Please give a Sentence or Word: ")
if len(main) <= 2:
  print("")
else:
  print(main[0:2] + main[-2:])
#Code Ends Here

"""
Author: Gabriel Edid
Date: September 28th 2022
Description: Palindrome
"""

#variables section
main = 0
new = 0

#Process Starts Here
main = input("Please give a Sentence or Word: ").upper().replace(" ", "")
new = (main[::-1])
#For Loop Ends Here
if new == main:
  print("It is a Palindorome")
else:
  print("It is not a Palindrome")
#Code Ends Here

"""
Author: Gabriel Edid
Date: September 28th 2022
Description: Uppercase Vowels
"""
#variables section
main = 0
count = 0
finish = ""
#Process Starts Here
main = input("Please give a Sentence or Word: ").lower()
#For Loop Starts Here
for count in(main):
  if count == "a" or count == "e" or count == "i" or count == "o" or count == "u":
    count = count.upper()
    finish = f"{finish}{count}"
  else:
    count =  count.lower()
    finish = f"{finish}{count}"
#For Loop Ends Here
print(finish)
#Code Ends Here

"""
Author: Gabriel Edid
Date: September 28th 2022
Description: Crazy Letters
"""
#variables section
main = 0
count = 0
finish = ""
#Process Starts Here
main = input("Please give a Sentence or Word: ").lower()
#For Loop Starts Here
for count in(main):
  if count == "e":
    count = 3
    finish = f"{finish}{count}"
  elif count == "o":
    count = "h"
    finish = f"{finish}{count}"
  elif count == "a":
    count = 4
    finish = f"{finish}{count}"
  else:
    count =  count.lower()
    finish = f"{finish}{count}"
#For Loop Ends Here
print(finish)
#Code Ends Here

"""
Author: Gabriel Edid
Date: September 28th 2022
Description: Separate a String with Hyphens Every n Characters
"""
#variables section
main = 0
numb = 0
count = 0
finish = ""

#Process Starts Here
main = input("Please give a Sentence or Word: ")
numb = int(input("Please give a number: "))
#While Loop Starts Here
while numb < 0:
  print("Error")
  numb = int(input("Please give a number (It Must be Positive Number): "))
#While Loop Ends Here
#For Loop Starts Here
for count in range(0, len(main), numb):
    if len(main) <= numb:
        finish += main
        print(finish)
    else:
        count = f"{main[:numb]}-"
        finish += count
        main = main[numb:]
#For Loop Ends Here
#Code Ends Here