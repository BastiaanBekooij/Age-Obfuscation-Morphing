# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 13:54:20 2021

@author: murie
"""

import numpy as np
import functions
from functions import read_npz_after_morph
import matplotlib.pyplot as plt
from scipy.optimize import brentq
from scipy.interpolate import interp1d
#from scipy.interpolate import inderp2d

#_, _, _, face_dist_after20, _ = read_npz_after_morph("../Data_npz/average20_30_N3(1).npz")
#_, _, _, face_dist_after30, _ = read_npz_after_morph("../Data_npz/average30_40_N3(0).npz")
#_, _, _, face_dist_after40, _ = read_npz_after_morph("../Data_npz/average40_50_N3(0).npz")
#_, _, _, face_dist_after50, _ = read_npz_after_morph("../Data_npz/average50_60_N3(0).npz")

_, _, _, face_dist_after10, _ = read_npz_after_morph("../Final data/average10_20_handpicked.npz")
_, _, _, face_dist_after20, _ = read_npz_after_morph("../Final data/average20_30_handpicked.npz")
_, _, _, face_dist_after30, _ = read_npz_after_morph("../Final data/average30_40_handpicked.npz")
_, _, _, face_dist_after40, _ = read_npz_after_morph("../Final data/average40_50_handpicked.npz")
_, _, _, face_dist_after50, _ = read_npz_after_morph("../Final data/average50_60_handpicked.npz")
_, _, _, face_dist_after60, _ = read_npz_after_morph("../Final data/average60_70_handpicked.npz")


print(np.mean(face_dist_after10))
print(np.mean(face_dist_after20))
print(np.mean(face_dist_after30))
print(np.mean(face_dist_after40))
print(np.mean(face_dist_after50))
print(np.mean(face_dist_after60))


once = True
data = []
face_dist_before_same = []
face_dist_before_other = []
FPR_before = []
FPR = []
FPR_10 = []
FPR_20 = []
FPR_30 = []
FPR_40 = []
FPR_50 = []
FPr_60 = []
TPR_10 = []
TPR_20 = []
TPR_30 = []
TPR_40 = []
TPR_50 = []
TPR_60 = []
TPR = []
FNMR = []
FNMR_10 = []
FNMR_20 = []
FNMR_30 = []
FNMR_40 = []
FNMR_50 = []
FNMR_60 = []
th_range = np.arange(0, 1, 0.01)

TP = 0
FN = 0
FP = 0
TN = 0
TP_10 = 0
FN_10 = 0
TP_20 = 0
FN_20 = 0
TP_30 = 0
FN_30 = 0
TP_40 = 0
FN_40 = 0
TP_50 = 0
FN_50 = 0
TP_60 = 0
FN_60 = 0

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
    if (TP_20+FN_20) != 0:
        #FPR_before.append(FP / (FP+TN))
        FPR.append(FP / (FP+TN))
        TPR.append(TP / (TP+FN))
        TPR_10.append(TP_10 / (TP_10+FN_10))
        TPR_20.append(TP_20 / (TP_20+FN_20))
        TPR_30.append(TP_30 / (TP_30+FN_30))
        TPR_40.append(TP_40 / (TP_40+FN_40))
        TPR_50.append(TP_50 / (TP_50+FN_50))
        TPR_60.append(TP_60 / (TP_60+FN_60))
        FNMR.append(1-(TP / (TP+FN)))
        FNMR_10.append(1- (TP_10 / (TP_10+FN_10)))
        FNMR_20.append(1- (TP_20 / (TP_20+FN_20)))
        FNMR_30.append(1- (TP_30 / (TP_30+FN_30)))
        FNMR_40.append(1- (TP_40 / (TP_40+FN_40)))
        FNMR_50.append(1- (TP_50 / (TP_50+FN_50)))
        FNMR_60.append(1- (TP_60 / (TP_60+FN_60)))
        
        #print("FPR: ", FP / (FP+TN))
        #print("TPR: ", TP / (TP+FN))
    
    TP = 0
    FN = 0
    FP = 0
    TN = 0
    TP_10 = 0
    FN_10 = 0
    TP_20 = 0
    FN_20 = 0
    TP_30 = 0
    FN_30 = 0
    TP_40 = 0
    FN_40 = 0
    TP_50 = 0
    FN_50 = 0
    TP_60 = 0
    FN_60 = 0
    
    for i in f:
        data = i.split(';')
        if once == True:
            face_dist_before_same.append(float(data[0]))
            face_dist_before_other.append(float(data[1]))
        if float(data[0]) > th:
            FN = FN+1
        if float(data[1]) > th:
            TN = TN+1
        if float(data[0]) <= th:
            TP = TP+1
        if float(data[1]) <= th:
            FP = FP+1
        f.close
    for h in face_dist_after10:
        if h > th:
            FN_10 = FN_10+1
        if h <= th:
            TP_10 = TP_10+1
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
    for m in face_dist_after60:
        if m > th:
            FN_60 = FN_60+1
        if m <= th:
            TP_60 = TP_60+1
    once = False
print(len(face_dist_after20))

# Plot ROC normal    
bins = np.arange(0, 1, 0.02) #left margin, right margin, step size (years)
plt.figure(figsize=(6.5,2.5), dpi=160)
plt.plot(FPR, TPR, label='Before morphing')
plt.plot(FPR, TPR_10, color='pink', label='Group 10-20')
plt.plot(FPR, TPR_20, color='yellow', label='Group 20-30')
plt.plot(FPR, TPR_30, color='green', label='Group 30-40')
plt.plot(FPR, TPR_40, color='red', label='Group 40-50')
plt.plot(FPR, TPR_50, color='purple', label='Group 50-60')
plt.plot(FPR, TPR_60, color='black', label='Group 60-70')
plt.plot([0, 1], [0, 1], color='darkblue', linestyle='--')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
#plt.title('Receiver Operating Characteristic (ROC) Curve')
plt.legend()
plt.show() 

"""
# Plot ROC zoomed in
ranges_h = 41
ranges_l = 27
#bins = np.arange(0, 1, 0.02) #left margin, right margin, step size (years)
plt.figure(figsize=(5,2.5), dpi=160)
plt.plot(FPR[ranges_l:ranges_h], TPR[ranges_l:ranges_h], color='blue', label='Before morphing')
plt.plot(FPR_10[ranges_l:ranges_h], TPR[ranges_l:ranges_h], color='yellow', label='Group 20-30')
plt.plot(FPR_20[ranges_l:ranges_h], TPR[ranges_l:ranges_h], color='yellow', label='Group 20-30')
plt.plot(FPR_30[ranges_l:ranges_h], TPR[ranges_l:ranges_h], color='green', label='Group 30-40')
plt.plot(FPR_40[ranges_l:ranges_h], TPR[ranges_l:ranges_h], color='red', label='Group 40-50')
plt.plot(FPR_50[ranges_l:ranges_h], TPR[ranges_l:ranges_h], color='purple', label='Group 50-60')
plt.plot(FPr_60[ranges_l:ranges_h], TPR[ranges_l:ranges_h], color='yellow', label='Group 20-30')
#plt.plot([0, 1], [0, 1], color='darkblue', linestyle='--')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver Operating Characteristic (ROC) Curve')
plt.legend()
plt.show() 
"""

# Plot DET normal
plt.figure(figsize=(6.5,2.5), dpi=160)
plt.yscale("log")
plt.xscale("log")
#plt.plot(FPR, FNMR, label='Before morphing')
plt.plot(FPR, FNMR_10, color='pink', label='10-20')
plt.plot(FPR, FNMR_20, color='yellow', label='20-30')
plt.plot(FPR, FNMR_30, color='green', label='30-40')
plt.plot(FPR, FNMR_40, color='red', label='40-50')
plt.plot(FPR, FNMR_50, color='purple', label='50-60')
plt.plot(FPR, FNMR_60, color='black', label='60-70')
plt.plot([0, 1], [0, 1], color='darkblue', linestyle='--')
plt.xlabel('False Match Rate')
plt.ylabel('False non-Match Rate')
#plt.title('Decision Error Trade-off (DET) curve')
plt.legend()
plt.show() 


"""
# Plot DET zoomed in
plt.figure(figsize=(5,2.5), dpi=160)
plt.plot(FPR[ranges_l:ranges_h], FNMR_20[ranges_l:ranges_h], color='yellow', label='Group 20-30')
plt.plot(FPR[ranges_l:ranges_h], FNMR_30[ranges_l:ranges_h], color='green', label='Group 30-40')
plt.plot(FPR[ranges_l:ranges_h], FNMR_40[ranges_l:ranges_h], color='red', label='Group 40-50')
plt.plot(FPR[ranges_l:ranges_h], FNMR_50[ranges_l:ranges_h], color='purple', label='Group 50-60')
plt.xlabel('False Positive Rate')
plt.ylabel('False non-Match Rate')
plt.title('Decision Error Trade-off (DET) curve')
plt.legend()
plt.show() 
"""

face_dist_mean = []
mean_TPR = []
mean_FNMR = []
FNR = []

for i in range(len(face_dist_after20)):
    #print(face_dist_after20[i-1])
    mean_array = (face_dist_after10[i], face_dist_after20[i], face_dist_after30[i], face_dist_after40[i], face_dist_after50[i], face_dist_after60[i])
    face_dist_mean.append(np.mean(mean_array))
    #face_dist_mean.append(np.mean(face_dist_after20[i], face_dist_after30[i]))#, int(face_dist_after40[i-1]), int(face_dist_after50[i-1])))
for n in range(len(FNMR_10)):    
    mean_FNRM_array = (FNMR_10[n], FNMR_20[n], FNMR_30[n], FNMR_40[n], FNMR_50[n], FNMR_60[n])
    mean_FNMR.append(np.mean(mean_FNRM_array))
    
for k in range(len(TPR_10)):    
    #print(TPR_10[k])
    mean_array_TPR = (TPR_10[k], TPR_20[k], TPR_30[k], TPR_40[k], TPR_50[k], TPR_60[k])
    mean_TPR.append(np.mean(mean_array_TPR))
    FNR.append(1-float(np.mean(mean_array_TPR)))

eer_threshold = th_range[np.nanargmin(np.abs(np.abs(FNR) - np.abs(FPR)))]
EER = FPR[np.nanargmin(np.abs(np.abs(FNR) - np.abs(FPR)))]
print(eer_threshold)


"""
#interp1d
#fst = np.array([4, 4, 1, 3, 1, 4, 3, 2, 5, 2])
#snd = np.array([1, 1, 3, 4, 1, 5, 5, 5, 4, 3])
line= np.arange(0, 1)
#print(len(mean_FNMR))
#linfit = interp1d(th_range[0:len(mean_FNMR)], np.vstack(FPR, mean_FNMR), axis=0)
linfit = interp2d(FPR, mean_FNMR, axis = 0)
#print(linfit(0))

