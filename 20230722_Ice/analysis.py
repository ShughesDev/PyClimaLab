#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 22 19:46:24 2023

@author: samuelhughes
"""

import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

def printmi(x):
    for i in range(len(x)):
        print(i, x[i])

def analyse(hem: str = "n"):
    
    filenames = {"n": "N_seaice_extent_daily_v3.0.csv",
                 "s": "S_seaice_extent_daily_v3.0.csv"}
    openfile = open(filenames[hem], "r")
    raw_data = []
    for line in openfile:
        raw_data.append(line.split("\n")[0].split(","))
    openfile.close()
    
    column_labels = raw_data[0]
    units = raw_data[1]
    raw_data = raw_data[2:]
    proc_data = []
    for i in range(len(raw_data)):
        l = raw_data[i]
        year = int(l[0])
        month = int(l[1])
        day = int(l[2])
        extent = float(l[3]) #10^6 sq km
        missing = float(l[4]) #10^6 sq km
        appn = [year, month, day, extent, missing]
        proc_data.append(appn)
    proc_data = np.array(proc_data, dtype = object)
    a = np.zeros((len(proc_data), 1), dtype = object)
    for i in range(len(proc_data)):
        year = proc_data[i,0]
        month = proc_data[i,1]
        day = proc_data[i,2]
        a[i,0] = datetime(year = year, month = month, day = day)
    proc_data = np.append(proc_data, a, axis = 1)
    
    return proc_data

'''
data_s = analyse("s")
data_n = analyse("n")

#plt.plot(data_s[:,5], data_s[:, 3])
#plt.plot(data_n[:,5], data_n[:,3])

series = data_s[:,3]

local_minima = []
local_maxima = []

for i in range(len(data_s)-1):
    if i > 0:
        if data_s[i,3] > data_s[i+1,3]:
            if data_s[i,3] > data_s[i-1,3]:
                local_maxima.append([data_s[i]])
        elif data_s[i,3] < data_s[i+1,3]:
            if data_s[i,3] < data_s[i-1, 3]:
                local_minima.append(data_s[i])
                
local_minima = np.array(local_minima, dtype = object)
local_maxima = np.array(local_maxima, dtype = object)

plt.plot(local_minima[:,5], local_minima[:,3])
plt.scatter(local_minima[:,5], local_minima[:,3])
'''