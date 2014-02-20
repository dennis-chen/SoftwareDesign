# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 11:34:57 2014

@author: pruvolo and dchen
"""

# you do not have to use these particular modules, but they may help
from random import randint
from random import choice
import Image
import math

def build_random_function(min_depth, max_depth):
    # recursively creates random functions from building block functions in functions_list, with maximum recursion depth of max_depth and min recursion depth of min_depth
    return build_random_function_with_specified_depth(randint(min_depth,max_depth))
    

def build_random_function_with_specified_depth(depth):
    # recursively creates random function of a specified depth from building block functions    
    functions_list = ['prod','cos_pi','sin_pi','x','y','sqrt_abs_val','cube'];
    function = choice(functions_list) #choice chooses a random element from the list. hooray for python!
    if depth == 2: #base case
        if function == 'prod' or function == 'x' or function == 'y':
            return [function,['x'],['y']]
        else:
            return[function,[choice(['x','y'])]]
    if function == 'prod' or function == 'x' or function == 'y':  #if function requires two inputs      
        return [function,build_random_function_with_specified_depth(depth-1),build_random_function_with_specified_depth(depth-1)]
    else: #else if function requires one input
        return [function,build_random_function_with_specified_depth(depth-1)]

def evaluate_random_function(f, x, y):
    #given a function f in list format, evaluates that function with inputs x and y
    if len(f) == 1 and f[0] == 'x': #the len(f) part is neccessary to distinguish between the function x and the variable x
        return x
    elif len(f) == 1 and f[0] == 'y':
        return y
    elif f[0] == 'prod':
        return evaluate_random_function(f[1],x,y)*evaluate_random_function(f[2],x,y)
    elif f[0] == 'cos_pi':
        return math.cos(math.pi*evaluate_random_function(f[1],x,y))
    elif f[0] == 'sin_pi':
        return math.sin(math.pi*evaluate_random_function(f[1],x,y))
    elif f[0] == 'x':
        return evaluate_random_function(f[1],x,y)
    elif f[0] == 'y':
        return evaluate_random_function(f[2],x,y)
    elif f[0] == 'sqrt_abs_val':
        return math.sqrt(math.fabs(evaluate_random_function(f[1],x,y)))
    elif f[0] == 'cube':
        return evaluate_random_function(f[1],x,y)**3
   
def remap_interval(val, input_interval_start, input_interval_end, output_interval_start, output_interval_end):
    """ Maps the input value that is in the interval [input_interval_start, input_interval_end]
        to the output interval [output_interval_start, output_interval_end].  The mapping
        is an affine one (i.e. output = input*c + b).
    """
    input_range = input_interval_end - input_interval_start
    output_range = output_interval_end - output_interval_start
    relative_val = val - input_interval_start
    new_val = float(relative_val)*output_range/input_range + output_interval_start #float is used to avoid integer division errors
    return new_val

def gen_random_image():
    """Generates a randomized image, with RGB values described by randomly generated functions. The function loops through 
    an array of pixel values and sets their values by evaluating the randomly generated functions with the pixel coordinates
    as inputs.
    """"
    im = Image.new("RGB",(350,350))
    pixels = im.load()
    rand_func_R = build_random_function(20,30)
    rand_func_G = build_random_function(20,30)
    rand_func_B = build_random_function(20,30)
    for i in range(im.size[0]):
        for j in range(im.size[1]):
            remap_x = remap_interval(i,0,im.size[0],-1,1)
            remap_y = remap_interval(j,0,im.size[1],-1,1)
            rValue = remap_interval(evaluate_random_function(rand_func_R,remap_x,remap_y),-1,1,0,255)
            gValue = remap_interval(evaluate_random_function(rand_func_G,remap_x,remap_y),-1,1,0,255)
            bValue = remap_interval(evaluate_random_function(rand_func_B,remap_x,remap_y),-1,1,0,255)
            pixels[i,j] = (int(rValue),int(gValue),int(bValue))
    im.save('example_8.png')
    
gen_random_image()
    