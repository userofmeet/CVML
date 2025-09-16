import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load grayscale image
imgpath1 = "D:/EC080/connectd_components_with_stats.png"
img1 = cv2.imread(imgpath1, 0)

# Compute histogram using numpy (NOT plt.hist)
hist_values, bin_edges = np.histogram(img1.ravel(), bins=256, range=(0, 256))
total = np.sum(hist_values)

# Initial values
w_0 = 0.0
w_1 = np.sum(hist_values) / total
mean_0 = 0.0
weighted_sum_0 = 0.0
weighted_sum_1 = np.dot(hist_values, bin_edges[:-1])
mean_1 = weighted_sum_1 / np.sum(hist_values)

# Recursive Otsu implementation
def recursive_otsu(hist, bins, total, w_0=0.0, w_1=1.0,
                   weighted_sum_0=0.0, weighted_sum_1=None,
                   thres=0, fn_max=-np.inf, thresh=0):
    if weighted_sum_1 is None:
        weighted_sum_1 = np.dot(hist, bins)

    if thres > 255:
        return fn_max, thresh

    if np.sum(hist[:thres + 1]) != 0 and np.sum(hist[thres + 1:]) != 0:
        pixel_value = bins[thres]
        weight = hist[thres]

        w_0 += weight / total
        w_1 -= weight / total

        weighted_sum_0 += weight * pixel_value
        weighted_sum_1 -= weight * pixel_value

        mean_0 = weighted_sum_0 / np.sum(hist[:thres + 1])
        mean_1 = weighted_sum_1 / np.sum(hist[thres + 1:]) if np.sum(hist[thres + 1:]) > 0 else 0

        # Between-class variance
        between_class_var = w_0 * w_1 * ((mean_0 - mean_1) ** 2)

        if between_class_var > fn_max:
            fn_max = between_class_var
            thresh = thres

    return recursive_otsu(hist, bins, total,
                          w_0, w_1,
                          weighted_sum_0, weighted_sum_1,
                          thres + 1, fn_max, thresh)

# Run recursive Otsu
var_value, custom_thresh = recursive_otsu(hist_values, bin_edges[:-1], total)
print("Max Variance:", var_value)
print("Optimal Threshold (Custom Otsu):", custom_thresh)

# Threshold using custom Otsu
_, thresh_custom = cv2.threshold(img1, custom_thresh, 255, cv2.THRESH_BINARY)

# Threshold using built-in Otsu
retval, thresh_otsu = cv2.threshold(img1, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
print("Built-in Otsu Threshold:", retval)

# Save output
outpath = "D:/EC080/BINARY_IMAGE.png"
cv2.imwrite(outpath, thresh_otsu)

# Show image
cv2.imshow('Custom Otsu Binary Image', thresh_custom)
cv2.imshow('Built-in Otsu Binary Image', thresh_otsu)
cv2.waitKey(0)
cv2.destroyAllWindows()
