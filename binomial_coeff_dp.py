# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 15:09:28 2020

@author: Apoorva
"""
def bc(n,k):
    c=[[0]*(k+1) for i in range(n+1)]
    for i in range(n+1):
        for j in range(min(i,k)+1):
            if j==0 or i==j:
                c[i][j]=1
            else:
                c[i][j]=c[i-1][j-1]+c[i-1][j]
    return (c[n][k])



n=5
k=3
print(bc(n,k))