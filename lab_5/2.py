# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 15:15:34 2020

@author: MARAT
"""

import re

txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)