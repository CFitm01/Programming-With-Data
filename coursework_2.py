# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 16:11:56 2019

@author: CFitz
"""
import random as rand
import matplotlib.pyplot as plt
import abnormalSignAnalytics as Abnorm
rand.seed(404)
import time as time

#Phase 1
Records = [["id", "Temperature", "Heart Rate", "Pulse", "Blood Pressure"\
               "Respiratory Rate", "Oxygen Saturation", "pH"]]


import random as rand
rand.seed(404)
start = float(time.time())
def myHealthcare(n):
    for i in range(1,n):
        temp = rand.randint(36, 39)
#        if temp > 38 or temp < 37:
#            temp = str(temp) + "-Abnormal"
        hr = rand.randint(55, 100)
#        if hr > 99 or hr < 60:
#            hr = str(hr) + "-Abnormal"
        pulse = rand.randint(55, 100)
#        if pulse > 99 or pulse < 60:
#            pulse = str(pulse) + "-Abnormal"
        bp = rand.randint(120, 121)
#        if bp == 121:
#            bp = str(bp) + "-Abnormal"
        rr = rand.randint(11, 17)
#        if rr < 12 or rr > 16:
#            rr = str(rr) + "-Abnormal"
        o2 = rand.randint(93, 100)
#        if o2 < 95 or o2 > 100:
#            o2 = str(o2) + "-Abnormal"
        ph = round(rand.uniform(7.1, 7.6), 1)
        ts = i
#        if ph < 7.3 or ph > 7.6:
#            ph = str(ph) + "-Abnormal"
        Records.append([ts, temp, hr, pulse, bp, rr, o2, ph])
    return Records
n = 50
print(myHealthcare(n))
end = float(time.time())
print(start-end)

print(Abnorm.abnormalSignAnalytics(Records))
print(Abnorm.frequencyAnalytics(result))

#The if statements correctly and accurately identify abnormalities,
#but presently only convert them to strings thus far.

