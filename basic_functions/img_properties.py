import cv2
imgpath = r"C:\MEET\B.Tech - Projects\IROC_ISRO\Demo\WhatsApp Image 2025-04-20 at 17.36.27.jpeg"
img = cv2.imread(imgpath, 0)
print(img.dtype)
print(img.shape)
print(img.size)
print(img.ndim)
print(type(img))
(nr, nc) = img.shape
print(nr,nc)
img2 = cv2.imread(imgpath,1)
cv2.imshow("display",img2)
cv2.waitKey(0)
cv2.destroyAllWindows()