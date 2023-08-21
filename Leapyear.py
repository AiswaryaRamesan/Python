# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 22:23:34 2023

@author: hp
"""
#Write A Python Program To Check A Year, Whether It Is Leap Year Or Not


yr=int(input("ente a year: "))
if((yr%400==0)or(yr%4==0 and yr%100!=0)):
    print('Leap year')
else:
    print('Not a Leap year')    