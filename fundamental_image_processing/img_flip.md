## Using inbuilt function
``` python
import cv2
imgpath = r"C:\MEET\B.Tech - Projects\IROC_ISRO\Demo\WhatsApp Image 2025-04-20 at 17.36.27.jpeg"
img = cv2.imread(imgpath,0)
flip = cv2.flip(img,-1)
cv2.imshow("flipped",flip)
cv2.waitKey(0)
cv2.destroyAllWindows()
```
## Without inbuilt function
``` python
import cv2
import numpy as np

imgpath = r"C:\MEET\B.Tech - Projects\IROC_ISRO\Demo\WhatsApp Image 2025-04-20 at 17.36.27.jpeg"
img = cv2.imread(imgpath, 0)

flipped = img[::-1, ::-1]

cv2.imshow("flipped", flipped)
cv2.waitKey(0)
cv2.destroyAllWindows()
```
