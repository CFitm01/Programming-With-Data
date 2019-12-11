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
    Vital_Record = {}
    Abnormal_Record = {}
    Abnormal_Patients = []
    for i in range(1, len(array)-1):
        if Vital == 'Pulse':
            if array[i][3] < 60 or array[i][3] > 99:
                Count += 1
                if array[i][3] in Abnormal_Record:
                    Abnormal_Record[array[i][3]] += 1
                    Abnormal_Patients.append(i)
                else:
                    Abnormal_Record[array[i][3]] = 1
                    Abnormal_Patients.append(i)
            else:
                if array[i][3] in Vital_Record:
                    Vital_Record[array[i][3]] += 1
                else:
                    Vital_Record[array[i][3]] = 1
        if Vital == 'Blood Pressure':
            if array[i][4] == 121:
                if array[i][4] not in Abnormal_Record:
                    Abnormal_Record[array[i][4]] = 1
                    Abnormal_Patients.append(i)
                    Count += 1
                else:
                    Abnormal_Record[array[i][4]] = 1
                    Abnormal_Patients.append(i)
                    Count += 1
            else:
                if array[i][4] not in Vital_Record:
                    Vital_Record[array[i][4]] = 1
                else:
                    Vital_Record[array[i][4]] += 1              
                
    print("There were {} abnormal {} values:".format(Count, Vital))
    print("The following patients have abnormal {} values:".format(Vital) +\
          str(Abnormal_Patients))
    Analyse = input('Do you wish to see these results in graphical form?: Y/N')
    if Analyse.upper() == 'Y':
        return frequencyAnalytics(Vital_Record, Abnormal_Record)
    else:
        return Vital_Record
        
    

def frequencyAnalytics(normalArray, abnormalArray):
    x = normalArray.keys()
    y = normalArray.values()
    plt.hist(xy, bins = [i for i in range(50, 100, 10)])

    
