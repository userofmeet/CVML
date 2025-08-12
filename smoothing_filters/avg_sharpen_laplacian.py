import cv2
import matplotlib.pyplot as plt
import numpy as np

path = r"D:\LAB SOURCE new\standard_test_images\standard_test_images\lena_gray_256.tif"
img = cv2.imread(path, 0)

title = ['3x3', '7x7', '11x11', 'sharpen', 'laplacian']
for i in range(3):
    j = i
    k = np.array(np.ones((3 + j, 3 + j), np.float32)) / (3 + j) ** 2
    j = j + 4
    output = cv2.filter2D(img, -1, k)
    plt.subplot(2, 3, i + 1)  
    plt.imshow(output, cmap='gray')
    plt.title(title[i])
    
shar = np.array([[0, -1, 0], [-1, 5,-1], [0, -1, 0]], dtype=np.float32)
oshar = cv2.filter2D(img, -1, shar)
plt.subplot(2,3, 4)
plt.imshow(oshar, cmap='gray')
plt.title(title[3])

lap = np.array(np.ones((3 , 3 ), np.float32)) * (-1)
lap[1][1] = 9
olap = cv2.filter2D(img, -1, lap)
plt.subplot(2, 3, 5)
plt.imshow(olap, cmap='gray')
plt.title(title[4])
plt.show()
