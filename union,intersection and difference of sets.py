# -*- coding: utf-8 -*-
"""
Created on Sun Feb  5 21:53:12 2023

@author: hp
"""
# union,intersection and difference of sets
a={2,3,8}
b={4,8,0}
c={2,7,9}
print('Union : ',a.union(b.union(c)))
print('Intersection : ',a.intersection(b.union(c)))
print('Diffrence : ',a.difference(b))