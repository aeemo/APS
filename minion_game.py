# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 18:36:16 2020

@author: Apoorva
"""

def minion_game(string):
        vowels=['A','E','I','O','U']
        n=len(s)
        stuart=0
        kevin=0
        for i in range(n):
            if s[i] in vowels:
                kevin += n - i
            else:
                stuart += n - i
        if kevin>stuart:
            print("Kevin",kevin)
        elif stuart>kevin:
            print("Stuart",stuart)
        else:
            print("Draw")

