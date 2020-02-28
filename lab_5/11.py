# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 15:28:13 2020

@author: MARAT
"""

import re

txt = "The rain in Spain"

#Find all lower case characters alphabetically between "a" and "m":

x = re.findall("[a-m]", txt)
print(x)
