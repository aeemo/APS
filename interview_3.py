# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 18:14:01 2020

@author: Apoorva
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    ride=[0]
    c=0
    
    for i in range(n):
        if s[i]=='D':
            c-=1
        else:
            c+=1
        ride.append(c)
    count_dracula=0
    for i in range(n):
        if ride[i]>=0 and ride[i+1]<0:
            count_dracula+=1
    return count_dracula


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
