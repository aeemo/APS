# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 00:02:17 2020

@author: Apoorva
"""

t = int(raw_input())
total = 0
n = 3
while total < t:
    total += n
    n *= 2
n /= 2
print total - n + (n-t)+1