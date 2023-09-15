"""
Author: Gabriel Edid and Santiago Vigil
Date: October 8-21, 2022
Description: Capstone Project
"""

#Variables Section

start = ""
menu_in = ""
total_sale = 0
want_to_buy = ""
how_many = 0
new_biggest = -1
op = 0
word = ""
update_in = ""
yes_or_no = ""
added_name = ""
added_desc = ""
added_price = 0
added_sku = ""
added_stock = 0
want_to_delete = ""
sure = ""
prod_index = 0
want_to = ""
change = ""
which_one = ""
indexnumb = 0 
new_value = ""
biggest_name = -1
biggest_desc = -1
biggest_price = -1
biggest_sku = -1
biggest_quant = -1
indx = 0
biggest_santi = 0
biggest_gab = 0
quant = 0
new_quant = 0
total_this_sale = 0
text = ""
what_want = ""
which_prod = ""
this_one = 0
new_sale = 0
#Main List used for the Inventory
inventory = [["Product", "Description", "Price($)", "SKU", "Quantity"], 
            ["Coffee Grinder","Grinder for coffee beans", 200, "COGR01", 25],
            ["Coffee Filters", "Filters for making coffee", 5, "COFI02", 57],
            ["Foam Maker","Milk heater to make foam", 85, "FOMA03",14],
            ["Ice Maker","Freezes water and makes ice", 120, "ICEMA04", 12],
            ["Coffee Maker", "Makes coffee with coffee beans", 150, "COMA05", 34],
            ["Coolers", "Keeps items cold", 90, "CO06", 20],
            ["Espresso Machine", "Machine for making espresso style coffee", 140, "EXMA15", 32],
            ["Coffee Roaster", "Roasts coffee beans", 80, "CORO07", 13],
            ["Kettle", "For heating water", 16, "KE08", 21],
            ["French Press", "Separates grinded coffee from water", 32, "FRPR09", 35],
            ["Coffee Bags", "Like tea bags but with coffee", 7, "COBA10", 77],
            ["Auto-Drip Machine", "Makes coffee overtime", 160, "AUMA11", 47],
            ["Chemex", "Manual pour-over coffee maker", 36, "CH12", 15],
            ["Cezve", "For making turkish coffee", 15, "CE13", 31],
            ["Pour Overs", "Like a filter for coffe water", 40, "POOV14", 23]]
#Main list used for Sale Registration
sales_people = [["Product", "Santiago", "Gabriel"], 
               ["Coffee Grinder", 5, 6],
               ["Coffee Filters", 3, 1],
               ["Foam Maker", 9, 10],
               ["Ice Maker", 15, 8],
               ["Coffee Maker", 3, 21],
               ["Coolers", 16, 4],
               ["Espresso Machine", 7, 7],
               ["Coffee Roaster", 6, 9],
               ["Kettle", 5, 3],
               ["French Press", 0, 1],
               ["Coffee Bags", 5, 2],
               ["Auto-Drip Machine", 18, 15],
               ["Chemex", 21, 7],
               ["Cezve", 7, 28],
               ["Pour Overs", 4, 9]]

#Variable Section Ends Here


#Function Section Starts Here

#---------------------> MENU
#Main Menu of the Program
def menu():
    #Prints the menu shown below
    print(""" 
+-----------------------------------------------------------+
|                            Menu                           |
+-----------+-----------+-----------+-----------+-----------+
|           |           |           |           |           |
|           |  Update   |   Sales   |  Product  |           |
|   Sales   | Inventory |   Query   |   Query   |   Exit    |
|           |           |           |           |           |
| Press "S" | Press "U" | Press "Q" | Press "P" | Press "X" |
+-----------+-----------+-----------+-----------+-----------+
""")
    
    #Asks for the Section to go/execute
    menu_in = input("Please Select an Action ").upper()
    #Evaluates the input and calls the necessary function
    while menu_in.isalnum(): 
        if menu_in == "S":
            sales()
        elif menu_in == "U":
            update_inv()
        elif menu_in == "Q":
            sales_que()
        elif menu_in == "P":
            prod_que()
        elif menu_in == "X":
            #If the input is "X" the program is terminated and a message is printed
            print()
            print("Good-Bye! See you again soon!")
            exit()
        else:
            #If the input is different from "S", "U", "Q", "P" or "X" it asks for it again  
            menu_in = input("Invalid Action. Please Select a Valid Action ").upper()


