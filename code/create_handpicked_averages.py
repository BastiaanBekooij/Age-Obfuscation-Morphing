# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 17:29:19 2021

@author: Basti
"""
import sys
sys.path.append('..')


import functions
from age_estimation import estimate_age

import os, fnmatch, facemorpher
from pyagender import PyAgender
import cv2
import random
import numpy as np
import matplotlib.pyplot as plt

agender = PyAgender()
age_detected = []
age_actual = []

# result = functions.find2('14*.jpg', '../CACD2000')
age_groups = [
    [10,20],
    [20,30],
    [30,40],
    [40,50],
    [50,60],
    [60,70]
    #[70,80],
    #[80,90],
    #[90,100],
    #[100,150]
    ]

people = [
    ['../CACD2000/14_Daveigh_Chase_0004.jpg', '../CACD2000/14_Lucas_Till_0001.jpg', '../CACD2000/16_Mia_Wasikowska_0008.jpg'],
    ['../CACD2000/22_Anna_Kendrick_0005.jpg', '../CACD2000/25_Tyler_Blackburn_0012.jpg', '../CACD2000/28_Eric_Winter_0003.jpg'],
    ['../CACD2000/32_Oliver_Hudson_0003.jpg', '../CACD2000/38_Mireille_Enos_0005.jpg', '../CACD2000/36_Freddie_Prinze_Jr._0013.jpg'],
    ['../CACD2000/42_Nikolaj_Coster-Waldau_0010.jpg', '../CACD2000/47_Mare_Winningham_0015.jpg', '../CACD2000/42_Paul_Rudd_0002.jpg'],
    ['../CACD2000/53_Dylan_Baker_0001.jpg', '../CACD2000/53_Fran_Drescher_0005.jpg', '../CACD2000/57_David_Hasselhoff_0005.jpg'],
    ['../CACD2000/61_Mark_Hamill_0001.jpg', '../CACD2000/61_Mary_McDonnell_0007.jpg', '../CACD2000/62_David_Patrick_Kelly_0001.jpg']
    ]



age_average = np.zeros(len(age_groups))
for idx, age_group in zip(range(0,len(age_groups)), age_groups):
    out_filename = f"../averages/average{age_group[0]}_{age_group[1]}_handpickedN2.png"
    if not os.path.exists(out_filename):
        facemorpher.averager(people[idx][0:3], plot=True, out_filename=out_filename)
    age_average[idx] = age_average[idx] + int(functions.age_estimation(out_filename))
