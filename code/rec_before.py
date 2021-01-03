# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 10:47:18 2021

@author: murie
"""

import os, fnmatch, facemorpher
#from pyagender import PyAgender
import cv2
#import random
import numpy
import matplotlib.pyplot as plt
import random
from PIL import Image
import face_recognition

#known = "C:/Users/murie/Documents/school/master/1B/Introduction2Biometrics/project_git/datasets/Siblings/DBs/HQfps/227/_DSC2305.jpg"
#known2 = "C:/Users/murie/Documents/school/master/1B/Introduction2Biometrics/project_git/datasets/test/teun.jpg" 
path = "C:/Users/murie/Documents/school/master/1B/Introduction2Biometrics/project_git/datasets/Siblings/DBs/HQfps/"
#path2 = "C:/Users/murie/Documents/school/master/1B/Introduction2Biometrics/project_git/datasets/test/"

def find2(pattern, path):
    result = []
    names = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                result.append(os.path.join(root, name))
                names.append(name)
    return result, names

def compare_img(Known, Test):
    known_image = face_recognition.load_image_file(Known)
    face_encoding = face_recognition.face_encodings(known_image)[0]
    known_encodings = [face_encoding]
    image_to_test = face_recognition.load_image_file(Test)
    image_to_test_encoding = face_recognition.face_encodings(image_to_test)[0]
    face_distances = face_recognition.face_distance(known_encodings, image_to_test_encoding)
    
    for i, face_distance in enumerate(face_distances):
        print("The test image has a distance of {:.2} from known image #{}".format(face_distance, i))
    #    print("- With a normal cutoff of 0.6, would the test image match the known image? {}".format(face_distance < 0.6))
    #    print("- With a very strict cutoff of 0.5, would the test image match the known image? {}".format(face_distance < 0.5))
    #    print()
    return face_distance

(result, names) = find2('*.jpg', path)
#(results, folders) = find2('/*', path)
#print(names)
count = 233
distance = []
countx_as = 1
x_as = []
print(len(result))

for known in result[232:len(result):4]:
    #print(result[count]+'\n')
    #print(known)
    #known1 = "C:/Users/murie/Documents/school/master/1B/Introduction2Biometrics/project_git/datasets/Siblings/DBs/HQfps/81/_DSC0015.jpg"
    #compare = "C:/Users/murie/Documents/school/master/1B/Introduction2Biometrics/project_git/datasets/Siblings/DBs/HQfps/119/_DSC0289.jpg"
    distance_same = compare_img(known, result[count]) # Same person
    distance.append(distance_same)
    count = count + 4
    countx_as = countx_as + 1
    x_as.append(countx_as)
    

#face_dist_10 = compare_img(Known, path + "227/_DSC2307.jpg") # Same person
#face_dist_20 = compare_img(Known, path + "227/_DSC2305.jpg") # Same image
#face_dist_30 = compare_img(Known, path + "209/_DSC0898.jpg") # Different person

#face_dist_10 = compare_img(known2, path2 + "dieuwertjeblok.jpg") # Same person
#face_dist_20 = compare_img(known2, path2 + "mariken.jpg") # Same image
#face_dist_30 = compare_img(known2, path2 + "teun2.jpg") # Different person

#face_dist = [face_dist_10, face_dist_20, face_dist_30, face_dist_40, face_dist_50]
#x_face = ["0-10", "10-20", "20-30", "30-40", "40-50"]

#plt.plot(x_as, distance, 'ro')
#plt.xlabel('Subject number')
#plt.ylabel('Face distance')
#plt.title("Images of same person with their face distance")