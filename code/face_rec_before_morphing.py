# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 10:47:18 2021

@author: murie
"""

import os, fnmatch
#import cv2
import numpy
import matplotlib.pyplot as plt
#import random
#from PIL import Image
import face_recognition
import sys

#path = "C:/Users/murie/Documents/school/master/1B/Introduction2Biometrics/project_git/datasets/Siblings/DBs/HQfps/"
#path2 = "C:/Users/murie/Documents/school/master/1B/Introduction2Biometrics/project_git/Siblings2fotos/"

path = "../datasets/Siblings/DBs/HQfps/"
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

(result, names) = find2('*.png', path2)
#print(names)

count = 1
distance = []
countx_as = 1
x_as = []
loop2 = 0
loop1 = 0
count4secondloop = 0
stepsize = 10

    
for known in result[:len(result):2]:
     loop1 = loop1 + 1
     print('First loop: ', loop1)
     count4secondloop = count4secondloop + 2
     loop2 = 0
     for compare in result[count4secondloop+1:len(result): stepsize]:
         count = count + stepsize
         distance_other = compare_img(known, compare) # Same person
         distance.append(distance_other)
         loop2 = loop2 + 1
         print('Second loop: ', loop2)


plt.plot(np.arange(0, len(distance)), distance, 'ro')
plt.xlabel('Subject')
plt.ylabel('Distance')
plt.title("Face distance of different persons")