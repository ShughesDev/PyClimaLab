#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 22 19:46:24 2023

@author: samuelhughes
"""

import numpy as np

def printmi(x):
    for i in range(len(x)):
        print(i, x[i])

openfile = open("S_seaice_extent_daily_v3.0.csv", "r")
raw_data = []

for line in openfile:
    raw_data.append(line.split("\n")[0].split(","))
    
openfile.close()


column_labels = raw_data[0]
units = raw_data[1]

raw_data = raw_data[2:]

print(raw_data[0])

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
    
printmi(proc_data[0:10])
    
    
    