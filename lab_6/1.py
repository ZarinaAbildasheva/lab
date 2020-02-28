# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 15:38:04 2020

@author: MARAT
"""

# compile() with string source
code_str = 'x=5\ny=10\nprint("sum =",x+y)'
code = compile(code_str, 'sum.py', 'exec')
print(type(code))
exec(code)