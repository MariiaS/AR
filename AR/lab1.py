import sys

import cv2
import numpy as np
# from OpenGL.GL import *
# from OpenGL.GLU import *
# from OpenGL.GLUT import *
from matplotlib import pyplot as plt

if __name__ == '__main__':
    objp = np.zeros((6 * 7, 3), np.float32)
    objp[:, :2] = np.mgrid[0:7, 0:6].T.reshape(-1, 2)

# Arrays to store image points.
    imgp = []  # 2d points in image plane.
# Read image
    img = cv2.imread('left1.jpg')
    plt.imshow(img)
    # Command #1
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Command #2
    ret, corners = cv2.findChessboardCorners(gray, (7, 6), None)
    # Termination criteria for Command 3
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
    # Command #3
    cv2.cornerSubPix(gray, corners, (11, 11), (-1, -1), criteria)
    imgp.append(corners)
    # Command #4
    cv2.drawChessboardCorners(img, (7, 6), corners, ret)
    # Image display with its points
    cv2.namedWindow('Test calibration')
    cv2.startWindowThread()
    cv2.imshow('Test calibration', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

