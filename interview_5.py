# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 18:15:21 2020

@author: Apoorva
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    a=len(s)
    b=n//a
    c=n%a
    count=0
    for i in range(a):
        if s[i]=='a':
            count+=1
    count=count*b
    for i in range(c):
        if s[i]=='a':
            count+=1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