#---------------------> SALES
#Makes sales 
def sales():
    #Variables to use:
    global total_sale 
    global want_to_buy 
    global how_many 
    global new_biggest
    global op
    global word
    global text
    
    print()
    
    #Finds the biggest value in the inventory list to use it as a standard for printing the table
    for big in inventory:
        for new in big:
            biggest = len(str(new))
            if biggest >= new_biggest:
                new_biggest = biggest            
    new_biggest = new_biggest - 20

    #Creates a Header for the table
    print(new_biggest*2*"-")
    text = " Sales "
    text = text.center(new_biggest*2, "-")
    print(text)
    print(new_biggest*2*"-")
    
    #Prints the Table for Sales
    for thing in inventory:
        for element in thing:
            if thing.index(element) == 1:
                continue
            elif thing.index(element) == 0:
                word = str(element)
                op = (new_biggest-len(word)+2)
                print(word, end = op*" " )
            elif thing.index(element) == 2:
                word = str(element)
                op = (new_biggest-len(word)+2)
                print(word, end = op*" " )
        print()
        print(new_biggest*2*"-")
        print()
    
    #Section where the user interacts and selects the product he wants and how many
    if total_sale > 0:
        print()
        print("The Total Sale is: $", total_sale)
        print()
    print("Welcome to the Sales Section, here you can see our products available and make a purchase")
    print()
    want_to_buy = input('Do you wish to buy any product? Press "Y" for Yes or "N" for No and return to the Menu and get your total ').upper()
    while want_to_buy.isalnum():
        if want_to_buy == "Y":
            which_product = input("Wich Product do you Want (Please write the product Name)? ").title()
            #Looks for the product the user wants in the inventory list and then looks for the index in the list where the price would be
            for product in inventory:
                for item in product:
                    if item == which_product:
                        item = product.index(item) + 2
                        how_many = int(input("How many do you want? "))
                        wanted = int(product[item])
                        #Calls the is_there_enough function to update the lists of salesman, the inventory and check abailability
                        is_there_enough(which_product, how_many, wanted) #Three values already defined by the process are given
        #Returns to the menu if input is "N" and prints the total sale value
        elif want_to_buy == "N":
            print("The Total Sale is: $", total_sale)
            print("Thank You for your Sale!")
            menu()
        #Asks for the input again if value is different from "Y" or "N"
        else:
            want_to_buy = input('Invalid Input. Please press "Y" for Yes or "N" for No ').upper()
             

