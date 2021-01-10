from pathlib import Path
import os,sys,inspect
sys.path.insert(0,'..')
import cv2
import dlib
import numpy as np
import argparse
from contextlib import contextmanager
from keras.utils.data_utils import get_file
from age_estimation.model import get_model
import os, fnmatch#, facemorpher
import matplotlib.pyplot as plt


pretrained_model = "https://github.com/yu4u/age-gender-estimation/releases/download/v0.5/age_only_resnet50_weights.061-3.300-4.410.hdf5"
modhash = "306e44200d3f632a5dccac153c2966f2"

def images_from_dir(image_path):
    img = cv2.imread(str(image_path), 1)
    if img is not None:
        h, w, _ = img.shape
        r = 640 / max(w, h)
        return cv2.resize(img, (int(w * r), int(h * r)))



def estimate_age(image_path):
    model_name = "ResNet50"
    margin = 0.4

    weight_file = get_file("age_only_resnet50_weights.061-3.300-4.410.hdf5", pretrained_model,
                               cache_subdir="pretrained_models",
                               file_hash=modhash, cache_dir=Path(__file__).resolve().parent)

    # for face detection
    detector = dlib.get_frontal_face_detector()

    # load model and weights
    model = get_model(model_name=model_name)
    model.load_weights(weight_file)
    img_size = model.input.shape.as_list()[1]
    
    if not os.path.exists(image_path):
        raise Exception("image_path does not exist!")

    img = images_from_dir(image_path)
    input_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img_h, img_w, _ = np.shape(input_img)

    # detect faces using dlib detector
    detected = detector(input_img, 1)
    faces = np.empty((len(detected), img_size, img_size, 3))

    if len(detected) > 0:
        for i, d in enumerate(detected):
            x1, y1, x2, y2, w, h = d.left(), d.top(), d.right() + 1, d.bottom() + 1, d.width(), d.height()
            xw1 = max(int(x1 - margin * w), 0)
            yw1 = max(int(y1 - margin * h), 0)
            xw2 = min(int(x2 + margin * w), img_w - 1)
            yw2 = min(int(y2 + margin * h), img_h - 1)
            cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 0), 2)
            faces[i, :, :, :] = cv2.resize(img[yw1:yw2 + 1, xw1:xw2 + 1, :], (img_size, img_size))

        # predict ages and genders of the detected faces
        results = model.predict(faces)
        ages = np.arange(0, 101).reshape(101, 1)
        predicted_ages = results.dot(ages).flatten()
        return int(predicted_ages[0])
    else:
        raise Exception("No face detected")

# age = estimate_age('../result.png')
# print(age)