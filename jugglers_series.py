# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 19:29:38 2020

@author: Apoorva
"""
import math

def juggler(n):
    a=n
    print(a)
    while(a!=1):
        b=0
        if(a%2==0):
            b=math.floor((a)**0.5)
        else:
            b=math.floor((a)**1.5)
        print(b)
        a=b
        
        
#driver
n=int(input())
juggler(n)
            