#---------------------> CHECK IF THERE IS ENOUGH OF A PRODUCT FOR A SALE
#Checks if there is enough inventory, updates lists and registers sales
def is_there_enough(which_product, how_many, wanted):
    #Variables to use:
    global total_sale
    global quant
    global new_quant
    global total_this_sale
    global new_sale
    
    #Looks for the product the user wants in the inventory list and then looks for the index in the list where the quantity would be
    for product in inventory:
        for item in product:
            if which_product == item:
                #Defines a new variables which is the quantity of the product the user wants
                quant = product[4]
                #Redefines both values to be an integer in case they are strings
                how_many = int(how_many)
                quant = int(quant)
                #Evaluates if there is enough of the product according to the ammount the user aksed for
                if how_many <= quant:
                    #If there is enough of the product the list updates
                    new_quant = quant - how_many
                    product[4] = new_quant
                    #Calculates the total sale 
                    total_sale += (wanted*how_many)
                    #Asks who of the two salesman did the sale 
                    who_did = input('Who did this sale? Press "S" for Santiago and "G" for Gabriel ').upper()
                    while who_did.isalnum():
                        #If Santigo did it
                        if who_did == "S":
                            #Updates the sales_poeple list according to the product selected, the sales person and how many products were sold
                            for product in sales_people:
                                for item in product:
                                    if item == which_product:
                                        new_sale = product[1] + how_many
                                        product[1] = new_sale
                                        #Goes back to the sales function to check if the user wants another product
                                        sales() 
                        #If Gabriel did it 
                        elif who_did == "G":
                            #Updates the sales_poeple list according to the product selected, the sales person and how many products were sold
                            for product in sales_people:
                                for item in product:
                                    if item == which_product:
                                        new_sale = int(product[2]) + how_many
                                        product[2] = new_sale
                                        #Goes back to the sales function to check if the user wants another product
                                        sales()
                        else:
                            #Asks for the input again if the input is different from "S" or "G"    
                            who_did = input('Who did this sale? Press "S" for Santiago and "G" for Gabriel ').upper()
                #If there is not enough of a product an error message is printed
                elif how_many > quant:
                    print()
                    print("There is not enough of that product")
                    print()
                    #Goes back to the sales function to check if the user wants another product
                    sales()
            

#---------------------> UPDATE INVENTORY MENU
#Main Menu for the Update Inventory Section
def update_inv():
    #Variables to use:
    global update_in
    
    #Prints the menu shown below
    print("""
+-----------------------------------------------+
|                Update Inventory               | 
+-----------+-----------+-----------+-----------+
|           |           |           |           |           
|    Add    |  Delete   |  Update   |   Back    |
|  Product  |  Product  |  Product  |           |
|           |           |           |           |
| Press "A" | Press "D" | Press "U" | Press "B" | 
+-----------+-----------+-----------+-----------+
""")
    #Asks for the Section to go/execute
    update_in = input("Please Select an Action ").upper()
    #Evaluates the input and calls the necessary function
    while update_in.isalnum():
        if update_in == "A":
            add_prod()
        elif update_in == "D":
            delete_prod()
        elif update_in == "U":
            update_prod()
        elif update_in == "B":
            menu()
        #Asks for the input again if the input is different from "A", "D", "U" or "B"    
        else:
            update_in = input("Invalid Action. Please Select a Valid Action ").upper()
           
           
