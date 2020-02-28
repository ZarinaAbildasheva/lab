# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 11:02:47 2020

@author: MARAT
"""

a=int(input())
b=int(input())
c=int(input())
d=int(input())
q=0
t=0

for i in range(0,1001):
    if (a*i**3)+(b*i**2)+(c*i)+d==0:
        print(i)
        

        