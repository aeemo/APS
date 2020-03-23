# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 20:54:18 2020

@author: Apoorva
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the appendAndDelete function below.
def appendAndDelete(s, t, k):
    i=0
    x,y=len(s),len(t)
    if s==t and x+y<=k:
        return('Yes')
    while(s[i]==t[i] and i<(min(x,y)-1) ):
        i+=1
   
    if len(s[i:])+len(t[i:])<=k:
        return('Yes')
    else: return('No')


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    t = input()

    k = int(input())

    result = appendAndDelete(s, t, k)

    fptr.write(result + '\n')

    fptr.close()
