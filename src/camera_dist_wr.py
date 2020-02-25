import numpy as np
import cv2
from imageio import imread

def camera_dist(img):

    mtx = np.load('mtx_wr.npy')
    dist = np.load('dist_wr.npy')
    newcameramtx = np.load('distmtx_wr.npy')

    # undistort
    dst = cv2.undistort(img, mtx, dist, None, newcameramtx)

    return dst
