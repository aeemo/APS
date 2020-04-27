# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 19:14:22 2020

@author: Apoorva
"""

import numpy
s1=input()
N=int(s1[0])
M=int(s1[2])
P=int(s1[4])
array_1=[]
array_2=[]
for i in range(N):
  a=input()
  o=[]
  for j in range(2*P-1):
    if j%2==0:
      o.append(int(a[j]))
  array_1.append(o)
for i in range(M):
  a=input()
  o=[]
  for j in range(2*P-1):
    if j%2==0:
      o.append(int(a[j]))
  array_2.append(o)
array_1=numpy.array(array_1)
array_2=numpy.array(array_2)


print(numpy.concatenate((array_1, array_2), axis = 0))


