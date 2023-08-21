# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 11:47:22 2023

@author: hp
"""
#Write A Python Program To Get A Number From The User To Find Factorial Of That Number


n=int(input('enetr a numnber : '))
fact=1
for i in range(1,n+1):
    fact=fact*i
print('factorial : ',fact)