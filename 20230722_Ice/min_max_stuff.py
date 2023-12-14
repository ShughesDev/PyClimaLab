#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 22 23:31:38 2023

@author: samuelhughes
"""

from analysis import (
    printmi,
    analyse)

import matplotlib.pyplot as plt
import numpy as np

from datetime import datetime, timedelta

def mod(x):
    if x < 0:
        return -x
    else:
        return x

def gradient(x, y):
    
    gx = [x[0]]
    gy = [0]
    
    for i in range(len(x)-1):
        if i > 0:
            dxm = (x[i] - x[i-1]).total_seconds()/(60*60*24)
            dym = y[i] - y[i-1]
            
            mm = dym/dxm
            
            dxp = (x[i+1] - x[i]).total_seconds()/(60*60*24)
            dyp = y[i+1] - y[i]
            
            mp = dyp/dxp
            
            gx.append(x[i])
            gy.append((mm+mp)/2)
            #gy.append(min([mm, mp]))
            
    gx.append(x[-1])
    gy.append(0)
    
    return gx, gy


def local_minmax(x, y):
    
    lmin_x = []
    lmin_y = []
    lmax_x = []
    lmax_y = []
    
    gx, gy = gradient(x, y)
    
    
    miny = min(y)
    maxy = max(y)
    
    c = (miny + maxy)/2
    
    print(c)
    
    for i in range(len(y)):
        
        if y[i] < 2*c/3:
            if mod(gy[i]) < 0.003:
                lmin_x.append(x[i])
                lmin_y.append(y[i])
        elif y[i] > 4*c/3:
            if mod(gy[i]) < 0.001:
                lmax_x.append(x[i])
                lmax_y.append(y[i])
                
    return lmin_x, lmin_y, lmax_x, lmax_y

        
data = analyse("s")

x = data[:,5]
y = data[:,3]

gx, gy = gradient(x, y)

lmix, lmiy, lmax, lmay = local_minmax(x, y)

fig, axs = plt.subplots(ncols = 1, nrows = 1)

axs.plot(x,y)
axs.set_ylabel("SIE (m sq km)")
fig.suptitle("Antarctic Sea-Ice Extent")
axs.set_xlabel("Date")

'''
axs[0].plot(x,y)
axs[1].plot(x,y)
axs[1].scatter(lmix, lmiy)
axs[1].scatter(lmax, lmay)

axs[0].set_ylabel("SIE (m sq km)")
axs[1].set_ylabel("SIE (m sq km)")

axs[1].set_xlabel("Date")

fig.suptitle("Antarctic Sea-Ice Extent")

'''