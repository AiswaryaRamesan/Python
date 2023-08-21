# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 22:56:10 2023

@author: hp
"""
#Write A Python Program To Print Characters From A String That Are Present At An Odd Index Number


s=input("Enter a sentence")
for i in range(len(s)):
    if(i%2!=0):
        print(s[i])