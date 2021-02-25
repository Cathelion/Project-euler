#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 18:01:41 2019

@author: flo
"""

import numpy as np

def divides(x):
    divider = np.array([])
    for i in range(2,x+1):
        if x%i==0:
            divider = np.append(divider,i)
    return divider


def relPrime(x,y):
    if x > y:
        y,x = x,y
        
    xDivider = divides(x)
    for i in xDivider:
        if y% i == 0:
            return False
    else:
        return True

def findCoprimes(x):
    coPrimes = np.array([])
    for i in range(1,x):
        if relPrime(i,x):
            coPrimes = np.append(coPrimes, i)
    return len(coPrimes)

biggestVal = 0
biggestNum = 0
for n in range(2,1000000):
    ratio = n/findCoprimes(n)
    if ratio > biggestVal:
        biggestVal = ratio
        biggestNum = n

print(biggestNum)
