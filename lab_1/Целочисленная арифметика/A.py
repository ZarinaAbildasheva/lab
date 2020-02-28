# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 17:07:25 2020

@author: MARAT
"""

import math
sign = True
s=0.0
for i in range(1,20,2):
    if (sign == True):
        s+=(4 / i)
    else:
        s -= (4 / i)
    sign = not sign
    
print(s)