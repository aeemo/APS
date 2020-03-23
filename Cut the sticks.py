# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 21:40:15 2020

@author: Apoorva
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the cutTheSticks function below.
def cutTheSticks(arr,n):
    a=sorted(arr)
    res=[]
    for i in a:
        count=0
        for j in a:
            if i<=j:
                count+=1
        if count not in res:
            res.append(count)
    return(res)


    


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr,n)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
