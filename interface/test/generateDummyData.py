'''
    AUTHOR:  Louis-Hendrik Barboutie
    CONTACT: louis.barboutie@gmail.com, loubar-3@student.ltu.se

    SUMMARY: Generates a csv file for testing purposes. The simulated data is plain sine waves.
'''

import time
import csv
import random
import numpy as np

# create or overwrite the csv file
open('dummyData.csv', 'w')

# list for the row elements
nData = 21
nExtraData = 10 # time, A0-A5, D1-D3
row = [0] * (nData + nExtraData)

elapsed_time = 0
time_increment = 0.01
while True:
    with open('dummyData.csv', 'a', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',', quoting=csv.QUOTE_MINIMAL)
        
        # all columns
        for i in range(0, nData + nExtraData):
           row[i] = 50 * np.sin(elapsed_time) + 50 
        
        # adjust indicator columns
        if row[2] > 50:
            row[12] = 1.0
            row[13] = 1.0
            row[14] = 1.0
            row[15] = 1.0
            row[16] = 1.0
            row[17] = 1.0
            row[28] = 1.0
            row[29] = 1.0
        else: 
            row[12] = 0.0
            row[13] = 0.0
            row[14] = 0.0
            row[15] = 0.0
            row[16] = 0.0
            row[17] = 0.0
            row[28] = 0.0
            row[29] = 0.0

        # adjust time value
        row[0] = elapsed_time * 1e6 # microsec

        # adjust software state and substate columns, epilepsy warning
        row[18] = random.randrange(6) # SW mode
        row[19] = random.randrange(6) # SW substate

        # message field
        new_msg = random.randrange(34)
        row[-1] = new_msg
        csv_writer.writerow(row)
        time.sleep(time_increment)
        elapsed_time = elapsed_time + time_increment