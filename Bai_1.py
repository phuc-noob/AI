# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
x =int (input('enter a: '))
y =int (input('enter b: '))
z =int (input('enter c: '))

for i in np.arange(0,100,0.01):
    if abs(x*i*i+y*i+z) <=0.5:
        print(i)