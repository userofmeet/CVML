import cv2
import matplotlib.pyplot as plt
import numpy as np
import random

path =  r"D:\LAB SOURCE new\standard_test_images\standard_test_images\lena_gray_256.tif"
imgpath = path 
img = cv2.imread(imgpath, 0)
noisy = np.zeros(img.shape, np.uint8)
p = 0.7

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
titles = ['Original', 'Noisy', 'Denoised_Median' , 'Averaged', 'sharped_denoised_median','edge']
for i in range(4):
    plt.subplot(2, 3, i+1)
    plt.imshow(output[i],'gray')
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

shar = np.array([[0, -1, 0], [-1, 5,-1], [0, -1, 0]], dtype=np.float32)
oshar = cv2.filter2D(denoised_median, -1, shar)
plt.subplot(2,3, 5)
plt.title(titles[4])
plt.imshow(oshar, cmap='gray')

edge = np.array([[-1, -1, -1], [-1, 8,-1], [-1, -1, -1]], dtype=np.float32)
oedge = cv2.filter2D(img, -1, edge)
plt.subplot(2,3, 6)
plt.imshow(oedge, cmap='gray')
plt.title(titles[5])


plt.show() 

