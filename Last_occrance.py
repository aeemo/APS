# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 22:16:34 2020

@author: Apoorva
"""

n,m=map(int,input().strip().split())
arr=list(map(int,input().strip().split()))
ind=-1
for i in range(n):
    if arr[i]==m and i>ind:
        ind=i
print(ind+1)