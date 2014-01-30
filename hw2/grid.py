# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 09:34:38 2014

@author: dchen
"""
topLine = '+ - - - - + - - - - +'
threeBars = '|         |         |\n'

def print_bars():
    print (threeBars*4),

def print_line():
    print topLine
    print_bars()

def print_grid():
    print_line()
    print_line()
    print topLine
    
print_grid()

topLine = '+ - - - - + - - - - + - - - - + - - - - +'
fiveBars = '|         |         |         |         |\n'

def print_bars():
    print (fiveBars*4),

def print_line():
    print topLine
    print_bars()

def print_four():
    print_line()
    print_line()
    print_line()
    print_line()
    print topLine

print_four()