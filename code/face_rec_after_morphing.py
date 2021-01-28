# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 12:41:36 2021

@author: murie
"""
import numpy as np
import functions
from functions import read_npz_after_morph
import matplotlib.pyplot as plt

_, _, _, face_dist_after10, _ = read_npz_after_morph("../Final data/average10_20_handpicked.npz")
_, _, _, face_dist_after20, _ = read_npz_after_morph("../Final data/average20_30_handpicked.npz")
_, _, _, face_dist_after30, _ = read_npz_after_morph("../Final data/average30_40_handpicked.npz")
_, _, _, face_dist_after40, _ = read_npz_after_morph("../Final data/average40_50_handpicked.npz")
_, _, _, face_dist_after50, _ = read_npz_after_morph("../Final data/average50_60_handpicked.npz")
_, _, _, face_dist_after60, _ = read_npz_after_morph("../Final data/average60_70_handpicked.npz")

data = []
face_dist_before_morph = []
FPR_before = []
FPR_10 = []
FPR_20 = []
FPR_30 = []
FPR_40 = []
FPR_50 = []
FPR_60 = []
TPR = []
FNMR = []
th_range = np.arange(0, 1, 0.01)

TP = 0
FN = 0
FP = 0
TN = 0
FP_10 = 0
TN_10 = 0
FP_20 = 0
TN_20 = 0
FP_30 = 0
TN_30 = 0
FP_40 = 0
TN_40 = 0
FP_50 = 0
TN_50 = 0
FP_60 = 0
TN_60 = 0

for th in th_range:
    f = open('../data/before_rec_csv', 'r')
    
    if (FP_20+TN_20) != 0:
        FPR_before.append(FP / (FP+TN))
        FPR_10.append(FP_10 / (FP_10+TN_10))
        FPR_20.append(FP_20 / (FP_20+TN_20))
        FPR_30.append(FP_30 / (FP_30+TN_30))
        FPR_40.append(FP_40 / (FP_40+TN_40))
        FPR_50.append(FP_50 / (FP_50+TN_50))
        FPR_60.append(FP_60 / (FP_60+TN_60))
        TPR.append(TP / (TP+FN))
        FNMR.append(1-TP / (TP+FN))
        #print("FPR: ", FP / (FP+TN))
        #print("TPR: ", TP / (TP+FN))
    TP = 0
    FN = 0
    FP = 0
    TN = 0
    FP_10 = 0
    TN_10 = 0
    FP_20 = 0
    TN_20 = 0
    FP_30 = 0
    TN_30 = 0
    FP_40 = 0
    TN_40 = 0
    FP_50 = 0
    TN_50 = 0
    FP_60 = 0
    TN_60 = 0
    
    for i in f:
        data = i.split(';')
        #face_dist_before_morph.append(float(data[0]))
        #face_dist_before_morph.append(float(data[1]))
        if float(data[0]) > th:
            FN = FN+1
        if float(data[1]) > th:
            TN = TN+1
        if float(data[0]) < th:
            TP = TP+1
        if float(data[1]) < th:
            FP = FP+1
        f.close
    for h in face_dist_after10:
        #print(i)
        if h > th:
            TN_10 = TN_10+1
        if h <= th:
            FP_10 = FP_10+1
    for i in face_dist_after20:
        #print(i)
        if i > th:
            TN_20 = TN_20+1
        if i <= th:
            FP_20 = FP_20+1
    for j in face_dist_after30: 
        #print(i)
        if j > th:
            TN_30 = TN_30+1
        if j <= th:
            FP_30 = FP_30+1
    for k in face_dist_after40:
        #print(i)
        if k > th:
            TN_40 = TN_40+1
        if k <= th:
            FP_40 = FP_40+1
    for l in face_dist_after50: 
        #print(i)
        if l > th:
            TN_50 = TN_50+1
        if l <= th:
            FP_50 = FP_50+1
    for m in face_dist_after60:
        #print(i)
        if m > th:
            TN_60 = TN_60+1
        if m <= th:
            FP_60 = FP_60+1
print(len(face_dist_after20))

# Plot ROC normal    
bins = np.arange(0, 1, 0.02) #left margin, right margin, step size (years)
#plt.figure(figsize=(5,2.5), dpi=160)
plt.figure(figsize=(5,2.5), dpi=160)
plt.gcf().subplots_adjust(bottom=0.20)
plt.plot(FPR_before, TPR, color='blue', label='Before morphing')
plt.plot(FPR_10, TPR, color='pink', label='Group 10-20')
plt.plot(FPR_20, TPR, color='orange', label='Group 20-30')
plt.plot(FPR_30, TPR, color='red', label='Group 30-40')
plt.plot(FPR_40, TPR, color='green', label='Group 40-50')
plt.plot(FPR_50, TPR, color='purple', label='Group 50-60')
plt.plot(FPR_60, TPR, color='black', label='Group 60-70')
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
plt.plot(FPR_10[ranges_l:ranges_h], TPR[ranges_l:ranges_h], color='pink', label='Group 10-30')
plt.plot(FPR_20[ranges_l:ranges_h], TPR[ranges_l:ranges_h], color='orange', label='Group 20-30')
plt.plot(FPR_30[ranges_l:ranges_h], TPR[ranges_l:ranges_h], color='red', label='Group 30-40')
plt.plot(FPR_40[ranges_l:ranges_h], TPR[ranges_l:ranges_h], color='green', label='Group 40-50')
plt.plot(FPR_50[ranges_l:ranges_h], TPR[ranges_l:ranges_h], color='purple', label='Group 50-60')
plt.plot(FPR_60[ranges_l:ranges_h], TPR[ranges_l:ranges_h], color='black', label='Group 60-70')

#plt.plot([0, 1], [0, 1], color='darkblue', linestyle='--')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver Operating Characteristic (ROC) Curve')
plt.legend()
plt.show() 

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

"""
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
"""