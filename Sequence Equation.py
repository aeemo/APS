# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 21:48:39 2020

@author: Apoorva
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the permutationEquation function below.
def permutationEquation(p,n):
    result=[]
    for i in range(n):
       a=(p.index(i+1))+1
       result.append((p.index(a)+1))

    return(result)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = list(map(int, input().rstrip().split()))

    result = permutationEquation(p,n)

    print(result)
