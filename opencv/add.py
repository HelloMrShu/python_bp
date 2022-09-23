import cv2
import numpy as np

path1 = r"C:\Users\Administrator\Desktop\\1.jpg"

img = cv2.imread(path1, cv2.IMREAD_UNCHANGED)
h, w, l = img.shape

mask = np.ones(img.shape, dtype=np.uint8) * 50

imga = img + mask # numpy加法
imgb = cv2.add(img, mask) #opencv add

fusion = cv2.add(imga, imgb) #融合
merge = np.hstack((imga, imgb, fusion))

hm = cv2.resize(merge, dsize = None, fx = 0.5, fy = 0.5)

cv2.imshow('add', hm)
cv2.waitKey(0)
#cv2.destroyAllWindows()