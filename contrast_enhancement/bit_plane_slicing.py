import cv2
import numpy as np
import matplotlib.pyplot as plt
image_path = r"C:\MEET\VS CODE\image_processing\bit_plane_slicing.jpg"
grayscale_image = cv2.imread(image_path, 0)
height, width = grayscale_image.shape
plt.figure(figsize=(12, 8))
for bit_position in range(8):
    mask = 1 << bit_position
    sliced_plane = np.bitwise_and(grayscale_image, mask)
    visible_plane = np.where(sliced_plane > 0, 255, 0).astype(np.uint8)
    plt.subplot(2, 4, bit_position + 1)
    plt.imshow(visible_plane, cmap='gray')
    plt.title(f'Bit Plane {bit_position}')
    plt.axis('off')
plt.show()
