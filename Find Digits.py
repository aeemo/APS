# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 21:47:37 2020

@author: Apoorva
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the findDigits function below.
def findDigits(n):
    temp=[i for i in str(n)]
    count=0
    for i in range(len(temp)):
        if int(temp[i])!=0:
            if n%int(temp[i])==0:
                count+=1
    return(count)
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = findDigits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
