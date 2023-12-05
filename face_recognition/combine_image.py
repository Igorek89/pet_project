import cv2
import numpy as np
img1 = cv2.imread('sessions6.png')
img2 = cv2.imread('temp_stats.png')
print(len(img1))
print(len(img2))
vis = np.concatenate((img1, img2), axis=0)

cv2.imwrite('out_66994.png', vis)
