# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 11:35:26 2020

@author: Apoorva
"""

import statistics as stat

t=int(input())

for _ in range(t):
    N,M,K=map(int,input().strip().split())
    ans=[]
    if K==2:
        for i in range(N):
            C=list(map(int,input().strip().split()))
            try:
                ans.append(stat.mode(C))
            except:
                ans.append(1)
    else:   
        for i in range(N):
            C=list(map(int,input().strip().split()))
            D=[0]*(M+1)
            for j in range(K):
                    D[C[j]]+=1
            m=max(D)
            ans.append(D.index(m))
    for j in range(N):
        print(ans[j],end=' ')
    print(" ")