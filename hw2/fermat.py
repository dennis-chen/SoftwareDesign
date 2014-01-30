# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 09:57:49 2014

@author: dchen
"""

def check_fermat(a,b,c,n):
    if (a**n + b**n) == c:
        print 'Holy smokes, Fermat was wrong!'
    else:
        print "No, that doesn't work."

a = raw_input("Enter integer a: ")
b = raw_input("Enter integer b: ")
c = raw_input("Enter integer c: ")
n = raw_input("Enter integer n: ")

if a.isdigit() and b.isdigit() and c.isdigit() and n.isdigit():
    a = int(a)
    b = int(b)
    c = int(c)
    n = int(n)
else:
    print 'enter numbers only please!'
    
check_fermat(a,b,c,n)