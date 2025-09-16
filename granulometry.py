import cv2
import numpy as np
import matplotlib.pyplot as plt
sizes = range(1, 20)
granulometry = []


# Load and preprocess the image
image = cv2.imread("D:\EC080\granulometry.png", 0)
ret, binary_image = cv2.threshold(image,0,255,cv2.THRESH_OTSU)

plt.imshow(binary_image, cmap = 'gray')

for size in sizes:
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (size, size))
    opened = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)
    #print(abs(opened-image))
    cv2.imshow("Image", opened)
    cv2.waitKey(0)

cv2.destroyAllWindows()
