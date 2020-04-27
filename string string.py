# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 19:00:03 2020

@author: Apoorva
"""

if __name__ == '__main__':
    s = input()
    lis=[]
    for i in s:
        lis.append(i)  
    
    
    check=[0]*5
    for i in lis:
        if i.isalnum():
            check[0]+=1
        if i.isalpha():
            check[1]+=1
        if i.isdigit():
            check[2]+=1
        if i.islower():
            check[3]+=1
        if i.isupper():
            check[4]+=1
        
    for i in check:
        if i>0:
            print("True")
        else:
            print("False")