#---------------------> INVENTORY
#Prints the inventory table
def func_inventory():
    #Variables to use:
    global inventory
    global new_biggest
    global biggest_name
    global biggest_desc
    global biggest_price
    global biggest_sku
    global biggest_quant
    global indx
    
    print()
    
    #Checks for the longest value in each of the indexes in the inventory list
    for item in inventory:
        for element in item:
            #Defines a varaible for the item that is being evaluated
            indx = inventory.index(item)
            #Checks the length of the element being evaluated
            biggest = len(str(element))
            #Checks if the element is in the index 0 and if it's the longest name
            if element == inventory[indx][0] and biggest >= biggest_name:
                #If it's longer, the value of biggest_name is re-defined
                biggest_name = biggest
            #Checks if the element is in the index 1 and if it's the longest description
            elif element == inventory[indx][1] and biggest >= biggest_desc:
                #If it's longer, the value of biggest_desc is re-defined
                biggest_desc = biggest
            #Checks if the element is in the index 2 and if it's the longest price
            elif element == inventory[indx][2] and biggest >= biggest_price:
                #If it's longer, the value of biggest_price is re-defined
                biggest_price = biggest
            #Checks if the element is in the index 3 and if it's the longest sku
            elif element == inventory[indx][3] and biggest >= biggest_sku:
                #If it's longer, the value of biggest_sku is re-defined
                biggest_sku = biggest
            #Checks if the element is in the index 4 and if it's the longest quantity
            elif element == inventory[indx][4] and biggest >= biggest_quant:
                #If it's longer, the value of biggest_quant is re-defined
                biggest_quant = biggest
    
    #Finds the biggest value in the inventory list to use it as a standard for printing the table
    for item in inventory:
        for element in item:
            biggest = len(str(element))
            if biggest >= new_biggest:
                new_biggest = biggest
        new_biggest = new_biggest - 3
    
    #Creates a Header for the table
    print(new_biggest*5*"-")
    text = " Inventory "
    text = text.center(new_biggest*5, "-")
    print(text)
    print(new_biggest*5*"-")

    #Gives each product and index number
    for index, thing in enumerate(inventory):
        if thing == inventory[0]:
                print(4*" ", end="")
        if index != 0 and index <= 9:
            print(index, end = 3*" ")   
        elif index >= 10:
            print(index, end = 2*" ")
        #Starts printing the table
        for element in thing:
            #Defines a varaible for the item that is being evaluated
            indx = inventory.index(thing)
            #Checks the index of each element and according to their index its how the element is printed
            #For each section of the inventory there is a standard spacing so all the table looks lined up
            #For example the first part checks if the element is at index 0, if it is:
            if element == inventory[indx][0]:
                #The element is converted to a string, no matter what is is
                word = str(element)
                #A variable is defined to be the standard spacing the product shall have
                #This would evaluate: the value of the longest name - the lenght of the element being evaluated + 5
                #This operation will always make the same spacing for each word and the table won't look funny 
                op = (biggest_name-len(word)+5)
                #The element being evaluated, now as a string, is printed and the neccesary spacing is given.
                print(word, end = op*" " )
                #This process is repeated with all the parts of the list, the only thing that changes is the index number
                #That way the values for the names will go always with the names, the prices with the prices and so on
            elif element == inventory[indx][1]:
                word = str(element)
                op = (biggest_desc-len(word)+5)
                print(word, end = op*" " )
            elif element == inventory[indx][2]:
                word = str(element)
                op = (biggest_price-len(word)+5)
                #This is the only exception where the op value has + 2 so the prices have a little bit more space
                print(word, end = (op+2)*" " )
            elif element == inventory[indx][3]:
                word = str(element)
                op = (biggest_sku-len(word)+5)
                print(word, end = op*" " )
            elif element == inventory[indx][4]:
                word = str(element)
                op = (biggest_quant-len(word)+5)
                print(word, end = op*" " )
        #Prints space and a line between each product according to the value of new_biggest * 5 because there are 5 sections to the table
        print()
        print(new_biggest*5*"-")
        print()


#---------------------> ADD PRODUCT
#Adds products to the inventory
def add_prod():
    #Variables to use:
    global yes_or_no
    global added_name
    global added_desc
    global added_price 
    global added_sku 
    global added_stock
    
    #Asks if the user wants to add a product or not
    print()
    print("Welcome to the Add Product Section, here you can add a new product to the inventory")
    print()
    
    yes_or_no = input('Do you wish to add a new product? Press "Y" for Yes or "N" for No and return to the Update Inventory Section ').upper()
    while yes_or_no.isalnum():
        if yes_or_no == "N":
            #If the input is "N" the update_inv function is called and goes back to the menu
            update_inv()
        elif yes_or_no == "Y":
            #If the input is "Y" the program asks for all the necessary information to add a new product
            added_name = input("What is the Name of the New Product? ").title()
            added_desc = input("What is the Description of the New Product? ")
            added_price = input("What is the Price of the New Product? ")
            added_sku = input("What is the SKU of the New Product? ").upper()
            added_stock = input("How many are there of the New Product? ")
            #All the new information is appended in order to the inventory list
            inventory.append([added_name, added_desc, added_price, added_sku, added_stock])
            #A new product is appended to the sales_people list only using the name of the product and setting the sales record at 0
            sales_people.append([added_name,0,0])
            #Asks if the user wants to add another product or go back to the Update Inventory menu
            yes_or_no = input('Do you wish to add another Product? Press "Y" for Yes or "N" for No and return to the Update Inventory Section ').upper()
            #Calls the func_inventory function and prints the inventory table
            func_inventory()
        #If the input is different from "Y" or "N" it asks for it again.
        else:
            yes_or_no = input('Invalid Input. Do you wish to add a Product? Press "Y" for Yes or "N" for No and return to the Update Inventory Section ').upper()
            
            
