# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 23:02:35 2020

@author: MARAT
"""

import math
a=int(input())
b=int(input())
c=int(input())
P=(a+b+c)/2
S=math.sqrt(P*(P-a)*(P-b)*(P-c))
print(S)