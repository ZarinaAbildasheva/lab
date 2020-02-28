# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 16:13:10 2020

@author: MARAT
"""

import math
s=0.0
for i in range(1,11):
    s+=(1.0/i**2)   
s *= 6
print(math.sqrt(s))