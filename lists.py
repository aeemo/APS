# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 18:34:13 2020

@author: Apoorva
"""

if __name__ == '__main__':
    N = int(input())
    li=[]
    for _ in range(N):
        a=input()
        a=a.split()
        if(a[0]=='insert'):
            li.insert(int(a[1]),int(a[2]))
        elif(a[0]=='print'):
            print(li)
        elif(a[0]=='remove'):
            li.remove(int(a[1]))
        elif(a[0]=='append'):
            li.append(int(a[1]))
        elif(a[0]=='sort'):
            li=sorted(li)
        elif(a[0]=='pop'):
            li.pop(len(li)-1)
        elif(a[0]=='reverse'):
            li.reverse()
