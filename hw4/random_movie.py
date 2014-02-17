# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 11:34:57 2014

@author: pruvolo
"""

from random import choice
import Image
import math

def build_random_function(depth):
    # your doc string goes here
    # recursively creates random functions from building block functions in functions_list, with maximum recursion depth of max_depth and min recursion depth of min_depth
    # your code goes here
    functions_list = ['prod','cos_pi','sin_pi','x','y','t'];
    #,'sqrt_abs_val','cube'
    function = choice(functions_list)
    if depth == 2:
        if function == 'prod' or function == 'x' or function == 'y' or function == 't':
            return [function,['x'],['y'],['t']]
        else:
            return[function,[choice(['x','y','t'])]]
    if function == 'prod' or function == 'x' or function == 'y' or function == 't':        
        return [function,build_random_function(depth-1),build_random_function(depth-1),build_random_function(depth-1)]
    else:
        return [function,build_random_function(depth-1)]
'''
rand_func = build_random_function(5)
print rand_func
print "length: "+str(len(rand_func))
'''
def evaluate_random_function(f, x, y, t):
    # your doc string goes here
    #given a function f in list format, evaluates that function with inputs x and y
    # your code goes here
    if len(f) == 1 and f[0] == 'x':
        return x
    elif len(f) == 1 and f[0] == 'y':
        return y
    elif len(f) == 1 and f[0] == 't':
        return t
    elif f[0] == 'prod':
        return evaluate_random_function(f[1],x,y,t)*evaluate_random_function(f[2],x,y,t)*evaluate_random_function(f[3],x,y,t)
    elif f[0] == 'cos_pi':
        return math.cos(math.pi*evaluate_random_function(f[1],x,y,t))
    elif f[0] == 'sin_pi':
        return math.sin(math.pi*evaluate_random_function(f[1],x,y,t))
    elif f[0] == 'x':
        return evaluate_random_function(f[1],x,y,t)
    elif f[0] == 'y':
        return evaluate_random_function(f[2],x,y,t)
    elif f[0] == 't':
        return evaluate_random_function(f[3],x,y,t)
    elif f[0] == 'sqrt_abs_val':
        return math.sqrt(math.fabs(evaluate_random_function(f[1],x,y,t)))
    elif f[0] == 'cube':
        return evaluate_random_function(f[1],x,y,t)**3
   
   
def remap_interval(val, input_interval_start, input_interval_end, output_interval_start, output_interval_end):
    """ Maps the input value that is in the interval [input_interval_start, input_interval_end]
        to the output interval [output_interval_start, output_interval_end].  The mapping
        is an affine one (i.e. output = input*c + b).
    """
    input_range = input_interval_end - input_interval_start
    output_range = output_interval_end - output_interval_start
    relative_val = val - input_interval_start
    new_val = float(relative_val)*output_range/input_range + output_interval_start
    return new_val

def gen_random_image(t,rand_func_R,rand_func_G,rand_func_B):
    im = Image.new("RGB",(350,350))
    pixels = im.load()
    for i in range(im.size[0]):
        for j in range(im.size[1]):
            remap_x = remap_interval(i,0,im.size[0],-1,1)
            remap_y = remap_interval(j,0,im.size[1],-1,1)
            #remap_t = remap_interval(t,t_start,t_end,-1,1)
            rValue = remap_interval(evaluate_random_function(rand_func_R,remap_x,remap_y,t),-1,1,0,255)
            gValue = remap_interval(evaluate_random_function(rand_func_G,remap_x,remap_y,t),-1,1,0,255)
            bValue = remap_interval(evaluate_random_function(rand_func_B,remap_x,remap_y,t),-1,1,0,255)
            pixels[i,j] = (int(rValue),int(gValue),int(bValue))
    return im
    
def gen_random_image_set(t_start,t_end,t_steps):
    counter = 0    
    rand_func_R = build_random_function(8)
    rand_func_G = build_random_function(8)
    rand_func_B = build_random_function(8)
    print rand_func_R
    print rand_func_G
    print rand_func_B
    for i in range(1,t_steps):
        im = gen_random_image((t_end - t_start)/float(t_steps)*i,rand_func_R,rand_func_G,rand_func_B)
        counter+=1
        if counter < 10:
            im.save('example_video_part_00'+str(counter)+'.png')        
        else:
            im.save('example_video_part_0'+str(counter)+'.png')
        
gen_random_image_set(-1,1,100)
        