# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 20:33:42 2023

@author: hp
"""
#Write A Python Program That Accepts Six Identity Numbers Of Students As Input And Display In Descending Order

lst=[]
print('Identity number : ')
for i in range(3):
    lst.append(int(input()))
lst.sort(reverse=True)
print(lst)

