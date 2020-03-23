# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 21:49:30 2020

@author: Apoorva
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the beautifulDays function below.
def beautifulDays(i, j, b):
    count_beauti=0
    for k in range(i,j+1):
        temp=str(k)
        temp=[temp[i] for i in range(len(temp)-1,-1,-1)]
        temp=int(''.join(temp))
        if abs(temp-k)%b==0:
            #print(temp)
            count_beauti+=1
    return count_beauti

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ijk = input().split()

    i = int(ijk[0])

    j = int(ijk[1])

    k = int(ijk[2])

    result = beautifulDays(i, j, k)

    fptr.write(str(result) + '\n')

    fptr.close()
