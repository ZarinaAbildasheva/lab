# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 01:06:48 2020

@author: MARAT
"""

a={1,5,10}
b=set()
for i in a:
    b.add(i)
    b.add(i-1)
    b.add(i+1)
b=sorted(b)
print (b)