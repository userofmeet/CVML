import cv2
import numpy as np
import matplotlib.pyplot as plt 
path = r"D:\LAB SOURCE new\DIP_IMAGES\DIP3E_Original_Images_CH04\Fig0421(car_newsprint_sampled_at_75DPI).tif"
img = cv2.imread(path, 0)
i = []
sr = 2
new =[]
samples = 3
q = np.zeros((img.shape[0],img.shape[1]),dtype = 'uint8') 
for i in range(img.shape[0]): 
    for j in range(img.shape[1]):
        if (img[i][j]>=0 and img[i][j]<=31) : 
            q[i,j] = 16 
        elif(img[i][j]>32 and img[i][j]<=63) : 
            q[i,j] = 48 
        elif(img[i][j]>64 and img[i][j]<=95) : 
            q[i,j] = 80 
        elif(img[i][j]>96 and img[i][j]<=127) : 
            q[i,j] = 112
        elif(img[i][j]>128 and img[i][j]<=159) : 
            q[i,j] =  144
        elif(img[i][j]>160 and img[i][j]<=191) : 
            q[i,j] = 176 
        elif(img[i][j]>192 and img[i][j]<=223) : 
            q[i,j] = 208
        elif(img[i][j]>224 and img[i][j]<=255) : 
            q[i,j] = 240 
images = [img,q] 
for k in range(sr): 
    plt.subplot(1, sr, k+1) 
    plt.imshow(images[k],cmap='gray') 
plt.show()
