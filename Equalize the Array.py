# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 21:27:39 2020

@author: Apoorva
"""

#!/bin/python3

import math
import os
import random
import re
import sys
import statistics as stat

# Complete the equalizeArray function below.
def equalizeArray(arr):
        d={}
        maxim=-1
        for i in arr:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        for j in d.values():
            if j>=maxim:
                maxim=j
        return(len(arr)-maxim)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = equalizeArray(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
