import cv2 
import numpy as np 
import matplotlib.pyplot as plt 
# Reading the input image 
imgpath = "D:\LAB SOURCE new\DIP_IMAGES\DIP3E_CH05_Original_Images\Fig0503 (original_pattern).tif"
img1 = cv2.imread(imgpath, 0) 
##########Salt & Pepper Noise 
max_val=np.max(img1);
print(max_val); 
img3 = (img1/max_val); # Normalization
pa=0.05;
pb=0.05;
(nr,nc) = img1.shape 
R = np.float32(np.zeros((nr,nc),dtype = 'float32')+0.11);
x=np.random.rand(nr,nc);
[r,c]=np.where(x<=pa);
for i in range(len(r)): 
    R[r[i]][c[i]]=np.uint8(0);
u=pa+pb 
[r,c]=np.where(x<=u);
for i in range(len(r)): 
 R[r[i]][c[i]]=np.uint8(255);
img_noise=img1+R;
###### Contra-Harmonic Filter 
(nr,nc) = img_noise.shape # to access row and column of image 
print('No. of Row: ',nr) 
print('No. of Column: ', nc) 
output=np.zeros((nr,nc),dtype='uint8');
Q=-5 
for i in range(1,nr-1,1): 
    for j in range(1,nc-1,1): 
        num=0;denom=0;
        for x in range(i-1,i+2): 
            for y in range(j-1,j+2): 
                num = num + (pow(img_noise[x][y],(Q+1))) 
                denom = denom + (pow(img_noise[x][y],Q)) 
        if denom != 0: 
            output[i][j]= num / denom;
 
 
plt.subplot(1, 3, 1) 
plt.imshow(img1,cmap='gray') 
plt.title('Original Image') 
plt.xticks([]) 
plt.yticks([]) 
plt.subplot(1, 3, 2) 
plt.imshow(img_noise,cmap='gray') 
plt.title('Img with S&P Noise') 
plt.xticks([]) 
plt.yticks([]) 
plt.subplot(1, 3, 3) 
plt.imshow(output,cmap='gray') 
plt.title('Filtered Output') 
plt.xticks([]) 
plt.yticks([]) 
plt.show() 
cv2.waitKey(0) #Wait until key strike from keyboard 
cv2.destroyAllWindows()#Close all windows 
