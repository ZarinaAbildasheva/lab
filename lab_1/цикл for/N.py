# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 23:20:19 2020

@author: MARAT
"""

n=int(input())
c=[]
c.append(n)

sum=0
for i in range(n):
    t=int(input())
    if t==0:
        sum+=1
        if sum==0:
            break
print(sum)