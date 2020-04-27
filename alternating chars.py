# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 18:11:50 2020

@author: Apoorva
"""

#!/bin/python3

import math
import os
import random
import re
import sys

def reduceString(s, l): 
   count=0
   for i in range(l-1):
        if s[i]==s[i+1]:
            count+=1
   return count



q = int(input())

for q_itr in range(q):
    s = input()

    print(reduceString(s,len(s)))

