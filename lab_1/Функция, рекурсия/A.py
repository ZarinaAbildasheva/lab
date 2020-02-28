# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 23:11:53 2020

@author: MARAT
"""

import math
def calc(x1, y1, x2, y2):
    d=(x1 - x2)
    q=(y1 - y2)    
    w=math.sqrt(d**2+q**2)
    return w
x1=float(input())
y1=float(input())
x2=float(input())
y2=float(input())
print(calc(x1,y1,x2,y2))