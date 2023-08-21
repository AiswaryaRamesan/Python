# -*- coding: utf-8 -*-
"""
Created on Sun Mar 12 11:03:00 2023

@author: hp
"""

#Write Python Program To Get Number From User To Display Table In Reverse Order
n=int(input("Enter a number:"))
for i in range(10,0,-1):
    print(n,"x",i,"=",n*i)