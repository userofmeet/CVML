import cv2
import numpy as np
import matplotlib.pyplot as plt

def sam_and_qua(imgpath, sample, quant):
    pth = imgpath
    im = cv2.imread(pth, 0)
    a1, a2 = im.shape[0], im.shape[1]
    s = []
    for i in range(0, a1, sample):
        for j in range(0, a2, sample):
            s.append(im[i][j])
    b1 = int(a1 / sample)
    b2 = int(a2 / sample)
    sampled = np.reshape(s, (b1, b2))
    qimg = np.zeros((a1, a2), dtype='uint8')
    z = 256 / quant
    for x in range(a1):
        for y in range(a2):
            level = int(im[x][y] // z)
            if level == quant:
                level -= 1
            qimg[x][y] = int((level + 0.5) * z)

    return im, sampled, qimg


path = r"D:\LAB SOURCE new\DIP_IMAGES\DIP3E_Original_Images_CH04\Fig0421(car_newsprint_sampled_at_75DPI).tif"
original, sampled, quantized = sam_and_qua(path, sample=3, quant=8)

sr = 3
for i, h in enumerate([original, sampled, quantized]):
    plt.subplot(1, sr, i+1)
    plt.imshow(h, cmap='gray')
plt.show()

path = r"D:\LAB SOURCE new\DIP_IMAGES\DIP3E_Original_Images_CH04\Fig0421(car_newsprint_sampled_at_75DPI).tif"
original, sampled, quantized = sam_and_qua(path, sample=3, quant=2)

sr = 3
for i, h in enumerate([original, sampled, quantized]):
    plt.subplot(1, sr, i+1)
    plt.imshow(h, cmap='gray')
plt.show()
