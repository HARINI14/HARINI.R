#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 14:56:44 2018

@author: ec2017b118
"""

import numpy as np
import matplotlib.pyplot as plt

# compute coefficients
coefficients = np.polyfit([-0.3, 0.8], [-0.5, 0.8], 1) 

# create a polynomial object with the coefficients
polynomial = np.poly1d(coefficients)

# for the line to extend beyond the two points, 
# create the linespace using the min and max of the x_lim
# I'm using -1 and 1 here
x_axis = np.linspace(-1, 1)

# compute the y for each x using the polynomial
y_axis = polynomial(x_axis)

fig = plt.figure()
axes = fig.add_axes([0.1, 0.1, 1, 1])
axes.set_xlim(-1, 1)
axes.set_ylim(-1, 1)
axes.plot(x_axis, y_axis)
axes.plot(-0.3, -0.5, 0.8, 0.8, marker='o', color='red')