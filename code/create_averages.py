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
    [60,70],
    #[70,80],
    #[80,90],
    #[90,100],
    #[100,150]
    ]
# grouped_images = [[] for i in range(len(age_groups))]            

# for img in result:
#     # getal = random.randint(0,1000)
#     # if getal == 500:
#     #     print(img)
#     age_actual = img.split('_')[0].split('\\')[-1]
#     # try:
#     #     age_detected = functions.age_estimation(img)
#     # except KeyboardInterrupt as e:
#     #     print(e)
#     #     break
#     # except:
#     #     print("failed age estimation, continuing...")
#     #     continue
#     #print(f"actual age: {age_actual}, estimated age: {age_detected}")
#     #print(img)
#     #print(age_actual)
#     #if int(age_actual) <= 10:
#         #print(img)
#         #onder_10.append(img)
        

#     for idx, age_group in zip(range(0,len(age_groups)), age_groups):
#         if int(age_actual) >= age_group[0] and int(age_actual) < age_group[1]:
#             grouped_images[idx].append(img)
#             #print(f"added to age group{idx}")
        
number_of_people = [1, 2, 3, 5, 7, 10]
age_average = np.zeros((len(number_of_people),len(age_groups)))
for idx, age_group in zip(range(0,len(age_groups)), age_groups):
    print(f"Starting age group {idx}")
    result = []
    for a in range(age_group[0], age_group[1]):
        result.extend(functions.find2(f'{a}*.jpg', '../CACD2000'))
        print(f"Added age {a}")
    for n in number_of_people:
        for i in range(0,3):
            out_filename = f"../averages/average{age_group[0]}_{age_group[1]}_N{n}({i}).png"
            if not os.path.exists(out_filename):
                facemorpher.averager(random.sample(result, n), plot=True, out_filename=out_filename)
            age_average[n-1, idx] = age_average[n-1, idx] + int(functions.age_estimation(out_filename))
        print(f"Estimated age for average face with {n} images.")
    #print("Age: ", age_average)
    
age_average = age_average/3 # Get mean age

plt.plot([10*x+5 for x in range(1, len(age_groups)+1)],age_average.T)
plt.legend(number_of_people)
plt.xlabel('Actual age')
plt.ylabel('Detected age')
plt.show()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    