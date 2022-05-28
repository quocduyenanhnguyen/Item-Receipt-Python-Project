#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 01:33:07 2021

@author: annanguyen
"""

from appJar import gui #imports the gui library from appJar


#Function to greet the user and ask for a category

import pandas
babydf=pandas.read_csv("babystore.csv")
bathlist = list(babydf.BathandSkinCare)
foodlist = list(babydf.FoodandFormula)
feedinglist = list(babydf.FeedingandNursing)
def greet_user(greeting,sentinel,categoryq,readyq):
    canswer = ' '
    ranswer = sentinel
    print(greeting)
    while ranswer == sentinel:
        canswer = input(categoryq)
        ranswer = input(readyq)
    if canswer == "Bath and Skin Care":
        bath("Welcome to our Bath and Skin Care section! Here are your choices:",bathlist,"Which item would you like? ","How many?","Your total will be: $ ")
    elif canswer == "Food and Formula":
        food("Welcome to our Food and Formula section!  Here are your choices:",foodlist,"Which item would you like? ","How many?","Your total will be: $ ")
    elif canswer == "Feeding and Nursing":
        feeding("Welcome to our Feeding and Nursing section!  Here are your choices:",feedinglist,"Which item would you like? ","How many?","Your total will be: $ ")
    else:
        print('Sorry, we do not carry that category. See you next time!')


#Function to ask user to pick Bath and Skin Care 

def bath(greeting,selection,pickq,quantity,total):
    print(greeting)
    for item in selection:
        print(item)
    bathpick = input(pickq)
    if bathpick == "None":
        print("Goodbye")
        print()
    elif bathpick == "Oil":
        quantity = int(input("How many? "))
        total = quantity * 10
        closing(quantity,"Oil",total,"Thank you for shopping with us!")
        print()
    elif bathpick == "Lotion":
        quantity = int(input("How many? "))
        total = quantity * 20
        closing(quantity,"Lotion",total,"Thank you for shopping with us!" )
        print()
    elif bathpick == "Shampoo":
        quantity = int(input("How many? "))
        total = quantity * 40
        closing(quantity,"Shampoo",total,"Thank you for shopping with us!" )
        print()
    else:
        quantity = int(input("How many? "))
        total = quantity * 30
        closing(quantity,"Body Wash",total,"Thank you for shopping with us!")
        print()
    

#Function to ask user to pick Food and Formula 

def food(greeting,selection,pickq,quantity,total):
    print(greeting)
    for item in selection:
        print(item)
    foodpick = input(pickq)
    if foodpick == "None":
        print("Goodbye")
        print()
    elif foodpick == "Powder Formula":
        quantity = int(input("How many? "))
        total = quantity * 5
        closing(quantity,"Powder Formula",total,"Thank you for shopping with us!" )
        print()
    elif foodpick == "Puree":
        quantity = int(input("How many? "))
        total = quantity * 30
        closing(quantity,"Puree",total,"Thank you for shopping with us!" )
        print()
    elif foodpick == "Yogurt":
        quantity = int(input("How many? "))
        total = quantity * 5
        closing(quantity,"Yogurt",total,"Thank you for shopping with us!" )
        print()
    else: 
        quantity = int(input("How many? "))
        total = quantity * 10
        closing(quantity,"Cereal",total,"Thank you for shopping with us!")
        print()


#Function to ask user to pick Feeding and Nursing

def feeding(greeting,selection,pickq,quantity,total):
    print(greeting)
    for item in selection:
        print(item)
    feedpick = input(pickq)
    if feedpick == "None":
        print("Goodbye")
        print()
    elif feedpick == "Pacifiers":
        quantity = int(input("How many? "))
        total = quantity * 3
        closing(quantity,"Pacifiers",total,"Thank you for shopping with us!" )
        print()
    elif feedpick == "Bottles":
        quantity = int(input("How many? "))
        total = quantity * 25
        closing(quantity,"Bottles",total,"Thank you for shopping with us!" )
        print()
    elif feedpick == "Bibs":
        quantity = int(input("How many? "))
        total = quantity * 2
        closing(quantity,"Bibs",total,"Thank you for shopping with us!" )
        print()
    else: 
        quantity = int(input("How many? "))
        total = quantity * 12
        closing(quantity,"Utensils",total,"Thank you for shopping with us")
        print()
#Function to ask user to pay

def closing(quantity,pickeditem,total,goodbye):
    print(quantity,pickeditem,"will cost you $"+str(total))
    more = input("Would you like to pick another item (y/n)? ")
    if more == "y":
        greet_user("Great!","n","What category would you like to browse (Bath and Skin Care, Food and Formula, Feeding and Nursing)? ", "Ready to browse (y/n)? ")
    else:
        for l in goodbye:
            print(l, end= "")
            

    
def press(btn):
    if btn == "Exit":
        app.stop()
    elif btn == "Greeting":
        greet_user("Welcome to our store!","n", "What would you like to buy (Bath and Skin Care, Food and Formula, Feeding and Nursing)? ", "Are you ready (y/n)? ")
        print()
    elif btn == "Bath and Skin Care":
        bath("Welcome to our Bath and Skin Care section! Here are your choices:",bathlist,"Which item would you like? ","How many?","Your total will be: $ ")
        print()
    elif btn == "Food and Formula":
         food("Welcome to our Food and Formula section! Here are your choices:",foodlist,"Which item would you like? ","How many?","Your total will be: $ ")
         print()
    elif btn == "Feeding and Nursing":
        feeding("Welcome to our Feeding and Nursing section! Here are your choices:",feedinglist,"Which item would you like? ","How many? ","Your total will be: $ ")
        print()
    else:
        print('Pick a valid option')

"""
The code below defines the gui, adding buttons, labels, images, color, etc.


"""


app=gui("Main Page","500x500")



app.addLabel("title", "Welcome to Our Store's Main Page")
app.setLabelBg("title", "violet")



app.addImage("decor","Cat.gif")
app.setFont(10)



app.addButton("Greeting", press)
app.addButton("Bath and Skin Care", press)
app.addButton("Food and Formula", press)
app.addButton("Feeding and Nursing", press)
app.addButton("Exit",press)
app.go() #displays the gui
    
        






