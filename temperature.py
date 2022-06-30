# -*- coding: utf-8 -*-
"""
Created on Thu Jun 30 15:35:13 2022

@author: kylea
"""

import numpy as np


def f_to_c(f):
    #This function converts fahrenheit to celsius
    c = (f - 32) * 5 / 9
    return c

def cToK(c):
    return c - 273.15
