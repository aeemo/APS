# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 20:25:18 2020

@author: Apoorva
"""

def value(a):
    if a>='0' and a<='9':
        return ord(a)-ord('0')
    else:
        return ord(a)-ord('A')+10
def ln(x):
    n = 1000000.0
    return n * ((x ** (1/n)) - 1)

def decimal(Q,qur):
    for i in range(Q):
        x,b=qur[i]
        if b=='2':
            print(len(x))
        else:        
                dec=0
                base=int(b)   
                mul=1         
                for i in range(len(x) - 1, -1, -1):
                    val=value(x[i])
                    dec+=val*mul
                    mul*=base
                le=round(ln(dec)/ln(2),4)
                print(int(le)+1)

            
Q=int(input())
qur=[]
for i in range(Q):
    q=input().split()
    qur.append(q) 
decimal(Q,qur)