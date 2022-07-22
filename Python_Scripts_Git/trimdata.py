import doctest
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd 

#### Script to cut down raw data into individual epochs of interest.

Sample_rate = 125
# Sample rate of EEG data capture. 


# Read CSV of experiment timings which defines regions of interest in the raw data.

ExperimentTimings = pd.read_csv('Study_timings.csv', sep=',', usecols=(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22), skiprows=1, header=0, nrows= 12)
print(ExperimentTimings)

#### Resting data 

resting_filenames = ExperimentTimings.iloc[:,4]
resting_start = Sample_rate * ExperimentTimings.iloc[:,5]
resting_end = Sample_rate * ExperimentTimings.iloc[:,6]

# Open raw EEG data for each participant, trim to region of interest for digital familiarisation and export as CSV.

for participant in range(12):
    rawdata = np.loadtxt(fname="RawData/%s" %resting_filenames[participant], delimiter=',', skiprows=5, usecols=(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,30))
    trimmed_data = rawdata[resting_start[participant]:resting_end[participant]]
    pcp =  int(participant) + 1
    np.savetxt("Trimmed_Data/P%s_Resting.csv" %pcp, trimmed_data, header="Sample Index, EEG1, EEG2, EEG3, EEG4, EEG5, EEG6, EEG7, EEG8, EEG9, EEG10, EEG11, EEG12, EEG13, EEG14, EEG15, EEG16, accl1, accl2, accl3, Unix TimeStamp", comments="", delimiter=',')

#### Digital familiarisation 

Dig_Fam_filenames = ExperimentTimings.iloc[:,8]
Dig_Fam_start = Sample_rate * ExperimentTimings.iloc[:,9]
Dig_Fam_end = Sample_rate * ExperimentTimings.iloc[:,10]

for participant in range(12):
    rawdata = np.loadtxt(fname="RawData/%s" %Dig_Fam_filenames[participant], delimiter=',', skiprows=5, usecols=(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,30))
    trimmed_data = rawdata[Dig_Fam_start[participant]:Dig_Fam_end[participant]]
    pcp =  int(participant) + 1
    np.savetxt("Trimmed_Data/P%s_Dig_Fam.csv" %pcp, trimmed_data, header="Sample Index, EEG1, EEG2, EEG3, EEG4, EEG5, EEG6, EEG7, EEG8, EEG9, EEG10, EEG11, EEG12, EEG13, EEG14, EEG15, EEG16, accl1, accl2, accl3, Unix TimeStamp", comments="", delimiter=',')

#### Digital Design 

Dig_Des_filenames = ExperimentTimings.iloc[:,12]
Dig_Des_start = Sample_rate * ExperimentTimings.iloc[:,13]
Dig_Des_end = Sample_rate * ExperimentTimings.iloc[:,14]

for participant in range(12):
    rawdata = np.loadtxt(fname="RawData/%s" %Dig_Des_filenames[participant], delimiter=',', skiprows=5, usecols=(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,30))
    trimmed_data = rawdata[Dig_Des_start[participant]:Dig_Des_end[participant]]
    pcp =  int(participant) + 1
    np.savetxt("Trimmed_Data/P%s_Dig_Des.csv" %pcp, trimmed_data, header="Sample Index, EEG1, EEG2, EEG3, EEG4, EEG5, EEG6, EEG7, EEG8, EEG9, EEG10, EEG11, EEG12, EEG13, EEG14, EEG15, EEG16, accl1, accl2, accl3, Unix TimeStamp", comments="", delimiter=',')

#### Physical familiarisation 

Phys_Fam_filenames = ExperimentTimings.iloc[:,16]
Phys_Fam_start = Sample_rate * ExperimentTimings.iloc[:,17]
Phys_Fam_end = Sample_rate * ExperimentTimings.iloc[:,18]

for participant in range(12):
    rawdata = np.loadtxt(fname="RawData/%s" %Phys_Fam_filenames[participant], delimiter=',', skiprows=5, usecols=(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,30))
    trimmed_data = rawdata[Phys_Fam_start[participant]:Phys_Fam_end[participant]]
    pcp =  int(participant) + 1
    np.savetxt("Trimmed_Data/P%s_Phys_Fam.csv" %pcp, trimmed_data, header="Sample Index, EEG1, EEG2, EEG3, EEG4, EEG5, EEG6, EEG7, EEG8, EEG9, EEG10, EEG11, EEG12, EEG13, EEG14, EEG15, EEG16, accl1, accl2, accl3, Unix TimeStamp", comments="", delimiter=',')

#### Physical Design

Phys_Des_filenames = ExperimentTimings.iloc[:,20]
Phys_Des_start = Sample_rate * ExperimentTimings.iloc[:,21]
Phys_Des_end = Sample_rate * ExperimentTimings.iloc[:,22]

for participant in range(12):
    rawdata = np.loadtxt(fname="RawData/%s" %Phys_Des_filenames[participant], delimiter=',', skiprows=5, usecols=(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,30))
    trimmed_data = rawdata[Phys_Des_start[participant]:Phys_Des_end[participant]]
    pcp =  int(participant) + 1
    np.savetxt("Trimmed_Data/P%s_Phys_Des.csv" %pcp, trimmed_data, header="Sample Index, EEG1, EEG2, EEG3, EEG4, EEG5, EEG6, EEG7, EEG8, EEG9, EEG10, EEG11, EEG12, EEG13, EEG14, EEG15, EEG16, accl1, accl2, accl3, Unix TimeStamp", comments="", delimiter=',')

