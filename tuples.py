# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 19:17:42 2020

@author: Apoorva
"""

if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    integer_list=list(integer_list)
    t=[]
    for i in range(len(integer_list)):
        t.append(integer_list[i])
    t=tuple(t)
    print(str(hash(t)))
    