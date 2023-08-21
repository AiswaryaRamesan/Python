# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 22:24:46 2023

@author: hp
"""
#Write A Python Program To Clone Or Copy Of a 10 Color List

color=[]
print("Enter color name")
for i in range(5):
    color.append(input())

print('color : ',color)

color1= color.copy()
print("Copied color : ",color1)