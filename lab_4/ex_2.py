# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 23:24:47 2020

@author: MARAT
"""

import json

# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)