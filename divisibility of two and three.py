# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 23:08:22 2023

@author: hp
"""
#Write A Python Program To Get A  Number From User To Check, It Is Divisible By 2 And 3


n=int(input("Enter a number : "))
if(n%2==0 and n%3==0):
    print("Number is divisbile by 2 & 3")
else:
    print("Not divisible by 2 & 3")