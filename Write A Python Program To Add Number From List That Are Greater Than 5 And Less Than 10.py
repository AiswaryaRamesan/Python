# -*- coding: utf-8 -*-
"""
Created on Sun Mar 12 12:13:47 2023

@author: hp
"""
#Write A Python Program To Add Number From List That Are Greater Than 5 And Less Than 10


lst=[]
print('numbers : ')
for i in range(5):
    lst.append(int(input()))
n=0
for j in lst:
    if(j > 5 and j < 10):   
        n=n+j
print(n)    


