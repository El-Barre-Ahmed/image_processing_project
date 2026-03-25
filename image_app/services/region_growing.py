import cv2
import numpy as np

def region_growing(image, seed=(0,0), threshold=10):
    h, w = image.shape[:2]
    result = np.zeros_like(image)
    visited = np.zeros((h,w), np.bool_)
    stack = [seed]
    orig_val = image[seed]

    while stack:
        x,y = stack.pop()
        if visited[x,y]:
            continue
        visited[x,y] = True
        if np.all(np.abs(image[x,y] - orig_val) <= threshold):
            result[x,y] = image[x,y]
            for dx in [-1,0,1]:
                for dy in [-1,0,1]:
                    nx, ny = x+dx, y+dy
                    if 0<=nx<h and 0<=ny<w:
                        stack.append((nx,ny))
    return result
