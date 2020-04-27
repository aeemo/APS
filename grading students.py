# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 23:50:41 2020

@author: Apoorva
"""

#!/bin/python3

import math
import os
import random
import re
import sys


def gradingStudents(grades):
    result=[]
    for i in grades:
        if i < 38:
            result.append(i)
        else:
            b=(i//5)*5+5
            if abs(i-b)<3:
                result.append(b)
            else:
                result.append(i)
    return(result)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
