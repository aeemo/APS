# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 18:43:59 2020

@author: Apoorva
"""

def compute(s,l,r):
    if(l==r):
        print(''.join(s))
    else:
        for i in range(l,r):
            s[l],s[i]=s[i],s[l]
            compute(s,l+1,r)
            s[l],s[i]=s[i],s[l]
            

s='APS'
s1=[]
s1=list(s)
n=len(s)
compute(s1,0,n)