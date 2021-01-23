#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 21:14:41 2021

@author: ellen
"""

# finde path to all pictures ending with "pattern" - *_1.jpg
import re
import os, fnmatch, facemorpher
from pyagender import PyAgender
import cv2
from PIL import Image
import face_recognition
import time
import numpy as np


def find2(pattern, path):
    result = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                result.append(os.path.join(root, name))
    return result

def average(pictures):
    facemorpher.averager(pictures, plot=True)
    
def morphing(orginele_foto, morph_foto):
    #agender = PyAgender()
    #faces = agender.detect_genders_ages(cv2.imread(orginele_foto))
    #original_age = faces[0]['age']
    pictures = [orginele_foto, morph_foto]
    facemorpher.morpher(pictures, plot=True, out_frames='output')
    # Output is fotos in de folder /output
    
    
def age_estimation(foto):
    agender = PyAgender()
    faces = agender.detect_genders_ages(cv2.imread(foto))
    age = faces[0]['age']
    return round(age)
    
def age_estimation_group(foto_list):
    age_group_detected = []
    age_group_actual = []
    for x in foto_list:
        age = age_estimation(x)
        age_group_detected.append(age)
        age_group_actual.append(x.split("_")[1])
    return age_group_detected, age_group_actual
    
def Face_recognition(known, test):
    known_image = face_recognition.load_image_file(known)
    face_encoding = face_recognition.face_encodings(known_image)[0]
    known_encodings = [face_encoding]
    image_to_test = face_recognition.load_image_file(test)
    image_to_test_encoding = face_recognition.face_encodings(image_to_test)[0]
    face_distances = face_recognition.face_distance(known_encodings, image_to_test_encoding)
    
    for i, face_distance in enumerate(face_distances):
        print("The test image has a distance of {:.2} from known image #{}".format(face_distance, i))
        print("- With a normal cutoff of 0.6, would the test image match the known image? {}".format(face_distance < 0.6))
        print("- With a very strict cutoff of 0.5, would the test image match the known image? {}".format(face_distance < 0.5))
        print()
    return face_distance

def after_morphing(morph, path):
    age_after_morph = []
    face_distance_after_morph = []
    face_distance_before_morph =[]
    actual_age = []
    age_before_morph = []
    result = find2("*_1.png", path)
    save_name = morph.split("/")[-1].replace('.png','.npz')
    for i in result:
        start = time.time()
        morphing(i, morph)
        age_after_morph.append(age_estimation("output/frame009.png"))
        face_distance_after_morph.append(Face_recognition(i.replace("_1.png", ".png"), "output/frame009.png" ))
        face_distance_before_morph.append(Face_recognition(i.replace("_1.png", ".png"), i ))
        actual_age.append(int(i.split("_")[2]))
        age_before_morph.append(age_estimation(i))
        print(age_after_morph)
        print(face_distance_after_morph)
        print(actual_age)
        stop = time.time()
        print(stop-start)
    np.savez(save_name, age_after_morph=age_after_morph,age_before_morph=age_before_morph, actual_age=actual_age, face_dist_after = face_distance_after_morph, face_dist_before=face_distance_before_morph)
   # Plots_print()
    #return age_after_morph, face_distance_after_morph, actual_age, face_distance_before_morph, age_before_morph

def read_npz_after_morph(file):
    x = np.load(file, mmap_mode='r')

    actual_age = x['actual_age'] # Array with actual ages
    age_after_morph = x['age_after_morph'] # Array with detected ages after morphing
    age_before_morph = x['age_before_morph'] # Array with detected ages before morphing
    face_dist_after = x['face_dist_after'] # Face distance after morphing
    face_dist_before = x['face_dist_before'] # Face distance before morphing
    
    return actual_age, age_after_morph, age_before_morph, face_dist_after, face_dist_before


path = "/Users/ellen/Documents/GitHub/Age-Obfuscation-Morphing/SiblingsDB/SiblingsDB_preproccesed"
#after_morphing("/Users/ellen/Documents/GitHub/Age-Obfuscation-Morphing/averages/average20_30_N3(1).png", path)
#after_morphing("/Users/ellen/Documents/GitHub/Age-Obfuscation-Morphing/averages/average30_40_N3(0).png", path)
after_morphing("/Users/ellen/Documents/GitHub/Age-Obfuscation-Morphing/averages/average40_50_N3(0).png", path)
after_morphing("/Users/ellen/Documents/GitHub/Age-Obfuscation-Morphing/averages/average50_60_N3(0).png", path)