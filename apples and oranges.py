# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 23:51:39 2020

@author: Apoorva
"""

s,t=map(int,input().strip().split(' '))
a,b=map(int,input().strip().split(' '))
m,n=map(int,input().strip().split(' '))
apples = list(map(int, input().strip().split(' ')))
oranges = list(map(int, input().strip().split(' ')))
c_apples=sum([1 for i in apples if (a+i) in range(s,t+1)])
c_oranges=sum([1 for i in oranges if (b+i) in range(s,t+1)])

print(c_apples)
print(c_oranges)