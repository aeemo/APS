# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 11:14:22 2020

@author: Apoorva
"""

t=int(input())
for _ in range(t):
    N=int(input())
    P=list(map(int,input().strip().split()))
    P=sorted(P,reverse=True)
    prof=0
    for i in range(N):
        if P[i]-i>0:
             prof+=P[i]-i
        else:
            break
    print(prof%(10**9+7))