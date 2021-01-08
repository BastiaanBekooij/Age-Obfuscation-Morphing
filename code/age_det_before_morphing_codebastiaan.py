# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 15:22:37 2021

@author: murie
"""

from pathlib import Path
import cv2
import dlib
import numpy as np
import argparse
from contextlib import contextmanager
from keras.utils.data_utils import get_file
from model import get_model
import os, fnmatch#, facemorpher
import matplotlib.pyplot as plt


pretrained_model = "https://github.com/yu4u/age-gender-estimation/releases/download/v0.5/age_only_resnet50_weights.061-3.300-4.410.hdf5"
modhash = "306e44200d3f632a5dccac153c2966f2"


def get_args():
    parser = argparse.ArgumentParser(description="This script detects faces from web cam input, "
                                                 "and estimates age for the detected faces.",
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("--model_name", type=str, default="ResNet50",
                        help="model name: 'ResNet50' or 'InceptionResNetV2'")
    parser.add_argument("--weight_file", type=str, default=None,
                        help="path to weight file (e.g. age_only_weights.029-4.027-5.250.hdf5)")
    parser.add_argument("--margin", type=float, default=0.4,
                        help="margin around detected face for age-gender estimation")
    parser.add_argument("--image_dir", type=str, default=None,
                        help="target image directory; if set, images in image_dir are used instead of webcam")
    args = parser.parse_args()
    return args


def draw_label(image, point, label, font=cv2.FONT_HERSHEY_SIMPLEX,
               font_scale=1, thickness=2):
    size = cv2.getTextSize(label, font, font_scale, thickness)[0]
    x, y = point
    cv2.rectangle(image, (x, y - size[1]), (x + size[0], y), (255, 0, 0), cv2.FILLED)
    cv2.putText(image, label, point, font, font_scale, (255, 255, 255), thickness)


@contextmanager
def video_capture(*args, **kwargs):
    cap = cv2.VideoCapture(*args, **kwargs)
    try:
        yield cap
    finally:
        cap.release()


def yield_images():
    # capture video
    with video_capture(0) as cap:
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

        while True:
            # get video frame
            ret, img = cap.read()

            if not ret:
                raise RuntimeError("Failed to capture image")

            yield img


def yield_images_from_dir(image_path):
    img = cv2.imread(str(image_path), 1)
    if img is not None:
        h, w, _ = img.shape
        r = 640 / max(w, h)
        yield cv2.resize(img, (int(w * r), int(h * r)))


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

def morphing(orginele_foto, morph_foto):
    pictures = [orginele_foto, morph_foto]
    #facemorpher.morpher(pictures, plot=True, out_frames='output')

    return 0


def main():
    args = get_args()
    model_name = args.model_name
    weight_file = args.weight_file
    margin = args.margin
    image_dir = args.image_dir

    if not weight_file:
        weight_file = get_file("age_only_resnet50_weights.061-3.300-4.410.hdf5", pretrained_model,
                               cache_subdir="pretrained_models",
                               file_hash=modhash, cache_dir=Path(__file__).resolve().parent)

    # for face detection
    detector = dlib.get_frontal_face_detector()

    # load model and weights
    model = get_model(model_name=model_name)
    model.load_weights(weight_file)
    img_size = model.input.shape.as_list()[1]
    
    # for layer in model.layers:
    #     print(layer.output_shape)

    detected_age = []
    actual_age = []
    
    if os.path.exists('SiblingsDB/'):
        path_DB = 'SiblingsDB/DBs'
    elif os.path.exists('../../Age-Obfuscation-Morphing/SiblingsDB'):
        path_DB = '../../Age-Obfuscation-Morphing/SiblingsDB/DBs'
    elif os.path.exists('../datasets/Siblings'):
        path_DB = '../datasets/Siblings/DBs'
    else:
        raise Exception("Database Missing! Download the Siblings Database from:\n    https://areeweb.polito.it/ricerca/cgvg/siblingsDB.html")
    f = open(os.path.join(path_DB,'../subjects.csv'), 'r')
    for row in f:
        data = (row.split(" "))
        data_split = (str(data).replace('"', ',').split(","))
        number = data_split[0].replace('\\t','').replace("'", "").replace('[', '')
        age = data_split[4].replace('\\t','')
        path = find(number, path_DB)
        print(age, number, path)
        if str(path) != "None":
            z = find2('*.jpg', path)
            if z[0]:
                image_dir = (str(z[0]))
            print(image_dir)
            image_generator = yield_images_from_dir(image_dir)
            for img in image_generator:
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
    
                # draw results
                for i, d in enumerate(detected):
                    label = str(int(predicted_ages[i]))
                    draw_label(img, (d.left(), d.top()), label)
    
            #cv2.imshow("result", img)
            
            actual_age.append(int(age))
            #age_detected = morphing(img, morph_foto)
            detected_age.append(int(predicted_ages[0]))
            
    
        key = cv2.waitKey(-1) if image_dir else cv2.waitKey(30)

        if key == 27:  # ESC
            cv2.destroyAllWindows()
            break

    #age = age_det()
    
    
    actual_age_arr = np.array(actual_age)
    detected_age_arr = np.array(detected_age)
    
    plt.scatter(actual_age_arr, detected_age_arr, s=40)
    plt.xlabel('Actual age')
    plt.ylabel('Detected age')
    plt.title("Detected age vs actual age of the complete siblings data set")
    plt.plot(range(0, 70))
    plt.savefig('actual-detect-morph20-SB.png')

if __name__ == '__main__':
    main()
