#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 17:30:42 2019

@author: flo
"""
import numpy as np

def pytho(p):
    count =0
    for a in range(1,p//2):
        for b in range(1,p):
            c = np.sqrt(a**2+b**2)
            if c.is_integer() and a+b+c==p:
                count = count+1
    return count                
                
max =0
max_val = 0                
for p in range(1,1000):
    if p%20 ==0:
        print(p)
    val = pytho(p)
    if val > max_val:
        max_val = val
        max = p
        
print(max)
print(max_val)
