# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 12:45:39 2020

@author: murie
"""

import facemorpher
import re
import os, fnmatch
import argparse
import cv2

x = os.getcwd()

# Get a list of image paths in a folder
#path = "C:/Users/murie/Documents/school/master/1B/Introduction2Biometrics/project_git/datasets/Siblings/"
path = "C:/Users/murie/Documents/school/master/1B/Introduction2Biometrics/project/datasets/FGNET/FGNET/images"
f = open('C:/Users/murie/Documents/school/master/1B/Introduction2Biometrics/project_git/datasets/Siblings/subjects.csv', 'r')

#imgpaths = facemorpher.list_imgpaths('C:/Users/murie/Documents/school/master/1B/Introduction2Biometrics/project/datasets/FGNET/FGNET/images')
imgpaths = facemorpher.list_imgpaths('C:/Users/murie/Documents/school/master/1B/Introduction2Biometrics/project_git/datasets/test')
#imgpaths = facemorpher.list_imgpaths('C:/Users/murie/Documents/school/master/1B/Introduction2Biometrics/project_git/datasets/fransbauer')

# To morph, supply an array of face images:
#facemorpher.morpher(imgpaths, plot=True)

# To average, supply an array of face images:
facemorpher.averager(imgpaths, plot=True)

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
	help="path to input image")
ap.add_argument("-f", "--face", required=True,
	help="path to face detector model directory")
ap.add_argument("-a", "--age", required=True,
	help="path to age detector model directory")
ap.add_argument("-c", "--confidence", type=float, default=0.5,
	help="minimum probability to filter weak detections")
args = vars(ap.parse_args())

AGE_BUCKETS = ["(0-2)", "(4-6)", "(8-12)", "(15-20)", "(25-32)",
	"(38-43)", "(48-53)", "(60-100)"]

print("[INFO] loading face detector model...")
prototxtPath = os.path.sep.join([args["face"], "deploy.prototxt"])
weightsPath = os.path.sep.join([args["face"],
	"res10_300x300_ssd_iter_140000.caffemodel"])
faceNet = cv2.dnn.readNet(prototxtPath, weightsPath)
# load our serialized age detector model from disk
print("[INFO] loading age detector model...")
prototxtPath = os.path.sep.join([args["age"], "age_deploy.prototxt"])
weightsPath = os.path.sep.join([args["age"], "age_net.caffemodel"])
ageNet = cv2.dnn.readNet(prototxtPath, weightsPath)


onder_10 = []
onder_20 = []
onder_30 = []
onder_40 = []
onder_50 = []
onder_60 = []
onder_70 = []
for row in f:
    data = (row.split(" "))
    data_split = (str(data).replace('"', ',').split(","))
    number = data_split[0].replace('\t','').replace("'", "").replace('[', '')
    leeftijd = data_split[4].replace('\t','')
    print(int(leeftijd))
    if int(leeftijd) < 10:
        onder_10.append(number)
    elif int(leeftijd) < 20 and int(leeftijd) > 10:
        onder_20.append(number)
    elif int(leeftijd) < 30 and int(leeftijd) > 20:
        onder_30.append(number)
    elif int(leeftijd) < 40 and int(leeftijd) > 30:
        onder_40.append(number)
    elif int(leeftijd) < 50 and int(leeftijd) > 40:
        onder_50.append(number)
    elif int(leeftijd) < 60 and int(leeftijd) > 50:
        onder_60.append(number)
    elif int(leeftijd) < 70 and int(leeftijd) > 60:
        onder_70.append(number)
        
def find(name, path):
    for root, dirs, files in os.walk(path):
        if name in dirs:
            return os.path.join(root, name)

def find2(pattern, path):
    result = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                result.append(os.path.join(root, name))
    return result

#pictures = ""
pictures = []
for i in onder_30:
    print(i)
    path = find(i,x)
    print(path)
    if str(path) != "None":
        z = find2('*.jpg', path)
        #pictures = pictures + " " + '"' + str(z[0]) + '"'
        #print(z)
        pictures.append(str(z[-1]))
#print(pictures)

#facemorpher.morpher(pictures, plot=True)
#facemorpher.averager(pictures, plot=True)