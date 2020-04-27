# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 23:49:44 2020

@author: Apoorva
"""

#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
  s=s.split(':')
  if s[2][2:]=='AM':
    if s[0]=='12':
      s[0]='00'
  if s[2][2:]=='PM':
    if s[0]=='12':
       s=s
    else:
      s[0]=int(s[0])+12
      s[0]=str(s[0])
  s[2]=s[2][:2]
  s=':'.join(s)
  return(s)

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
