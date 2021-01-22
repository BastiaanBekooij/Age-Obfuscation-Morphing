# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 15:06:32 2021

@author: murie
"""

import numpy as np
import pandas as pd
#%matplotlib inline
import matplotlib.pyplot as plt 
  
#f = open('C:/Users/murie/Documents/school/master/1B/Introduction2Biometrics/project_git/data/before_rec_other_v2_csv.txt', 'r')
f = open('../data/before_rec_csv', 'r')
data = []
dist2self = []
dist2otherNE = []
dist2otherE = []
other = []

for i in f:
    #print(i)
    data = i.split(';')
    print(data)
    #other.append(float(data[0]))
    dist2self.append(float(data[0]))
    dist2otherNE.append(float(data[1]))
    #dist2otherE.append(float(data[2]))
    f.close

print(type(other))
#print(type(dist2self))
#[float(i) for i in dist2self]
#print(type(dist2self))
#gym = pd.DataFrame({'Distance to self': dist2self, 'Distance to other (no expression)': dist2otherNE})
#gym.plot.hist(bins = 40, alpha=0.5)

bins = np.arange(0, 1, 0.02) #left margin, right margin, step size (years)
plt.figure(figsize=(5,2.5), dpi=160)
plt.gcf()#.subplots_adjust(bottom=0.20)
plt.hist(dist2self, bins, alpha=0.5, label='Estimated age')
plt.hist(dist2otherNE, bins, alpha=0.5, label='Estimated age after morph')
#plt.title('Age distribution of dataset')
plt.xlabel('Age (years)')
plt.ylabel('Amount')
plt.legend()
plt.savefig('age_distribution_estimated_special.png')
plt.show() 

#bins = np.arange(-10, 35, 2) #left margin, right margin, step size (years)
#plt.figure(figsize=(5,2.5), dpi=160)
#plt.gcf().subplots_adjust(bottom=0.20)

