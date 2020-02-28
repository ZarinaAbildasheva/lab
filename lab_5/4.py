# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 15:16:02 2020

@author: MARAT
"""

import re

txt = "The rain in Spain"
x = re.search("\s", txt)

print("The first white-space character is located in position:", x.start())