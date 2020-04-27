# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 00:01:38 2020

@author: Apoorva
"""

t=int(input())
for _ in range(t):
    s=input()
    su=[]
    n=len(s)
    for i in range(1,n+1):
        for j in range(0,n):
            if (s[j:j+i] not in su):
                su.append(s[j:j+i])
    print(su)
