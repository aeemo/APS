# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 18:20:37 2020

@author: Apoorva
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(n, m):
    c=min(n,m)
    d=max(n,m)
    return c*(d-1)+(c-1)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    result = solve(n, m)

    fptr.write(str(result) + '\n')

    fptr.close()
