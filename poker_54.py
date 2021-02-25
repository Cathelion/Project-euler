#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 22:32:24 2020

@author: flo
"""
class card():
    def __init__(self, value, suit):
        self.value = value
        self.suit =  suit
    def getVal(self):
        return self.value
    def getSuit(self):
        return self.suit



