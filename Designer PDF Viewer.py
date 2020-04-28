# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 10:42:01 2020

@author: Apoorva
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the designerPdfViewer function below.
def designerPdfViewer(h, word):
    w=len(word)
    heights=[]
    for i in word:
        heights.append(h[ord(i)-97])
    return max(heights)*w

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    fptr.write(str(result) + '\n')

    fptr.close()
