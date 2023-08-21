# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 17:19:50 2023

@author: hp
"""
#Write A Python Program To Get Name From A List, That Ends At ‘n'


lst=[]
print("enter the Name : ")
for i in range(3):
    lst.append(input())
print('Name : ')
for i in lst:
    if i[-1]=='n':
        print(i)
    