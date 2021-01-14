# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 12:07:24 2021

@author: murie
"""

import matplotlib.pyplot as plt
import numpy as np
#import scikitplot as skplt

f = open('C:/Users/murie/Documents/school/master/1B/Introduction2Biometrics/project_git/data/before_rec_csv', 'r')

TP = []
FP = []
FN = []
TN = []
FPR = []
TPR = []

#TP =0
#FP = 0
#FN = 0
#TN = 0
#FPR = 0
#TPR = 0

th=0.5

for i in f:
    #print(i)
    data = i.split(';')
    #print(data[0])
    #other.append(float(data[0]))
    #print(float(data[0]))
    #print(float(data[1]))
    if float(data[0]) > th:
        FN.append(float(data[0]))
    if float(data[1]) > th:
        TN.append(float(data[1]))
        #print(len(TN))
    if float(data[0]) < th:
        TP.append(float(data[0]))
        #print(TP)
    if float(data[1]) < th:
        FP.append(float(data[1]))
    #dist2otherE.append(float(data[2]))
    f.close
    
    
    
print("TP: ", len(TP))
print("FP: ", len(FP))  
print("TN: ", len(TN))  
print("FN: ", len(FN))    
#skplt.metrics.plot_roc_curve(y_true, y_probas)

for i in range(len(FP+TN)):
    FPR.append(sum(FP[0:i]) / len(FP+TN))
    #FPR.append(sum(FP[0:i]) / len(FP+TN))
    #print(FPR)
for j in range(len(TP+FN)):
    TPR.append(sum(FP[0:i]) / len(TP+FN))   
    
print(np.shape(TPR))
print(np.shape(FPR))
print(len(TPR))
print(len(FPR))
            
#TPR = np.array(TPR)
#TPR = np.expand_dims(a, axis=-1) # Add an extra dimension in the last axis.
#FPR = np.array(FPR)
    
#fpr, tpr, threshold = metrics.roc_curve(y_test, preds)

#FPR = float(len(FP) / len(FP+TN)) # 0,5
#TPR = float(len(TP) / len(TP+FN)) # 1
#print(TPR)

#x = FPR # false_positive_rate
#y = TPR # true_positive_rate 

# This is the ROC curve
plt.plot(FPR, TPR)
plt.show() 


