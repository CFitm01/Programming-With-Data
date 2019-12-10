# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 14:35:32 2019

@author: CFitz
"""
import matplotlib.pyplot as plt
import numpy as num
#We want to find the abnormal values for pulse or blood pressure.
#The abnormal values for pulse is anything that  is below 60 or above 99.
#The abnormal values for blood pressure is 121.
#The pulse values are stored at [i][3] & [i][4] respectively.
#Searching functions include for loops, 



def abnormalSignAnalytics(array):
    Vital = input('Which Vital do you wish to search for?: ')
    Count = 0
    Vital_Record = []
    for i in range(1, len(array)-1):
        if Vital == 'Pulse':
            if array[i][3] < 60 or array[i][3] > 99:
                Vital_Record.append([array[i][0], array[i][3]])
                Count += 1
        if Vital == 'Blood Pressure':
            if array[i][4] == 121:
                Vital_Record.append([array[i][0], array[i][4]])
                Count += 1
    print("There were {} abnormal {} values: ".format(Count, Vital) + \
          str(Vital_Record))
        
    

def frequencyAnalytics(array):
    Vital = input('Which Vital do you wish to search for?: ')
    Index = 0
    Vital_Record = {}
    for i in array[0]:
        if i != Vital:
            Index += 1
        else:
            break
    for j in range(1, len(array)-1):
        if array[j][Index] not in Vital_Record:
            Vital_Record[(array[j][Index])] = 1
        else:
            Vital_Record[(array[j][Index])] += 1
    print("These are the following {} values and their counts:\n".format(Vital)\
          + str(Vital_Record))
    graph = input("Would you like these values presented as a graph? Y/N")
    if graph.upper() == 'Y':
        return genHisto(Vital_Record, Vital)
    else:
        return
    
def genHisto(dictionary, Vitals):
    xy = [(x,y) for x in dictionary.keys() for y in dictionary.values()]
    
