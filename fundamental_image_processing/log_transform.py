import cv2
import numpy as np
import matplotlib.pyplot as plt 
imgpath = r"C:\MEET\B.Tech - Projects\IROC_ISRO\Demo\WhatsApp Image 2025-07-02 at 08.44.54.jpeg"
img = cv2.imread(imgpath,0)
img_float = img.astype(float)
c = 255 / np.log(1 + np.max(img_float))
log_img = c * np.log(1 + img_float)
log_img = np.uint8(log_img)

plt.subplot(1,2,1)
plt.imshow(img, cmap='gray')
plt.subplot(1,2,2)
plt.imshow(log_img, cmap='gray')
plt.show()