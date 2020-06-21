# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 12:33:10 2020

@author: DELL
"""
#This is the program for flowchart 3 
import time
age1 = int(input("Enter your age"))
time.sleep(1)
age2 = int(input("Enter your age"))
time.sleep(1)
age3 = int(input("Enter your age"))

if age1 > age2 and age1 > age3:
    print("User1 age is the eldest")
elif age2 > age1 and age2 > age3:
        print("User2 is the eldest ")
else:
       
        print("User2 is the eldest ")
        if age3 > age1 and age3 > age2:
            print("User3 is the eldest")
            
            for var in range(2):
                print("Flowchart 3 program is done")
    
        
        
    
    
    