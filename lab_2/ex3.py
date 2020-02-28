# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 00:58:21 2020

@author: MARAT
"""

def asd(a,b):
    for i in range(b,len(a)):
        a[i]=a[i]**2
    return a
a=[1,2,3,4,5]
b=int(input())
print(asd(a,b))