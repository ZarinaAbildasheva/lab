# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 15:09:36 2020

@author: MARAT
"""

import re

#Check if the string starts with "The" and ends with "Spain":

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

if (x):
  print("YES! We have a match!")
else:
  print("No match")