import cv2
import numpy as np

def seuillage(image, thresh=128):
    _, result = cv2.threshold(image, thresh, 255, cv2.THRESH_BINARY)
    return result

def kmeans(image, k=2):
    Z = image.reshape((-1,3))
    Z = np.float32(Z)
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
    _, label, center = cv2.kmeans(Z, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
    center = np.uint8(center)
    res = center[label.flatten()]
    return res.reshape((image.shape))