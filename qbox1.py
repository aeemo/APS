# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 17:50:45 2020

@author: Apoorva
"""

import numpy as np
E,D,A=map(int, input().strip().split())
H1=E
H2=np.tan(np.deg2rad(A))*D
H=H1+H2
print ('%.2+f'%H)