# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 18:59:09 2020

@author: Apoorva
"""

def solve(s):
    s1=list(s)
    s1[0]=s[0].upper()
    for c in range(len(s1)):
        if s1[c]==" ":
            n=c
            s1[n+1]=s[n+1].upper()
        else: continue
    s1=''.join(s1)
    return s1