import cv2
import numpy as np
import matplotlib.pyplot as plt 
path = r"D:\LAB SOURCE new\DIP_IMAGES\DIP3E_Original_Images_CH04\Fig0421(car_newsprint_sampled_at_75DPI).tif"
img = cv2.imread(path, 0)

i = []
sr = 2
new =[]
samples = 3

x=int(img.shape[0]/samples) 
y=int(img.shape[1]/samples) 
for i in range(0,img.shape[0],samples): 
    for j in range(0,img.shape[1],samples): 
        new.append(img[i][j]) 
sampled=np.reshape(new,(x,y)) 
titles = ['org', 'sampled image'] 
images = [img,sampled] 

for k in range(sr): 
    plt.subplot(1, sr, k+1) 
    plt.imshow(images[k],cmap='gray') 
plt.show()

