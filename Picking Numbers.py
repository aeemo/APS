# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 21:30:10 2020

@author: Apoorva
"""

#!/bin/python3

import math
import os
import random
import re
import sys


def pickingNumbers(a,n):
    a=sorted(a)
    count=[]
    mx=0
    for i in range(n-1):
        c=0
        for j in range(i,n):
            if abs(a[i]-a[j])<=1:
                c+=1
        if c>=mx:
            mx=c

    return(mx)

            



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a,n)

    fptr.write(str(result) + '\n')

    fptr.close()
