# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 01:06:17 2020

@author: MARAT
"""

a=(1,2,3,[1,2,3],5)
for i in range(len(a)):
    if type(a[i])==list:
        print(True)
        exit()
print(False)