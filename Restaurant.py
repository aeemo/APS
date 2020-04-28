# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 10:48:59 2020

@author: Apoorva
"""

#!/bin/python3

import os
import sys

#
# Complete the restaurant function below.
#
def restaurant(l, b):
    if l==b:
        return 1
    a=max(l,b)
    facts=[]
    for i in range(1,a):
        if l%i==0 and b%i==0:
            facts.append(i)
    a=max(facts)
    return (l*b)//(a*a)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        lb = input().split()

        l = int(lb[0])

        b = int(lb[1])

        result = restaurant(l, b)

        fptr.write(str(result) + '\n')

    fptr.close()
