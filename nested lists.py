# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 18:51:15 2020

@author: Apoorva
"""

if __name__ == '__main__':
   n=int(input())
   mat=[0]*n
   for _ in range(n):
        name = input()
        score = float(input())
        mat[_]=[name,score]
   scr=[]
   for _ in range(n):
        scr.append(mat[_][1])
   scr=list(set(scr))
   scr=sorted(scr)
   new_mat=[]
   for _ in range(n):
        if mat[_][1]==scr[1]:
            new_mat.append(mat[_][0])
   new_mat=sorted(new_mat)
   for _ in range(len(new_mat)):
        print(new_mat[_])


