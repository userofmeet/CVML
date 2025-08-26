# 

import cv2
import numpy as np

def hsi(img):
    img = img.astype(np.float32) / 255
    B, G, R = cv2.split(img)
    I = (R + G + B) / 3

    min_val = np.minimum(np.minimum(R, G), B)
    S = 1 - (3 / (R + G + B + 1e-6)) * min_val  

    
    num = 0.5 * ((R - G) + (R - B))
    den = np.sqrt((R - G)**2 + (R - B)*(G - B)) + 1e-6  
    theta = np.arccos(num / den)

    H = np.where(B <= G, theta, 2 * np.pi - theta)
    H = H * 180 / np.pi  
    return H, S, I

def main():
    img = cv2.imread(r"D:\LAB Source\DIP_IMAGES\DIP3E_Original_Images_CH06\Fig0630(01)(strawberries_fullcolor).tif",  1)  
    cv2.imshow("Original Image", img)
    H, S, I = hsi(img)
    cv2.imshow("hue", H.astype(np.uint8))
    cv2.waitKey(0)
    cv2.imshow("sat", (S * 255).astype(np.uint8))
    cv2.waitKey(0)
    cv2.imshow("int", (I * 255).astype(np.uint8))
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
if __name__ == "__main__":
    main()
