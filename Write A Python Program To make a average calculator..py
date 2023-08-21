# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 12:25:42 2023

@author: hp
"""
#Write A Python Program To make a average calculator. 


lst=[]
l=int(input('enter the limit : '))
print('amount :')
for i in range(l):
    lst.append(int(input()))
avg=sum(lst)/l
print('Average = ',avg)