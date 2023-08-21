# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 11:16:01 2023

@author: hp
"""
#Write A Python Program To Get 10 Name Of The Students From The User In A List, Display That Students Name In Descending Order


studname=[]
for i in range(0,5):
    studname.append(input('enter the Name : '))
studname.sort(reverse=True)
print(studname)
