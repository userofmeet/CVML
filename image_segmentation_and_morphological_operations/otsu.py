# Calculate the histogram 
import cv2 
import numpy as np
import matplotlib.pyplot as plt 
imgpath1 = "D:\LAB Source\DIP_IMAGES\DIP3E_CH08_Original_Images\Fig0840_0266.tif"
img1 = cv2.imread(imgpath1, 0) 
#Between class variance 
hist = plt.hist(img1.ravel(),256,[0,256]) 
print(hist[0],"\n", hist[1])
# y axis -> hist[0] = vaalues of pixels
# x axis -> hist[1] = just shows the x axia
# Total pixels in the image 


total = np.sum(hist[0]) 
# calculate the initial weights and the means 
left, right = np.hsplit(hist[0],[0]) 
left_bins, right_bins = np.hsplit(hist[1],[0]) 
print(left, right)

# left weights 
w_0 = 0.0 
# Right weights 
w_1 = np.sum(right)/total 
# Left mean 
mean_0 = 0.0 
weighted_sum_0 = 0.0 
# Right mean 
weighted_sum_1 = np.dot(right,right_bins[:-1]) 
mean_1 = weighted_sum_1/np.sum(right) 

def recursive_otsu1(hist, w_0=w_0, w_1=w_1, weighted_sum_0=weighted_sum_0, 
weighted_sum_1=weighted_sum_1, thres=1, fn_max=-np.inf, thresh=0, total=total): 
    if thres<=255: 
 # To pass the division by zero warning 
        if np.sum(hist[0][:thres+1]) !=0 and np.sum(hist[0][thres+1:]) !=0: 
 # Update the weights 
             w_0 += hist[0][thres]/total 
             w_1 -= hist[0][thres]/total 
 # Update the mean 
             weighted_sum_0 += (hist[0][thres]*hist[1][thres]) 
             mean_0 = weighted_sum_0/np.sum(hist[0][:thres+1]) 
             weighted_sum_1 -= (hist[0][thres]*hist[1][thres]) 
             if thres == 255: 
                 mean_1 = 0.0 
             else:
                mean_1 = weighted_sum_1/np.sum(hist[0][thres+1:]) 
 # Calculate the between-class variance 
             out = w_0*w_1*((mean_0-mean_1)**2) 
             print(out,thres)
 # # if variance maximum, update it 
             if out>fn_max: 
                fn_max = out 
                thresh = thres 
                return recursive_otsu1(hist, w_0=w_0, w_1=w_1, weighted_sum_0=weighted_sum_0, 
weighted_sum_1=weighted_sum_1, thres=thres+1, fn_max=fn_max, thresh=thresh, total=total) 
 # Stopping condition 
             else: 
                return fn_max,thresh 
# Check the results 
var_value, thresh_value = recursive_otsu1(hist, w_0=w_0, w_1=w_1, 
weighted_sum_0=weighted_sum_0, weighted_sum_1=weighted_sum_1, thres=1, 
fn_max=-np.inf, thresh=0, total=total) 
print(var_value, thresh_value) 
# threshold the image 
ret, thresh_Between = cv2.threshold(img1,0,255,thresh_value) 
plt.imshow(thresh_Between)
# Otsu's thresholding using inbuilt function 
retval, thresh_Otsu = cv2.threshold(img1,0,255,cv2.THRESH_OTSU) 
plt.imshow(thresh_Otsu)
print(retval)
