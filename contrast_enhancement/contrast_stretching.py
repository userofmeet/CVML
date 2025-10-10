import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread(r"C:\MEET\B-Tech\sem_7\image_processing\cv.jpg", 0)
final = np.zeros_like(img, dtype='float16')
r1, r2 = 40, 180   # input intensity range (from histogram)
s1, s2 = 0, 255    # output intensity range (full contrast)
m1 = s1 / r1
m2 = (s2 - s1) / (r2 - r1)
m3 = (256 - s2) / (256 - r2)
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        pixel = img[i, j]
        if pixel <= r1:
            final[i, j] = m1 * pixel
        elif pixel <= r2:
            final[i, j] = m2 * (pixel - r1) + s1
        else:
            final[i, j] = m3 * (pixel - r2) + s2
im1 = np.clip(final, 0, 255).astype(np.uint8)
cv2.imshow("Original Image", img)
cv2.imshow("Contrast Stretched Image", im1)
cv2.waitKey(0)
cv2.destroyAllWindows()
titles = ['Original Image', 'Contrast Stretched Image']
images = [img, im1]

plt.figure(figsize=(10, 5))
for k in range(2):
    plt.subplot(1, 2, k + 1)
    plt.imshow(images[k], cmap='gray')
    plt.title(titles[k])
    plt.axis('off')
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 4))
plt.subplot(1, 2, 1)
plt.hist(img.ravel(), bins=256, range=[0, 256])
plt.title('Original Histogram')
plt.xlabel('Pixel Intensity')
plt.ylabel('Frequency')

plt.subplot(1, 2, 2)
plt.hist(im1.ravel(), bins=256, range=[0, 256])
plt.title('Stretched Histogram')
plt.xlabel('Pixel Intensity')
plt.ylabel('Frequency')

plt.tight_layout()
plt.show()
