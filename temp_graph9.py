#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 14:53:37 2018

@author: ec2017b118
"""

import numpy as np
x = np.linspace(0,10)
y = x**2

p1 = [1,20]
p2 = [6,70]

plt.plot(x, y)
newline(p1,p2)
plt.show()