# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 15:17:03 2020

@author: MARAT
"""

import re

txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x)