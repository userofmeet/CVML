#---------------AVG FILER----------------
import cv2
import matplotlib.pyplot as plt
import numpy as np
path = r"D:\LAB SOURCE new\standard_test_images\standard_test_images\house.tif"
img = cv2.imread(path, 0)
OP = []
title = ['filter_1','filter_2','filter_3']

for i in range (3):
    j = i + 4
    k = np.array(np.ones((3+j, 3+j), np.float32))/(3+j)**2 
    
    output = cv2.filter2D(img, -1, k)
    plt.subplot(1,3,i+1)
    plt.imshow(output,cmap='gray')
    plt.title(title[i])

plt.show()
