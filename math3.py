# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 18:18:28 2020

@author: Apoorva
"""

#!/bin/python3

import sys
import math

def lowestTriangle(base, area):
    return math.ceil(2*area/base)

base, area = input().strip().split(' ')
base, area = [int(base), int(area)]
height = lowestTriangle(base, area)
print(height)
