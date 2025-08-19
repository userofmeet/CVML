# To implement the Alpha- trimmed Order Statistic Restoration filter. 

``` python
import cv2
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from numpy import mean
def trimmeanval(arr, d):
    n = len(arr)
    k = int(d/2)
    return mean(arr[k:n-k])
# Reading the input image
imgpath = "D:\LAB SOURCE new\DIP_IMAGES\DIP3E_CH05_Original_Images\Fig0503 (original_pattern).tif"
img1 = cv2.imread(imgpath, 0)
##### Gaussian Filter
max_val=np.max(img1);
print(max_val);
img2=(img1/max_val); # Normalization
a=0;
b=0.01;
(nr,nc) = img1.shape

x = a+(b*np.random.normal(a,b,(nr,nc))); # Gaussian Distribution with mean (a) and variance (b)
y = a+((b-a)*np.random.rand(nr,nc)); # Uniform Distribution
img_guassian=(img2+x)*max_val;
##########Salt & Pepper Noise
max_val=np.max(img_guassian);
print(max_val);
img3=(img_guassian/max_val); # Normalization
pa=0.05;
pb=0.05;
(nr,nc) = img_guassian.shape
R = np.uint8(np.zeros((nr,nc),dtype = 'uint8')+0.11);
x=np.random.rand(nr,nc);
[r,c]=np.where(x<=pa);
for i in range(len(r)):
    R[r[i]][c[i]]=np.uint8(0);
u=pa+pb;
[r,c]=np.where(x<=u);
for i in range(len(r)):
     R[r[i]][c[i]]=np.uint8(255);

img_noise = img_guassian+R;

###### Alpha Trimmed Filter
img = img_noise;
(nr,nc) = img_noise.shape # to access row and column of image
print('No. of Row: ',nr)
print('No. of Column: ', nc)
output=np.zeros((nr,nc),dtype='uint8');
ary=np.zeros(9,dtype='uint8');
ary1=np.zeros(9,dtype='uint8');
output = np.zeros((nr, nc), dtype='uint8')

for i in range(1, nr-1):
    for j in range(1, nc-1):
        temp = 0
        for x in range(i-1, i+2):
            for y in range(j-1, j+2):
                ary[temp] = img_noise[x, y]
                temp += 1

        ary.sort()
        ary1 = ary
        output[i][j] = np.uint8(np.clip(np.median(ary1), 0, 255))

# Displaying images
plt.subplot(1, 4, 1)
plt.imshow(img1, cmap='gray')
plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(1, 4, 2)
plt.imshow(img_guassian, cmap='gray')
plt.title('Gaussian')
plt.xticks([]), plt.yticks([])
plt.subplot(1, 4, 3)
plt.imshow(img_noise, cmap='gray')
plt.title('Gaussian + S&P')
plt.xticks([]), plt.yticks([])
plt.subplot(1, 4, 4)
plt.imshow(output, cmap='gray')
plt.title('Filtered')
plt.xticks([]), plt.yticks([])
plt.show()
```
<img width="349" height="103" alt="image" src="https://github.com/user-attachments/assets/53222f8c-7a4c-4ed9-b953-ab35f7e868be" />
