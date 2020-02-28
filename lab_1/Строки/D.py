# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 23:05:48 2020

@author: MARAT
"""

s = input()
first=s[:s.find(' ')]
second=s[s.find(' ')+1:]
print(second+' '+first)