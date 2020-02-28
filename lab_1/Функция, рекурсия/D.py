# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 23:13:37 2020

@author: MARAT
"""

import math
def f(x,y):
    if (abs(x)+abs(y))<=1:
        return "YES"
    else:
        return "NO"
x=float(input())
y=float(input())
print(f(x,y))