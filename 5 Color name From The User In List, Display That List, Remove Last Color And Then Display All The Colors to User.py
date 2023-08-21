# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 11:04:32 2023

@author: hp
"""
#Write A Python Program To Get 5 Color name From The User In List, Display That List, Remove Last Color And Then Display All The Colors to User


color=[]
for i in range(0,5):
    color.append(input('enter the color : '))
print(color) 
color.pop(4)
print(color)

