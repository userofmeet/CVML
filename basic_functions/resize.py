import cv2
import matplotlib.pyplot as plt
imgpath = r"C:\MEET\B.Tech - Projects\IROC_ISRO\Demo\WhatsApp Image 2025-07-02 at 08.44.54.jpeg"
img = cv2.imread(imgpath,1)
cv2.imshow("original",img)
cv2.waitKey(0)
(nr,nc,nch) = img.shape
r = 800
c = 800

img2 = cv2.resize(img,(r,c),interpolation=cv2.INTER_AREA)
cv2.imshow("resize",img2)
cv2.waitKey(0)
print('original',img.shape)
print('resized', img2.shape)
cv2.destroyAllWindows()