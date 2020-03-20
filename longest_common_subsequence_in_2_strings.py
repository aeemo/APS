# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 20:39:42 2020

@author: Apoorva
"""

def max_seq(string1,string2):
    l1=len(string1)
    l2=len(string2)
    lcs=[[0]*(l1+1) for i in range(l2+1)]

    for i in range(1,l2+1):
        for j in range(1,l1+1):
            if string2[i-1]!=string1[j-1]:
                lcs[i][j]=max(lcs[i-1][j],lcs[i][j-1])
            elif string2[i-1]==string1[j-1]:
                lcs[i][j]=lcs[i-1][j-1]+1
    print(max(max(lcs)))

string1=input()
string2=input()
max_seq(string1,string2)