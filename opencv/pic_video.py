import os
import cv2

path = './material'
filelist = os.listdir(path)
filelist = sorted(filelist)

# 视频每秒1帧
fps = 1
# 需要转为视频的图片的尺寸
size = (640, 480)
# 可以使用cv2.resize()进行修改

fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
video = cv2.VideoWriter("./videos/pic_video.mp4", fourcc, fps, size)

for item in filelist:
    if item.endswith('.jpeg'):
        item = os.path.join(path, item)
        img = cv2.imread(item)
        # resize图片
        img = cv2.resize(img, (640, 480))
        video.write(img)

video.release()
cv2.destroyAllWindows()
