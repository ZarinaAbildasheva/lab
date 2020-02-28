# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 15:43:28 2020

@author: MARAT
"""

import ast

ast_object = ast.parse("print('Hello world!')")
print(type(ast_object))
code = compile(ast_object, filename="", mode="exec")
print(type(code))
exec(code)