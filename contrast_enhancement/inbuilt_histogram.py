import cv2
from matplotlib import pyplot as plt
img = cv2.imread(r"C:\MEET\VS CODE\image_processing\cv.jpeg",0)
histr = cv2.calcHist([img],[0],None,[256],[0,256])
plt.plot(histr)
plt.show()
