#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 19:09:29 2021

@author: alexsheehan
"""
from random import randint
import csv
def MainLogic():
    with open('MainDishes.csv',newline='') as f:
        reader = csv.reader(f)
        data = list(reader)
        
    
    length = len(data[0])
    
    while True:
        randindex = randint(0,length-1)
        print("You should consider making " + data[0][randindex] + "!")
    
        yesno = input("Does that sound good? Or would you like to make something else? (Yes/No) ")
        
        if(yesno == "Yes"):
            break
        else:
            continue
    
    
def SideDish():
    with open('SideDishes.csv',newline='') as f:
        reader = csv.reader(f)
        data = list(reader)
        
    
    length = len(data[0])
    
    while True:
        randindex = randint(0,length-1)
        print("You should consider making " + data[0][randindex] + "!")
    
        yesno = input("Does that sound good? Or would you like to make something else? (Yes/No) ")
        
        if(yesno == "Yes"):
            break
        else:
            continue
    
    
    
    
    
def BakedGoods():
    with open('BakedGoods.csv',newline='') as f:
        reader = csv.reader(f)
        data = list(reader)
        
    
    length = len(data[0])
    
    while True:
        randindex = randint(0,length-1)
        print("You should consider making " + data[0][randindex] + "!")
    
        yesno = input("Does that sound good? Or would you like to make something else? (Yes/No) ")
        
        if(yesno == "Yes"):
            break
        else:
            continue
    
        
    
    
    
def DishLogic():
    val= int(input("Are you looking for a 1. Main Dish, 2. Side Dish, or 3. Baked Good ?: "))
    if val == 1 :
        MainLogic()
    elif val == 2:
        SideDish()
    elif val == 3:
        BakedGoods()
    



                       
DishLogic()