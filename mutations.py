# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 18:38:01 2020

@author: Apoorva
"""

def mutate_string(string, position, character):
    l = list(string)
    l[position] = character
    string = ''.join(l)
    return string