# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 00:06:15 2020

@author: Apoorva
"""

import sys


n = int(input().strip())
B = map(int, list(input().strip()))

count=0
for i in range(2,n):
    if B[i-2]==0 and B[i-1]==1 and B[i]==0:
        B[i]=1
        count+=1
print (count)
