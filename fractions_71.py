#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 20:59:13 2019

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
    return n,d


closestFrac = np.array([1,3])
for d in range(3,1000000):
    nLow =  (d * 3) // 7
    #nUp =  (d * 3) // 7 + 1
    num,denom = reduce(nLow, d)
    if num == 3 and denom == 7:
        continue
    
    elif  (3/7)- (num/denom) < (3/7) - (closestFrac[0]/closestFrac[1]):
        closestFrac[0] = num
        closestFrac[1] = denom

print(closestFrac)



















    