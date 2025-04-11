print("Hello Sir/Mam, Welcome to our Aalu Padey CAFE.\n")

#Menu

menu = """
          1. Pizza, 
          2. Burger, 
          3. Black_Coffee, 
          4. Latte, 
          5. Cappuccino, 
          6. Noodles, 
          7. Corndog""" 
menu1 = """
         1. Chicken_Pizza,
         2. Veg_Pizza,
         3. Mix_Pizza"""
menu2 = """
            1. Chicken_Burger,
            2. Beef_Burger,
            3. Ham_Burger,
            4. Full_Meal,
            5. Double_patty_Burger"""
menu3 = """
            1. Salted_caramel_latte,
            2. Cinnamon_latte,
            3. Coconut_milk_latte,
            4. Hazelnut_latte,
            5. Vanilla_latte"""
menu4 = """
            1. Vanilla,
            2. Caramel,
            3. Hazelnut,
            4. Chocolate,"""
menu5 = """
            1. Current,
            2. Buldak,
            3. Current_2x,
            4. wai_wai,"""
menu6 = """
            1. Chicken_corndog,
            2. Beef_corndog,
            3. Cheese_corndog,
            4. Mix_corndog"""

#Check user name

name = input("Can I get your name to match with our reservation?\n")

if name == "Aaryan":
    print("Welcome " + name + ", Please have a seat.\n")
elif name == "Sovina":
    print("Welcome " + name + ", Please have a seat.\n")
else:
    print("Sorry sir, We don't see your name on our reservation list.\n")
    exit()

print("Here's your water " + name + ".\n")

#Take order

order = input("Here's our menu " + menu + "\nWhat would you like to order?\n")

if order == "Pizza":
    order1 = int(input("What kind of Pizza?"+menu1+"\n"))
    if order1 == "Chicken_Pizza":
        price = 20
    elif order1 == "Veg_Pizza":
        price = 15
    elif order1 == "Mix_Pizza":
        price = 25
    else:
        print("Sorry,"+order1+" is not available!\n")
        exit()
elif order == "Burger":
    order1 = int(input("What kind of Burger?"+menu2+"\n"))
    if order1 =="Chicken_Burger":
        price = 15
    elif order1 == "Beef_Burger":
        price = 10
    elif order1 == "Ham_Burger":
        price = 15
    elif order1 == "Full_Meal":
        price = 20
    elif order1 == "Double_Patty_Burger":
        price = 25
    else:
        print("Sorry, "+order1+" is not available.")
        exit()
elif order == "Black_Coffee":
    price = 5
    order1 = "Black_Coffee"
elif order == "Latte":
    order1 = int(input("What kind of Latte?"+menu3+"\n"))
    if order1 =="Salted_caramel_latte":
        price = 16
    elif order1 == "Cinnamon_latte":
        price = 19
    elif order1 == "Coconut_milk latte":
        price = 10
    elif order1 == "Hazelnut_latte":
        price = 20
    elif order1 == "Vanilla_latte":
        price = 25
    else:
        print("Sorry, "+order1+" is not available.")
        exit()
elif order == "Cappuccino":
    order1 = int(input("Which flavour of Cappuccino"+menu4+"\n"))
    if order1 =="Vanilla":
        price = 15
    elif order1 =="Caramel":
        price = 10
    elif order1 =="Hazelnut":
        price = 20
    elif order1 =="Chocolate":
        price = 10
    else:
        print("Sorry, "+order1+" is not available.")
        exit()
elif order == "Noodles":
    order1 = int(input("What kind of Noodles?"+menu5+"\n"))
    if order1 =="Current":
        price = 5
    elif order1 =="Buldak":
        price = 6
    elif order1 =="Current_2x":
        price = 10
    elif order1 =="wai_wai":
        price = 5
    else:
        print("Sorry, "+order1+" is not available")
        exit()
elif order == "Corndog":
    order1 = int(input("What kind of Corndog?"+menu6+"\n"))
    if order1 =="Chicken_corndog":
        price = 15
    elif order1 == "Beef_corndog":
        price = 10
    elif order1 == "Cheese_corndog":
        price = 20
    elif order1 == "Mix_corndog":
        price = 25
    else:
        print("Sorry, "+order1+" is not available.")
        exit()
else:
    print("Sorry, we don't have that item!!\n")
    exit()

quantity = int(input("How many do you want?\n"))

print("Thank you!! Your " + order1 + " will be at your table in a moment.\n")

print("Here's your "+order1+" .")

#Total Calculator

total = quantity * price

print("Here's your bill sir:\n" + order1 + ": $" + str(total))

print("\nThank you for your visit. Come again soon!!")