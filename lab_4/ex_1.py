# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 23:22:55 2020

@author: MARAT
"""

import json

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])