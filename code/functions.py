#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 10:43:48 2021

@author: ellen
"""

# finde path to all pictures ending with "pattern" - *_1.jpg
import re
import os, fnmatch, facemorpher
from pyagender import PyAgender
import cv2
from PIL import Image
import face_recognition


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
    pictures = [orginele_foto, morph_foto]
    facemorpher.morpher(pictures, plot=True, out_frames='output')
    # Output is fotos in de folder /output
    
    
def age_estimation(foto):
    agender = PyAgender()
    faces = agender.detect_genders_ages(cv2.imread(foto))
    age = faces[0]['age']
    return age
    
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
    actual_age = []
    result = find2("*_1.png", path)
    for i in result:
        morphing(i, morph)
        age_estimate = age_estimation("output/frame009.png")
        face_dist = Face_recognition(i.replace("_1.jpg", ".jpg"), "output/frame009.png" )
        age_after_morph.append(age_estimate)
        face_distance_after_morph.append(face_dist)
        actual_age.append(int(i.split("_")[1]))
        print(age_after_morph)
        print(face_distance_after_morph)
        print(actual_age)
    return age_after_morph, face_distance_after_morph, actual_age