#---------------------> DELETE PRODUCT
#Deletes products from the inventory
def delete_prod():
    #Variables to use:
    global want_to_delete
    global sure
    
    #Calls the func_inventory function and prints the inventory table
    func_inventory()
    
    #Asks if the user wants to delete a product or not and go back to the Update Inventory menu
    print("Welcome to the Delete Product Section, here you can delete products from the inventory")
    print()
    want_to_delete = input('Do you want to Delete a Product? Press "Y" for Yes or "N" for No and return to the Update Inventory Section ').upper()
    while want_to_delete.isalnum() or sure.isalnum():
        if want_to_delete == "N":
            #If the input is "N" the update_inv function is called and goes back to the menu
            update_inv()
        elif want_to_delete == "Y":
            #If the input is "Y" it asks which product it wants to delete by its SKU
            which_one = input("Wich product do you want to Delete (Please write the Product Name as it is shown)? ").title()
            #Looks for the product in the inventory list
            for product in inventory:
                for to_delete in product:
                    if to_delete == which_one:
                        #If the product is found a confirmation message is shown and asks for an input
                        sure = input('Are you sure you want to delete that product? Press "Y" for Yes or "N" for No ').upper()
                        if sure == "N":
                            #If the Input is "N" the program goes back to the start of this function and asks if the user wants to delete a product or not
                            want_to_delete = input('Do you want to Delete a Product? Press "Y" for Yes or "N" for No and return to the Update Inventory Section').upper()
                        elif sure == "Y":
                            #If the input is "Y" the product is deleted from the inventory list 
                            inventory.remove(product)
                            #And also the product will be removed from the sales_people list
                            for product in sales_people:
                                for to_delete in product:
                                    if to_delete == which_one:
                                        sales_people.remove(product)
                            #Calls the func_inventory function and prints the updated inventory table
                            func_inventory()
                            #Asks if the user wants to delete another product or not and go to the Update Inventory menu
                            want_to_delete = input('Do you want to Delete another Product? Press "Y" for Yes or "N" for No and return to the Update Inventory Section ').upper()
                        else:
                            #If the Input is different from "Y" or "N" it asks for it again
                            sure = input('Invalid Input. Are you sure you want to delete that product? Press "Y" for Yes or "N" for No and return to the Update Inventory Section ').upper()
        else:
            #If the Input is different from "Y" or "N" it asks for it again
            want_to_delete = input('Invalid Input. Do you wish to Delete a Product? Press "Y" for Yes or "N" for No and return to the Update Inventory Section ').upper()
        
        
