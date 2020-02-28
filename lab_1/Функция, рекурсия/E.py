# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 23:14:36 2020

@author: MARAT
"""

def f(x,y,xc,yc,r):
    if (x - xc) * (x - xc) + (y - yc) * (y - yc) <= r * r:
        return "YES"
    else:
        return "NO"
x=float(input())
y=float(input())
xc=float(input())
yc=float(input())
r=float(input())
print(f(x,y,xc,yc,r))