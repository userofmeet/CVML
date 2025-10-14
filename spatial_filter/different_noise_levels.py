import cv2
import matplotlib.pyplot as plt
import numpy as np
import random

path = r"C:\MEET\B-Tech\sem_7\image_processing\cv.jpg"
img = cv2.imread(path, 0)

mask_sizes = [3, 5, 7]  # example median/average mask sizes
noise_levels = [0.05, 0.1, 0.2]  # different noise probabilities

for p in noise_levels:
    noisy = np.zeros(img.shape, np.uint8)
    
    # Add salt-and-pepper noise
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            r = random.random()
            if r < p / 2:
                noisy[i, j] = 0
            elif r < p:
                noisy[i, j] = 255
            else:
                noisy[i, j] = img[i, j]
    
    median_results = [cv2.medianBlur(noisy, k) for k in mask_sizes]
    average_results = [cv2.filter2D(noisy, -1, np.ones((k, k), np.float32)/(k*k)) for k in mask_sizes]
    
    plt.figure(figsize=(20, 10))
    plt.suptitle(f"Noise Level = {int(p*100)}%", fontsize=16)
    
    # Top row: Original, Noisy, Median 3x3, Median 5x5
    plt.subplot(2, 4, 1)
    plt.imshow(img, cmap='gray')
    plt.title("Original")
    plt.axis('off')
    
    plt.subplot(2, 4, 2)
    plt.imshow(noisy, cmap='gray')
    plt.title("Noisy")
    plt.axis('off')
    
    for i in range(2):
        plt.subplot(2, 4, i + 3)
        plt.imshow(median_results[i], cmap='gray')
        plt.title(f"Median k={mask_sizes[i]}")
        plt.axis('off')
    
    # Bottom row: Median 7x7, Average 3x3, Average 5x5, Average 7x7
    plt.subplot(2, 4, 5)
    plt.imshow(median_results[2], cmap='gray')
    plt.title(f"Median k={mask_sizes[2]}")
    plt.axis('off')
    
    for i in range(3):
        plt.subplot(2, 4, 6 + i)
        plt.imshow(average_results[i], cmap='gray')
        plt.title(f"Average k={mask_sizes[i]}")
        plt.axis('off')
    
    plt.tight_layout()
    plt.show()
