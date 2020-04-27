# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 22:52:14 2020

@author: Apoorva
"""

n=int(input())
 
chats=[]
for i in range(n):
    chats.append(input().strip().split())
 
weig={'19':0,'20':0}
 
for i in range(n):
    for j in chats[i]:
        if j.isnumeric():
            weig[j]=0
 
for i in range(n):
    for j in chats[i]:
        if j.isnumeric():
            if chats[i][0]=='G:':
                    weig[j]+=2
            else:
                weig[j]+=1
    
flag=1            
for i in weig:
    if (weig['19']<weig[i] or weig['19']==weig[i]) and (weig['20']<weig[i] or weig['20']==weig[i]) and i!='19' and i!='20':
        flag=0
 
if flag==0:
    print('No Date')
else:
    print('Date')
        