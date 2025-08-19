import cv2
import numpy as np
import matplotlib.pyplot as plt
# Reading the input image
imgpath = "D:\LAB SOURCE new\DIP_IMAGES\DIP3E_CH05_Original_Images\Fig0503 (original_pattern).tif"
img1 = cv2.imread(imgpath, 0)
##### Gaussian Filter
max_val=np.max(img1);
print(max_val);
img2=(img1/max_val); # Normalization
a=0;
b=0.2;
(nr,nc) = img1.shape

x=a+(b*np.random.normal(a,b,(nr,nc))); # Gaussian Distribution with mean (a) and variance (b)
y=a+((b-a)*np.random.rand(nr,nc)); # Uniform Distribution
img_guassian=(img2+x)*max_val;
###### Arithmetic Mean Filter
filterSize = 3
k1 = np.array(np.ones((filterSize, filterSize), np.float32))/(filterSize * filterSize) #average filter
print(k1) #printing mask
output = cv2.filter2D(img_guassian, -1, k1) #here change mask variable
plt.subplot(1, 3, 1)
plt.imshow(img1,cmap='gray')
plt.title('Original Image')
plt.xticks([])
plt.yticks([])
plt.subplot(1, 3, 2)
plt.imshow(img_guassian,cmap='gray')
plt.title('Noisy Image')
plt.xticks([])
plt.yticks([])
plt.subplot(1, 3, 3)
plt.imshow(output,cmap='gray')
plt.title('Filtered Image')
plt.xticks([])
plt.yticks([])
plt.show()
cv2.waitKey(0) #Wait until key strike from keyboard
cv2.destroyAllWindows()#Close all windows
