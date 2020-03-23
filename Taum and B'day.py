# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 21:26:49 2020

@author: Apoorva
"""

#!/bin/python3

import math
import os
import random
import re
import sys


def taumBday(b, w, bc, wc, z):
    a=b*bc+w*wc
    c=b*bc+w*(bc+z)
    d=b*(wc+z)+w*wc
    return(min(a,d,c))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        b = int(first_multiple_input[0])

        w = int(first_multiple_input[1])

        second_multiple_input = input().rstrip().split()

        bc = int(second_multiple_input[0])

        wc = int(second_multiple_input[1])

        z = int(second_multiple_input[2])

        result = taumBday(b, w, bc, wc, z)

        fptr.write(str(result) + '\n')

    fptr.close()
