# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 01:10:56 2020

@author: MARAT
"""

def asd(a,b):
    c=set()
    for i in range (0,len(a)):
        if a[i]>b:
            c.add(a[i])
    return c

a=[1,2,3,4,5]
b=int(input())
print(asd(a,b))