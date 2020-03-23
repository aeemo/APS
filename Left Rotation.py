# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 20:54:01 2020

@author: Apoorva
"""

#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(str, input().rstrip().split()))

    print(' '.join(a[d:]+a[:d]))
