#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  2 15:35:29 2022

@author: mg0353
"""

import doctest
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os

SampleRate = 125

path = os.path.dirname(os.getcwd())+"/Trimmed_Data"

def POW_function (fname):
    filename = path + "/" + fname
    RawData = pd.read_csv(filename, sep=',', usecols=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16), skiprows=1, header=None)
    output = np.log(np.mean(np.square(RawData),axis=0))
    #print (output)
    return output

def TRP_function (measurement, reference):
    a = POW_function(measurement)
    b = POW_function(reference)
    TRP = np.subtract(a,b)
    return TRP
    print(TRP)


# For Digital Design - Resting TRP

TRPpath = os.path.dirname(os.getcwd())+"/TRPs"

DigDes_Rest =  np.zeros((16,12),dtype=float)

for participant in range(12):
    N = str(participant+1)
    fnameDigDes = 'P'+N+'_Dig_Des.csv' 
    fnameRest = 'P'+N+'_Resting.csv' 
    TRPoutput = TRP_function(fnameDigDes,fnameRest)
    x = int(participant)
    DigDes_Rest[:,x]=TRPoutput

np.savetxt(TRPpath+"DigDes_Rest_TRP.csv", DigDes_Rest,header="P1,P2,P3,P4,P5,P6,P7,P8,P9,P10,P11,P12",comments="", delimiter=',')

# For Physical Design - Resting TRP

PhysDes_Rest =  np.zeros((16,12),dtype=float)

for participant in range(12):
    N = str(participant+1)
    fnameDigDes = 'P'+N+'_Phys_Des.csv' 
    fnameRest = 'P'+N+'_Resting.csv' 
    TRPoutput = TRP_function(fnameDigDes,fnameRest)
    x = int(participant)
    PhysDes_Rest[:,x]=TRPoutput

np.savetxt(TRPpath+"PhysDes_Rest_TRP.csv", PhysDes_Rest,header="P1,P2,P3,P4,P5,P6,P7,P8,P9,P10,P11,P12",comments="", delimiter=',')

# For Digital Familiarisation - Resting TRP

DigFam_Rest =  np.zeros((16,12),dtype=float)

for participant in range(12):
    N = str(participant+1)
    fnameDigDes = 'P'+N+'_Phys_Des.csv' 
    fnameRest = 'P'+N+'_Resting.csv' 
    TRPoutput = TRP_function(fnameDigDes,fnameRest)
    x = int(participant)
    DigFam_Rest[:,x]=TRPoutput

np.savetxt(TRPpath+"DigFam_Rest_TRP.csv", DigFam_Rest,header="P1,P2,P3,P4,P5,P6,P7,P8,P9,P10,P11,P12",comments="", delimiter=',')

# For Physical Familiarisation - Resting TRP
    
PhysFam_Rest =  np.zeros((16,12),dtype=float)

for participant in range(12):
    N = str(participant+1)
    fnameDigDes = 'P'+N+'_Phys_Des.csv' 
    fnameRest = 'P'+N+'_Resting.csv' 
    TRPoutput = TRP_function(fnameDigDes,fnameRest)
    x = int(participant)
    PhysFam_Rest[:,x]=TRPoutput

np.savetxt(TRPpath+"PhysFam_Rest_TRP.csv", PhysFam_Rest,header="P1,P2,P3,P4,P5,P6,P7,P8,P9,P10,P11,P12",comments="", delimiter=',')
 