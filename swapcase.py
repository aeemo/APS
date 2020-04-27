# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 18:33:48 2020

@author: Apoorva
"""

def swap_case(s):

    return s.swapcase()

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)