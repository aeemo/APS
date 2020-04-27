# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 19:06:20 2020

@author: Apoorva
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT

s=input()
l1=[]
upper=[]
lower=[]
oddnumber=[]
evennumber=[]
for _ in s:
  if _.isupper():
    upper.append(_)
  elif _.islower():
    lower.append(_)
  elif _.isdigit():
    if int(_)%2==0:
      evennumber.append(_)
    elif int(_)%2!=0:
      oddnumber.append(_)
upper=sorted(upper)
lower=sorted(lower)
oddnumber=sorted(oddnumber)
evennumber=sorted(evennumber)

lis=(lower+upper+oddnumber+evennumber)
print("".join(lis))
    
