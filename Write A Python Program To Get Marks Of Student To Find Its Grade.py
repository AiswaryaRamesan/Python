# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 23:13:26 2023

@author: hp
"""
#Write A Python Program To Get Marks Of Student To Find Its Grade
mark=int(input("Enter the mark : "))
if(mark>= 95):
    print("Grade = A+")
elif(mark>=80):
    print("Grade = A")
elif(mark>=70):
    print("Grade = B")
elif(mark>=60):
    print("Grade = C") 
else:
    print("Fail")