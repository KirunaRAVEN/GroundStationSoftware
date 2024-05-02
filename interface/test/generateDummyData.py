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
nData = 23
row = [0] * nData

elapsed_time = 0 
time_increment = 0.01
while True:
    with open('dummyData.csv', 'a', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',', quoting=csv.QUOTE_MINIMAL)
        
        # all columns
        for i in range(0, nData):
           row[i] = 50 * np.sin(elapsed_time) + 50 
        
        # adjust indicator columns
        if row[15] > 50:
            row[14] = 1.0
            row[15] = 1.0
            row[17] = 1.0
        else: 
            row[14] = 0.0
            row[15] = 0.0
            row[17] = 0.0

        # adjust time value
        row[2] *= 1000

        # adjust software columns
        if row[21] < 17:
            row[20] = 0.0
            row[21] = 0.0
        elif row[21] < 34:
            row[20] = 1.0
            row[21] = 1.0
        elif row[21] < 51:
            row[20] = 2.0
            row[21] = 2.0
        elif row[21] < 68:
            row[20] = 3.0
            row[21] = 3.0
        elif row[21] < 75:
            row[20] = 4.0
            row[21] = 4.0
        else:
            row[20] = 5.0
            row[21] = 5.0

        # message field
        new_msg = ''
        for i in range(20):
            new_msg += 'a' # f'elapsed time: {elapsed_time:.1f}'
        #if new_msg != old_msg:
        row[-1] = new_msg
        csv_writer.writerow(row)
        time.sleep(time_increment)
        elapsed_time = elapsed_time + time_increment