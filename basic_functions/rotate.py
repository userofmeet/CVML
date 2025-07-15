import cv2
imgpath = r"C:\MEET\B.Tech - Projects\IROC_ISRO\Demo\WhatsApp Image 2025-04-20 at 17.36.27.jpeg"
img = cv2.imread(imgpath, 0)
(h, w) = img.shape[:2]
center = (w // 2, h // 2)

M = cv2.getRotationMatrix2D(center, 45, 1.0)  # Rotate 45 degrees
rotated = cv2.warpAffine(img, M, (w, h))
cv2.imshow("Rotated", rotated)
cv2.waitKey(0)
cv2.destroyAllWindows()