# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 22:18:41 2023

@author: hp
"""

#Write A Python Program To Get 5 Author Name With Their Book Name And Display Last Author With It's Book Name


authbooks = {}

for i in range(2):
    authorname = input("Enter author name") 
    bookname = input("Enter its book name")
    authbooks[authorname] = bookname

print("Last auther is ",list(authbooks.keys())[-1])
print("Last book is ",list(authbooks.values())[-1])