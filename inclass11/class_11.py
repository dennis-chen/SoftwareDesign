# -*- coding: utf-8 -*-
"""
Created on Mon Mar  3 14:11:17 2014

@author: dchen
"""
import math
from point import *

def distance_between_points(point_1,point_2):
    return math.sqrt(abs(point_1.x - point_2.x)**2 + abs(point_1.y - point_2.y)**2)
    
def distance_between_points_unit_test():
    p1 = Point()
    p2 = Point()
    p1.x = 3
    p1.y = 3
    p2.x = 0
    p2.y = 0
    print distance_between_points(p1,p2)

#distance_between_points_unit_test()

def move_rectangle(rectangle,dx,dy):
    rectangle.corner[0] = rectangle.corner[0] + dx
    rectangle.corner[1] = rectangle.corner[1] + dy
    return None
    
def move_rectangle_unit_test():
    r = Rectangle()
    r.corner = [1,1]
    move_rectangle(r,1,1)
    print r.corner
    
#move_rectangle_unit_test()
    
def return_new_moved_rectangle(r,dx,dy):
    r2 = Rectangle()
    r2.corner[0] = r2.corner[0] + dx
    r2.corner[1] = r2.corner[1] + dy
    return None

    