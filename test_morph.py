# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 12:45:39 2020

@author: murie
"""

import facemorpher
#import re


# Get a list of image paths in a folder
#imgpaths = facemorpher.list_imgpaths('C:/Users/murie/Documents/school/master/1B/Introduction2Biometrics/project/datasets/FGNET/FGNET/images')
imgpaths = facemorpher.list_imgpaths('C:/Users/murie/Documents/school/master/1B/Introduction2Biometrics/project/datasets/test')

# To morph, supply an array of face images:
facemorpher.morpher(imgpaths, plot=True)

# To average, supply an array of face images:
facemorpher.averager(['image1.png', 'image2.png'], plot=True)

#path = "C:/Users/murie/Documents/school/master/1B/Introduction2Biometrics/project/datasets/SiblingsDB/"
#f = open('C:/Users/murie/Documents/school/master/1B/Introduction2Biometrics/project/datasets/SiblingsDB/subjects.csv', 'r')

# onder_10 = []
# onder_20 = []
# onder_30 = []
# onder_40 = []
# onder_50 = []
# onder_60 = []
# onder_70 = []

# for row in f:
#     data = (row.split(" "))
#     data_split = (str(data).replace('"', ',').split(","))
#     number = data_split[0].replace('\t','').replace("'", "").replace('[', '')
#     leeftijd = data_split[4].replace('\t','')
#     if int(leeftijd) < 10:
#         onder_10.append(number)
#     elif int(leeftijd) < 20 and int(leeftijd) > 10:
#         onder_20.append(number)
#     elif int(leeftijd) < 30 and int(leeftijd) > 20:
#         onder_30.append(number)
#     elif int(leeftijd) < 40 and int(leeftijd) > 30:
#         onder_40.append(number)
#     elif int(leeftijd) < 50 and int(leeftijd) > 40:
#         onder_50.append(number)
#     elif int(leeftijd) < 60 and int(leeftijd) > 50:
#         onder_60.append(number)
#     elif int(leeftijd) < 70 and int(leeftijd) > 60:
#         onder_70.append(number)