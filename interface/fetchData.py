import csv

def fetchData():
    csvData = []
    with open('data.csv', 'r') as csvFile:
        csvReader = csv.reader(csvFile)
        for line in csvFile:
            break
    return csvData