#---------------------> UPDATE PRODUCT
#Updates products from the inventory
def update_prod():
    #Variables to use:
    global prod_index
    global want_to
    global change
    global which_one
    global indexnumb
    global new_value
    
    #Calls the func_inventory function and prints the inventory table
    func_inventory()
    
    print("Welcome to the Update Product Section, here you can update any product in the inventory")
    print()
    
    #Asks if the user wants to update a product or not and go to the Update Inventroy menu
    want_to = input('Do you want to Upadate a Product? Press "Y" for Yes or "N" for No and return to the Update Inventory Section ').upper()
    while want_to.isalnum() or change.isalnum():
        if want_to == "N":
            #If the input is "N" the update_inv function is called and goes back to the menu
            update_inv()
        elif want_to == "Y":
            #If the Input is "Y" it asks what does the user want to change, either the name, the description, the price, the sku or the quantity
            change = input('What do you want to change? Press "N" for Name, "D" for Description, "P" for Price, "S" for SKU or "Q" for Quantity ').upper()
            #Ask for the name of the product which the user wishes to update something within
            which_one = input("What is the name of the product where you want to update? ").title()
                #It goes product by product in the inventory list
            for product in inventory:
                    #It saves in a variable the index value of the product being evaluated
                indexnumb = inventory.index(product)
                    #It goes element by element in each product
                for element in product:
                    if element == which_one:
                        #If the product wanted to change is found and it is at index 0 (because that's where names are) it will ask for the new value
                        if change == "N":
                            new_value = input("What will be the new name? ").title()
                        #It replaces the old value with the new value
                            inventory[indexnumb][0] = new_value
                            #It replaces the old value with the new value in the sales_people list, this is only done for the name
                            for product in sales_people:
                                for item in product:
                                    if item == which_one:
                                        sales_people[indexnumb][0] = new_value
                        #The code repeats the same process for all the data types in inventory list
                        elif change == "D":
                            new_value = input("What will be the new description? ")
                            inventory[indexnumb][1] = new_value
                        elif change == "P":
                            new_value = input("What will be the new price? ")
                            inventory[indexnumb][2] = new_value
                        elif change == "S":
                            new_value = input("What will be the new sku? ").upper()
                            inventory[indexnumb][3] = new_value
                        elif change == "Q":
                            new_value = input("What will be the new quantity? ")
                            inventory[indexnumb][4] = new_value
                        else:
                            want_to = input('Invalid Input. Do you want to Upadate a Product? Press "Y" for Yes or "N" for No and return to the Update Inventory Section ').upper()
                        #Calls the func_inventory function and prints the updated inventory table
                        func_inventory()
                        #Asks if the user wants to update another product or not and go to the Update Inventory menu
                        want_to = input('Do you want to Upadate a another Product? Press "Y" for Yes or "N" for No and return to the Update Inventory Section ').upper()
        else:
            #If the Input is different from "Y" or "N" it asks for it again
            want_to = input('Invalid Input. Do you want to Upadate a Product? Press "Y" for Yes or "N" for No and return to the Update Inventory Section ').upper()


#---------------------> SALES QUERY
#Shows the sales made by each sales person
def sales_que():
    #Variables to use:
    global sales_people
    global new_biggest
    global biggest_name
    global biggest_santi
    global biggest_gab
    global indx
    global text

    print("Welcome to the Sales Query Section, here you can consult the sales made by each sales person")
    print()

    #Checks for the longest value in each of the indexes in the sales_people list
    for item in sales_people:
        for element in item:
            #Defines a varaible for the item that is being evaluated
            indx = sales_people.index(item)
            #Checks the length of the element being evaluated
            biggest = len(str(element))
            #Checks if the element is in the index 0 and if it's the longest name
            if element == sales_people[indx][0] and biggest >= biggest_name:
                #If it's longer, the value of biggest_name is re-defined
                biggest_name = biggest
            #Checks if the element is in the index 1 and if it's the longest value
            if element == sales_people[indx][1] and biggest >= biggest_santi:
                #If it's longer, the value of biggest_santi is re-defined
                biggest_santi = biggest
            #Checks if the element is in the index 2 and if it's the longest value
            elif element == sales_people[indx][2] and biggest >= biggest_gab:
                #If it's longer, the value of biggest_gab is re-defined
                biggest_gab = biggest

    #Finds the biggest value in the sales_people list to use it as a standard for printing the table
    for item in sales_people:
        for element in item:
            biggest = len(str(element))
            if biggest >= new_biggest:
                new_biggest = biggest

    #Creates a Header for the table        
    print(new_biggest*3*"-")
    text = " Sales Query "
    text = text.center(new_biggest*3, "-")
    print(text)
    print(new_biggest*3*"-")
    
    #Starts printing th table
    for index, thing in enumerate(sales_people):
        for element in thing:
            #Defines a varaible for the item that is being evaluated
            indx = sales_people.index(thing)
            #Checks the index of each element and according to their index its how the element is printed
            #For each section of the inventory there is a standard spacing so all the table looks lined up
            #For example the first part checks if the element is at index 0, if it is:
            if element == sales_people[indx][0]:
                #The element is converted to a string, no matter what is is
                word = str(element)
                #A variable is defined to be the standard spacing the product shall have
                #This would evaluate: the value of the longest name - the lenght of the element being evaluated + 5
                #This operation will always make the same spacing for each word and the table won't look funny 
                op = (biggest_name-len(word)+5)
                #The element being evaluated, now as a string, is printed and the neccesary spacing is given.
                print(word, end = op*" " )
            #This process is repeated with all the parts of the list, the only thing that changes is the index number
            #That way the values for the names will go always with the names, the sales of Santiago with it's own and so on
            elif element == sales_people[indx][1]:
                word = str(element)
                op = (biggest_santi-len(word)+5)
                print(word, end = op*" " )
            elif element == sales_people[indx][2]:
                word = str(element)
                op = (biggest_gab-len(word)+5)
                print(word, end = (op)*" " )
        #Prints space and a line between each product according to the value of new_biggest * 3 because there are 3 sections to the table
        print()
        print(new_biggest*3*"-")
        print()
    
    print("Welcome to the Sales Query Section, here you can consult the sales made by each sales person")
    print()
    #Where user interacts, the user is asked to press "B" to go back
    back = input('To go Back press "B" ').upper()
    while back.isalnum():
        if back == "B":
            #If the input is "B" the menu function will be called and goes back to the menu
            menu()
        else:
            #If the Input is different from "B" it asks for it again
            back = input('Invalid Input. To go Back press "B" ').upper()
           
           
