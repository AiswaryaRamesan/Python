# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 15:24:03 2023

@author: hp
"""
#Write A Python Program To Get Name From A List, That Start From ‘f'


lst=[]
print('enter the name : ')
for i in range(4):
    lst.append(input())
print('Name: ')
for i in lst:
    if i[0]=='f':
        print(i)
    
