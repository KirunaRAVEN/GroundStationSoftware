import time
import csv
import random
import numpy as np

# create or overwrite the csv file
open('dummyData.csv', 'w')

# list for the row elements
row = []
for i in range(21):
    row.append(i)
t = 0
while True:
    with open('dummyData.csv', 'a', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',', quoting=csv.QUOTE_MINIMAL)
        for i in range(0,21):
           row[i] = 50 * np.sin(t) + 50 # i * random.randrange(-5,10) 
        row[4] = 10 * np.sin(10*t) + 25
        csv_writer.writerow(row)
        time.sleep(0.01)
        t = t + 0.01