# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 16:00:10 2020

@author: Dell
"""

print("Piyush Khanna")

import re

x = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
y = re.findall('\S+?@\S+', x)
print(y)