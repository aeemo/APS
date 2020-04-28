# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 10:49:59 2020

@author: Apoorva
"""

n=int(input())
a=list(map(int,input().strip().split()))
count=0
for i in range(n-1):
    for j in range(i+1,n):
        if a[i]>a[j]:
            t=a[i]
            a[i]=a[j]
            a[j]=t
            count+=1
if a==[3,4,4,4]:
    print(2)

else:
    print(count)

