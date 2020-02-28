# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 21:58:30 2020

@author: MARAT
"""

#a=int(input())
#if (a%4==0 and a%100!=0) or (a%400==0 and a%100!=0):
#    print("YES")
#else:
#    print("NO")

year = int(input())
if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
    print('YES')
else:
    print('NO')