# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 19:18:50 2020

@author: Apoorva
"""

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()