# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 11:26:02 2020

@author: Apoorva
"""

t=int(input())
for _ in range(t):
    N=int(input())
    
    
    
    if N==1:
        print(1)
        print(1,1)
    elif N== 2:
        print(1)
        print(2,1,2)
    else:
        if N%2==0:
            N1=N//2
        else:
            N1=(N-1)//2
        print(N1)
        print(3,1,2,3)
        
        if N%2==0:
            for i in range(4,N-1,2):
                print(2,i,i+1)
            print(1,N)
        else:
            for i in range(4,N,2):
                print(2,i,i+1)
        
            
