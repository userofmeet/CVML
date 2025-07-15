import cv2
imgpath = r"C:\MEET\B.Tech - Projects\IROC_ISRO\Demo\WhatsApp Image 2025-04-20 at 17.36.27.jpeg"
img = cv2.imread(imgpath, 0)
flip_horizontal = cv2.flip(img, 1)  # Horizontal flip
flip_vertical = cv2.flip(img, 0)    # Vertical flip
flip_both = cv2.flip(img, -1)       # Both axes

cv2.imshow("Flipped Horizontally", flip_vertical)
cv2.waitKey(0)
cv2.destroyAllWindows()