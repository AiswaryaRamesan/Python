# -*- coding: utf-8 -*-
"""
Created on Sun Mar 12 16:27:13 2023

@author: hp
"""
#Write A Python Program To Search Any Character (or Set of Character) From a String


s=input("Enter a string")
print(s)
ch=input("Enter the chararacter")
if ch in s:
    print("Yes")
else:
    print("No")