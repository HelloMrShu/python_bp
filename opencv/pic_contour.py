import cv2 as cv
import numpy as np

img = cv.imread("./images/word.png")
gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

cv.imshow("img", img)
cv.waitKey(0)

# 降噪
ret, thresh = cv.threshold(gray_img, 127, 255, 0)

# 寻找轮廓
contours, hierarchy = cv.findContours(gray_img, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)

# 绘制绿色轮廓
cv.drawContours(img, contours, -1, (0, 255, 0), 3)

cv.imshow("draw", img)
cv.waitKey(0)
cv.destroyAllWindows()
