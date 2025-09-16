import cv2 
import numpy as np 
import matplotlib.pyplot as plt 
# Reading the input image 
imgpath = "D:\LAB Source\DIP_IMAGES\DIP3E_Original_Images_CH10\Fig1007(a)(wirebond_mask).tif"
img = cv2.imread(imgpath, 1)# ‘0’ is for gray scale image 
# Taking a matrix of size 5 as the kernel 
kernel1      = np.array ([[1,1,1,1,1],
                [1,1,1,1,1],
                [1,1,1,1,1],
                [1,1,1,1,1],
                [1,1,1,1,1]], dtype = np.uint8) 
#kernel = ([0,1,0],[1,1,1],[0,1,0]) 
print(kernel1)
img_erosion = cv2.erode(img, kernel1, iterations=1) 
img_dilation = cv2.dilate(img, kernel1, iterations = 1)
#cv2.imshow('Input', img) 
#cv2.imshow('Eroded Output', img_erosion)
outpath = 'C:/MANUAL/IMAGE_PROCESSING/B.TECH/2019-20/EXP. 9/erosionOut.tif' 
cv2.imwrite(outpath, img) 
plt.subplot(1, 3, 1) 
plt.imshow(img, cmap='binary') 
plt.title('Original Image') 
plt.xticks([]) 
plt.yticks([]) 
plt.subplot(1, 3, 2) 
plt.imshow(img_erosion, cmap='binary') 
plt.title('Eroded Image') 
plt.xticks([]) 
plt.yticks([]) 

plt.subplot(133) 
plt.imshow(img_dilation, cmap='binary') 
plt.title('Dilated Image') 
plt.xticks([]) 
plt.yticks([]) 
plt.show() 
cv2.waitKey(0) #Wait until key strike from keyboard 
cv2.destroyAllWindows()#Close all windows
