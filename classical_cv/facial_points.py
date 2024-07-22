from scipy.spatial import distance as dist
import matplotlib.pyplot as plt
from imutils.video import VideoStream
from imutils import face_utils
from threading import Thread
import numpy as np
import argparse
import imutils
import time
import dlib
import cv2
import os


detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml") 
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat") 
frame = cv2.imread("why-wear-safety-glasses.jpg")
frame = imutils.resize(frame, width=350)
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
rects = detector.detectMultiScale(frame, scaleFactor=1.1, 
		minNeighbors=5, minSize=(30, 30),
		flags=cv2.CASCADE_SCALE_IMAGE)

print(rects)


for (x,y,w,h) in rects:
    rect = dlib.rectangle(int(x), int(y), int(x+w), int(y+h))

    arr = predictor(gray, rect)
    arr = face_utils.shape_to_np(arr)
    print()
    
    for points in range(len(arr)):
        # if points in [2,30,14]:
        gray = cv2.circle(gray, (arr[points][0], arr[points][1]), radius=1, color=(0, 255, 0), thickness=-1)
        

print()