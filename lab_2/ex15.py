# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 01:11:20 2020

@author: MARAT
"""

def asd(a):
    cnt=0
    for i in range(0,len(a),2):
        if a[i]%2==1:
            cnt+=1
    return cnt
a=[1,2,3,4,5]

print(asd(a))