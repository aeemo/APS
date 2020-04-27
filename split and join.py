# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 18:53:33 2020

@author: Apoorva
"""

def split_and_join(line):
    line=line.split(" ")
    line= "-".join(line)
    return line

    # write your code here

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)