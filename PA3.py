# -*- coding: utf-8 -*-
"""
Created on Thu Feb 29 13:05:15 2024

@author: MPenella
"""

import numpy as np
#Part 1
p = np.poly1d([2, 3, 0, 1])
print(p)

q = np.polyval(p, 2)
print(q)

p2 = np.polyder(p)
q2 = np.polyval(p2, 1)
print(q2)
#%%
#Part 2
import numpy as np

def next(p, x, n=1): #Recursion occurs in this function
    xn = x - np.polyval(p, x)/np.polyval((np.polyder(p)), x)  #use newtons method here
    xn = round(xn, 3)
    if xn ==x:              #Checks if x_n+1 is close enough to x_n
        print(f'x_{n}: {xn}')  #if so return x_n+1 as approximate root
        return xn
    else:                           #if not continue recursing with next x
        print(f'x_{n}: {xn}')
        return next(p, xn, n+1)
        
def Newt():
    ps = input("Enter polynomial coefficients: ") #take in polynomial coefficients
    ps = (ps.split(","))
    for i in range(len(ps)):
        ps[i] = int(ps[i])      #convert coefficients into a list of integers
    print(np.poly1d(ps))                #show the polynomial equation
    x1 = float(input("Enter x1: "))   #take in first x_n
    xfinal = next(ps, x1)               #ask for final x_n that is approximate root
    print(f'the final value with stabilized thousandths place is: {xfinal}')
    print(f'roots are {np.roots(ps)}')  #check roots
Newt()


