# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 20:54:02 2023

@author: hp
"""
#Write Python Program To Get A Username From The User That Should Have Alphanumeric Characters, Then Pass That Username To Function As Parameter, To Display That Username


uname=input('UserName : ')
def username(a):
    if a.isalnum():
        return('your username is {}'.format(uname))
    else:
         return('wrong username')  
username(uname)