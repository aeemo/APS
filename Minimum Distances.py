# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 20:50:27 2020

@author: Apoorva
"""

#!/bin/python3

import math
import os
import random
import re
import sys

n=int(input())
a=list(map(int,input().strip().split()))

if len(set(a))==n:
    print(-1)
else:
    indices=[]
    for _ in range(n):
        indices.append([i for i, x in enumerate(a) if x == a[_]])
    h=[]
    for _ in range(n):
        if len(indices[_])>1:
            h.append(indices[_][1]-indices[_][0])
    print(min(h))


