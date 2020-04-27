# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 18:49:06 2020

@author: Apoorva
"""

def  countSetBits(n): 
    count = 0
    while (n): 
        count += n & 1
        n >>= 1
    return count 
  
i = 9
print(countSetBits(i)) 