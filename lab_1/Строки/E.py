# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 23:06:17 2020

@author: MARAT
"""

s=str(input())
first = s.find('f')
rev = s[len(s)::-1]
last = len(s) - rev.find('f')-1
if(first == -1):
    pass
elif(first == last):
    print(first)
else:
    print(first,last)