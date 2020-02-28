# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 23:13:09 2020

@author: MARAT
"""

def f(x,y):
    while True:
        if x>=-1 and x<=1 and y>=-1 and y<=1:
            return "YES"
        else:
            return "NO"
x=float(input())
y=float(input())
print(f(x,y)) 