import cv2
imgpath = r"C:\MEET\B.Tech - Projects\IROC_ISRO\Demo\WhatsApp Image 2025-07-02 at 08.44.54.jpeg"
img = cv2.imread(imgpath, 1)
x = img.item(10,10,0)
print("x: ", x)
img[10,10,0] = 255 # if older version then use img.itemset((10,10,0),newpixelvalue)
y = img.item(10,10,0)
print("y: ", y)
