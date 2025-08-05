import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread(r"C:\MEET\VS CODE\image_processing\cv.jpeg", 0)
histr = np.zeros(256, dtype=int)
height, width = img.shape
for i in range(height):
    for j in range(width):
        intensity = img[i, j]
        histr[intensity] += 1
plt.plot(histr)
plt.title('Histogram without cv2.calcHist')
plt.xlabel('Pixel Intensity')
plt.ylabel('Frequency')
plt.show()
