# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 22:16:42 2020

@author: Apoorva
"""

T=int(input())
for _ in range(T):
        N,M=map(int,input().strip().split())
        f=list(map(int,input().strip().split()))
        P=list(map(int,input().strip().split()))
        
        d={}
        
        for i in range(N):
            if f[i] not in d:
                d[f[i]]=P[i]
            else:
                d[f[i]]+=P[i]
        
        
        a=[]
        
        for i in d.values():
                a.append(i)
                
        print(min(a))