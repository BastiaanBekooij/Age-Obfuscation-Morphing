# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 15:06:32 2021

@author: murie
"""

import numpy as np
import pandas as pd
#%matplotlib inline

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
    #print(data[0])
    #other.append(float(data[0]))
    dist2self.append(float(data[0]))
    dist2otherNE.append(float(data[1]))
    #dist2otherE.append(float(data[2]))
    f.close

print(type(other))
#print(type(dist2self))
#[float(i) for i in dist2self]
#print(type(dist2self))
gym = pd.DataFrame({'Distance to self': dist2self, 'Distance to other': dist2otherNE})
#gym = pd.DataFrame({'Distance to other': other})
#gym.groupby('dist2other_exp').count().plot(kind='bar')
gym.plot.hist(bins=50, alpha=0.6)