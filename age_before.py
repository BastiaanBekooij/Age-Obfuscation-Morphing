# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 10:12:17 2021

@author: murie
"""

import os, fnmatch, facemorpher
#from pyagender import PyAgender
import cv2
import random
import numpy
import matplotlib.pyplot as plt
import random
from PIL import Image

#agender = PyAgender()
detected_age = []
actual_age = []

def find2(pattern, path):
    result = []
    names = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                result.append(os.path.join(root, name))
                names.append(name)
    print(result)
    print(names)
    return result, names

def age_det(name):
    faces = agender.detect_genders_ages(cv2.imread(name))
    #print(faces)
    if len(faces) == 0:
        age = 5000        
    else:
        age = faces[0]['age']
    #print(age)
    return age

def leeftijden_uit_CSV():
    f = open('C:/Users/murie/Documents/school/master/1B/Introduction2Biometrics/project_git/datasets/Siblings/subjects.csv', 'r')
    x=[]
    for i in f:
        data = (i.split(" "))
        data_split = (str(data).replace('"', ',').split(","))
        leeftijd = data_split[4].replace('\\t','')
        x.append(leeftijd)
    f.close
    return x

path = "C:/Users/murie/Documents/school/master/1B/Introduction2Biometrics/project_git/datasets/Siblings/HQfps/"
path2 = "C:/Users/murie/Documents/school/master/1B/Introduction2Biometrics/project_git/datasets/Siblings2fotos/"
(result, names) = find2('*.jpg', path)
actual_age = leeftijden_uit_CSV()
print(actual_age)
for i in result:
    #age = age_det(i)
    age = 1
    detected_age.append(int(age))
    if age != 5000:
        # Save picture
        Subject_num = i.split('/')[9]
        leeftijd_per = leeftijd[int(Subject_num)-1]
        print(Subject_num)
        print(leeftijd_per)
        im = Image.open(i)
        new_file_name = path2 + Subject_num + "_" + leeftijd_per + ".png"
        if os.path.exists(new_file_name):
            new_file_name = path2 + Subject_num + "_" + leeftijd_per + "_1.png"
        im.save(new_file_name, "png")
                
"""actual_age_arr = numpy.array(actual_age)
detected_age_arr = numpy.array(detected_age)
plt.scatter(actual_age_arr, detected_age_arr)
plt.xlabel('Actual age')
plt.ylabel('Detected age')
plt.title("Detected age vs actual age of the complete siblings data set")
plt.plot(range(0, 70))
plt.savefig('actual-detect-morph20-SB.png')
"""