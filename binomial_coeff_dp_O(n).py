# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 15:27:08 2020

@author: Apoorva
"""
def bc(n,k):
    c=[1]
    for i in range(n):
        c.append(0)
    for i in range(1,n+1):
        for j in range(min(i,k),0,-1):
            c[j]=c[j]+c[j-1]
    return c[k]


n=int(input())
k=int(input())
c=bc(n,k)
print(c)