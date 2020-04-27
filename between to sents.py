# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 23:53:48 2020

@author: Apoorva
"""

#!/bin/python3

import os


def getTotalX(a, b):
    t=0
    for i in range(max(a),min(b)+1):
        temp_a=[i%j for j in a]
        temp_b=[k%i for k in b]
        if set(temp_a)=={0} and set(temp_b)=={0}:
            t+=1
    return t

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
