import cv2
import numpy as np

p1 =r"C:\Users\Administrator\Desktop\\1.jpg"
p2 =r"C:\Users\Administrator\Desktop\\2.jpg"
p3 =r"C:\Users\Administrator\Desktop\\3.jpg"

img1 = cv2.imread(p1, cv2.IMREAD_UNCHANGED)
img2 = cv2.imread(p2, cv2.IMREAD_UNCHANGED)

hm = np.hstack((img1, img2))
vm = np.hstack((img2, img1))

inputs = np.vstack((hm, vm))

cv2.namedWindow('myPicture', 0)
cv2.imshow('myPicture',inputs)
cv2.waitKey(0)
