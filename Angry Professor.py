# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 00:18:44 2020

@author: Apoorva
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the angryProfessor function below.
def angryProfessor(n, k, a):
        count=0
        for i in a:
            if i<=0:
                count+=1
        if count<k:
            return 'YES'
        else: return 'NO'




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])

        a = list(map(int, input().rstrip().split()))

        result = angryProfessor(n, k, a)

        fptr.write(result + '\n')

    fptr.close()
