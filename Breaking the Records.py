# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 23:54:08 2020

@author: Apoorva
"""

#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    maxi=scores[0]
    mini=maxi
    count_max=0
    count_min=0
    for i in range(1,n):
        if scores[i]>maxi:
            maxi=scores[i]
            count_max+=1
        if scores[i]<mini:
            mini=scores[i]
            count_min+=1
    result=(count_max,count_min)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
