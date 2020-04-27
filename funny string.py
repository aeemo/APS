# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 00:09:54 2020

@author: Apoorva
"""

t=int(input())

for _ in range(t):
    s=input()
    o=[ord(s[i]) for i in range(len(s))]
    a=[]
    for i in range(len(s)-1):
        a.append(abs(o[i]-o[i+1]))

    if a==a[::-1]:
        print('Funny')
    else:
        print('Not Funny')
    
