#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 18:40:25 2020

@author: flo
"""
days = []

for year in range(1,101):
    for m in range(1,13):
        if m==4 or m==6 or m==9 or m==11:
            for d in range(1,31):
                days.append(d)
        elif m == 2:
            if year%4 ==0:
                for d in range(1,30):
                    days.append(d)
            else:
                for d in range(1,29):
                    days.append(d)
        else:
            for d in range(1,32):
                days.append(d)
count = 0
for i in range(len(days)):
    if days[i] == 1 and i%7 ==5:
        count +=1
        

