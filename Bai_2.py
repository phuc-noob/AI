# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 20:16:38 2021

@author: PC
"""
import numpy as np

a8 =int(input('enter a8: '))
a7 =int(input('enter a7: '))
a6 =int(input('enter a6: '))
a5 =int(input('enter a5: '))
a4 =int(input('enter a4: '))
a3 =int(input('enter a3: '))
a2 =int(input('enter a2: '))
a1 =int(input('enter a1: '))
a0 =int(input('enter a0: '))

for i in np.arange(0,1000000,0.01):
    if a8*i**8 +a7*i**7+a6*i**6+a5*i**5+a4*i**4+a3*i**3+a2*i**2+a1*i+a0 <=0.5:
        print(i)
print("end ...")