plt.figure(figsize=(6.5,2.5), dpi=160)
plt.gcf()#.subplots_adjust(bottom=0.20)
plt.yscale("log")
plt.xscale("log")
xnew = np.arange(0, 1, 0.1)
ynew = linfit(xnew)   # use interpolation function returned by `interp1d`
plt.plot(FPR, mean_FNMR, 'o', xnew, ynew, '-')
plt.show()
"""

bins = np.arange(0, 1, 0.02) #left margin, right margin, step size (years)
plt.figure(figsize=(6.5,2.5), dpi=160)
plt.gcf()#.subplots_adjust(bottom=0.20)
plt.hist(face_dist_before_same, bins, alpha=0.5, label='Same subject')
plt.hist(face_dist_before_other, bins, alpha=0.5, label='Other subject')
plt.hist(face_dist_mean, bins, alpha=0.5, label='Morph same subject')
#plt.hist(face_dist_after20, bins, alpha=0.5, color = 'yellow', label='Group 20-30')
#plt.hist(face_dist_after30, bins, alpha=0.5, color = 'green', label='Group 30-40')
#plt.hist(face_dist_after40, bins, alpha=0.5, color = 'red', label='Group 40-50')
#plt.hist(face_dist_after50, bins, alpha=0.5, color = 'purple', label='Group 50-60')
plt.xlabel('Face distance')
plt.ylabel('Amount')
plt.legend()
#plt.savefig('age_distribution_estimated_special.png')
plt.show() 