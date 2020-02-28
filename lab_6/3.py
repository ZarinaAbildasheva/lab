# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 15:43:00 2020

@author: MARAT
"""

# eval example
x = 5
code = compile('x == 5', '', 'eval')
result = eval(code)
print(result)

code = compile('x + 5', '', 'eval')
result = eval(code)
print(result)