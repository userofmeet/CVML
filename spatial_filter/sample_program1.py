import cv2
import matplotlib.pyplot as plt
import numpy as np

imgpath = r"C:\MEET\B-Tech\sem_7\image_processing\cv.jpg"
img = cv2.imread(imgpath, 0)  
k1 = np.ones((11, 11), np.float32) / 121 
print(k1)
output = cv2.filter2D(img, -1, k1)
plt.subplot(1, 2, 1)
plt.imshow(img, cmap='gray')  
plt.title('Original Image')
plt.subplot(1, 2, 2)
plt.imshow(output, cmap='gray') 
plt.title('Filtered Image')
plt.show()
