# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 07:15:40 2020

@author: S.Narain Ramaswamy
"""

from multipledispatch import dispatch
@dispatch(float)
def CalculateArea(side):
    area_of_square = 4 * (side**2)
    print("The area of square is: ",format(area_of_square,'0.2f'))
@dispatch(float,float)
def CalculateArea(length,breadth):
    area_of_rect = length * breadth
    print("The area of rectangle is: ",format(area_of_rect,'0.2f'))
@dispatch(float,int)
def CalculateArea(pi,radius):
    area_of_circle = 4 * pi * (radius**2)
    print("The area of circle is: ",format(area_of_circle,'0.2f'))
        
choice = int(input("Which area would you like to find 1.Square,2.Rectangle,3.Circle"))
if choice == 1:
    CalculateArea(5.6)
elif choice == 2:
    CalculateArea(9.8,4.9)
else:
    CalculateArea(3.14,7)    
