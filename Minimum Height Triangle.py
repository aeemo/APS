# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 20:29:24 2020

@author: Apoorva
"""

import sys
import math

def lowestTriangle(base, area):
    return math.ceil(2*area/base)

base, area = input().strip().split(' ')
base, area = [int(base), int(area)]
height = lowestTriangle(base, area)
print(height)
