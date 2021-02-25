#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 15:40:22 2019

@author: flo
"""

import numpy as np

def gcd(a, b):  
    if a == 0 : 
        return b        
    return gcd(b%a, a) 


def reduce(n,d):
    gcd1 = gcd(n,d)
    n = n/gcd1
    d = d/ gcd1
    return (n,d)

A = set()
for d in range(4,12001):
    for i in range((d//3+1),int(np.ceil(d/2-1))+1):
        frac = reduce(i,d)
        A.add(frac)
    

print(len(A))
# takes about 15 seconds to calculate