import cv2 
import matplotlib.pyplot as plt 

path = r"D:\standard_test_images\peppers_color.tif"
img = cv2.imread(path, 1) 
cv2.imshow('org', img) 
cv2.waitKey(0) 

b,g,r = cv2.split(img) 
rgb_img = cv2.merge([b,g,r]) 
cv2.imshow('color', rgb_img) 
cv2.waitKey(0) 
cv2.imshow('Blue ', b) 
cv2.waitKey(0) 
cv2.imshow('Green ', g) 
cv2.waitKey(0) 
cv2.imshow('Red ', r) 
cv2.waitKey(0) 
cv2.imshow('merged', rgb_img)
cv2.waitKey(0)
cv2.destroyAllWindows() 
titles = ['red', 'green', 'blue '] 
images = [r, g, b] 
for i in range(3): 
 plt.subplot(1, 3, i+1) 
 plt.imshow(images[i],cmap='gray') 
 plt.title(titles[i]) 
 plt.xticks([]) 
 plt.yticks([]) 
 plt.show()
