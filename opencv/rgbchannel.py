import cv2
import numpy as np

def resetRGB(path, t):
	img = cv2.imread(path, cv2.IMREAD_UNCHANGED)

	if len(t) == 0:
		return img

	h, w, l = img.shape
	
	for row in range(h):
		for col in range(w):
			b, g, r = img[row, col]
			if t == "b":
				img[row, col] = (b, 0, 0)
			elif t == "g":
				img[row, col] = (0, g, 0)
			else:
				img[row, col] = (0, 0, r)
	
	return img

path = r"./images/1.jpg"

ori = resetRGB(path, "")
imgb = resetRGB(path, "b")
imgg = resetRGB(path, "g")
imgr = resetRGB(path, "r")
inputs = np.hstack((ori, imgb, imgg, imgr))

cv2.namedWindow('myPicture', 0)
cv2.imshow('myPicture',inputs)
cv2.waitKey(0)