#---------------------> PRODUCT QUERY
#Shows all the inventory table or one product in particular
def prod_que():
    #Variables to use:
    global what_want
    global which_prod
    global this_one

    print()
    print("Welcome to the Product Query Section, here you can consult the inventory")
    print()
    
    #Asks if the user wants to see all the Inventory, to only see only one product or not and go back to the menu
    what_want = input('What do you want to see? Press "A" for all the Inventory, Press "O" for only One Product or Press "B" to go Back to the menu ').upper()
    while what_want.isalnum():
        if what_want == "A":
            #If the input is "A" the func_inventory function is called and prints the inventory table
            func_inventory()
            #Asks again if the user wants to see only see only one product or not and go back to the menu
            what_want = input('Do you want to see anything else? Press "O" for only One Product or Press "B" to go Back to the menu ').upper()
        elif what_want == "O":
            #If the input is "O" the program asks which product the user wants to see
            which_prod = input("Which Product do you wish to see? (Write the product name) ").title()
            #Looks for the product
            for product in inventory:
                #Looks for the input given
                for item in product:
                    if item == which_prod:
                        #If the input given is found, the product will be displayed with all its elements: Name, Description, Price, SKU and Quantity 
                        print()
                        print("Name:", product[0], "   ", "Description:", product[1], "   ", "Price($):", product[2], "   ", "SKU:", product[3], "   ", "Quantity:", product[4])
                        print()
                        #Asks again if the user wants to see all the Inventory, to only see only one product or not and go back to the menu
                        what_want = input('Do you want to see anything else? Press "A" for all the Inventory, Press "O" for only One Product or Press "B" to go Back to the menu ').upper()
        elif what_want == "B":
            #If the input is "B" it calls the menu function and goes back to the menu
            menu()
        else:
            #If the input is different from "A", "O" or "B" it asks for it again 
            what_want = input('Invalid Input. What do you want to see? Press "A" for all the Inventory, Press "O" for only One Product or Press "B" to go Back to the menu ').upper()


#Function Section Ends Here
            
#---------------------> PROCESS STARTER
#Process Starts Here
#Asks if the user wants to start or not
start = input('Do you wish to start? Press "Y" for Yes or "N" for No ').upper()
while start != "N":
    if start == "Y":
        #If the input is "Y" the menu function is called, goes to the menu and starts the whole program above
        menu()
    else:
        #If the input is different from "A" or "N" it asks for it again
        start = input('Invalid Input. Please press "Y" for Yes or "N" for No ').upper()
#If the input is "N" the program is terminated
exit()
#Process Ends Here