# -*- coding:utf-8 -*-
import cv2
import numpy as np

img = cv2.imread('./images/1.jpg')
logo = cv2.imread('./images/4.png')

#调整大小
logo = cv2.resize(logo, (50, 50))

#图像宽度
imgWidth = img.shape[1]
#logo高度
logoHeight = logo.shape[0]

# 在右上角创建logo图像大小的ROI感兴趣的区域，距上右边距各50像素
roi = img[50 : 50 + logoHeight, imgWidth - 100 : imgWidth - 50]

# 创建logo掩码和掩码取反
img2gray = cv2.cvtColor(logo, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2gray, 200, 255, cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)

# 取反和相与操作
bg = cv2.bitwise_and(roi, roi, mask = mask)

# 取反和相与操作
fg = cv2.bitwise_and(logo, logo, mask = mask_inv)

# 将logo放到整张图像上
dst = cv2.add(bg, fg)
img[50 : 50 + logoHeight, imgWidth - 100 : imgWidth - 50] = dst

ret = cv2.resize(img, dsize = None, fx = 0.5, fy = 0.5)

cv2.imshow('res', ret)
cv2.waitKey(0)
cv2.destroyAllWindows()
