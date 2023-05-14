import cv2
import numpy as np
 
cap = cv2.VideoCapture(0)

while (cap.isOpened()):
    # 获取每一帧
    ret, frame = cap.read()
    # 转换HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # 设定蓝色的阈值
    lower_blue = np.array([100, 43, 46])
    upper_blue = np.array([124, 255, 255])
    # 根据阈值构建掩模
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
 
    # 计算图像中目标的轮廓
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) 
    for c in contours:
      # 计算面积
      if cv2.contourArea(c) > 1000:
        # 该函数计算矩形的边界框
        (x, y, w, h) = cv2.boundingRect(c)
	# 设置绿色轮廓线
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
 
    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
 
    # 对原图像和掩模进行位运算
    res = cv2.bitwise_and(frame, frame, mask=mask)
    cv2.imshow('res', res)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

# 关闭窗口
cv2.destroyAllWindows()
