#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 20:46:24 2019

@author: flo
"""

import numpy as np

def findDiv(n):
    divisors = 0 
    for i in range(1,n+1):
        if n%i ==0:
            divisors =divisors +1
    return divisors

def triangle(n):
    num = 0
    for i in range(n+1):
        num = num +i
    return num

biggest = 1
big_pos = 1
for i in range(5000,7000):
    tri = triangle(i)
    div = findDiv(tri)
    if div > biggest:
        biggest = div
        big_pos = i

print(f"{biggest} at {big_pos}")

# 480 divisors at 5984