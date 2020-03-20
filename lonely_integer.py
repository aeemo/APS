# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 20:48:28 2020

@author: Apoorva
"""
def lonelyinteger(a):
    d={}
    for i in a:
        d[i]=0
    for i in a:
        d[i]+=1
    for i in d.keys():
        if d[i]==1:
            return i
        

n = int(input())
a = list(map(int, input().rstrip().split()))

print( lonelyinteger(a))
