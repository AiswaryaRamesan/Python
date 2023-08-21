# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 19:57:01 2023

@author: hp
"""
#Write A Python Program To Find Maximum Number From A List Using Function 


lst=[]
print('enter number : ')
for i in range(5):
    lst.append(int(input()))
def maximum(a):
    return max(lst)
maximum(lst)