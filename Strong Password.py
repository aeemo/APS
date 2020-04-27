# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 00:02:55 2020

@author: Apoorva
"""

N=int(input())
s=input()

D={'D':0,'L':0,'U':0,'S':0}

for i in range(N):
    if ord(s[i])>47 and ord(s[i])<59:
        D['D']+=1
    elif ord(s[i])>96 and ord(s[i])<123:
        D['L']+=1
    elif ord(s[i])>64 and ord(s[i])<91:
        D['U']+=1
    else:
        D['S']+=1

c=0
for i in D.values():
    if i>0:
        c+=1

if c==4 and N>5:
    print(0)
elif N<6 and c==4:
    print(6-N)
else:
    if N>5:
        print(4-c)
    if N<6:
        a=6-N
        b=4-c
        print(max(a,b))

