import cv2
import matplotlib.pyplot as plt
import numpy as np
import random

path =  r"D:\LAB SOURCE new\standard_test_images\standard_test_images\lena_gray_256.tif"
imgpath = path 
img = cv2.imread(imgpath, 0)
noisy = np.zeros(img.shape, np.uint8)
p = 0.2

for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        r = random.random()
        if r < p/2:
            noisy[i][j] = 0
        elif r < p:
            noisy[i][j] = 255
        else:
            noisy[i][j] = img[i][j]
denoised_median = cv2.medianBlur(noisy, 5)

k1 = np.array(np.ones((11, 11), np.float32))/121
print(k1) 
Averaged = cv2.filter2D(noisy, -1, k1)  
output = [img, noisy, denoised_median, Averaged]
titles = ['Original', 'Noisy', 'Denoised_Median' , 'Averaged']
for i in range(4):
    plt.subplot(2, 2, i+1)
    plt.imshow(output[i],'gray')
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])
plt.show() 
