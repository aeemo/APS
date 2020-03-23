# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 20:46:26 2020

@author: Apoorva
"""

#!/bin/python3


import os


# Complete the serviceLane function below.
def serviceLane(n, cases,w):
    res=[]
    for a in cases:
        res.append(min(w[a[0]:a[1]+1]))
    return(res)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nt = input().split()

    n = int(nt[0])

    t = int(nt[1])

    width = list(map(int, input().rstrip().split()))

    cases = []

    for _ in range(t):
        cases.append(list(map(int, input().rstrip().split())))

    result = serviceLane(n, cases,width)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
