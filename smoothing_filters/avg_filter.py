import cv2
import matplotlib.pyplot as plt
import numpy as np
path = "D:\LAB SOURCE new\DIP_IMAGES\DIP3E_CH05_Original_Images\Fig0525(a)(aerial_view_no_turb).tif"
img = cv2.imread(path, 1)
# img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
k1 = np.array(np.ones((3, 3), np.float32))/9 #average filter
print(k1) #printing mask
output = cv2.filter2D(img, -1, k1) #here change mask variable 
plt.subplot(1, 2, 1)
plt.imshow(img)
plt.title('Original Image')
plt.subplot(1, 2, 2)
plt.imshow(output)
plt.title('Filtered Image')
plt.show()
