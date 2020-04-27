# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 19:12:58 2020

@author: Apoorva
"""

def arrays(arr):
        temp=[]
        for i in arr:
            temp.append(float(i))
        temp=numpy.array(temp)
        return(temp[::-1])