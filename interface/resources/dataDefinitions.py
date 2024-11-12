# TODO: add plot index, so multiple data can be displayed in the same plot. E.g. 2 blanket temps

oxidizerPressure1 = {
    'title': 'Ox. Bottle 1 Pressure',
    'xLabel': 'Time',
    'yLabel': 'Pressure', 
    'xUnit': 's', 
    'yUnit': 'Bar', 
    'yLowerBound': 0,
    'yUpperBound': 80,
    'warningValue': 40,
    'dangerValue' : 60,
    'csvIndex' : 4
}

oxidizerPressure2 = {
    'title': 'Ox. Bottle 2 Pressure',
    'xLabel': 'Time',
    'yLabel': 'Pressure', 
    'xUnit': 's', 
    'yUnit': 'Bar', 
    'yLowerBound': 0,
    'yUpperBound': 80,
    'warningValue': 40,
    'dangerValue' : 60,
    'csvIndex' : 1
}

oxidizerBottleTemperature1 = {
    'title': 'Ox. Bottle 1 Temperature',
    'xLabel': 'Time',
    'yLabel': 'Temperature', 
    'xUnit': 's', 
    'yUnit': '°C', 
    'yLowerBound': -15,
    'yUpperBound': 40,
    'warningValue': 25,
    'dangerValue' : 35,
    'csvIndex' : 6
}

oxidizerBottleTemperature2 = {
    'title': 'Ox. Bottle 2 Temperature',
    'xLabel': 'Time',
    'yLabel': 'Temperature', 
    'xUnit': 's', 
    'yUnit': '°C', 
    'yLowerBound': -15,
    'yUpperBound': 40,
    'warningValue': 25,
    'dangerValue' : 35,
    'csvIndex' : 25
}

nitrogenPressure = {
    'title': 'Nitrogen Pressure',
    'xLabel': 'Time',
    'yLabel': 'Pressure', 
    'xUnit': 's', 
    'yUnit': 'Bar', 
    'yLowerBound': 0,
    'yUpperBound': 80,
    'warningValue': 40,
    'dangerValue' : 60,
    'csvIndex' : 21
}

linePressure = {
    'title': 'Line Pressure',
    'xLabel': 'Time',
    'yLabel': 'Pressure', 
    'xUnit': 's', 
    'yUnit': 'Bar', 
    'yLowerBound': 0,
    'yUpperBound': 80,
    'warningValue': 40,
    'dangerValue' : 60,
    'csvIndex' : 2
}

loadCell = {
    'title': 'Load',
    'xLabel': 'Time',
    'yLabel': 'Force', 
    'xUnit': 's', 
    'yUnit': 'N',
    'yLowerBound': 0,
    'yUpperBound': 1000,
    'warningValue': 2000,
    'dangerValue' : 2000,
    'csvIndex' : 5
}