# -*- coding: utf-8 -*-
"""
Created on Tue Sep  9 11:51:30 2025

@author: USER 1
"""

import cv2 
import numpy as np 
import matplotlib.pyplot as plt 
# Reading the input image 
imgpath ="D:\standard_test_images\cameraman.tif"
img = cv2.imread(imgpath, 0)
retval, thresh_Otsu = cv2.threshold(img,0,255,cv2.THRESH_OTSU) 


kernel1 = np.ones((5,5), np.uint8)

kernel2 = np.array([[0, 0, 1, 0, 0],
                    [0, 0, 1, 0, 0],
                    [1, 1, 1, 1, 1],
                    [0, 0, 1, 0, 0],
                    [0, 0, 1, 0, 0]], dtype=np.uint8)


kernel3 = np.array([[0, 0, 1, 0, 0],
                    [0, 0, 1, 0, 0],
                    [0, 0, 1, 0, 0],
                    [0, 0, 1, 0, 0],
                    [0, 0, 1, 0, 0]], dtype=np.uint8)

kernel4 = np.ones(5, np.uint8)


img_erosion = cv2.erode(thresh_Otsu, kernel3, iterations=1) 
img_dilation = cv2.dilate(thresh_Otsu, kernel3, iterations=1) 

opening = cv2.dilate(img_erosion, kernel3, iterations=1) 
closing = cv2.erode(img_dilation, kernel3, iterations=1) 

plt.subplot(2, 3, 1) 
plt.imshow(thresh_Otsu, cmap='binary') 
plt.title('Original Image') 
plt.xticks([]) 
plt.yticks([])
plt.subplot(2, 3, 2) 
plt.imshow(img_erosion, cmap='binary') 
plt.title('Eroded Image') 
plt.xticks([]) 
plt.yticks([])
plt.subplot(2, 3, 3) 
plt.imshow(img_dilation, cmap='binary') 
plt.title('Dilated Image')
plt.xticks([]) 
plt.yticks([])
plt.subplot(2, 3, 4) 
plt.imshow(opening, cmap='binary') 
plt.title('Opened Image')
plt.xticks([]) 
plt.yticks([])

plt.subplot(2, 3, 5) 
plt.imshow(closing, cmap='binary') 
plt.title('Closed Image')
plt.xticks([]) 
plt.yticks([])

plt.show() 
