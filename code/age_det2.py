# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 11:36:51 2020

@author: murie
"""
#import os, fnmatch, facemorpher
from pyagender import PyAgender
import cv2

agender = PyAgender() # see available options in __init__() src

faces = agender.detect_genders_ages(cv2.imread("C:/Users/murie/Documents/school/master/1B/Introduction2Biometrics/project_git/datasets/test"))
image = agender.detect_genders_ages(cv2.imread("acaro.png"))

