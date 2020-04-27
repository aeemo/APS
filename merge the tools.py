# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 19:02:04 2020

@author: Apoorva
"""

def merge_the_tools(string, k):
    n=len(string)
    mat1=[]
    mat2=[]
    for i in range(int(n/k)):
        mat=string[i*k:((i+1)*k)]
        mat=list(mat)
        mat1.append(mat)
    for i in range(int(n/k)):
            a=[]
            for j in range(k):
                if (mat1[i][j] not in a):
                    a.append(mat1[i][j])
            mat2.append(a)
    for i in range(int(n/k)):
            mat2[i]=''.join(mat2[i])
            print(mat2[i])