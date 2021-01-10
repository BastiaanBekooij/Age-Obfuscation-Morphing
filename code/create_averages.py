# -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 11:30:14 2021

@author: Basti
"""

import functions

import os, fnmatch, facemorpher
from pyagender import PyAgender
import cv2
import random
import numpy
import matplotlib.pyplot as plt



agender = PyAgender()
age_detected = []
age_actual = []

result = functions.find2('*.jpg', '../CACD2000')
age_groups = [
    [10,20],
    [20,30],
    [30,40],
    [40,50],
    [50,60],
    [60,70],
    #[70,80],
    #[80,90],
    #[90,100],
    #[100,150]
    ]
grouped_images = [[] for i in range(len(age_groups))]            

for img in result:
    getal = random.randint(0,1000)
    if getal == 500:
        print(img)
        age_actual = img.split('_')[0].split('\\')[-1]
        # try:
        #     age_detected = functions.age_estimation(img)
        # except KeyboardInterrupt as e:
        #     print(e)
        #     break
        # except:
        #     print("failed age estimation, continuing...")
        #     continue
        #print(f"actual age: {age_actual}, estimated age: {age_detected}")
        #print(img)
        #print(age_actual)
        #if int(age_actual) <= 10:
            #print(img)
            #onder_10.append(img)
            

        for idx, age_group in zip(range(0,len(age_groups)-1), age_groups):
            if int(age_actual) >= age_group[0] and int(age_actual) < age_group[1]:
                grouped_images[idx].append(img)
                print(f"added to age group{idx}")
        

for idx, age_group in zip(range(0,len(age_groups)-1), age_groups):
    out_filename = f"../averages/average{age_group[0]}_{age_group[1]}.png"
    print(out_filename)
    facemorpher.averager(grouped_images[idx], plot=True, out_filename=out_filename)