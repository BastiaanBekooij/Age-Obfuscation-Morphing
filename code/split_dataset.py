# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 12:14:49 2021

@author: murie
"""

import os, fnmatch, facemorpher
from pyagender import PyAgender
import cv2
import random
import numpy
import matplotlib.pyplot as plt
import random
from PIL import Image
import sys

path1 = "../SiblingsDB/DBs/HQfps"
path2 = "../SiblingsDB/SiblingsDB_preprocessed/"


def find2(pattern, path):
    result = []
    names = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                #print(sys.platform)
                if sys.platform == 'win32':
                    #result.append(os.path.join(root, name))
                    result.append(os.path.join(root, name).replace("\\","/"))
                    #result = os.path.normpath(test)
                else : 
                    result.append(os.path.join(root, name)) # Does not work on Windows
                names.append(name)
    return result, names


def ages_from_CSV():
    f = open('../SiblingsDB/subjects.csv', 'r')
    x=[]
    for i in f:
        data = (i.split(" "))
        data_split = (str(data).replace('"', ',').split(","))
        age = data_split[4].replace('\\t','')
        x.append(age)
    f.close
    return x

(result, names) = find2('*.jpg', path1)
age = ages_from_CSV()
#print(result)

count = 1
print(len(result)) # nr of pictures is 4x nr of subjects  (which is 115)

for i in result[:len(result):4]:
    #print(i)
    subject_num = i.split("/")[4] # [x] depending on path
    age_per = age[int(subject_num)-1]
    print("subject nr: ", subject_num,", age: ", age_per)
    
    # Open first 2 images, first one i = normal, result[count] = second image
    im1 = Image.open(i)
    im2 = Image.open(result[count])
    
    filename1 = path2 + subject_num + "_" + age_per + ".png"
    filename2 = path2 + subject_num + "_" + age_per + "_1.png"
    im1.save(filename1, "png")
    im2.save(filename2, "png")
    count = count + 4
    
        
        
        
        
        