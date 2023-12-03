import cv2
 
img = cv2.imread('./images/1.jpg')

cv2.imwrite("./images/1.webp", img, [cv2.IMWRITE_WEBP_QUALITY, 50])

