import cv2 
import numpy as np 
import matplotlib.pyplot as plt 

# Reading the input image 
imgpath = "D:\\LAB SOURCE new\\DIP_IMAGES\\DIP3E_CH05_Original_Images\\Fig0503 (original_pattern).tif"
img1 = cv2.imread(imgpath, 0) 

########## Salt & Pepper Noise
max_val = np.max(img1)
print(max_val) 
img3 = (img1 / max_val)  # Normalization
pa = 0.05
pb = 0.05
(nr, nc) = img1.shape
R = np.float32(np.zeros((nr, nc), dtype='float32') + 0.11)
x = np.random.rand(nr, nc)
[r, c] = np.where(x <= pa)
for i in range(len(r)): 
    R[r[i]][c[i]] = np.uint8(0)
u = pa + pb 
[r, c] = np.where(x <= u)
for i in range(len(r)): 
    R[r[i]][c[i]] = np.uint8(255)
img_noise = img1 + R

###### Contra-Harmonic Filter
op = np.zeros((nr, nc), dtype='uint8')
Q = -5
for i in range(1, nr-1, 1): 
    for j in range(1, nc-1, 1): 
        num = 0
        denom = 0
        for x in range(i-1, i+2): 
            for y in range(j-1, j+2): 
                num = num + (pow(img_noise[x][y], (Q+1))) 
                denom = denom + (pow(img_noise[x][y], Q)) 
        if denom != 0: 
            op[i][j] = num / denom

###### Geometric Mean Filter
gm = np.zeros((nr, nc), dtype='uint8')
for i in range(1, nr-1, 1): 
    for j in range(1, nc-1, 1): 
        prod = 1
        for x in range(i-1, i+2): 
            for y in range(j-1, j+2): 
                prod *= img_noise[x][y]
        gm[i][j] = int(pow(prod, 1/9))

###### Harmonic Mean Filter
hm = np.zeros((nr, nc), dtype='uint8')
for i in range(1, nr-1, 1): 
    for j in range(1, nc-1, 1): 
        hsum = 0
        for x in range(i-1, i+2): 
            for y in range(j-1, j+2): 
                hsum += 1.0 / (img_noise[x][y] + 1e-5) 
        hm[i][j] = int(9 / hsum) 

plt.subplot(1, 5, 1) 
plt.imshow(img1, cmap='gray') 
plt.title('org') 
plt.xticks([]), plt.yticks([]) 

plt.subplot(1, 5, 2) 
plt.imshow(img_noise, cmap='gray') 
plt.title('s & p ') 
plt.xticks([]), plt.yticks([]) 
plt.subplot(1, 5, 3) 
plt.imshow(op, cmap='gray') 
plt.title('con') 
plt.xticks([]), plt.yticks([]) 

plt.subplot(1, 5, 4) 
plt.imshow(gm, cmap='gray') 
plt.title('geo') 
plt.xticks([]), plt.yticks([]) 

plt.subplot(1, 5, 5) 
plt.imshow(hm, cmap='gray') 
plt.title('harr') 
plt.xticks([]), plt.yticks([]) 
plt.show()
cv2.waitKey(0)  # Wait until key strike from keyboard 
cv2.destroyAllWindows()  # Close all windows
