# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 20:42:11 2023

@author: hp
"""
#Write A Python Program To Create A File And Write User Name, And Age In That File


file = open("nameage.txt","w+")
name = input("Name : ")
age = input("Age : ")
file.write("Your name is "+str(name))
file.write("Your age is "+str(age))
file.close()