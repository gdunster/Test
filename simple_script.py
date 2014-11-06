#!/usr/bin/env python
# encoding: utf-8
"""
simple_script.py - generate some random data and then plot a histogram of it

Created by GPD on Nov 6, 2014
"""

import matplotlib.pyplot as plt
import numpy as np



def show_bryant(data_length=200000, bins=100):
    """Create some data with the normal distribution, then plot it as a histogram
    Takes:
        data_length: how many point to generate (200000)
        bins: how many bins to sort the data into for the histogram (100)
    Gives:
        None
    """

    data = np.random.normal(0,1,data_length)
    plt.hist(data, bins)
    plt.show()


def main():
    show_bryant(200000, 100)


if __name__ == '__main__':
    main()