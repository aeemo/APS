# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 11:25:13 2020

@author: Apoorva
"""

t=int(input())
for _ in range(t):
    N=int(input())
    a=list(map(int,input().strip().split()))
    ind=[]
    for i in range(N):
        if a[i]==1:
            ind.append(i)
    flag=1
    for i in range(len(ind)-1):
        if (ind[i+1]-ind[i])<6:
            flag=0
    if flag==1:
        print('YES')
    else:
        print('NO')
            