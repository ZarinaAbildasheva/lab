# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 23:11:04 2020

@author: MARAT
"""

n = int(input())
k = 0
while 2**k < n:
    k += 1
print( k )