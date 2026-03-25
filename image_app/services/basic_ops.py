import cv2
import numpy as np

def inversion(image):
    return cv2.bitwise_not(image)

def decalage(image, val=50):
    return cv2.add(image, val)

def mise_echelle(image, factor=1.5):
    return cv2.convertScaleAbs(image, alpha=factor, beta=0)

def rotation(image, angle=90):
    h, w = image.shape[:2]
    M = cv2.getRotationMatrix2D((w//2, h//2), angle, 1)
    return cv2.warpAffine(image, M, (w, h))

def miroir(image):
    return cv2.flip(image, 1)