# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 18:32:33 2020

@author: Apoorva
"""

def count_substring(string, sub_string):
    count=0
    n=len(sub_string)
    for i in range(len(string)):
        if string[i:i+n]==sub_string:
            count+=1
    return count
 



    return

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)