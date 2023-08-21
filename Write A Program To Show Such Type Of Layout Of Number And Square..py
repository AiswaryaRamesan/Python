# -*- coding: utf-8 -*-
"""
Created on Sun Feb  5 21:04:47 2023

@author: hp
"""

# Write A Program To Show Such Type Of Layout Of Number And Square,cube.

print('{0:15} {1:8} {2:6}'.format('Number','Square','Cube'))
for i in range(1,6):
    print('{0:<15} {1:<8} {2:<6}'.format(i,i**2,i**3))