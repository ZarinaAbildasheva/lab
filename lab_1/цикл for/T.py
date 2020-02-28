# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 16:04:34 2020

@author: MARAT
"""

n=int(input())
for i in range(n):
    print(i+1)
    for i in range(1, i+2):
            print(i,end="")