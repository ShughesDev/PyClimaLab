#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 22 23:39:29 2023

@author: samuelhughes
"""

import numpy as np
import matplotlib.pyplot as plt

import math

x_test = list(range(0,1000))


y_test = []

for x in x_test:
    y_test.append(math.sin(x/(math.pi*4))*math.sin(x/math.pi*20.012))
    
    
plt.plot(x_test, y_test)

