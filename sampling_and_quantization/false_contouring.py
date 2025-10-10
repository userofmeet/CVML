import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread(r"C:\MEET\B-Tech\sem_7\image_processing\cv.jpg",0)
# Create zeros array to store the stretched image
final1 = np.zeros((img.shape[0],img.shape[1]),dtype = 'uint8')
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        if (img[i][j]>=0 and img[i][j]<=25) :
            final1[i,j] = 13
        elif(img[i][j]>25 and img[i][j]<=50) :
            final1[i,j] = 38
        elif(img[i][j]>50 and img[i][j]<=75) :
            final1[i,j] = 63
        elif(img[i][j]>75 and img[i][j]<=100) :
            final1[i,j] = 88
        elif(img[i][j]>100 and img[i][j]<=125) :
            final1[i,j] = 113
        elif(img[i][j]>125 and img[i][j]<=150) :
            final1[i,j] = 138
        elif(img[i][j]>150 and img[i][j]<=175) :
            final1[i,j] = 163
        elif(img[i][j]>175 and img[i][j]<=200) :
            final1[i,j] = 188
        elif(img[i][j]>200 and img[i][j]<=225) :
            final1[i,j] = 213
        elif(img[i][j]>225 and img[i][j]<=255) :
            final1[i,j] = 238
titles = ['Original Image', 'False Contouring With 10 Intensity Level ']
images = [img,final1]
no=2
for k in range(no):
    plt.subplot(1, no, k+1)
    plt.imshow(images[k],cmap='gray')
    plt.title(titles[k])
    plt.xticks([])
    plt.yticks([])
plt.show()
