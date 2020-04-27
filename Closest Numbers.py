# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 00:04:35 2020

@author: Apoorva
"""

N=int(input())
a=list(map(int,input().strip().split()))
a.sort()

mi=1000000
for i in range(N-1):
        if abs(a[i]-a[i+1])<mi: 
            mi=abs(a[i]-a[i+1])
            diff=[a[i],a[i+1]]
        elif abs(a[i]-a[i+1])==mi :
            diff.append(a[i])
            diff.append(a[i+1])


print(' '.join([str(i) for i in diff]))
