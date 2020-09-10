# -*- coding: utf-8 -*-
import numpy as np

x=[1,10,1000]

a = np.e**(1/(np.sin(x)+1))

for i in x:
    b = 5/4 +(i**1)*15
    y = (np.log(a/b)) / (np.log(1+i**2))

print (x)

print (y)

