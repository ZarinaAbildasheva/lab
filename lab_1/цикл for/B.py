# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 22:54:14 2020

@author: MARAT
"""

a=int(input())
b=int(input())
if a<b:
    for i in range(a,b+1):
        print(i)
elif a>b:
    for i in range(a,b-1,-1):
        print(i)
elif a==b:
    print(a)