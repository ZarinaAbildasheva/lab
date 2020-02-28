# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 23:01:54 2020

@author: MARAT
"""

n=float(input())
k=float(n)-int(n)
if k < 0.5:
    print(int(n))
elif k >=0.5:
    print(int(n)+1)