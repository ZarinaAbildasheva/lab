# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 22:16:41 2020

@author: MARAT
"""

a=int(input())
b=int(input())
c=int(input())
if (a>b and a>c) or (a>=b and a>=c):
    print(a)
elif (b>a and b>c) or (b>=a and b>=c):
    print(b)
elif (c>a and c>b) or (c>=a and c>=b):
    print(c)
