# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 23:51:28 2020

@author: MARAT
"""
import math
n=int(input())
k=int(input())
c=math.factorial(n)/(math.factorial(k)*math.factorial(n-k))
print(int(c))