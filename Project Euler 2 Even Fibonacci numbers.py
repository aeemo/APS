# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 20:15:32 2020

@author: Apoorva
"""

import sys
def compute(n):
    ans = 0
    x = 1  
    y = 2  
    while x <=n:
        if x % 2 == 0:
            ans += x
        x, y = y, x + y
    return str(ans)

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    a=compute(n)
    print(a)