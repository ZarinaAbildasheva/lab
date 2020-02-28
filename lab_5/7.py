# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 15:16:49 2020

@author: MARAT
"""

import re

txt = "The rain in Spain"
x = re.split("\s", txt, 1)
print(x)