# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 13:54:20 2021

@author: murie
"""

import numpy as np
import functions
from functions import read_npz_after_morph
import matplotlib.pyplot as plt

_, _, _, face_dist_after20, _ = read_npz_after_morph("../Data_npz/average20_30_N3(1).npz")
_, _, _, face_dist_after30, _ = read_npz_after_morph("../Data_npz/average30_40_N3(0).npz")
_, _, _, face_dist_after40, _ = read_npz_after_morph("../Data_npz/average40_50_N3(0).npz")
_, _, _, face_dist_after50, _ = read_npz_after_morph("../Data_npz/average50_60_N3(0).npz")




data = []
face_dist_before_morph = []
FPR_before = []
FPR = []
FPR_20 = []
FPR_30 = []
FPR_40 = []
FPR_50 = []
TPR_20 = []
TPR_30 = []
TPR_40 = []
TPR_50 = []
TPR = []
FNMR_20 = []
th_range = np.arange(0, 1, 0.01)

f = open('../data/before_rec_csv', 'r')
for a in f:
    data = a.split(';')
    face_dist_before_morph.append(float(data[1]))
    f.close()


TP = 0
FN = 0
FP = 0
TN = 0
TP_20 = 0
FN_20 = 0
TP_30 = 0
FN_30 = 0
TP_40 = 0
FN_40 = 0
TP_50 = 0
FN_50 = 0
FP_20 = 0
TN_20 = 0
FP_30 = 0
TN_30 = 0
FP_40 = 0
TN_40 = 0
FP_50 = 0
TN_50 = 0

for th in th_range:
    f = open('../data/before_rec_csv', 'r')
    
    if (TP_20+FN_20) != 0:
        #FPR_before.append(FP / (FP+TN))
        FPR.append(FP / (FP+TN))
        TPR_20.append(TP_20 / (TP_20+FN_20))
        TPR_30.append(TP_30 / (TP_30+FN_30))
        TPR_40.append(TP_40 / (TP_40+FN_40))
        TPR_50.append(TP_50 / (TP_50+FN_50))
        #FNMR_20.append(1-TPR_20)
        #print("FPR: ", FP / (FP+TN))
        #print("TPR: ", TP / (TP+FN))
    
    TP = 0
    FN = 0
    FP = 0
    TN = 0
    TP_20 = 0
    FN_20 = 0
    TP_30 = 0
    FN_30 = 0
    TP_40 = 0
    FN_40 = 0
    TP_50 = 0
    FN_50 = 0
    
    for i in f:
        data = i.split(';')
        if float(data[1]) > th:
            TN = TN+1
        if float(data[1]) < th:
            FP = FP+1
        f.close
    for i in face_dist_after20:
        if i > th:
            FN_20 = FN_20+1
        if i <= th:
            TP_20 = TP_20+1
    for j in face_dist_after30: 
        #print(i)
        if j > th:
            FN_30 = FN_30+1
        if j <= th:
            TP_30 = TP_30+1
    for k in face_dist_after40:
        #print(i)
        if k > th:
            FN_40 = FN_40+1
        if k <= th:
            TP_40 = TP_40+1
    for l in face_dist_after50: 
        #print(i)
        if l > th:
            FN_50 = FN_50+1
        if l <= th:
            TP_50 = TP_50+1
print(len(face_dist_after20))

# Plot ROC normal    
bins = np.arange(0, 1, 0.02) #left margin, right margin, step size (years)
plt.figure(figsize=(5,2.5), dpi=160)
#plt.plot(FPR_before, TPR, color='blue', label='Before morphing')
plt.plot(FPR, TPR_20, color='orange', label='Group 20-30')
plt.plot(FPR, TPR_30, color='red', label='Group 30-40')
plt.plot(FPR, TPR_40, color='green', label='Group 40-50')
plt.plot(FPR, TPR_50, color='purple', label='Group 50-60')
plt.plot([0, 1], [0, 1], color='darkblue', linestyle='--')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver Operating Characteristic (ROC) Curve')
plt.legend()
plt.show() 

# Plot ROC zoomed in
ranges_h = 41
ranges_l = 27
#bins = np.arange(0, 1, 0.02) #left margin, right margin, step size (years)
plt.figure(figsize=(5,2.5), dpi=160)
#plt.plot(FPR_before[ranges_l:ranges_h], TPR[ranges_l:ranges_h], color='blue', label='Before morphing')
plt.plot(FPR_20[ranges_l:ranges_h], TPR[ranges_l:ranges_h], color='orange', label='Group 20-30')
plt.plot(FPR_30[ranges_l:ranges_h], TPR[ranges_l:ranges_h], color='red', label='Group 30-40')
plt.plot(FPR_40[ranges_l:ranges_h], TPR[ranges_l:ranges_h], color='green', label='Group 40-50')
plt.plot(FPR_50[ranges_l:ranges_h], TPR[ranges_l:ranges_h], color='purple', label='Group 50-60')
#plt.plot([0, 1], [0, 1], color='darkblue', linestyle='--')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver Operating Characteristic (ROC) Curve')
plt.legend()
plt.show() 
"""
# Plot DET normal
plt.figure(figsize=(5,2.5), dpi=160)
plt.plot(FPR_before, FNMR, color='blue', label='Before morphing')
plt.plot(FPR_20, FNMR, color='orange', label='Group 20-30')
plt.plot(FPR_30, FNMR, color='red', label='Group 30-40')
plt.plot(FPR_40, FNMR, color='green', label='Group 40-50')
plt.plot(FPR_50, FNMR, color='purple', label='Group 50-60')
plt.plot([0, 1], [0, 1], color='darkblue', linestyle='--')
plt.xlabel('False Positive Rate')
plt.ylabel('False non-Match Rate')
plt.title('Decision Error Trade-off (DET) curve')
plt.legend()
plt.show() 

# Plot DET zoomed in
plt.figure(figsize=(5,2.5), dpi=160)
plt.plot(FPR_20[ranges_l:ranges_h], FNMR[ranges_l:ranges_h], color='orange', label='Group 20-30')
plt.plot(FPR_30[ranges_l:ranges_h], FNMR[ranges_l:ranges_h], color='red', label='Group 30-40')
plt.plot(FPR_40[ranges_l:ranges_h], FNMR[ranges_l:ranges_h], color='green', label='Group 40-50')
plt.plot(FPR_50[ranges_l:ranges_h], FNMR[ranges_l:ranges_h], color='purple', label='Group 50-60')
plt.xlabel('False Positive Rate')
plt.ylabel('False non-Match Rate')
plt.title('Decision Error Trade-off (DET) curve')
plt.legend()
plt.show() 

"""


bins = np.arange(0, 1, 0.02) #left margin, right margin, step size (years)
plt.figure(figsize=(5,2.5), dpi=160)
plt.gcf()#.subplots_adjust(bottom=0.20)
plt.hist(face_dist_before_morph, bins, alpha=0.5, label='Distance to same subject')
plt.hist(face_dist_after20, bins, alpha=0.5, label='Distance to other subject')
plt.hist(face_dist_after30, bins, alpha=0.5, label='Distance to other subject')
plt.hist(face_dist_after40, bins, alpha=0.5, label='Distance to same subject')
plt.hist(face_dist_after50, bins, alpha=0.5, label='Distance to other subject')
plt.xlabel('Face distance')
plt.ylabel('Amount')
plt.legend()
#plt.savefig('age_distribution_estimated_special.png')
plt.show() 