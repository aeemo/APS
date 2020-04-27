# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 23:56:43 2020

@author: Apoorva
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the divisibleSumPairs function below.
def divisibleSumPairs(n, k, ar):
    count=0
    for i in range(n):
        for j in range(n):
            if i<j and (ar[i]+ar[j])%k==0:
                count+=1
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n,k = list(map(int,input().split()))

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
