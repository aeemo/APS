# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 18:14:47 2020

@author: Apoorva
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c,n):
    count=0
    i=0
    if n==2:
            count=1
    while(i<n-2):
        count+=1
        if c[i+2]!=1:
            i=i+2
        elif c[i+2]==1:
            i=i+1
        if i==n-2 and c[i]==0:
            count+=1
        print(i)
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c,n)

    fptr.write(str(result) + '\n')

    fptr.close()
