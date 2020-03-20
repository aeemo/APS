# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 20:44:25 2020

@author: Apoorva
"""

def summingSeries(n):
        return n*n%(10**9+7)


t = int(input())
for _ in range(t):
    n = int(input())
    print(summingSeries(n))
        