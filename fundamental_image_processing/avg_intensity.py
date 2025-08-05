import cv2
import numpy as np
import matplotlib.pyplot as plt

imgpath = r"C:\MEET\VS CODE\image_processing\cv.jpeg"
img = cv2.imread(imgpath,0)
(nr,nc) = img.shape
print(nr,nc)
cv2.imshow("drone", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

temp = 0
for i in range(nr):
    for j in range(nc):
        temp = temp + int(img[i][j])

avgintensity = temp / (nr*nc)
print(avgintensity)
