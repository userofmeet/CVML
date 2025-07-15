import cv2
import matplotlib.pyplot as plt
imgpath1 = r"C:\MEET\B.Tech - Projects\IROC_ISRO\Demo\WhatsApp Image 2025-04-20 at 17.36.27.jpeg"
imgpath2 = r"C:\MEET\Portfolio\src\Assets\Projects\a2X_CAM.png"

img1 = cv2.imread(imgpath1,0)
img2 = cv2.imread(imgpath2,0)

title = ['img1','img2']
img = [img1,img2]

for i in range(2):
    plt.subplot(1,2,i+1)
    plt.imshow(img[i],cmap='gray')
    plt.title(title[i])

plt.show()