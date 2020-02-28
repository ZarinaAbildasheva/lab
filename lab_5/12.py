# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 15:28:31 2020

@author: MARAT
"""

import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.string)