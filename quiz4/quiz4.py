# -*- coding: utf-8 -*-
"""
Created on Thu Mar  6 13:32:10 2014

@author: dchen
"""

def exclusive_or_dict(d1,d2):
    new_dict = {}
    for key in d1:
        if key not in d2:
            new_dict[key] = d1[key]
    for key in d2:
        if key not in d1:
            new_dict[key] = d2[key]
    return new_dict
    
def exclusive_or_dict_unit_test():
    print "input: {'a':5,'b':3},{'a':7,'c':3}, expected: {'b':3,'c':3}"
    print exclusive_or_dict({'a':5,'b':3},{'a':7,'c':3})
    print "input: {'test':5,'b':7.0,3:'q'},{'b':'world',3:'q'}, expected: {'test':5}"
    print exclusive_or_dict({'test':5,'b':7.0,3:'q'},{'b':'world',3:'q'})
    print "input: {'c':67,'d':99},{'c':7,'d':12}, expected: {}"
    print exclusive_or_dict({'c':67,'d':99},{'c':7,'d':12})    
    
    
exclusive_or_dict_unit_test()