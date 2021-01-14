# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 12:07:24 2021

@author: murie
"""

import matplotlib.pyplot as plt
import numpy as np
#import scikitplot as skplt

#f = open('C:/Users/murie/Documents/school/master/1B/Introduction2Biometrics/project_git/data/before_rec_csv', 'r')

#TP = []
#FP = []
#FN = []
#TN = []
FPR = []
TPR = []
FNMR = []

TP =0
FP = 0
FN = 0
TN = 0
#FPR = 0
#TPR = 0

#th=0.5
th_range = np.arange(0, 1, 0.01)

for th in th_range:
    #print("th: ", th)
    if (FP+TN) != 0:
        FPR.append(FP / (FP+TN))
        TPR.append(TP / (TP+FN))
        FNMR.append(1-TP / (TP+FN))
        #print("FPR: ", FP / (FP+TN))
        #print("TPR: ", TP / (TP+FN))
        print("TP: ", TP)
        #print("FP: ", FP)  
        #print("TN: ", TN)  
        #print("FN: ", FN)
    
    TP = 0
    FP = 0
    FN = 0
    TN = 0
    f = open('C:/Users/murie/Documents/school/master/1B/Introduction2Biometrics/project_git/data/before_rec_ADJUSTED_csv', 'r')

    for i in f:
        data = i.split(';')
        #print("data: ", data[0])
        if float(data[0]) > th:
            FN = FN+1
        if float(data[1]) > th:
            TN = TN+1
        if float(data[0]) < th:
            TP = TP+1
        if float(data[1]) < th:
            FP = FP+1
        f.close
        

#print("TP: ", TP)
#print("FP: ", FP)  
#print("TN: ", TN)  
#print("FN: ", FN)


# Plot FPR
plt.plot(th_range[0:len(FPR)], FPR)
plt.xlabel('Threshold')
plt.ylabel('False Positive Rate')
plt.title('FPR')
plt.show()

# Plot TPR
plt.plot(th_range[0:len(TPR)], TPR)
plt.xlabel('Threshold')
plt.ylabel('True Positive Rate')
plt.title('TPR')
plt.show()

# Plot ROC
plt.plot(FPR, TPR, color='orange', label='ROC')
plt.plot([0, 1], [0, 1], color='darkblue', linestyle='--')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver Operating Characteristic (ROC) Curve')
plt.legend()
plt.show() 

# Plot DET
plt.plot(FPR, FNMR, color='orange', label='DET')
plt.plot([0, 1], [0, 1], color='darkblue', linestyle='--')
plt.xlabel('False Positive Rate')
plt.ylabel('False non-Match Rate')
plt.title('Decision Error Trade-off (DET) curve')
plt.legend()
plt.show() 



