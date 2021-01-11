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

#agender = PyAgender()
path1 = "C:/Users/murie/Documents/school/master/1B/Introduction2Biometrics/project_git/SiblingsDB/DBs/HQfps"
path2 = "C:/Users/murie/Documents/school/master/1B/Introduction2Biometrics/project_git/Siblings2fotos/"

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

#def age_det(name):
#    faces = agender.detect_genders_ages(cv2.imread(name))
    #print(faces)
#    if len(faces) == 0:
#        age = 5000        
#    else:
#        age = faces[0]['age']
    #print(age)
#    return age

def ages_from_CSV():
    #f = open('/Users/ellen/Documents/Twente/Q2/Introduction to biometrics/Final/SiblingsDB/subjects.csv', 'r')
    f = open('C:/Users/murie/Documents/school/master/1B/Introduction2Biometrics/project_git/SiblingsDB/subjects.csv', 'r')
    x=[]
    for i in f:
        data = (i.split(" "))
        data_split = (str(data).replace('"', ',').split(","))
        age = data_split[4].replace('\\t','')
        x.append(age)
    f.close
    return x

(result, names) = find2('*.png', path2)
age = ages_from_CSV()
#print(root)

count = 1
print(len(result)) # nr of pictures is 4x nr of subjects  (which is 115)

for i in result[:len(result):4]:
    #print(i)
    subject_num = i.split("/")[12] # [x] depending on path
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
    

#for i in result:
#    age = age_det(i)
#    if age != 5000:
#        # Save picture
#       Subject_num = i.split('/')[9]
#        leeftijd_per = leeftijd[int(Subject_num)-1]
#        print(Subject_num)
#        print(leeftijd_per)
#        im = Image.open(i)
#        new_file_name = path2 + Subject_num + "_" + leeftijd_per + ".png"
#        if os.path.exists(new_file_name):
#            new_file_name = path2 + Subject_num + "_" + leeftijd_per + "_1.png"
#        im.save(new_file_name, "png")
        
        
        
        
        
        