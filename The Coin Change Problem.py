# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 21:33:57 2020

@author: Apoorva
"""

#!/bin/python3

import math
import os
import random
import re
import sys


def getWays(n, c):
    result=[0]*(n+1)
    result[0]=1

    for j in c:
        for i in range(j,n+1):
            result[i]+=result[i-j]


    return(result[n])
    
   



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    c = list(map(int, input().rstrip().split()))

    ways = getWays(n, c)

    print(ways)
