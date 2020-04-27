# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 11:34:36 2020

@author: Apoorva
"""

t=int(input())

for _ in range(t):

        n=int(input())
        
        arr=list(map(int,input().strip().split()))
        
        a=[0]*n
        for i in range(n):
            if arr[i]%2!=0:
                a[i]=0
            if arr[i]%2==0:
                a[i]=1
                if arr[i]%4==0:
                    a[i]=2
                    
        if len(a)==1:
            if a[0]==0 or a[0]==2:
                print(1)
            else:
                print(0)
        else:   
                left=[]
                right=[]
                
                for i in range(n):
                    if a[i]==1:
                        if i==0:
                            left.append(0)
                            k=i+1
                            while(a[k]==0):
                                k+=1
                                if k>n-1:
                                     break
                            right.append(k-i-1)
                        elif i==n-1:
                            right.append(0)
                            k=i-1
                            while(a[k]==0):
                                k-=1
                                if k<0:
                                        break
                            left.append(i-k-1)
                        else:
                            k=i-1
                            while(a[k]==0):
                                k-=1
                                if k<0:
                                        break
                            left.append(i-k-1)
                            k=i+1
                            while(a[k]==0):
                                    k+=1
                                    if k>n-1:
                                        break
                            right.append(k-i-1)
                   
                      
                count=n*(n+1)//2
                c=0
                for i in range(len(left)):
                    c+=left[i]+right[i]+1+left[i]*right[i]
                    
                print(count-c)
                        
                    