# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 00:00:51 2020

@author: Apoorva
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    new=list(set(ar))
    arr=[]
    for i in range(len(new)):
        temp=0
        for j in range(n):
            if new[i]==ar[j]:
                temp+=1
        arr.append(temp)
    a=0
    for i in arr:
        a+=i//2
    return a

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
