import cv2
imgpath = r"C:\MEET\B.Tech - Projects\IROC_ISRO\Demo\WhatsApp Image 2025-04-20 at 17.36.27.jpeg"
img = cv2.imread(imgpath, 0)

blur = cv2.GaussianBlur(img, (5, 5), 0)
cv2.imshow("Blurred", blur)

cv2.waitKey(0)
cv2.destroyAllWindows()