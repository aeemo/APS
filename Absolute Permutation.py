# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 00:12:37 2020

@author: Apoorva
"""

s=input()

c=1

for i in range(len(s)):
    if s[i].isupper():
        c+=1

print(c)