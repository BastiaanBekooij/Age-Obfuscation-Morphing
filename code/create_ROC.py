# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 12:07:24 2021

@author: murie
"""

import matplotlib.pyplot as plt
import numpy as np
#import scikitplot as skplt

f = open('C:/Users/murie/Documents/school/master/1B/Introduction2Biometrics/project_git/data/before_rec_csv', 'r')

#TP = []
#FP = []
#FN = []
#TN = []
FPR = []
TPR = []

TP =0
FP = 0
FN = 0
TN = 0
#FPR = 0
#TPR = 0

#th=0.5
th_range = []

for th in np.arange(0, 1, 0.0001):
    #print("th: ", th)
    if (FP+TN) != 0:
        FPR.append(FP / (FP+TN))
        TPR.append(TP / (TP+FN))
        #print("FPR: ", FPR)
        #print("TPR: ", TPR)
        print("TP: ", TP)
        print("FP: ", FP)  
        print("TN: ", TN)  
        print("FN: ", FN)
        
    TP = 0
    FP = 0
    FN = 0
    TN = 0
    f = open('C:/Users/murie/Documents/school/master/1B/Introduction2Biometrics/project_git/data/before_rec_csv', 'r')

    for i in f:
        #print("th: ", th)
        data = i.split(';')
        if float(data[0]) > th:
            #FN.append(float(data[0]))
            FN = FN+1
        if float(data[1]) > th:
            #TN.append(float(data[1]))
            #print(len(TN))
            TN = TN+1
        if float(data[0]) < th:
            #TP.append(float(data[0]))
            TP = TP+1
        if float(data[1]) < th:
            #FP.append(float(data[1]))
            FP = FP+1
        f.close
        
    
#print("TP: ", len(TP))
#print("FP: ", len(FP))  
#print("TN: ", len(TN))  
#print("FN: ", len(FN))    

print("TP: ", TP)
print("FP: ", FP)  
print("TN: ", TN)  
print("FN: ", FN)

#for i in range(len(FP)+len(TN)):
#    FPR.append(sum(FP[0:i]) / len(FP+TN)) # does not change
    #FPR.append(sum(FP[0:i]) / len(FP+TN))
    #print(FPR)
#for j in range(len(TP)+len(FN)):
#    TPR.append(sum(TP[0:j]) / len(TP+FN)) 


# This is the ROC curve
plt.plot(FPR, TPR)
plt.show() 


