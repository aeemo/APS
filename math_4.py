# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 18:19:15 2020

@author: Apoorva
"""

#!/bin/python3

import os
import sys
import math

#
# Complete the primeCount function below.
def isprime(x):
    if x < 2:
        return False
    if x == 2:
        return True
    elif x == 3:
        return True
    else:  # x > 3:
        if x % 2 == 0:
            return False
        if x % 3 == 0:
            return False

        max_divisor = int(math.sqrt(x)) + 1
        increment = 2
        divisor = 5
        while divisor <= max_divisor:
            if x % divisor == 0:
                return False
            divisor += increment
            increment = 6 - increment
        return True



def primeCount(n):
    count=0
    pro=1
    for i in range(2,n+1):
        if isprime(i):
            if pro*i<=n:
                pro*=i
                count+=1
                
            else:
                break

    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        n = int(input())

        result = primeCount(n)

        fptr.write(str(result) + '\n')

    fptr.close()
