# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 18:50:11 2020

@author: Apoorva
"""

t=int(input())

for _ in range(t):
       A,B=map(str,input().strip().split())
    
       if int(A) < 10 and int(B)<10:
           print(int(A)+int(B))
       elif int(B)<10 and int(A)>9: 
           val=[[A[0]+B[0],A[1]],[B[0]+A[1],A[0]]]
           
           val=[[int(i) for i in a] for a in val]
           val=[sum(i) for i in val]
           val.append(int(A)+int(B))
           print(max(val))
           
    
       elif int(A)<10 and int(B)>9:
           val=[[B[0]+A[0],B[1]],[A[0]+B[1],B[0]]]
           
           val=[[int(i) for i in a] for a in val]
           val=[sum(i) for i in val]
           val.append(int(A)+int(B))
           print(max(val))
           
           
       else:
           val=[[A[0]+B[0],A[1]+B[1]],[B[1]+A[1],B[0]+A[0]]]
           
           val=[[int(i) for i in a] for a in val]
           val=[sum(i) for i in val]
           val.append(int(A)+int(B))
           print(max(val))