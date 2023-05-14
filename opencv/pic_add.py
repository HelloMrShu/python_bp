# -*- coding:utf-8 -*-

import cv2
import numpy as np

path1 = r"./images/1.jpg"

# load image
img = cv2.imread(path1, cv2.IMREAD_UNCHANGED)
# get height,width
h, w, l = img.shape

#生成一个和原图同尺寸的单位矩阵，并乘以15
mask = np.ones(img.shape, dtype=np.uint8) * 10

# matrix add,取模处理 (250+10) % 256 = 4
imga = img + mask

# opencv add,饱和处理 250 + 10 = 255
imgb = cv2.add(img, mask) 

# 图像水平拼接
merge = np.hstack((img, imga, imgb))

hm = cv2.resize(merge, dsize = None, fx = 0.5, fy = 0.5)

# show window
cv2.imshow('add', hm)
cv2.waitKey(0)
cv2.destroyAllWindows()
