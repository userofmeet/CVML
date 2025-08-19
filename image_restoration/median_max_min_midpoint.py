
import cv2
import numpy as np
import matplotlib.pyplot as plt
from numpy import mean
from scipy import stats
from numpy import mean

imgpath = "D:/LAB SOURCE new/DIP_IMAGES/DIP3E_CH05_Original_Images/Fig0503 (original_pattern).tif"
img1 = cv2.imread(imgpath, 0)

max_val = np.max(img1)
print(max_val)
img2 = (img1 / max_val)  # Normalization
a = 0
b = 0.01
(nr, nc) = img1.shape

x = a + (b * np.random.normal(a, b, (nr, nc)))  
y = a + ((b - a) * np.random.rand(nr, nc)) 
img_guassian = (img2 + x) * max_val

# s and p Noise
max_val = np.max(img_guassian)
print(max_val)
img3 = (img_guassian / max_val)  # Normalization
pa = 0.05
pb = 0.05
(nr, nc) = img_guassian.shape
R = np.uint8(np.zeros((nr, nc), dtype='uint8') + 0.11)
x = np.random.rand(nr, nc)
[r, c] = np.where(x <= pa)
for i in range(len(r)):
    R[r[i]][c[i]] = np.uint8(0)
u = pa + pb
[r, c] = np.where(x <= u)
for i in range(len(r)):
    R[r[i]][c[i]] = np.uint8(255)

img_noise = img_guassian + R

def median(img):
    nr, nc = img.shape
    output = np.zeros((nr, nc), dtype='uint8')
    for i in range(1, nr-1):
        for j in range(1, nc-1):
            neighborhood = img[i-1:i+2, j-1:j+2]
            sortedf = np.sort(neighborhood.flatten())
            output[i, j] = sortedf[4] 
    return output

def maxi(img):
    nr, nc = img.shape
    output = np.zeros((nr, nc), dtype='uint8')
    for i in range(1, nr-1):
        for j in range(1, nc-1):
            n = img[i-1:i+2, j-1:j+2]
            output[i, j] = np.max(n)
    return output

def mini(img):
    nr, nc = img.shape
    output = np.zeros((nr, nc), dtype='uint8')
    for i in range(1, nr-1):
        for j in range(1, nc-1):
            n = img[i-1:i+2, j-1:j+2]
            output[i, j] = np.min(n)
    return output

def midpoint(img):
    nr, nc = img.shape
    output = np.zeros((nr, nc), dtype='uint8')
    for i in range(1, nr-1):
        for j in range(1, nc-1):
            n = img[i-1:i+2, j-1:j+2]
            mini = np.min(n)
            maxi = np.max(n)
            output[i, j] = (mini + maxi) // 2
    return output

median = median(img_noise)
maxi = maxi(img_noise)
mini = mini(img_noise)
midpoint = midpoint(img_noise)

plt.subplot(231)
plt.imshow(img1, cmap = 'gray')
plt.title('original')
plt.xticks([]), plt.yticks([])
plt.subplot(232)
plt.imshow(img_noise, cmap = 'gray')
plt.title('noisy')
plt.xticks([]), plt.yticks([])
plt.subplot(2, 3, 3)
plt.imshow(median, cmap='gray')
plt.title('median')
plt.xticks([]), plt.yticks([])

plt.subplot(2, 3, 4)
plt.imshow(maxi, cmap='gray')
plt.title('max')
plt.xticks([]), plt.yticks([])

plt.subplot(2, 3, 5)
plt.imshow(mini, cmap='gray')
plt.title('min')
plt.xticks([]), plt.yticks([])

plt.xticks([]), plt.yticks([])
plt.subplot(2, 3, 6)
plt.imshow(midpoint, cmap='gray')
plt.title('midpoint')
plt.xticks([]), plt.yticks([])


plt.show()
