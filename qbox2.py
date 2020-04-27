# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 17:52:30 2020

@author: Apoorva
"""

def to_dec(bi):
    bi=bi[::-1]
    d=0
    for i in range(len(bi)):
        d+=bi[i]*(2**i)
    return(d)

def to_bin(A):
    b=[]
    while(A!=0):
        b.append(A%2)
        A//=2
    b=b[::-1]
    return b


def check_err(D):
    b=to_bin(D)
    t=b[0]
    for i in range(1,len(b)-1):
        t^=b[i]
    if t==b[len(b)-1]:
        print("NO")
        print(to_dec(b[:len(b)-1]))
    else:
        print("YES")

T=int(input())
for _ in range(T):
    D=int(input())
    check_err(D)