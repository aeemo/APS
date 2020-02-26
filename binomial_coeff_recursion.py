# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 15:22:15 2020

@author: Apoorva
"""

def bc(n,k):
    if n==k or k==0:
        return 1
    else:
        return(bc(n-1,k-1)+bc(n-1,k))
        
        
print(bc(5,5))