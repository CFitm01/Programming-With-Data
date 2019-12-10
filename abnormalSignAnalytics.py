def abnormalSignAnalytics(array):
    Vital = input('Which Vital do you wish to search for?: ')
    Count = 0
    Vital_Record = []
    Abnormal_Record = []
    graphNormal = []
    graphAbnormal = []
    for i in range(1, len(array)-1):
        if Vital == 'Pulse':
            if array[i][3] < 60 or array[i][3] > 99:
                Abnormal_Record.append([array[i][0], array[i][3]])
                graphAbnormal.append(array[i][3])
                Count += 1
            else:
                Vital_Record.append([array[i][0], array[i][3]])
                graphNormal.append(array[i][3])
        if Vital == 'Blood Pressure':
            if array[i][4] == 121:
                Vital_Record.append([array[i][0], array[i][4]])
                graphAbnormal.append(array[i][4])
                Count += 1
            else:
                Vital_Record.append([array[i][0], array[i][4]])
                graphNormal.append(array[i][4])
    print("There were {} abnormal {} values: ".format(Count, Vital) + \
          str(Abnormal_Record))
    Analyse = input('Do you wish to see these results in graphical form?: Y/N')
    if Analyse.upper() == 'Y':
        return frequencyAnalytics(graphNormal, graphAbnormal)
    else:
        return Vital_Record
        
    

def frequencyAnalytics(normalArray, abnormalArray):
    plt.hist(abnormalArray, bins = [range(50, 100, 10)], rwidth = 0.95,\
             color = 'orange')
