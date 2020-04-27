# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 11:26:13 2020

@author: Apoorva
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 20:33:54 2020

@author: Apoorva
"""

import math as mt 
  

def kFactors(n, k): 
      
    a = list() 
      
    while n % 2 == 0: 
        a.append(2) 
        n = n // 2
          
    for i in range(3, mt.ceil(mt.sqrt(n)), 2): 
        while n % i == 0: 
            n = n / i; 
            a.append(i) 
              
    if n > 2: 
        a.append(n) 
          
    if len(a) < k: 
        print(0) 
        return
    else:
        print(1)
  

t=int(input())

for _ in range(t):
    x,k=map(int,input().strip().split())
    kFactors(x, k)
    
    