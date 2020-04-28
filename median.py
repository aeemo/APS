# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 10:42:21 2020

@author: Apoorva
"""

N=int(input())
arr=list(map(int,input().strip().split()))
arr.sort()
print(arr[N//2])
