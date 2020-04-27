# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 00:14:13 2020

@author: Apoorva
"""

#!/bin/python3

import os
import sys

#
# Complete the pageCount function below.
#
def pageCount(n, p):
    front=0
    back=0
    for i in range(1,p,2):
        front+=1
    for j in range(n,p+1,-2):
        back+=1
    if n-p==1 and n%2==0:
        back+=1
    return min(front,back)

    


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = int(input())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()
