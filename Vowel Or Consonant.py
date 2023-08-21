# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 21:41:56 2023

@author: hp
"""
#Write A Python Program To Check Alpha Character, Whether Vowel Or Consonant

l=input('enter the letter : ')
l=l.lower()
if l in ('a','e','i','o','u'):
    print('vowel')
else:
    print('consonant')
    