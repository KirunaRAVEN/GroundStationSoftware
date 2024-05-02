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
nData = 22
row = [0] * nData

elapsed_time = 0 
time_increment = 0.01
old_msg = ' '
while True:
    with open('dummyData.csv', 'a', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',', quoting=csv.QUOTE_MINIMAL)
        for i in range(0, nData):
           row[i] = 50 * np.sin(elapsed_time) + 50 
        new_msg = ''
        for i in range(20):
            new_msg += 'a' # f'elapsed time: {elapsed_time:.1f}'
        #if new_msg != old_msg:
        row[-1] = new_msg
        #else:
        #    row[-1] = ' '
        old_msg = new_msg
        csv_writer.writerow(row)
        time.sleep(time_increment)
        elapsed_time = elapsed_time + time_increment