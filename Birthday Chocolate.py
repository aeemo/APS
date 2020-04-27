# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 23:55:43 2020

@author: Apoorva
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the birthday function below.
def birthday(s, d, m,n):
    res=0
    for i in range(0,n-m+1):
        if sum(s[i:i+m])==d:
            res+=1
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    dm = input().rstrip().split()

    d = int(dm[0])

    m = int(dm[1])

    result = birthday(s, d, m,n)

    fptr.write(str(result) + '\n')

    fptr.close()
