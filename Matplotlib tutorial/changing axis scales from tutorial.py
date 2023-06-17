#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt

x = []
y = []

for i in range(-10000,10000):
    x.append(i/100)
    y.append(i/100)
    
plt.plot(x,y)
plt.xscale("linear")
plt.yscale("linear")
plt.show()

plt.plot(x,y)
plt.xscale("log",basex = 10,subsx = [2,3,4,5,6])
#plt.yscale("log",basey = 5,subsy)
plt.show()

plt.plot(x,y)
plt.xscale("symlog",basex = 5,subsx = [2,3],linthreshx = 1)
#(-10,10)
plt.show()

plt.plot(x,y)
plt.xscale("logit")
plt.show()