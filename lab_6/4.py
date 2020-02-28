# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 15:43:12 2020

@author: MARAT
"""

bytes_str = bytes('x == 5', 'utf-8')
print(type(bytes_str))
code = compile(bytes_str, '', 'eval')
result = eval(code)
print(result)