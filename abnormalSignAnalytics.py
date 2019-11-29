# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 14:35:32 2019

@author: CFitz
"""
import matplotlib.pyplot as plt

def abnormalSignAnalytics(array):
    abnormality_count = 0
    abnormality_records = []
    count = 0
    Pulse_Range = list(range(60, 99))
    vital = input("Which vital sign do you wish to search? ").title()
    for i in array[0]:
        if vital != i:
            count += 1
        else:
            break
    for j in range(1, len(array)):
        if array[j][count] > max(Pulse_Range) or\
        array[j][count] < min(Pulse_Range):
            abnormality_count += 1
            abnormality_records.append([array[j][count]])
    result = [vital, abnormality_count, abnormality_records]
    return frequencyAnalytics(result)

def frequencyAnalytics(result):
    x = result[-1]
    plt.hist(x = x, bins = 'auto', color = 'red')
    plt.grid(axis = 'y')
    plt.xlabel(str(result[0]))
    plt.ylabel('Abnormality Count')
    plt.title(str(result[0]) + " Abnormalities")
    
    