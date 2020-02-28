# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 11:11:15 2020

@author: MARAT
"""

a=int(input())
b=int(input())
c=int(input())
d=int(input())
e=int(input())

cnt = 0
for i in range(0,1001):
    if (i - e == 0): 
        continue
    if (a*i**3+b*i**2+c*i+d)/(i-e)==0:
        cnt += 1
print (cnt)

