# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 20:51:02 2020

@author: Apoorva
"""

#!/bin/python3

import math
import os
import random
import re
import sys


t=int(input())

for i in range(t):
    a,b=map(int,input().strip().split())
    a=math.ceil(a**0.5)
    b=math.floor(b**0.5)+1
    print(b-a)


