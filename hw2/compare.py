# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 10:11:45 2014

@author: dchen
"""

def compare(x,y):
    if x > y:
        return 1;
    elif x == y:
        return 0;
    else:
        return -1;
        
print compare(1,2)
print compare(1,1)
print compare(2,1)