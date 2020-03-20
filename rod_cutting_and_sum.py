# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 20:42:36 2020

@author: Apoorva
"""

def rod_cutting(n,arr):
    result=[0]*(n+1)
    for i in range(1,(n+1)):
        result[i]=0
        for j in range(i):
            result[i]=max(result[i],arr[j]+result[i-j-1])
    print(result[n])



n=int(input())
arr=list(map(int,(input().strip().split())))
rod_cutting(n,arr)