import cv2
import itertools
import numpy as np
import openface
import os

# read model and stream for face recognition
webcam = cv2.VideoCapture(0)
model = openface.AlignDlib('model.dat')

# get video size parameters
width = int(webcam.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH))
height = int(webcam.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT))
size = (width, height)

# set parameters to save video
fourcc = cv2.cv.CV_FOURCC(*'DIVX')
fps = webcam.get(cv2.cv.CV_CAP_PROP_FPS)

print type(fps)

output = cv2.VideoWriter('result.avi', fourcc, 8, size, 1)

while webcam.isOpened():
    ret, frame = webcam.read()

    try:
        # find region of interest and landmarks
        roi = model.getLargestFaceBoundingBox(frame)
        landmarks = model.findLandmarks(frame, roi)

        # draw landmarks
        for landmark in landmarks:
            cv2.circle(frame, landmark, radius=3, color=(0, 0, 0))

    except AssertionError:
        pass

    # write image to the file
    output.write(frame)

# release everything
webcam.release()
output.release()

