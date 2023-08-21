# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 11:24:52 2023

@author: hp
"""
#Write A Python Program To Display Number From 1 To 30, Only Odd Number


sno = int(input("Enter a starting no, that is larger"))
eno = int(input("Enter a ending no that is lower"))
for i in range(sno, eno-1,-1):
    print(i)