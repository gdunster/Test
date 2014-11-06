#!/usr/bin/env python
# encoding: utf-8
"""
simple_script.py - generate some random data and then plot a histogram of it

Created by GPD on Nov 6, 2014
"""


import matplotlib.pyplot as plt
import numpy as np

print 'Hello there!'
data = np.random.normal(0,1,200000)
plt.hist(data,100)
plt.show()