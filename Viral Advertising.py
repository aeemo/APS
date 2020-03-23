# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 21:53:34 2020

@author: Apoorva
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the viralAdvertising function below.
def viralAdvertising(n):
    shares=5
    likes=shares//2
    for i in range(n-1):
        shares=(shares//2)*3
        likes+=shares//2
    return(likes)
        



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()
