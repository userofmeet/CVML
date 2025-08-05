import cv2
import numpy as np
import matplotlib.pyplot as plt
imgpath = r"C:\MEET\B.Tech - Projects\IROC_ISRO\Demo\WhatsApp Image 2025-07-02 at 08.44.54.jpeg"
img = cv2.imread(imgpath, 0)
norm_img = img / 255.0
gamma = 2.2
new_gamma = np.power(norm_img, gamma)
new_gamma = new_gamma * 255
new_gamma = np.uint8(new_gamma)
plt.subplot(121)
plt.imshow(img, cmap='gray')

plt.subplot(122)
plt.imshow(new_gamma, cmap='gray')
plt.show()