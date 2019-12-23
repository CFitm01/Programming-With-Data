import random as rand
import numpy as np
import scipy as sc
import matplotlib.pyplot as plt
import abnormalSignAnalytics as ab
import healthAnalyzer as ha
import binaryhealthanalyzer as ba
rand.seed(404)
import time as time

#Phase 1
Records = [["id", "Temperature", "Heart Rate", "Pulse", "Blood Pressure", \
               "Respiratory Rate", "Oxygen Saturation", "pH"]]


import random as rand
rand.seed(404)


def myHealthcare(n):
    for i in range(0,n+1):
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
n = 10000
print(myHealthcare(n))
end = float(time.time())

def benchmarking(MyHealthCareDevice):
    y = []
    start = time.time()
    myHealthcare(1000)
    n1 = time.time() - start
    y.append(round(n1,3))
    start = time.time()
    myHealthcare(2500)
    n2 = time.time() - start
    y.append(round(n2,3))
    start = time.time()
    myHealthcare(5000)
    n3 = time.time() - start
    y.append(round(n3,3))
    start = time.time()
    myHealthcare(7500)
    n4 = time.time() - start
    y.append(round(n4,3))
    start = time.time()
    myHealthcare(10000)
    n5 = time.time() - start
    y.append(round(n5,3))
    x = [1000, 2500, 5000, 7500, 10000]
    print(list(zip(x,y)))
#    print(x)
#    print(y)
    plt.bar(x, y, align = 'center', width = 500.00, color = 'blue')
    plt.xlabel("Value of n")
    plt.ylabel("Completion Time (s)")
    return plt.show()

def HealthAnalyzer(array):
    Vital = input("Which vital do you wish to search for?: ")
    Value = input("What value do you wish to search for?: ")
    Index = 0
    Match_Patient = []
    if Vital == 'pH':
        Value = float(Value)
    else:
        Value = int(Value)
    for i in range(len(array[0])):
        if Vital != array[0][i]:
            Index += 1
            if Vital == array[0][Index]:
                break
        else:
            return print("I am sorry, but that vital is not recorded here.")
    for j in range(1, len(array)-1):
        if array[j][Index] == Value:
            Match_Patient.append(array[j])
    print("The following patients have the {} of {}:".format(Vital, Value))
    Match_Patient.insert(0,array[0])
    print(Match_Patient)

def abnormalSignAnalytics(array):
    Vital = input('Which Vital do you wish to search for?: ')
    Count = 0
    Vital_Record = []
    Abnormal_Record = []
    Patient_Abnormal = []
    for i in range(1, len(array)-1):
        if Vital == 'Pulse':
            if array[i][3] < 60 or array[i][3] > 99:
                Abnormal_Record.append(array[i][3])
                Patient_Abnormal.append(i)
                Count += 1
            else:
                Vital_Record.append(array[i][3])
        if Vital == 'Blood Pressure':
            if array[i][4] == 121:
                Abnormal_Record.append(array[i][4])
                Patient_Abnormal.append(i)
                Count += 1
            else:
                Vital_Record.append(array[i][4])
    print("There were {} abnormal {} values: ".format(Count, Vital))
    print("The following patients have abnormal {} values:".format(Vital) +\
          str([(Patient_Abnormal[i],Abnormal_Record[i]) for i in range(len(\
           Patient_Abnormal))]))
    Analyse = input('Do you wish to see these results in graphical form?: Y/N')
    if Analyse.upper() == 'Y':
        return frequencyAnalytics(Vital_Record, Abnormal_Record)
    else:
        return Vital_Record

def frequencyAnalytics(Normal, Abnormal):
    legend = ["Normal", "Abnormal"]
    plt.hist([Normal, Abnormal], bins = [i for i in range(50, 110,5)])
    plt.title("Abnormal and Normal Pulse Values")
    plt.xlabel("Pulse Rate (BPM)")
    plt.ylabel("Number of Occurences")
    plt.legend(legend)
    plt.show()

benchmarking(_)


#for i in range(len(Records[0])):
#    print(Records[0][i])
#abnormalSignAnalytics(Records)
#ba.HealthAnalyzer(Records)
#ab.frequencyAnalytics(Records)

#print(Abnorm.frequencyAnalytics(result))

#The if statements correctly and accurately identify abnormalities,
#but presently only convert them to strings thus far.
