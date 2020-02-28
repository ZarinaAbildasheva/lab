# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 23:10:12 2020

@author: MARAT
"""

n=int(input())
i=0
while 2**i<=n:
    h=pow(2,i)
    i+=1
    print(h)