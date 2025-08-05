import cv2
import matplotlib.pyplot as plt 
imgpath = r"C:\MEET\B.Tech - Projects\IROC_ISRO\Demo\WhatsApp Image 2025-04-20 at 17.36.27.jpeg"
img1 = cv2.imread(imgpath,0)
cv2.imshow("picture", img1)
cv2.waitKey(0)
img2 = abs(255-img1)
cv2.imshow("negative",img2)
cv2.waitKey(0)
titles = ['original','negative']
images = [img1, img2]

for i in range(2):
    plt.subplot(1,2,i+1)
    plt.imshow(images[i], cmap='gray')
    plt.title(titles[i])

plt.show()
cv2.destroyAllWindows()