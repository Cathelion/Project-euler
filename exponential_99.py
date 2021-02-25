#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 20:25:58 2019

@author: flo
"""
import numpy as np

data = np.array([])

f = open('p099_base_exp.ext', 'r')
x = f.readlines()
f.close()

for line in x:
    data.append(line)