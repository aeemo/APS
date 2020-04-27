# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 23:58:01 2020

@author: Apoorva
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the dayOfProgrammer function below.
def dayOfProgrammer(year):
    m=[31,28,31,30,31,30,31,31,30,31,30,31]
    d=256
    s=0
    if year>=1700 and year<=1917:
        z=0
        if year%4==0:
            z=1
        for i in range(8):
            s+=m[i]
        d=256-s-z
    if year==1918:
        return '26.09.1918'
    if year>=1919 and year<=2700:
        z=0
        if year%400==0 or (year%4==0 and year%100!=0):
            z=1
        for i in range(8):
            s+=m[i]
        d=256-s-z
    dd=str(d)
    yy=str(year)
    
    ddmmyy=dd+'.'+'09'+'.'+yy
    return ddmmyy
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()
