# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 10:51:48 2020

@author: Apoorva
"""

#!/bin/python3

import os
import sys

#
# Complete the findPoint function below.
#
def findPoint(px, py, qx, qy):
    rx=qx+(qx-px)
    ry=qy+(qy-py)

    return(''.join([str(rx),str(ry)]))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    for n_itr in range(n):
        pxPyQxQy = input().split()

        px = int(pxPyQxQy[0])

        py = int(pxPyQxQy[1])

        qx = int(pxPyQxQy[2])

        qy = int(pxPyQxQy[3])

        result = findPoint(px, py, qx, qy)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
