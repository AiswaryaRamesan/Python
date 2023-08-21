# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 21:07:16 2023

@author: hp
"""
#Write A Python Program To Get a Angle From The User And Find Its Sin And Cos Value In Radian


from math import sin
from math import cos
angle=float(input('enter an angle : '))
sres=sin(angle)
cres=cos(angle)
print('sin {} = '.format(angle),sres)
print('cos {} = '.format(angle),cres)