# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 20:36:51 2020

@author: Apoorva
"""

def Moby(W, wt, val, n): 
    K = [[0 for x in range(W+1)] for x in range(n+1)] 
  
 
    for i in range(n+1): 
        for w in range(W+1): 
            if i==0 or w==0: 
                K[i][w] = 0
            elif wt[i-1] <= w: 
                K[i][w] = max(val[i-1] + K[i-1][w-wt[i-1]],  K[i-1][w]) 
            else: 
                K[i][w] = K[i-1][w] 
  
    return K[n][W] 


n=int(input())
val=[]
wt=[]
for i in range(n):
    a=list(map(int,input().strip().split()))
    val.append(a[1])
    wt.append(a[0])
W=int(input())

res=Moby(W,wt,val,n)
print(res)