# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 23:59:59 2020

@author: Apoorva
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the bonAppetit function below.
def bonAppetit(bill, k, b):
    bill.remove(bill[k])
    temp=sum(bill)/2
    if temp<b:
        print( int(abs(temp-b)))
    else: print ('Bon Appetit')

if __name__ == '__main__':
    nk = input().rstrip().split()

    n = int(nk[0])

    k = int(nk[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)
