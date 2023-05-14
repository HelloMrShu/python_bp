import cv2
import numpy as np

img = cv2.imread('./images/word.png',0)

# 腐蚀
kernel = np.ones((5, 5), np.uint8)
erosion = cv2.erode(img,kernel,iterations = 1)

# 膨胀
dilation = cv2.dilate(img,kernel,iterations = 1)

# 梯度, 膨胀与腐蚀的差别
gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)

# 开运算，1-腐蚀 2-膨胀
open = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)

# 闭运算，1-膨胀 2-腐蚀
close = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

all = np.hstack((img, erosion, dilation, gradient, open, close))

cv2.imshow('形态学', all)
cv2.waitKey(0)
cv2.destroyAllWindows()
